#initialize global variablea
global score #the variable "score" is now global
score = int(0) #setting up the score


#Initialize local variables
a1 = int(3) #correct answer for question 1
c1 = False #check whether user has answered question properly loop
u1 = int(0) #users answer to question
q1 = str("""1. What is the biggest channel on YouTube (based on subscribers)?
1) T-Series
2) Youtube Gaming
3) PewDiePie
4) JustDestiny""") #first question

a2 = int(4) #correct answer for question 2
c2 = False #checks whether user has answered question
u2 = int(0) #users answer to second question
q2 = str("""2. What does PewDiePie posts on his channel?
1) Meme review
2) LWIAY (Last Week I Asked You)
3) You Laugh, You Lose (YLYL)
4) All of the above""") #string of second question

a3 = int(2) #correct answer for question 3
c3 = False #check whether user has answered question
u3 = int(0) #users answer to third question
q3 = str("""3. Where was PewDiePie born?
1) America
2) Sweden
3) England
4) Norway""") #third question string

a4 = int(4) #correct answer for fouth question
c4 = False #check whether user has answered the question
u4 = int(0) #users answer to fouth question
q4 = str("""4. What media outlet made an article that PewDiePie is anti-semetic?
1) Vox
2) CNN
3) The Verge
4) 1 and 3""") #fouth question string

a5 = int(4) #correct answer for fifth question
c5 = False #check whether user has answered the question
u5 = int(0) #users answer to fifth question
q5 = str("""5. How many subscribers does PewDiePie have?
1) 100 million
2) 113 million
3) 66 million
4) 80 million""") #fifth question string

a6 = int(3) #correct answer for sixth question
c6 = False #check whether user has answered the question
u6 = int(0) #users answer to sixth question
q6 = str("""6. Why did PewDiePie drop out of University?
1) His grades weren't good
2) He wanted to focus on Youtube
3) He just didn't like school
4) He wanted to move to a different country""") #sixth question string

a7 = int(4) #correct answer for seventh question
c7 = False #check whether the user has answered the question
u7 = int(0) #users answer to seventh question
q7 = str("""7. Who is PewDiePie dating?
1) No one
2) Ben Shapiro
3) The Slavic girl
4) Marzia""") #seventh question string

a8 = int(3) #correct answer for eigth question
c8 = False #check whether the user has answered the question
u8 = int(0) #users answer to eigth question
q8 = str("""8. What is the political stance of most of his fan base?
1) Liberal
2) I don't want to make a generalization
3) Conservative
4) Mixed""") #eigth question string

a9 = int(4) #correct answer for ninth question
c9 = False #check whether the user has answered the question
u9 = int(0) #users answer to ninth question
q9 = str("""9. What did Logan Paul do to PewDiePie recently?
1) He made an Ad out of him
2) He helped him with the fight with T-Series
3) Talk about Jake Paul on his Channel
4) Both 1 and 2""") #ninth question string

a10 = int(3) #correct answer for tenth question
c10 = False #check whether the user has answered the question
u10 = int(0) #users answer to tenth question
q10 = str("""10. Do you like PewDiePie?
1) No
2) I don't know him
3) Yes
4) Don't ask me personal questions""") #tenth question string


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
