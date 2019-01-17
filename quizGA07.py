#initialize global variablea
global score #the variable "score" is now global
score = int(0) #setting up the score


#Initialize local variables
a1 = int(3) #correct answer for question 1
c1 = False #check whether user has answered question properly loop
u1 = int(0) #users answer to question
q1 = str("""What is the biggest channel on YouTube (based on subscribers)?
1) T-Series
2) Youtube Gaming
3) PewDiePie
4) JustDestiny""") #first question

a2 = int(4) #correct answer for question 2
c2 = False #checks whether user has answered question
u2 = int(0) #users answer to second question
q2 = str("""What does PewDiePie posts on his channel?
1) Meme review
2) LWIAY (Last Week I Asked You)
3) You Laugh, You Lose (YLYL)
4) All of the above""") #string of second question

a3 = int(2) #correct answer for question 3
c3 = False #check whether user has answered question
u3 = int(0) #users answer to third question
q3 = str("""Where was PewDiePie born?
1) America
2) Sweden
3) England
4) Norway""") #third question string

a4 = int(4) #correct answer for fouth question
c4 = False #check whether user has answered the question
u4 = int(0) #users answer to fouth question
q4 = str("""What media outlet made an article that PewDiePie is anti-semetic?
1) Vox
2) CNN
3) The Verge
4) 1 and 3""") #fouth question string

a5 = int(4) #correct answer for fifth question
c5 = False #check whether user has answered the question
u5 = int(0) #users answer to fifth question
q5 = str("""How many subscribers does PewDiePie have?
1) 100 million
2) 113 million
3) 66 million
4) 80 million""") #fifth question string

a6 = int(3) #correct answer for sixth question
c6 = False #check whether user has answered the question
u6 = int(0) #users answer to sixth question
q6 = str("""Why did PewDiePie drop out of University?
1) His grades weren't good
2) He wanted to focus on Youtube
3) He just didn't like school
4) He wanted to move to a different country""") #sixth question string

a7 = int(4) #correct answer for seventh question
c7 = False #check whether the user has answered the question
u7 = int(0) #users answer to seventh question
q7 = str("""Who is PewDiePie dating?
1) No one
2) Ben Shapiro
3) The Slavic girl
4) Marzia""") #seventh question string

a8 = int(3) #correct answer for eigth question
c8 = False #check whether the user has answered the question
u8 = int(0) #users answer to eigth question
q8 = str("""What is the political stance of most of his fan base?
1) Liberal
2) I don't want to make a generalization
3) Conservative
4) Mixed""") #eigth question string

a9 = int(4) #correct answer for ninth question
c9 = False #check whether the user has answered the question
u9 = int(0) #users answer to ninth question
q9 = str("""What did Logan Paul do to PewDiePie recently?
1) He made an Ad out of him
2) He helped him with the fight with T-Series
3) Talk about Jake Paul on his Channel
4) Both 1 and 2""") #ninth question string

a10 = int(3) #correct answer for tenth question
c10 = False #check whether the user has answered the question
u10 = int(0) #users answer to tenth question
q10 = str("""Do you like PewDiePie?
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

#end of quiz, score is said
print("  ") #blank space
print("Thanks for taking the quiz.") #thank user for using program
print("Your score is", score * 10,"out of 100.") #tell user the score at the end of quiz
