from random import randint

print("WELCOME to the number guessing game🎮")

print("🤔guess a number btw 1-10")

print("you have 5 chances😺")

secret_num = randint(1,20)

for attempt in range(1,6):

    num = int(input("guess the number..."))


    if num == secret_num:

        print("congrats,you guessed the number correctly👍")

        print("you guessed correct in {attempt}",attempt)

        break

    elif num < secret_num:

        print("too low")

    elif num > secret_num:

        print("too high")

        break

else:

    print("you have used all attempts")

    print("the secret number was",secret_num)