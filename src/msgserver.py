import asyncio
import logging
import message_pb2 as message
import msgprotocol
import msgdb
from data_model import User,Game

logging.basicConfig(level = logging.DEBUG)
# -----------------------------------------------------------------------------
def game_other_user(users,user):
	assert len(users) == 2
	return users[0] == user? users[1] : users[0]
# -----------------------------------------------------------------------------
class Dead:
	def __init__(self):
		# user color -> dead stones
		self.color_stones = {}
		
	def add(self,color,stones):
		self.color_stones[color] = stones
	
	def is_ok(self):
		return len(self.color_stones) == 2 
# -----------------------------------------------------------------------------		
class DeadManager:
	def __init__(self):
		self.id_deads = {}
		
	def new_dead(self,game):
		self.id_deads[game.id] = Dead()
		
	def remove_dead(self,game):
		self.id_deads[game.id]
		
	def add_stones(self,game,color,stones):
		dead = self.id_deads[game.id]
		dead.add(color,stones)
		
	def is_dead_ok(self,game):
		dead = self.id_deads[game.id]
		return dead.is_ok()
# -----------------------------------------------------------------------------
class BrokenTimer:
    # when line broken,we wait for him 5 minutes
	timeout = 60*5
	def __init__(self):
		self.timer_running = False
		self.game_user_timeout = []
		
	def add_game_user(self,game,user):
		self.game_user_timeout.append((game,user,BrokenTimer.timeout))
		if not self.timer_running:
            now_loop = asyncio.get_running_loop()
            asyncio.run_coroutine_threadsafe(self.start_timer(1),now_loop)
            
	def remove_user(self,user):
		self.game_user_timeout = filter(lambda u,_,_ : u != user, self.game_user_timeout)
	
	def game_over(self,game):
		self.game_user_timeout = filter(lambda g,_,_ : g != game,self.game_user_timeout)
		
	def countdown(self):
		gu = map(lambda g,u,t : (g,u,t-1),self.game_user_timeout)
		self.game_user_timeout = filter(lambda g,u,t : t > 0,gu)
		for game,user,timeout in self.game_user_timeout:
			msg = message.Msg()
			msg.type = message.MsgType.TCountdown
			msg.countdown.game_id = game.id
			msg.countdown.user = user
			msg.countdown.timeout = timeout
			users_manager.send_user_msg(user,msg)
			users_manager.send_users_msg(game.watchers,msg)
		for game,user,_ in filter(lambda g,u,t: t <= 0,gu):
			other_user = game_other_user(game,user)
			result = message.Result()
			result.end_type  = message.EndType.time_out
			result.winner = users_manager.game_user_color(game,other_user)
			games_manager.end_game(game,result)
	
	def one_round_run(self,future):
		self.countdown()
		
	async def delay(self,time):
		await asyncio.sleep(time)
		
	async def start_timer(self,time):
		self.timer_running = True
		while len(self.game_user_timeout) > 0:
			future= asyncio.ensure_future(self.delay(time))
			future.add_done_callback(self.one_round_run)
			await future
		self.timer_running = False
# -----------------------------------------------------------------------------
class LineBrokenManager:
	def __init__(self):
		self.broken_users = []
		self.broken_timer = BrokenTimer()
	
	def is_user_broken(self,user):
		return user in self.broken_users
		
	def user_line_broken(self,user):
		# first,when line broken,protocol is useless
		users_manager.remove_user(user)
		self.broken_users.append(user)
		
		for game in user.games:
			#as player
			if user in game.players:
				other_user = game_other_user(game.players,user)
				if not self.is_user_broken(other_user):
					if not game.line_broken:
						game.line_broken = True
						# first,tell other user the game line broken!
						msg = message.Msg()
						msg.type = message.MsgType.TLineBroken
						msg.line_broken.game_id = game.id
						users_manager.send_user_msg(other_user,msg)
					else:
						# already linebroken,nothing to do another
						pass
				# line broken count down
				self.broken_timer.add_game_user(game,user)
			#as watcher
			if user in game.watchers:
				# wather line broken
				game.watchers.remove(user)
				# wacher leave msg
				msg = message.Msg()
				msg.type = message.MsgType.TWatcherLeave
				msg.watcher_leave.game_id = game.id
				msg.watcher_leave.user = user
				users_manager.send_users_msg(game.players + game.watchers,msg)
				
	def user_come_back(self,user):
		# line broken user come back.
		# some game paused for the user line broken,we should rerun it
		assert user in self.broken_users
		index = self.broken_users.index(user)
		myuser = self.broken_users[index] # myuser have games
		user.games = myuser.games
		
		self.broken_users.remove(user)
		self.broken_timer.remove_user(user)
		
		for game in user.games:
			# as player
			if user in game.players:
				# first,give the game data to the comeback user
				msg = message.Msg()
				msg.type = message.MsgType.TGameData
				msg.game_data.game = game
				users_manager.send_user_msg(user,msg)
				# can we restart the game? it's about other_user
				other_user = msgserver.game_other_user(game.players,user)
				if not self.is_user_broken(other_user):
					# i come back,and you not line broken,so we can start again
					assert game.line_broken == True
					game.line_broken = False
					msg = message.Msg()
					msg.type = message.MsgType.TComeBack
					msg.come_back.game_id = game.id
					users_manager.send_users_msg(game.players,msg)
				else:
					# means other_user linebroken too,and not login now. nothing to do!
					pass
