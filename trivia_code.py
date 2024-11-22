import random
import json
'''
A fazer: Aumentar base de dados

Traceback (most recent call last):
  File "/Users/martimoliveira/Documents/GitHub/Trivia/trivia_code.py", line 203, in <module>
    start_game = game()
                 ^^^^^^
  File "/Users/martimoliveira/Documents/GitHub/Trivia/trivia_code.py", line 143, in game
    question = draw_question(question_number,chosen_category,special)[0]
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/martimoliveira/Documents/GitHub/Trivia/trivia_code.py", line 62, in draw_question
    return special_sports_questions[question_number-1]
           ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
IndexError: list index out of range

When trying to get the 2nd right in a row
'''
questions_sports = [["Which Club has the most Champions League trofies?\nA) Milan FC\nB) Real Madrid\nC) Barcelona\nD) Manchester United ","B"],\
                    ["Who was the first 7 time F1 world champion?\nA) Lewis Hamilton FC\nB) Max Vestappen\nC) Michael Shumacher\nD)Ayrton Senna ","C"],\
                    ["Which sport is known as 'The Beautiful Game'?\nA) Cricket\nB) Basketball\nC) Soccer\nD) Tennis ", "C"],
                    ["How many players are there in a soccer team on the field?\nA) 9\nB) 10\nC) 11\nD) 12 ", "C"],
                    ["Which sport uses a bat and a ball?\nA) Soccer\nB) Cricket\nC) Tennis\nD) Swimming ", "B"],
                    ["What color flag is waved in Formula 1 to indicate the race is over?\nA) Red\nB) Green\nC) Yellow\nD) Checkered ", "D"],
                    ["Which country hosts the Tour de France?\nA) Italy\nB) Spain\nC) France\nD) Germany ", "C"],
                    ["How many points is a touchdown worth in American football?\nA) 5\nB) 6\nC) 7\nD) 3 ", "B"],
                    ["Which sport is played at Wimbledon?\nA) Basketball\nB) Soccer\nC) Tennis\nD) Golf ", "C"],
                    ["What is the shape of a standard soccer ball?\nA) Square\nB) Round\nC) Oval\nD) Triangle ", "B"],
                    ["What is the main piece of equipment used in golf?\nA) Racket\nB) Bat\nC) Club\nD) Paddle ", "C"],
                    ["Which sport involves shooting an arrow at a target?\nA) Fencing\nB) Archery\nC) Shooting\nD) Golf ", "B"]]
    
special_sports_questions = [["Who is the Champions Legue's top Scorer of all time?\nA) Cristiano Ronaldo\nB) Lionel Messi\nC) Robert Lewandauski\nD) Neymar Jr","A"],\
                            ["Which country has won the most FIFA World Cup titles in men's football?\nA) Brazil\nB)Germany\nC) France\nD)Argentina ","A"]]

def player_names(number_of_players):
    names_list = ()
    print("\nPlease input the players' names in playing order")
    for i in range(number_of_players):
        name = input("What is the player's name? ")
        if name not in names_list:
            print(f"\nHello {name} welcome to the game\n")
            names_list += (name,)
        else:
            print("That name is alredy attributed to another player please input another player-name: ")
            i-=1
        
    return names_list

def default_info():
    categories = ("Sports","History","Culture","All")
    
    while True:
        chosen_category =  input('\nCategory options: "Sports", "History", "Culture", "All" \n\nWhat is the category you wish to play? ')
        if chosen_category not in categories:
            print("The input was not a possible category.\n")
        else:
            break

    while True:
        number_of_players = (input("\nHow many players are there in this game? "))
        try:
            number_of_players = int(number_of_players)
            if 2<= number_of_players:
                break
            print("At least 2 players.")
        except:
            print("The input was not a possible number of players.\n")

    streak = 0
    playing_player = 1
    name_list = player_names(number_of_players)
    scores = {}
    done_questions = []
    done_special_questions = []
    for names in name_list:
        if names not in scores:
            scores[names] = [0,0]

    default_information = {"chosen_category": chosen_category,
                           "number_of_players":number_of_players,
                            "name_list": name_list,
                            "playing_player": playing_player,
                            "streak": streak,
                            "done_questions": done_questions,
                            "done_special_questions": done_special_questions,
                            "scores":scores
                            }
    return default_information

def ending_the_game(scores,name_list):
    tie_braking_points = []
    for points in scores.values():
        tie_braking_points.append(points[0]+ 2 * points[1])
    winner_points = 0
    for j in tie_braking_points:  
        if j > winner_points:
            winner_points = j
    multiple_winners=[]
    for y,x in enumerate(tie_braking_points):
        if x == winner_points:
            multiple_winners.append(name_list[y])
    winner_counter = len(multiple_winners)
    winer_names = ""
    for k in multiple_winners:    
        winer_names = winer_names + str(k) + " "
    if winner_counter != 1:
        return(f"\nCongrats {winer_names} you all won, you scored {winner_points} tie-braking points\n")
    
    else:
        return(f"Congrats {multiple_winners[0]} you won, you scored {winner_points} tie-braking points\n")

