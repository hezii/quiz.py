#score = int(0) #setting up the score
c1 = False #check whether user has answered question properly loop
a1 = int(0) #users answer to question
q1 = str("""What is the biggest channel on YouTube (based on subscribers)?
1) T-Series
2) Youtube Gaming
3) PewDiePie
4) JustDestiny""") #first question
c2 = False
a2 = int(0) #users answer to second question
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
            if userA == corrA
                score = score + 1
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

print(q1) #prints first question
#while loop for the first question
while c1 == False: #while the first question isn't answered...
    try: #try...
        a1 = int(input("Your answer >>> "))
        if a1 == 3:  #if the user says the answer is 3 then...
            score = score + 1 #add 1 to the score
            print("Thanks for your answer") #thank the user
            c1 = True #set the boolean to true to get out of loop
        elif 0<a1<5: #if the user gives an answer between 1-4
            print("Thanks for your answer") #thank the user
            c1 = True #set the boolean to true to escape loop
        else: #if user types in something else
            print("You must type in a number 1-4") #tell user that something is wrong
            c1 = False
    except ValueError: #if user doesn't type a number or uses a decimal...
        print("You typed something that wasn't a number") #tell user something is wrong
        print("You must type in a number 1-4") #tell user what to type

print(q2) #prints second question
c2 = False #set the boolean to false to get into next loop
while c2 == False: #while the first question isn't answered...
    try: #try...
        a2 = int(input("Your answer >>> "))
        if a2 == 4:  #if the user says the answer is 4 then...
            score = score + 1 #add 1 to the score
            print("Thanks for your answer") #thank the user
            c2 = True #set the boolean to true to get out of loop
        elif 0<a2<5: #if the user gives an answer between 1-4
            print("Thanks for your answer") #thank the user
            c2 = True #set the boolean to true to escape loop
        else: #if user types in something else
            print("You must type in a number 1-4") #tell user that something is wrong
            c2 = False
    except ValueError: #if user doesn't type a number or uses a decimal...
        print("You typed something that wasn't a number") #tell user something is wrong
        print("You must type in a number 1-4") #tell user what to type

print("Thanks for taking the quiz") #thank user for using program
print("Your score is",score," ") #tell user the score at the end of quiz
