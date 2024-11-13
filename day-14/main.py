from data import data
from random import choice
import os

vs_art = '''
        ____   ____     
    \   \ /   /_____
     \   Y   /  ___/
      \     /\___ \ 
       \___//____  >
'''
def get_random_person(data_list):
    """Choose a random person from the data list and remove them from the list."""
    person = choice(data_list)
    data_list.remove(person)
    return person

def display_person(label, person):
    print(f"Compare {label} : {person['name']} , {person['description']} , from {person['country']}")

def check_answer(person1, person2, user_answer):
    """Check if the user's answer is correct based on the follower count."""
    if person1['followers_count'] > person2['followers_count'] and user_answer == 'a':
        return True
    elif person2['followers_count'] > person1['followers_count'] and user_answer == 'b':
        return True
    else:
        return False

def play_game(data):
    score = 0
    game_continue = True
    person1 = get_random_person(data)

    while game_continue and len(data)>0:
        display_person("A" , person1)
        print(vs_art)

        person2 = get_random_person(data)
        display_person("B" , person2)

        user_answer = input("Which has more followers? Type 'A' or 'B'\n").lower()

        if check_answer(person1 , person2 , user_answer):
            score +=1
            os.system("cls" if os.name =="nt" else "clear")
            person1 = person2
        else:
            game_continue = False
            print("You lose")
            print(f"Your score is: {score}")

if __name__ == "__main__":
    play_game(data)
