# Driver's License Exam
correct_answers=["A", "C", "A", "A", "D",
                "B", "C", "A", "C", "B",
                "A", "D", "C", "A", "D",
                "C", "B", "B", "D", "A"]
user_answers = []
score = 0
with open('answers.txt', 'r') as f:
    for line in f:
        line = (line.rstrip()).upper()
        user_answers.append(line)

score = 0
for i in range(len(user_answers)):
    if user_answers[i] == correct_answers[i]:
        print("Answer #", (i+1), " is correct.", sep ='')
        score += 1
    else:
        print("Answer #", (i+1), " is incorrect.", sep = '')

if (score / (len(correct_answers))) >= .75:
    print("You passed with", score, "correct answers.")
else:
    print("You failed with", (len(correct_answers) - score), "incorrect answers.")
