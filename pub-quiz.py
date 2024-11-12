# Welcome message for the quiz
print("Welcome to the Pub Quiz!")

# List of questions, options, and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "Which of the following is the largest planet in the solar system?",
        "options": ["A) Earth", "B) Saturn", "C) Mars", "D) Jupiter"],
        "answer": "D"

    },
    {
        "question": "Which year did Lewis Hamilton win his first world championship in Formula 1 racing?",
        "options": ["A) 2001", "B) 2005", "C) 2007", "D) 2008"],
        "answer": "D"
        
    },
    {
        "question": "Which of the following animals is the fastest land mammal?",
        "options": ["A) Horse", "B) Cow", "C) Cat", "D) Cheetah"],
        "answer": "D"
        
    },
    # Learners can add more questions here following the same structure
]

score = 0

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
        score += 1
    else:
        print(f"Wrong! The correct answer was {question['answer']}.")
    
# Display score
print(f"You scored {score} out of {len(quiz_questions)}.")

# Goodbye message
print("Thanks for playing the Pub Quiz!")
