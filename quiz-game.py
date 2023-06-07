print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play\n")
score = 0

answer = input("What does CPU stand for?\n")
if answer.lower() == "central processing unit":
    print("Correct!\n")
    score += 1
else:
    print("I'm sorry, the correct answer is: 'central processing unit'\n")

answer = input("What does GPU stand for?\n")
if answer.lower() == "graphics processing unit":
    print("Correct!\n")
    score += 1
else:
    print("I'm sorry, the correct answer is: 'graphics processing unit'\n")

answer = input("What does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("Correct!\n")
    score += 1
else:
    print("I'm sorry, the correct answer is: 'random access memory'\n")

answer = input("What does PSU stand for?\n")
if answer.lower() == "power supply":
    print("Correct!\n")
    score += 1
else:
    print("I'm sorry, the correct answer is: 'power supply'\n")

print("Score: " + str(score))
print(str((score/4)*100) + "%.")