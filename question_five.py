def main_menu():
    print("SIM 1")
    print("1. Safaricom")
    print("2. M-PESA")
    print("Enter your choice: ", end="")
    choice = input()
    if choice == "1":
        safaricom_menu()
    elif choice == "2":
        mpesa_menu()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

def safaricom_menu():
    print("\nSIM 1 - Safaricom")
    print("1. Check Balance")
    print("2. Buy Bundles")
    print("3. Back")
    print("Enter your choice: ", end="")
    choice = input()
    if choice == "1":
        print("\nBalance: Ksh 0.00 (Demo)")
        safaricom_menu()
    elif choice == "2":
        print("\nBundles: Not implemented (Demo)")
        safaricom_menu()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        safaricom_menu()

def mpesa_menu():
    print("\nSIM 1 - M-PESA")
    print("1. Send Money")
    print("2. Withdraw Cash")
    print("3. Buy Airtime")
    print("4. Loans and Savings")
    print("5. Lipa na M-PESA")
    print("6. My Account")
    print("7. Back")
    print("Enter your choice: ", end="")
    choice = input()
    if choice == "1":
        send_money()
    elif choice == "2":
        print("\nWithdraw Cash: Not implemented (Demo)")
        mpesa_menu()
    elif choice == "3":
        print("\nBuy Airtime: Not implemented (Demo)")
        mpesa_menu()
    elif choice == "4":
        print("\nLoans and Savings: Not implemented (Demo)")
        mpesa_menu()
    elif choice == "5":
        print("\nLipa na M-PESA: Not implemented (Demo)")
        mpesa_menu()
    elif choice == "6":
        print("\nMy Account: Not implemented (Demo)")
        mpesa_menu()
    elif choice == "7":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        mpesa_menu()

def send_money():
    print("\nSIM 1 - M-PESA - Send Money")
    phone_number = input("Enter Phone Number (10-13 digits, allowed characters: 0-9, *, #, +): ")
    if validate_phone_number(phone_number):
        print(f"Sending money to {phone_number}. Not implemented (Demo).")
        mpesa_menu()
    else:
        print("Invalid phone number. Please try again.")
        send_money()

def validate_phone_number(phone_number):
    valid_chars = "0123456789*#+"
    return (
        10 <= len(phone_number) <= 13
        and all(char in valid_chars for char in phone_number)
    )

def start_sim_toolkit():
    print("Welcome to the Safaricom SIM Toolkit CLI")
    main_menu()

if __name__ == "__main__":
    start_sim_toolkit()
