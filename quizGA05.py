#score = int(0) #setting up the score
a1 = int(3)
c1 = False #check whether user has answered question properly loop
u1 = int(0) #users answer to question
q1 = str("""What is the biggest channel on YouTube (based on subscribers)?
1) T-Series
2) Youtube Gaming
3) PewDiePie
4) JustDestiny""") #first question
a2 = int(4) #correct answer
c2 = False #checks whether user has answered question
u2 = int(0) #users answer to second question
q2 = str("""What does the Youtuber, PewDiePie posts on his channel?
1) Meme review
2) LWIAY (Last Week I Asked You)
3) You Laugh, You Lose (YLYL)
4) All of the above""") #string of second question

def runQuest (quest, chek, userA, corrA):
    print(quest)
    while chek == False:
        try:
            userA = int(input("Your answer >>> "))
            if userA == corrA:
                #score = score + 1
                print("Thanks for your answer.")
                chek = True
            elif 0<userA<5:
                print("Thanks for your answer.")
                chek = True
            else:
                print("Please type in a number that is between 1-4.")
                chek = False
        except ValueError:
            print("I'm sorry to say but, you typed in something that wasn't a number")
            print("Please type in a number that is between 1-4")

runQuest(q1, c1, u1, a1)
runQuest(q2, c2, u2, a2)


print("Thanks for taking the quiz") #thank user for using program
#print("Your score is",score," ") #tell user the score at the end of quiz
