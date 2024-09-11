import sys

questions = [
    "1. Which element has the chemical symbol 'O'?",
    "2. Which is the largest planet in our solar system?",
    "3. What is the capital of Japan?",
    "4. Which metal is liquid at room temperature?",
    "5. Who wrote the play \"Romeo and Juliet\"?",
    "6. Which country is famous for the Great Wall?",
    "7. Which is the longest river in the world?",
    "8. What is the chemical symbol for water?",
    "9. Which language is the most spoken native language in the world?",
    "10. Who was the first woman Prime Minister of India?"
]
answers = [
    "Oxygen",
    "Jupiter",
    "Tokyo",
    "Mercury",
    "William Shakespeare",
    "China",
    "Nile",
    "H2O",
    "Mandarin Chinese",
    "Indira Gandhi"
]
options = [
    ["Hydrogen", "Oxygen", "Carbon", "Nitrogen"],
    ["Earth", "Mars", "Jupiter", "Saturn"],
    ["Beijing", "Seoul", "Tokyo", "Bangkok"],
    ["Iron", "Silver", "Mercury", "Gold"],
    ["Charles Dickens", "Jane Austen", "William Shakespeare", "Leo Tolstoy"],
    ["India", "China", "Egypt", "Greece"],
    ["Amazon", "Nile", "Yangtze", "Mississippi"],
    ["H2", "H2O", "O2", "HO2"],
    ["English", "Mandarin Chinese", "Spanish", "Hindi"],
    ["Indira Gandhi", "Margaret Thatcher", "Golda Meir", "Benazir Bhutto"]
]

print("Welcome to KBC-2024.\nHere you will answer 10 questions each worth Rs. 10000. So best of luck!\n")

c = 0  # Counter for correct answers
j = 0
for i in range(10):
    print("\n",questions[i])
    
    print(options[i])
    
    ans = int(input("Answer option (1-4): "))
    
    if options[j][ans-1] == answers[i]:
        print("Right answer!")
        j += 1
        c += 1
    else:
        print("Wrong answer")
        print("The right answer was:", answers[i])
        print("\nYou have won Rs. ",c * 10000,". And given ",c," answers correctly.")
        
        sys.exit("\nGame Over!")
if c == 10:
    c = 10
    print("\nCongratulations you have answered all questions correctly and won the total amount Rs.", 100000)

