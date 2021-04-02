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
        },

    'splash' : {
        'name' : 'splash',
        'type' : 'normal',
        'point' : -10
        },
    
    'psychic' : {
        'name' : 'psychic',
        'type' : 'psychic',
        'point' : 20
        }
    
    }

pokemon = {
    'charmander' : {
        "original_name" : "Charmander",
        'element_type' : "fire",
        'hp' : 55,
        'attack_points' : 15,
        'move' : [ moves["ember"], moves["flamewheel"], moves["splash"] ]
         },

     'pikachu' : {
        'original_name' : "Pikachu",
        'element_type' : "Electric",
        'hp' : 50,
        'attack_points' : 10,
        'move' : [ moves["thunderbolt"], moves["volt_tackle"], moves["splash"] ]
        
         },

    'mewtwo' : {
        'original_name' : "Mewtwo",
        'element_type' : "psychic",
        'hp' : 100,
        'attack_points' : 50,
        'move' : [ moves["psychic"] ]
        }
    
    }

'''*****************************************************************************************************************************'''

class Trainer():
    #class for each human trainer
    #string trainer_name
    #list trainer_pokemon stores list of all trainer's pokemon
        
    def __init__(self, trainer_name, trainer_pokemon):
        self.trainer_name = trainer_name
        self.trainer_pokemon = trainer_pokemon
        self.trainer_fainted_pokemon = []

    def meet_wild_pokemon(self):
        #decision of a trainer is decided
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
        #takes an integer id and return a corresponding Pokemon(or LegendaryPokemon) object
        if id == 0:
            return Pokemon("charmander","charmander")
        elif id == 1:
            return Pokemon("pikachu","pikachu")
        elif id == 2:
            return LegendaryPokemon("mewtwo", "Mewtwo")

    def catch_pokemon(self,opponent_pokemon):
        #catch any pokemon and append it to trainer_pokemon list
        #opponent_pokemon is Pokemon object            
        print("%s threw a pokeball.. nice catch.. you caught a %s" %(self.trainer_name, opponent_pokemon.original_name) )
        nick_name = input("Give nick name to your %s " %(opponent_pokemon.original_name))
        opponent_pokemon.nick_name = nick_name
        self.trainer_pokemon.append(opponent_pokemon)
        file = open("trainerpoke.txt", "a")
        file.write("%s %s\n" %(opponent_pokemon.original_name, nick_name))
        file.close()
        

    def battle_pokemon(self,opponent_pokemon):
        #trainer v/s pokemon(wild only) battle
        while len(self.trainer_pokemon) > 0 and not opponent_pokemon.is_dead():
            for creature in self.trainer_pokemon:
                print("%d : %s " %(self.trainer_pokemon.index(creature),creature.nick_name))
            trainer_pokemon_id = int(input("\nwhich pokemon to chose? "))
        
            #checking out of bound entry
            while trainer_pokemon_id not in range(len(self.trainer_pokemon)):
                print("\nThere is no such pokemon in your party.. try again")
                trainer_pokemon_id = int(input("\nwhich pokemon to chose? "))
        
            trainer_pokemon = self.trainer_pokemon[trainer_pokemon_id]                              #select a pokemon object from trainer_pokemon
            print("go %s " %(trainer_pokemon.nick_name))
                                                           
            pokemon_that_has_lost_the_battle = trainer_pokemon.start_battle(opponent_pokemon)       #battle opponent_pokemon object
            if pokemon_that_has_lost_the_battle == trainer_pokemon:
                self.trainer_pokemon.remove(pokemon_that_has_lost_the_battle)
                self.trainer_fainted_pokemon.append(pokemon_that_has_lost_the_battle)
        else:
            if len(self.trainer_pokemon) == 0:
                print("\nyou have no fighting pokemon left")
            else:
                print("\nyou move on")
        

    def battle_npc_trainer(self, npc_trainer):
        #trainer v/s trainer battle
        while len(self.trainer_pokemon) > 0 and len(npc_trainer.trainer_pokemon) > 0:
            npc_pokemon_number = randint(0, len(npc_trainer.trainer_pokemon)-1)
            npc_pokemon = npc_trainer.trainer_pokemon[npc_pokemon_number]
            print("\n%s chose %s\n" %(npc_trainer.trainer_name, npc_pokemon.original_name))
            
            for creature in self.trainer_pokemon:
                print("%d : %s " %(self.trainer_pokemon.index(creature),creature.nick_name))
            player_pokemon_number = int(input("\nwhich pokemon to chose? "))

            #checking out of bound entry
            while player_pokemon_number not in range(len(self.trainer_pokemon)):
                print("\nThere is no such pokemon in your party.. try again")
                player_pokemon_number = int(input("\nwhich pokemon to chose? "))

            trainer_pokemon = self.trainer_pokemon[player_pokemon_number]                           #select a pokemon object from trainer_pokemon
            print("go %s " %(trainer_pokemon.nick_name))

            pokemon_that_has_lost_the_battle = trainer_pokemon.start_battle(npc_pokemon)            #battle opponent_pokemon object

            if pokemon_that_has_lost_the_battle == trainer_pokemon:
                self.trainer_pokemon.remove(pokemon_that_has_lost_the_battle)
                self.trainer_fainted_pokemon.append(pokemon_that_has_lost_the_battle)
                
            elif pokemon_that_has_lost_the_battle == npc_pokemon:
                npc_trainer.trainer_pokemon.remove(pokemon_that_has_lost_the_battle)
                npc_trainer.trainer_fainted_pokemon.append(pokemon_that_has_lost_the_battle)
        else:
            if len(self.trainer_pokemon) == 0:
                print("\n %s won the match" %(npc_trainer.trainer_name))
            elif len(npc_trainer.trainer_pokemon) == 0:
                print("\n %s won the match" %(self.trainer_name))
                

