#initialize global variablea
global score #the variable "score" is now global
score = int(0) #setting up the score


#defining the function
def runQuest (quest, chek, userA, corrA): #defining the function "run question", (question, checking if user answered question, user answer, correct answer)
    print(quest) #print the question
    while chek == False: #while user hasn't put in an answer (false)
        try: #try this..
            userA = int(input("Your answer >>> ")) #userA is the user's answer to the question
            if userA == corrA: #if the users answer matches the correct answer, then...
                global score #calling the global variable "score"
                score = score + 1 #adding 1 to the score because the user got question right
                print("Thanks for your answer.") #thanking the user for their answer
                print("   ")
                chek = True #the user has answered the question, the condition can be escaped
            elif 0<userA<5: #or if the user types in an answer that is other than the correct answer...
                print("Thanks for your answer.") #thank the user for their answer
                print("   ")
                chek = True #the user has answered the question, the condition can be escaped
            else: #if all else fails, then...
                print("Please type in a number that is between 1-4.") #tell the user to type in an acceptable answer
                chek = False #the user hasn't answered the question, therefore, the condition cannot be escaped
        except ValueError: #if the user types something that isn't an integer
            print("I'm sorry to say but, you typed in something that wasn't a number") #tell the user what they did
            print("Please type in a number that is between 1-4") #tell the user to type in a correct answer


#calling the function for it to run on different variables
runQuest(q1, c1, u1, a1) #calling the function "runQuest" and use (question 1, check 1, user answer 1 and correct answer 1)
runQuest(q2, c2, u2, a2) #calling the function "runQuest" and use (question 2, check 2, user answer 2 and correct answer 2)
runQuest(q3, c3, u3, a3) #calling the function "runQuest" and use (question 3, check 3, user answer 3 and correct answer 3)
runQuest(q4, c4, u4, a4) #calling the function "runQuest" and use (question 4, check 4, user answer 4 and correct answer 4)
runQuest(q5, c5, u5, a5) #calling the function "runQuest" and use (question 5, check 5, user answer 5 and correct answer 5)
runQuest(q6, c6, u6, a6) #calling the function "runQuest" and use (question 6, check 6, user answer 6 and correct answer 6)
runQuest(q7, c7, u7, a7) #calling the function "runQuest" and use (question 7, check 7, user answer 7 and correct answer 7)
runQuest(q8, c8, u8, a8) #calling the function "runQuest" and use (question 8, check 8, user answer 8 and correct answer 8)
runQuest(q9, c9, u9, a9) #calling the function "runQuest" and use (question 9, check 9, user answer 9 and correct answer 9)
runQuest(q10, c10, u10, a10) #calling the function "runQuest" and use (question 10, check 10, user answer 10 and correct answer 10)


#end of quiz, score is printed out
print("  ") #blank space
print("Your score is", score * 10,"out of 100.") #tell user the score at the end of quiz

#comment about the score
if score == 10: #if the score calculated is equal to 100, then...
    print("""
    It seems like you know PewDiePie pretty well.
    You probably also know that he is in a deadly war with T-Series and the caualties
    are very high at the moment.
    Therefore, you must support the war against T-Series by telling everyone you know to subscribe to
    PewDiePie.""")
    print("""
    ░░░░░░░░░░░░░░░░░░░░░
    ░░░▄█▀█▄█▀█▄▄▄░░░░░░░
    ░░█▒░░▀█▄▄░░░▀▀█░░░░░
    ░█▒░░░░░▒░░░░▒▄░▀▀█▄░
    ░█▒░░░░█▒░░▄▀░░░▒░░█░
    ░█▒░░░█▒░░█▀▒░░█▀░░▀█
    ░█▒░░░█▒░░█▒░░█▓░░░▓█
    ▄▀█▓▓░█▒░▓█▓░░█▓░░▓▄█
    █▒▒████▄▓▓█▓░░█▓░░▄█░
    █▒▒░░░░░▀█▄▀░▄▀▓▄█▀░░
    █▒▓▓▓█▀▀▄▀█▄▄▀▄▄▀░░░░ 
    ░▀▄▄▄█▄▄▀░░░░░░░░░░░░
    -a brofist, from PewDiePew to you""")

