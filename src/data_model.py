import message_pb2 as message
import random

def other_color(color):
    assert color in message.Color.values()
    if color == message.Color.black:
        return message.Color.white
    if color == message.Color.white:
        return message.Color.black

class IdPool:
    def __init__(self):
        self.not_used_ids = list(range(1,20))
        self.used_ids = []
        
    def new_id(self):
        # we always return the min() one
        if len(self.not_used_ids) > 0:
            min_id = min(self.not_used_ids)
            self.not_used_ids.remove(min_id)
        else:
            min_id = max(self.used_ids)+1
        self.used_ids.append(min_id)                                       
        return min_id
    
    def del_id(self,id):
        self.used_ids.remove(id)
        self.not_used_ids.append(id)
# -----------------------------------------------------------------------------
class Packer:
    def pack(self):
        pass
    def unpack(packed):
        pass
# -----------------------------------------------------------------------------
class Game(Packer):
    id_pool = IdPool()
    
    def __init__(self):
        self.stones = []
        self.watchers = []
        self.color_user = {}
        self.color_clock = {}
        self.removed_stones = []
        self.removed_ok_colors = []
    
    def new_game(rule,user1,user2):
        def other_user(user):
            assert user in [user1,user2]
            if user == user1:
                return user2
            if user == user2:
                return user1
                
        game = Game()    
        game.line_broken = False
        game.id = Game.id_pool.new_id()
        game.state = message.State.playing
        game.rule = rule
        
        # define the color from the rule
        if game.rule.who_first == message.WhoFirst.earmark:
            first_user = game.rule.first_user
            assert first_user in [user1,user2]
            game.color_user[message.Color.black] = first_user
            game.color_user[message.Color.white] = other_user(first_user)
        if game.rule.who_first == message.WhoFirst.random:
            random_color = random.choice([message.Color.black,message.Color.white])
            game.color_user[random_color] = user1
            game.color_user[other_color(random_color)] = user2
            
        # set clock
        game.color_clock[message.Color.black] = message.Clock()
        game.color_clock[message.Color.white] = message.Clock()
        
        return game
        
    def game_over(self,result):
        self.state = message.State.stopped
        self.result.CopyFrom(result)
    
    def pack(self):
        packed_game = message.Game()
        packed_game.id = self.id
        packed_game.state = self.state
        packed_game.rule.CopyFrom(self.rule)
        
        if self.state == message.State.stopped:
            packed_game.result.CopyFrom(self.result)
            
        for stone in self.stones:
            packed_game.stones.append(stone)
        for watcher in self.watchers:
            packed_game.watchers.append(watcher.pack())
        for color in message.Color.values():
            packed_game.colors.append(color)
            packed_game.clocks.append(self.color_clock[color])
            packed_game.players.append(self.color_user[color].pack())
        for stone in self.removed_stones:
            packed_game.removed_stones.append(stone)

        return packed_game
        
    def unpack(packed):
        game = Game()
        game.id = packed.id
        game.state = packed.state
        game.rule = packed.rule
        game.result = packed.result
        game.line_broken = packed.line_broken
        
        for stone in packed.stones:
            game.stones.append(stone)
        for watcher in packed.watchers:
            game.watchers.append(User.unpack(watcher))
        for index,color in enumerate(packed.colors):
            game.color_user[color] = User.unpack(packed.players[index])
            game.color_clock[color] = packed.clocks[index]
        for stone in packed.removed_stones:
            game.removed_stones.append(stone)
            
        return game
# -----------------------------------------------------------------------------
class User(Packer):
    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.games = []
        
    def remove_game(self,game):
        self.games.remove(game)
        
    def add_game(self,game):
        self.games.append(game)
        
    def __hash__(self):
        return hash(self.name)
        
    def __eq__(self,other):
        return self.name == other.name
        
    def __str__(self):
        return self.name+"("+self.level+")"
        
    def pack(self):
        user = message.User()
        user.name = self.name
        user.level = self.level
        return user
    
    def unpack(packed):
        return User(packed.name,packed.level)