'''*****************************************************************************************************************************'''

class Pokemon(): 
    def __init__(self, poke_original_name, poke_nick_name):
        #initialise value from pokemon dictionary
        self.original_name = poke_original_name
        self.nick_name = poke_nick_name
        self.element_type = pokemon[poke_original_name]["element_type"]
        self.hp = pokemon[poke_original_name]["hp"]
        self.attack_points = pokemon[poke_original_name]["attack_points"]
        self.move = pokemon[poke_original_name]["move"]
    
    def use_attack(self,opponent,move):
        #single attack and its effects between 2 pokemon 
        print("\n%s used %s on %s..its a hit" %(self.nick_name, move["name"] , opponent.nick_name) )
        opponent.hp -= self.attack_points + move["point"]
        print("\n%s has %s hp remaining" %(opponent.nick_name ,str(opponent.hp)))


    def start_battle(self,opponent):
        #start battle between 2 pokemon till one dies
        #returns the defeated pokemon
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
                return opponent
                break
            
            num = randint(0, len(opponent.move)-1 )
            opponent.use_attack(self, opponent.move[num])
            if self.is_dead():
                print("\n%s fainted.. %s won" %(self.nick_name,opponent.nick_name))
                return self
                break

    def is_dead(self):
        #check whether a pokemon is fainted
        if self.hp <= 0:
            return True
        else:
            return False
        
'''*****************************************************************************************************************************'''
#this class derived from class Pokemon and uses its variables and methods

class LegendaryPokemon(Pokemon):
    #overridden method
    def use_attack(self,opponent,move):
        print("\nlegendary pokemon %s used %s on %s..its a massive hit" %(self.original_name, move["name"] , opponent.nick_name) )
        opponent.hp -= 500
        print("\n%s has %s hp remaining" %(opponent.nick_name ,str(opponent.hp)))
        
'''*****************************************************************************************************************************'''
player_poke = []
file = open("trainerpoke.txt", "r")
count = 0
while True:
    line = file.readline()
    if not line:
        break
    poke = line.split()
    player_poke.append(Pokemon(poke[0],poke[1]))
    
file.close()

ash = Trainer("ash",player_poke)

#gary = Trainer("gary",[Pokemon("pikachu","garpika"), Pokemon("charmander","garcharm")] )
#ash.battle_npc_trainer(gary)
ash.meet_wild_pokemon()




