import message_pb2 as message

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
        self.id = id_pool.new_id()
        self.state = None
        self.rule = None
        self.result = None
        self.stones = []
        self.watchers = []
        self.players = []
        self.colors = []
        self.clocks = []
    
    def pack(self):
        packed_game = message.Game()
        packed_game.id = self.id
        packed_game.state = self.state
        packed_game.rule.CopyFrom(self.rule)
        packed_game.result.CopyFrom(self.result)
        for stone in self.stones:
            packed_game.stones.add().CopyFrom(stone)
        for watcher in self.watchers:
            packed_game.watchers.add().CopyFrom(watcher.pack())
        for user in self.players:
            packed_game.players.add().CopyFrom(user.pack())
        for color in self.colors:
            packed_game.colors.add() = color
        for clock in self.clocks:
            packed_game.clocks.add().CopyFrom(clock)
        return game
        
    def unpack(packed):
        game = Game()
        game.id = packed.id
        game.state = packed.state
        game.rule = packed.rule
        game.result = packed.result
        for stone in packed.stones:
            game.stones.append(stone)
        for watcher in packed.watchers:
            game.watchers.append(User.unpack(watcher))
        for user in packed.players:
            game.players.append(User.unpack(user))
        for color in packed.colors:
            game.colors.append(color)
        for clock in packed.clocks:
            game.clocks.append(clock)
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
        
    def pack(self):
        user = message.User()
        user.name = self.name
        user.level = self.level
        return user
    
    def unpack(packed):
        user = User()
        user.name = packed.name
        user.level = packed.level
        return user
