#!/usr/bin/env python3.9

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"  # Reset to default color

# Welcome message for the quiz
print("Welcome to the Git Pub Quiz!")

# List of funny Git-related questions, options, and answers
quiz_questions = [
    {
        "question": "What does 'git commit -m' do?",
        "options": [
            "A) Starts a therapy session for your code",
            "B) Creates a new branch for experimentation",
            "C) Saves changes with a message",
            "D) Deletes your project for a fresh start"
        ],
        "answer": "C"
    },
    {
        "question": "What's the best way to undo your last commit?",
        "options": [
            "A) Close your laptop and walk away",
            "B) 'git reset --hard' (and hope for the best)",
            "C) Copy all your files to another folder",
            "D) Run 'git blame' and find someone else to blame"
        ],
        "answer": "B"
    },
    {
        "question": "What does 'git blame' actually do?",
        "options": [
            "A) Finds out who introduced the bug",
            "B) Calls your coworker to apologize",
            "C) Opens a confessional for your code sins",
            "D) Tells Git to remove all blame from your code"
        ],
        "answer": "A"
    },
    {
        "question": "Which command is used to update your local repository with changes from the remote?",
        "options": [
            "A) git-pull-push-yank",
            "B) git-summon",
            "C) git fetch and git merge (or git pull)",
            "D) git telepathy"
        ],
        "answer": "C"
    },
    {
        "question": "What is the purpose of 'git fork'?",
        "options": [
            "A) To start eating while coding",
            "B) To copy a repository into your own GitHub account",
            "C) To combine two branches into one",
            "D) To send your code to another developer"
        ],
        "answer": "B"
    }
]

# Initialize score counter
score = 0

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print("\n" + question["question"])
    for option in question["options"]:
        print(f"{YELLOW}{option}{RESET}")
    
    # Get answeR
    while True:
        user_answer = input("Your answer (A, B, C, D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break  # Valid input, proceed to check the answer
        else:
            print(f"{RED}Invalid answer! Please enter A, B, C, or D.{RESET}")

    # Check if the answer is correct
    if user_answer == question["answer"]:
        print(f"{GREEN}Correct!{RESET}")
        score += 1  
    else:
        print(f"{RED}Wrong! The correct answer was {question['answer']}.{RESET}")

# final score
total_questions = len(quiz_questions)
print(f"\n{GREEN}Your final score is {score}/{total_questions}.{RESET}")
print("Thanks for playing the Git Pub Quiz!")
