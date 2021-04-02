from random import randint
moves = {
    'thunderbolt' : {
        'name' : 'Thunderbolt',
        'type' : 'Electric',
        'point' : 15
        },

    'ember' : {
        'name' : 'Ember',
        'type' : 'fire',
        'point' : 6
        },
    
    'flamewheel' : {
        'name' : 'Flamewheel',
        'type' : 'fire',
        'point' : 15
        },

    'volt_tackle' : {
        'name' : 'Volt tackle',
        'type' : 'Electric',
        'point' : 18
        }
    
    }

pokes = {
    0 : "Charmander",
    1 : "Pikachu"
    }

class Player():
    """ class for player
        string player_name
        list player_pokemon stores list of all player pokemon
        """
    def __init__(self, player_name, player_pokemon):
        self.player_name = player_name
        self.player_pokemon = player_pokemon

    def meet_wild_pokemon(self):
        """decision of a player is decided"""
        random_poke_id = randint(0,1)
        random_pokemon = pokes[random_poke_id]
        decision = input("you saw a wild %s.. what will you do? " %(random_pokemon))
        if decision == "f":
            self.battle_pokemon(random_poke_id)
        elif decision == "c":
            self.catch_pokemon(random_poke_id)
        else:
            print("you ran away")

    def battle_pokemon(self,pokemon_id):
        """battle any pokemon mentioned by pokemon_id
            int pokemon_id            
        """
        player_pokemon_id = int(input("which pokemon to chose? "))
        player_pokemon = self.player_pokemon[player_pokemon_id]                 #select a pokemon object from player_pokemon
        print("go %s " %(player_pokemon.nick_name))
        if pokemon_id == 0:                                                     #create new opponent pokemon object(based on pokemon_id)
            player_pokemon.start_battle(Charmander("Charmander"))
        elif pokemon_id == 1:
            player_pokemon.start_battle(Pikachu("Pikachu"))

    def catch_pokemon(self,pokemon_id):
        """catch any pokemon mentioned by pokemon_id and append it to player_pokemon list
            int pokemon_id            
        """
        pokemon = pokes[pokemon_id]
        print("%s threw a pokeball.. nice catch.. you caught a %s" %(self.player_name,pokemon) )
        nick_name = input("Give nick name to your %s " %(pokemon))
        if pokemon_id == 0:
            self.player_pokemon.append(Charmander(nick_name))
        elif pokemon_id == 1:
            self.player_pokemon.append(Pikachu(nick_name))   

class Pokemon(): 
	    
    def use_attack(self,opponent,move):
        print("\n%s used %s on %s..its a hit" %(self.nick_name, move["name"] , opponent.nick_name) )
        opponent.hp -= self.attack_points + move["point"]
        print("\n%s has %s hp remaining" %(opponent.nick_name ,str(opponent.hp)))


    def start_battle(self,opponent):
        while(self.hp > 0 and opponent.hp > 0):
            my_move_id = int(input("\nwhich move to use? "))
            self.use_attack(opponent,self.move[my_move_id])
            if opponent.is_dead():
                print("\n%s is dead %s won" %(opponent.nick_name,self.nick_name))
                break
            
            num = randint(0,1)
            opponent.use_attack(self, opponent.move[num])
            if self.is_dead():
                print("\n%s is dead %s won" %(self.nick_name,opponent.nick_name))
                break

    def is_dead(self):
        if self.hp <= 0:
            return True
        else:
            return False
        
class Charmander(Pokemon):
    
    def __init__(self, nick_name):
        self.original_name = "Charmander"
        self.element_type = "fire"
        self.hp = 55
        self.attack_points = 15
        self.nick_name = nick_name
        self.move = [ moves["ember"], moves["flamewheel"] ]

class Pikachu(Pokemon):
    
    def __init__(self, nick_name):
        self.original_name = "Pikachu"
        self.element_type = "Electric"
        self.hp = 50
        self.attack_points = 10
        self.nick_name = nick_name
        self.move = [ moves["thunderbolt"], moves["volt_tackle"] ]
        


ash = Player("ash",[Pikachu("pikachu"),Charmander("charmi")])
ash.meet_wild_pokemon()


