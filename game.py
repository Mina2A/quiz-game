print("Welcome to my game!")
playing = input("Do you want to play? : ").lower()

if playing != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What is the fastest animal in the world on land? : ").lower()
if answer == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the fastest animal in the world in the air? : ").lower()
if answer == "peregrine falcon":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + "questions correct!")
print("You got " + str((score / 4) * 100) + "%.")