# -----------------------------------------------------------------------------
class UsersManager:
	def __init__(self):
		self.user_protocol = {}
	
	def add_user(self,user,protocol):
		protocol.user = user
		self.user_protocol[user] = protocol
	
	def remove_user(self,user):
		del self.user_protocol[user]

	def send_user_msg(self,user,msg):
		self.user_protocol[user].send_msg(msg)
	
	def send_users_msg(self,users,msg):
		map(lambda user: self.send_user_msg(user,msg),users)
# -----------------------------------------------------------------------------
class GamesManager:
	def __init__(self):
		self.live_games = []
		self.dead_games = []
		
	def create_game(self,rule,user1,user2):
        game = Game(rule,user1,user2)
        
        self.live_games.append(game)
        
        msg = message.Msg()
        msg.type = message.MsgType.TGameData
        msg.game_data.game = game
        users_manager.send_user_msg(game.players,msg)
        
        return game
	
	def end_game(self,game,result):
	    game.game_over(result)
		
		for user in game.players:
		    user.remove(game)
		
		self.live_games.remove(game)
		self.dead_games.append(game)
		# tell broken timer,the game is dead
		line_broken_manager.broken_timer.game_over(game)
		
		msg = message.Msg()
		msg.type = message.MsgType.TGameOver
		msg.game_over.game_id = game.id
		msg.game_over.result.CopyFrom(result)
		
		users_manager.send_users_msg(game.players,msg)
		users_manager.send_users_msg(game.watchers,msg)
# -----------------------------------------------------------------------------
class MsgServerProtocol(msgprotocol.MsgProtocol):
    def __init__(self):
        msgprotocol.MsgProtocol.__init__(self)
        self.user = None

    # override
    def connection_lost(self,exc):
        logging.debug("connection losted")
        msgprotocol.MsgProtocol.connection_lost(self,exc)
        if exc is not None:
        	logging.info("---exit EXCEPTION---")
			if self.user is not None:
				line_broken_manager.user_line_broken(user)
    # override
    def process_msg(self,msg):
        logging.debug(msg)
        
        # login 
        if msg.type == message.MsgType.TLogin:
            user = msgdb.get_user(msg.login.name)
            if user is not None:
            	# found the user from users db
                logging.debug("---login ok!---")
        		users_manager.add_user(user,self)
                #if i am line broken
                if line_broken_manager.is_user_broken(user):
                	line_broken_manager.user_come_back(user)
                	
                msg = message.Msg()
                msg.type = message.MsgType.TLoginOk
                self.send_msg(msg)
            else:
            	# the user not in db
                logging.debug("---login error!---")
                msg = message.Msg()
                msg.type = message.MsgType.TLoginFail
                self.send_msg(msg)
        else:
        	# no that msg!
            logging.info("not support the type msg now")
# -----------------------------------------------------------------------------
async def main():
    loop = asyncio.get_running_loop()
    
    server = await loop.create_server(
        lambda: MsgServerProtocol(), '127.0.0.1', 5678)
    
    async with server:
        await server.serve_forever()
# -----------------------------------------------------------------------------
if __name__ == '__main__':
	users_manager = UsersManager()
	games_manager = GamesManager()
	line_broken_manager = LineBrokenManager()
	dead_manager = DeadManager()

	asyncio.run(main())