import random
'''
A fazer: Aumentar base de dados
'''
questions_sports = [["Which Club has the most Champions League trofies?\nA) Milan FC\nB) Real Madrid\nC) Barcelona\nD) Manchester United ","B"],\
                        ["Who was the first 7 time F1 world champion?\nA) Lewis Hamilton FC\nB) Max Vestappen\nC) Michael Shumacher\nD)Ayrton Senna ","C"]]
    
special_sports_questions = [["Who is the Champions Legue's top Scorer of all time?\nA) Cristiano Ronaldo\nB) Lionel Messi\nC) Robert Lewandauski\nD) Neymar Jr","A"],\
                                ["Which country has won the most FIFA World Cup titles in men's football?\nA) Brazil\nB)Germany\nC) France\nD)Argentina ","A"]]

def player_names(number_of_players):
    names_list = ()
    print("\nPlease input the players'names in playing order")
    for i in range(number_of_players):
        name = input("What is the player's name? ")
        if name not in names_list:
            print(f"\nHello {name} welcome to the game\n")
            names_list += (name,)
        else:
            print("That name is alredy attributed to another player please input another player-name: ")
            i-=1
        
    return names_list

def ending_the_game(scores,name_list):
    tie_braking_points = []
    for points in scores.values():
        tie_braking_points.append(points[0]+ 2 * points[1])
    winner_points = 0
    for winner,j in enumerate(tie_braking_points):  
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

        

start_game = game()
