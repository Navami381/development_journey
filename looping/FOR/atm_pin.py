
db_pin = 3322

for attempt in range(1,4):

    pin = int(input("enter atm pin="))

    if db_pin == pin:

        print("ATM pin unlocked👍")

        break

else:

    print("atm card blocked🚫")

    