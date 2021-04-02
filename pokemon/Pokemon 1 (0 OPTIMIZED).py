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

pokemon = {
    'charmander' : {
        "original_name" : "Charmander",
        'element_type' : "fire",
        'hp' : 55,
        'attack_points' : 15,
        'move' : [ moves["ember"], moves["flamewheel"] ]
         },

     'pikachu' : {
        'original_name' : "Pikachu",
        'element_type' : "Electric",
        'hp' : 50,
        'attack_points' : 10,
        'move' : [ moves["thunderbolt"], moves["volt_tackle"] ]
        
         }
    }

'''*****************************************************************************************************************************'''

class Trainer():
##        class for each human trainer
##        string trainer_name
##        list trainer_pokemon stores list of all trainer's pokemon
        
    def __init__(self, trainer_name, trainer_pokemon):
        self.trainer_name = trainer_name
        self.trainer_pokemon = trainer_pokemon

    def meet_wild_pokemon(self):
##        """decision of a trainer is decided"""
        random_poke_id = randint(0, len(pokemon)-1)                               
        random_pokemon = self.find_pokemon_by_id(random_poke_id)                
        decision = input("you saw a wild %s.. what will you do?\n f : fight\n c : catch \n other : run away \n" %(random_pokemon.original_name))
        if decision == "f":
            self.battle_pokemon(random_pokemon)
        elif decision == "c":
            self.catch_pokemon(random_pokemon)
        else:
            print("you ran away")

    def find_pokemon_by_id(self, id):
##      takes an integer id and return a corresponding Pokemon object
        if id == 0:
            return Pokemon("charmander","charmander")
        elif id == 1:
            return Pokemon("pikachu","pikachu")
        

    def battle_pokemon(self,opponent_pokemon):
##        """battle any pokemon object
##            opponent_pokemon is Pokemon object           
##        """
        for creature in self.trainer_pokemon:
            print("%d : %s " %(self.trainer_pokemon.index(creature),creature.nick_name))
        trainer_pokemon_id = int(input("\nwhich pokemon to chose? "))
        
        #checking out of bound entry
        while trainer_pokemon_id not in range(len(self.trainer_pokemon)):
            print("\nThere is no such pokemon in your party.. try again")
            trainer_pokemon_id = int(input("\nwhich pokemon to chose? "))
        
        trainer_pokemon = self.trainer_pokemon[trainer_pokemon_id]                 #select a pokemon object from trainer_pokemon
        print("go %s " %(trainer_pokemon.nick_name))
                                                           
        trainer_pokemon.start_battle(opponent_pokemon)                           #battle opponent_pokemon object
        

    def catch_pokemon(self,opponent_pokemon):
##        """catch any pokemon and append it to trainer_pokemon list
##            opponent_pokemon is Pokemon object            
##        """
        print("%s threw a pokeball.. nice catch.. you caught a %s" %(self.trainer_name, opponent_pokemon.original_name) )
        nick_name = input("Give nick name to your %s " %(opponent_pokemon.original_name))
        opponent_pokemon.nick_name = nick_name
        self.trainer_pokemon.append(opponent_pokemon)

'''*****************************************************************************************************************************'''

class Pokemon(): 
    def __init__(self, poke_original_name, poke_nick_name):
##        #initialise value from pokemon dictionary
        self.original_name = poke_original_name
        self.nick_name = poke_nick_name
        self.element_type = pokemon[poke_original_name]["element_type"]
        self.hp = pokemon[poke_original_name]["hp"]
        self.attack_points = pokemon[poke_original_name]["attack_points"]
        self.move = pokemon[poke_original_name]["move"]
    
    def use_attack(self,opponent,move):
##        #single attack and its effects between 2 pokemon 
        print("\n%s used %s on %s..its a hit" %(self.nick_name, move["name"] , opponent.nick_name) )
        opponent.hp -= self.attack_points + move["point"]
        print("\n%s has %s hp remaining" %(opponent.nick_name ,str(opponent.hp)))


    def start_battle(self,opponent):
##        """start battle between 2 pokemon till one dies"""
        while(self.hp > 0 and opponent.hp > 0):
            for eachmove in self.move:
                print("%d : %s " %(self.move.index(eachmove), eachmove["name"]))
            my_move_id = int(input("\nwhich move to use? "))

            #out of bound move check
            while my_move_id not in range(len(self.move)):
                print("\nno such move.. try again")
                my_move_id = int(input("\nwhich move to use? "))
            
            self.use_attack(opponent,self.move[my_move_id])
            if opponent.is_dead():
                print("\n%s fainted.. %s won" %(opponent.nick_name,self.nick_name))
                break
            
            num = randint(0, len(opponent.move)-1 )
            opponent.use_attack(self, opponent.move[num])
            if self.is_dead():
                print("\n%s fainted.. %s won" %(self.nick_name,opponent.nick_name))
                break

    def is_dead(self):
##      check whether a pokemon is fainted
        if self.hp <= 0:
            return True
        else:
            return False
'''*****************************************************************************************************************************'''
        

ash = Trainer("ash",[Pokemon("pikachu","piki")])
ash.meet_wild_pokemon()