elif score == 9:
    print("""
    Not bad, but you need improvement.
    You know what you can do to improve?
    Tell all your friends about the war against T-Series and to subscribe to PewDiePie.
    PewDiePie and the general (MrBeast) will thank you for your bravery.
    ⣿⣿⣿⣿⡟⠄⣌⠻⣿⣿⣿⣿⣿⠟⠋⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡇⢸⣭⡇⢽⣿⣿⠏⣀⣶⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣷⣾⢿⣿⣿⣿⣿⣶⣭⣛⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⡛⠈⠛⠁⠙⠉⠛⠿⠛⢟⡿⣿⣷⡝⢿⡿⢻⣿⣿⣿⣿⣿⣿
    ⣿⡹⠄⢀⣷⣶⣶⣿⣿⣿⣿⣷⣶⡍⠹⡿⠆⠙⣼⣿⣿⣿⣿⣿⣿
    ⢫⣷⣧⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⢀⣴⣶⣏⡛⢿⣿⣿⣿⣿
    ⢸⣿⣿⠛⠿⣿⣿⣿⣿⣿⣿⠿⠁⠄⠄⣾⣿⣿⣿⡟⣨⣿⣿⣿⣿
    ⡘⣿⣿⣧⣀⣀⣹⣏⢀⣀⣀⣀⣠⡄⢸⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿
    ⣷⣼⣋⠈⣿⣿⣿⣿⣿⣿⣿⣿⠟⠄⠈⠛⢿⠏⢙⠈⠁⠄⠙⣿⣿
    ⣿⣿⣿⠄⠹⠟⠛⠉⠡⠿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⣿
    ⣿⣿⠿⠃⠄⠄⣀⡀⠄⠄⠈⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢹
    ⠄⠄⢀⡆⣰⠟⠷⣤⠤⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
    ⠄⢀⠎⠄⠃⢀⠞⠉⢳⣴⣶⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣀
    -PewDiePie with his cat ears and headphones (PewDiePie Bridge)""")

elif score == 8:
    print("""
    oof
    Not too bad, but you need to make up for the 2 questions you got wrong.
    So, you must make a donation to Brad 1 and Brad 2 for being underpaid by PewDiePie.
    You must also tell everyone you know to...

    ▒█▀▀▀█ ▒█░▒█ ▒█▀▀█ 　 ▀▀█▀▀ ▒█▀▀▀█ 　 ▒█▀▀█ ▒█▀▀▀ ▒█░░▒█ ▒█▀▀▄ ▒█▀▀▀█ 
    ░▀▀▀▄▄ ▒█░▒█ ▒█▀▀▄ 　 ░▒█░░ ▒█░░▒█ 　 ▒█▄▄█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ ░▀▀▀▄▄ 
    ▒█▄▄▄█ ░▀▄▄▀ ▒█▄▄█ 　 ░▒█░░ ▒█▄▄▄█ 　 ▒█░░░ ▒█▄▄▄ ▒█▄▀▄█ ▒█▄▄▀ ▒█▄▄▄█""")

elif score == 7:
    print("""
    You really need a better score.
    But Pewds still loves you, its okay. He will stop loving you though
    if you don't tell everyone to subscribe to him. So...
    +-+-+-+ +-+-+ +-+-+-+-+-+
    |S|u|b| |t|o| |P|e|w|d|s|
    +-+-+-+ +-+-+ +-+-+-+-+-+""")

elif score == 6:
    print("""
    Bruh the quiz isn't even that hard. While you figure out how to
    be a better person...
    -/S\  /u\  /b\     /t\  /o\     /P\  /e\  /w\  /d\  /s\-""")

elif score == 5:
    print("""At least you didn't get a 4, but go ahead and... subscribe to PewDiePie""")

elif score == 4:
    print("""
    This score is not okay for a fellow nine year old, you must watch Bitch Lasagna 100
    times in public in order for you to become a bro again.
    ...and create 50 fake accounts and subscribe to pewds.""")
    
else:
    print("""You clearly support T-Series and you do not deserve to be taking this quiz.
    Please close the quiz and unsubscribe from what us, real bros, call T Gay.
    -death to all those who watches T Gay""")
