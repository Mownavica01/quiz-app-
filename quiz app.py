import random

def run_quiz():
    score = 0

    questions = [
        {"question": "What is the capital of India?", "options": ["a) Mumbai", "b) Delhi", "c) Chennai"], "answer": "b"},
        {"question": "Which is a programming language?", "options": ["a) Python", "b) Snake", "c) Tiger"], "answer": "a"},
        {"question": "Which planet is known as Red Planet?", "options": ["a) Earth", "b) Mars", "c) Venus"], "answer": "b"},
        {"question": "2 + 2 = ?", "options": ["a) 3", "b) 4", "c) 5"], "answer": "b"},
        {"question": "Which data type is used for text?", "options": ["a) int", "b) str", "c) float"], "answer": "b"},
        {"question": "Which keyword is used for loop?", "options": ["a) for", "b) if", "c) else"], "answer": "a"},
        {"question": "HTML stands for?", "options": ["a) Hyper Trainer Marking Language", "b) Hyper Text Markup Language", "c) High Text Machine Language"], "answer": "b"},
        {"question": "CSS is used for?", "options": ["a) Styling", "b) Database", "c) Logic"], "answer": "a"},
        {"question": "Which symbol is used for comments in Python?", "options": ["a) //", "b) #", "c) /*"], "answer": "b"},
        {"question": "Which function takes input?", "options": ["a) print()", "b) input()", "c) len()"], "answer": "b"},
        {"question": "Which is an operating system?", "options": ["a) Windows", "b) Python", "c) HTML"], "answer": "a"},
        {"question": "Which device is used to input data?", "options": ["a) Monitor", "b) Keyboard", "c) Printer"], "answer": "b"},
        {"question": "Which number is even?", "options": ["a) 3", "b) 7", "c) 8"], "answer": "c"},
        {"question": "Which is a search engine?", "options": ["a) Google", "b) Python", "c) Excel"], "answer": "a"},
        {"question": "Which file extension is for Python?", "options": ["a) .py", "b) .java", "c) .html"], "answer": "a"},
        {"question": "Which is used to store multiple values?", "options": ["a) Variable", "b) List", "c) Integer"], "answer": "b"},
        {"question": "Which company developed Python?", "options": ["a) Microsoft", "b) Google", "c) None"], "answer": "c"},
        {"question": "Which function shows output?", "options": ["a) input()", "b) print()", "c) open()"], "answer": "b"},
        {"question": "Which is a web browser?", "options": ["a) Chrome", "b) Python", "c) Linux"], "answer": "a"},
        {"question": "Which symbol is used for multiplication?", "options": ["a) x", "b) *", "c) %"], "answer": "b"}
    ]

    random.shuffle(questions)

    print("🎯 Welcome to Quiz Game!\n")

    name = input("Enter your name: ")
    print(f"\nHello {name}, let's start the quiz!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        
        for option in q["options"]:
            print(option)
        
        answer = input("Enter your answer (a/b/c): ").lower()

        if answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}\n")

    print(f"{name}, your final score is: {score}/20")

    if score >= 16:
        print("🏆 Excellent!")
    elif score >= 10:
        print("👍 Good job!")
    else:
        print("🙂 Keep practicing!")

    # Save score
    with open("scores.txt", "a") as file:
        file.write(f"{name}: {score}/20\n")

    print("\n📁 Score saved successfully!")

run_quiz()