def draw_question(question_number,category,special): #Continue to make questions
    if category == "Sports" and not special:
        return questions_sports[question_number-1]
    elif category == "Sports" and special:
        return special_sports_questions[question_number-1]

def number_of_questions(category,special=False):
    if category == "Sports" and not special:
        return len(questions_sports)
    elif category == "Sports" and special:
        return len(special_sports_questions)

def game():
    print("\nWelcome to the Trivia Game\n")
    print("These are the Rules:\n\n1. The first player to correctly answer 7 questions and 3 special questions wins.")
    print("2. There can be from 2 to as many players as you want.")
    print("3. If you get a normal questions right you play again.")
    print("4. If you get 2 questions right in a row will get the chance to answer a special question.")
    print("5. Even if you get the special question right you won't play again.")
    print("6. The youngest player will start the game and after the game will continue clockwise.")
    print("7. If you end the game early, wins whoever has the most tiebraker points: question points + special question points (are worth 2 tiebraker points)\n")
    print('If you want to end the game answer "quit" to any question')
    print('If you want to save the game answer "save" to any question')

    while True:
        load = input("\nDo you wish to load a save file? ")
        if load == "yes":
            information =load_game()
            chosen_category = information["chosen_category"]
            number_of_players = information["number_of_players"]
            name_list = information["name_list"]
            playing_player = information["playing_player"]
            streak = information["streak"]
            done_questions = information["done_questions"]
            done_special_questions = information["done_special_questions"]
            scores = information["scores"]
            break
        elif load == "no":
            information = default_info()
            chosen_category = information["chosen_category"]
            number_of_players = information["number_of_players"]
            name_list = information["name_list"]
            playing_player = information["playing_player"]
            streak = information["streak"]
            done_questions = information["done_questions"]
            done_special_questions = information["done_special_questions"]
            scores = information["scores"]
            break
        else:
            print("Invalid input answer (yes/no)")
    

    game_running = True
    while game_running:

        name = name_list[playing_player-1]
        special = False
        num_questions = number_of_questions(chosen_category,special)
        print(f"\n{name} it's your turn\n")
        if streak == 2:
            special = True
        question_number = random.randint(1,num_questions)
        while question_number in done_questions and not special or question_number in done_special_questions and  special:
            if (len(done_questions) == num_questions and not special) or (len(done_special_questions) == num_questions and special):
                repeat = input("You have finished this categories' questions. Do you want to finish the game like this or would like to repeat questions?(end/repeat): ")
                if repeat == "end":
                    game_running = False
                    tie_breaker = ending_the_game(scores,name_list)
                    print(tie_breaker)
                    break
                elif repeat == "repeat":
                    done_questions = []
                    done_special_questions = []
            else:
                question_number = random.randint(1,num_questions)
        
        if game_running == True:
            if special:
                done_special_questions.append(question_number)
            else:
                done_questions.append(question_number)
            question = draw_question(question_number,chosen_category,special)[0]
            answer = draw_question(question_number,chosen_category,special)[1]
            print(question)
            guess = input("\nANSWER: ")
            if guess == "quit":
                game_running == False
                tie_breaker = ending_the_game(scores,name_list)
                print(tie_breaker)
                break
            elif guess == "save":
                save = save_game(chosen_category,number_of_players,name_list,playing_player,streak,done_questions,done_special_questions,scores)
                print("\nGame saved successfully.\n")
                break

            elif guess.upper() == answer.upper() and not special:
                print(f"You are correct, the answer was: {answer}")
                streak +=1
                scores[name][0] += 1
                
            elif guess.upper() == answer.upper() and  special:
                print(f"You are correct, the answer was: {answer}")
                streak = 0
                scores[name][1] += 1
                if playing_player +1 <= number_of_players:
                    playing_player += 1
                else:
                    playing_player = 1
                
            else:
                print(f"Wrong answer, the answer was: {answer}")
                streak = 0
                if playing_player +1 <= number_of_players:
                    playing_player += 1
                else:
                    playing_player = 1
        if game_running == False:
            print(tie_breaker)

        if scores[name][0]>=7 and scores[name][1]>=3:
            print(f"\nCongrats {name}you won, your score was {scores[name]}")
            game_running = False

def save_game(chosen_category,number_of_players,name_list,playing_player,streak,done_questions,done_special_questions,scores):
    data_to_save = {"chosen_category": chosen_category,
                    "number_of_players":number_of_players,
                    "name_list": name_list,
                    "playing_player": playing_player,
                    "streak": streak,
                    "done_questions": done_questions,
                    "done_special_questions": done_special_questions,
                    "scores":scores
                    }
    with open("save_file_trivia.json","w") as file:
        json.dump(data_to_save, file)  

def load_game():
    with open("save_file_trivia.json", "r") as file:
        loaded_data = json.load(file)
    print("Loaded data:", loaded_data)
    return loaded_data


start_game = game()
