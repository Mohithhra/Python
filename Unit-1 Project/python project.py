print("Welcome to the Python Quiz App")
print("------------------------------")

score = 0

print("\n1. Who developed Python?")
print("A. Dennis Ritchie")
print("B. James Gosling")
print("C. Guido van Rossum")
print("D. Bjarne Stroustrup")

answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C")


print("\n2. Which symbol is used for comments in Python?")
print("A. //")
print("B. #")
print("C. /* */")
print("D. <!-- -->")

answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B")


print("\n3. What is the correct file extension for Python files?")
print("A. .pt")
print("B. .py")
print("C. .pyt")
print("D. .python")

answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B")


print("\n4. Which keyword is used to define a function in Python?")
print("A. func")
print("B. define")
print("C. def")
print("D. function")

answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is C")


print("\n5. What will print(type(10)) output?")
print("A. int")
print("B. <class 'int'>")
print("C. integer")
print("D. number")

answer = input("Enter your answer (A/B/C/D): ").upper()
if answer == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong! Correct answer is B")


print("\n------------------------------")
print("Quiz Completed!")
print("Your Score:", score, "/5")

if score == 5:
    print("Excellent ")
elif score >= 3:
    print("Good Job ")
else:
    print("Keep Practicing ")
