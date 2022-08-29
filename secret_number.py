import random

secret_num = random.randint(1,20)
attempts = 0

with open("secret_number.txt", "r") as score_file:
    best_score = int(score_file.read())
    print(f"Top score: {best_score}!")

while True:
    guess = int(input("Whats your guess: "))
    attempts += 1

    if guess == secret_num:
        if attempts < best_score:
            with open("secret_number.txt", "w") as score_file:
                score_file.write(str(attempts))
        print("Congratulate!!")
        print(f"Attempts needed: {attempts}!")
        break
    elif guess > secret_num:
        print("Your guess is not correct.. try something smaller!")
    elif guess < secret_num:
        print("Your guess is not correct.. try something bigger!")

