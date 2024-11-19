import random

game_running = True

def player_names(number_of_players):
    names_list = ()
    print("\nPlease input the players'names in playing order")
    for i in range(number_of_players):
        name = input("What is the player's name? ")
        if name not in names_list:
            print(f"\nHello {name} welcome to the game")
            names_list += (name,)
        else:
            print("That name is alredy attributed to another player please input another player-name: ")
            i-=1
        
    return names_list
    
def draw_question(question_number,category,special): #Continue to make questions
    questions_sports = [["Which Club has the most Champions League trofies?\nA) Milan FC\nB) Real Madrid\nC) Barcelona\nD) Manchester United ","B"],\
                        ["Who was the first 7 time F1 world champion?\nA) Lewis Hamilton FC\nB) Max Vestappen\nC) Michael Shumacher\nD)Ayrton Senna ","C"]]
    if category == "Sports" and not special:
        return questions_sports[question_number-1]

def scores(player_name,player_list):
    scores = {}
    for names in player_list:
        scores[names] = [0,0]
    return scores[player_name]

def game():
    print("Welcome to the Trivia Game")
    print("These are the Rules:\n\n1. The first player to correctly answer 7 questions and 3 special questions wins.")
    print("2. There can be from 2 to as many players as you want.")
    print("3. If you get a normal questions right you play again.")
    print("4. If you get 2 questions right in a row will get the chance to answer a special question.")
    print("5. Even if you get the special question right you won't play again.")
    print("6. The youngest player will start the game and after the game will continue clockwise.\n")
    
    number_of_questions = 2
    categories = ("Sports","History","Culture","All")
    
    while True:
        chosen_category =  input('Category options: "Sports", "History", "Culture", "All" \nWhat is the category you wish to play? ')
        if chosen_category not in categories:
            print("The input was not a possible category.\n")
        else:
            break

    while True:
        number_of_players = (input("\nHow many players are there in this game? "))
        try:
            number_of_players = int(number_of_players)
            break
        except:
            print("The input was not a possible number of players.\n")

    playing_player = 1
    name_list = player_names(number_of_players)
    while game_running:
        name = name_list[playing_player-1]
        streak = 0
        special = False
        print(f"\n{name} it's your turn\n")
        player_score = scores(name,name_list)
        question_number = random.randint(1,number_of_questions)
        if streak == 2:
            special = True
        question = draw_question(question_number,chosen_category,special)[0]
        answer = draw_question(question_number,chosen_category,special)[1]
        print(question)
        guess = input("\nANSWER: ")
        if guess == answer and not special:
            print(f"You are correct, the answer was: {answer}.")
            streak +=1
            player_score[0] += 1
            
        elif guess == answer and  special:
            print(f"You are correct, the answer was: {answer}.")
            if playing_player +1 <= number_of_players:
                playing_player += 1
            else:
                playing_player = 1
            sreak = 0
            player_score[1] += 1
        else:
            print(f"Wrong answer, the answer was: {answer}.")
            if playing_player +1 <= number_of_players:
                playing_player += 1
            else:
                playing_player = 1
            sreak = 0
    if player_score == [7,3]:
        print(f"Congrats {name} you won")
        game_running == False

start_game = game()
print(start_game)
