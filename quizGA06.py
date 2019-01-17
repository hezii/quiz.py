global score #the variable "score" is now global
score = int(0) #setting up the score


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
q2 = str("""What does the Youtuber, PewDiePie posts on his channel?
1) Meme review
2) LWIAY (Last Week I Asked You)
3) You Laugh, You Lose (YLYL)
4) All of the above""") #string of second question

def runQuest (quest, chek, userA, corrA): #defining the function "run question", (question, checking if user answered question, user answer, correct answer)
    print(quest) #print the question
    while chek == False: #while user hasn't put in an answer (false)
        try: #try this..
            userA = int(input("Your answer >>> ")) #userA is the user's answer to the question
            if userA == corrA: #if the users answer matches the correct answer, then...
                global score #calling the global variable "score"
                score = score + 1 #adding 1 to the score because the user got question right
                print("Thanks for your answer.") #thanking the user for their answer
                chek = True #the user has answered the question, the condition can be escaped
            elif 0<userA<5: #or if the user types in an answer that is other than the correct answer...
                print("Thanks for your answer.") #thank the user for their answer
                chek = True #the user has answered the question, the condition can be escaped
            else: #if all else fails, then...
                print("Please type in a number that is between 1-4.") #tell the user to type in an acceptable answer
                chek = False #the user hasn't answered the question, therefore, the condition cannot be escaped
        except ValueError: #if the user types something that isn't an integer
            print("I'm sorry to say but, you typed in something that wasn't a number") #tell the user what they did
            print("Please type in a number that is between 1-4") #tell the user to type in a correct answer

runQuest(q1, c1, u1, a1) #calling the function "runQuest" and use (question 1, check 1, user answer 1 and correct answer 1)
runQuest(q2, c2, u2, a2) #calling the function "runQuest" and use (question 2, check 2, user answer 2 and correct answer 2)

print("Thanks for taking the quiz") #thank user for using program
print("Your score is", score * 10," ") #tell user the score at the end of quiz
