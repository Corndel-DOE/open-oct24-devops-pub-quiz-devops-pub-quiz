# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the symbol (ticker) for Bitcoin??",
        "options": ["A) BB", "B) BTC", "C) BT", "D) BIT"],
        "answer": "B"
    },
    {
        "question": "Who created Bitcoin?",
        "options": ["A) USA goverment", "B) Satoshi Nakamoto", "C) Craig Wright", "D) Adam Back"],
        "answer": "B"
    },
    {
        "question": "What is the market cap of Bitcoin?",
        "options": ["A) 100 milion", "B) Unlimited", "C) 1 bilion", "D) 21 milion"],
        "answer": "D"
    },
    # Learners can add more questions here following the same structure
]

# Loop through each question
for question in quiz_questions:
    # Display the question and options
    print(question["question"])
    for option in question["options"]:
        print(option)
    
    # Get the user's answer
    user_answer = input("Your answer (A, B, C, D): ").strip().upper() # Ensuring the input is uppercase for comparison
    
    # Check if the answer is correct
    if user_answer == question["answer"]:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
