"""
✅ 5. ATM Withdrawal

Task:
Ask for PIN.

If PIN is correct:

Ask for withdrawal amount

If amount ≤ balance → "Withdrawal successful"

Else → "Insufficient balance"

Else → "Incorrect PIN"
"""
db_pin = 12345

db_balance = 100000

pin = int(input("enter pin="))

if db_pin == pin:

    amt=int(input("enter the amount="))

    if amt<=db_balance:

        print("TRANSACTION COMPLETE")

    else :

        print("INSUFFICIENT BALANCE")
else:

    print("incorrect pin")
