
from db import create_account, record_transaction, get_balance, get_statement

def menu():
    while True:
        print("""
1) Create Account
2) Deposit
3) Withdraw
4) Check Balance
5) Print Statement
6) Exit
        """)
        choice = input("Choose: ")
        if choice == '1':
            acc_no = int(input("Account No: "))
            data = {
                'name':    input("Name: "),
                'dob':     input("DOB (YYYY‑MM‑DD): "),
                'address': input("Address: "),
                'mob_no':  int(input("Mobile No: ")),
                'initial_balance': float(input("Initial Balance: "))
            }
            create_account(acc_no, **data)
            print("✅ Account created.")
        elif choice in ('2','3'):
            acc_no = int(input("Account No: "))
            amt    = float(input("Amount: "))
            tx_type = 'deposit' if choice=='2' else 'withdraw'
            record_transaction(acc_no, tx_type, amt)
            print(f"✅ {tx_type.title()} successful.")
        elif choice == '4':
            bal = get_balance(int(input("Account No: ")))
            print(f"🗒 Current Balance: {bal}")
        elif choice == '5':
            stmt = get_statement(int(input("Account No: ")))
            for tx in stmt:
                print(tx)
        elif choice == '6':
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    menu()
