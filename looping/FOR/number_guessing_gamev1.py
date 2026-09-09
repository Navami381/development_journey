from random import randint

secret_num = randint(1,10)

for attempt in range(1,6):

    num = int(input("guess the number..."))

    if num == secret_num:

        print("congrats👍")

        break

else:

    print("badluck🙃")