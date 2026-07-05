import random

print("🎮 Number Guessing Game")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too small!")
        elif guess > secret_number:
            print("📈 Too big!")
        else:
            print("🎉 Correct! You won!")
            print("Attempts:", attempts)
            break

    except ValueError:
        print("❌ Please enter a valid number!")