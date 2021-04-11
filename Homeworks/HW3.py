#KnowLedge Competition

questions={ "q1" : "Which is the most crowded country in the world?",
            "q2" : "What is the name of the first computer?",
            "q3" : "Who is the 2nd place in 2010 eurovision?",
            "q4" : "Who is the lead role of Downfall movie?",
            "q5" : "In which year did world war 2 end?",
            "q6" : "How many colors are there in the flag Turkey?",
            "q7" : "Who is a Turkish scientist who receives nobel?",
            "q8" : "Who composed the Turkish March?",
            "q9" : "Who is the Turkish actor who won the Emmy?",
            "q10": "When was founded Turkey Republic?"}

right_answers={"ra1" : "China",
               "ra2" : "ENIAC",
               "ra3" : "Manga",
               "ra4" : "Bruno Ganz",
               "ra5" : "1945",
               "ra6" : "2",
               "ra7" : "Aziz Sancar",
               "ra8" : "Beethoven",
               "ra9" : "Haluk Bilginer",
               "ra10": "1923"}
score=0
print(questions["q1"])
a1=str(input("Answer:"))
if(a1==right_answers["ra1"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print(questions["q2"])
a2=str(input("Answer:"))
if(a2==right_answers["ra2"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print(questions["q3"])
a3=str(input("Answer:"))
if(a3==right_answers["ra3"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print(questions["q4"])
a4=str(input("Answer:"))
if(a4==right_answers["ra4"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print(questions["q5"])
a5=str(input("Answer:"))
if(a5==right_answers["ra5"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print(questions["q6"])
a6=str(input("Answer:"))
if(a6==right_answers["ra6"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")
print(questions["q7"])
a7=str(input("Answer:"))
if(a7==right_answers["ra7"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")
print(questions["q8"])
a8=str(input("Answer:"))
if(a8==right_answers["ra8"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")
print(questions["q9"])
a9=str(input("Answer:"))
if(a9==right_answers["ra9"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")
print(questions["q10"])
a10=str(input("Answer:"))
if(a10==right_answers["ra10"]):
    score+=10
    print("||Right Answer!!!!!||")
    print("Your Score:",score)
else:
    print("||Wrong Aswer!!||")

print("YOUR FİNAL SCORE:",score)

if(score>50):
    print("CONGRATULATIONS!!!!! You Won The Award")
else:
    print("Unfortunately You Didn't Win Anything")
