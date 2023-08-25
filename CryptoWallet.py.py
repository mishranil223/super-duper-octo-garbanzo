# Class called CryptoWallet to represent a cryptocurrency wallet.
class CryptoWallet:
    # Initializing the wallet with a starting balance.
    def __init__(self, balance):
        self.balance = balance

    # Method to send cryptocurrency with a fee, here 1% is used as fee
    def send(self, amount):
        fee = amount * 0.01  # Calculate the transaction fee.
        total_amount = amount + fee  # Calculate the total transaction amount.

        # Checking if the total transaction amount is greater than the wallet balance.
        if total_amount > self.balance:
            print("Not enough balance.")
        else:
            self.balance -= total_amount  # Deduct the total transaction amount from the balance.
            print(f"Sent {amount:.2f} crypto with a fee. New balance: {self.balance:.2f}")

    # Method to receive cryptocurrency and update the balance.
    def receive(self, amount):
        self.balance += amount  # Add the received amount to the balance.
        print(f"Received {amount:.2f} crypto. New balance: {self.balance:.2f}")

# Main function to run the cryptocurrency wallet program.
def main():
    initial_balance = float(input("Starting balance: "))  # Getting  the initial balance from the user.
    wallet = CryptoWallet(initial_balance)  # Creating a wallet object with the initial balance.

    # Displaying the main menu and handle user choices.
    while True:
        print("\nCrypto Wallet Menu:")
        print("1. Send Crypto")
        print("2. Receive Crypto")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option: ")  # Getting the user's menu choice.

        # Handling the user's choice based on the selected option.
        if choice == "1":
            amount = float(input("Amount to send: "))  # Getting the amount to send from the user.
            wallet.send(amount)  # Call the send method of the wallet.
        elif choice == "2":
            amount = float(input("Amount to receive: "))  # Getting the amount to receive from the user.
            wallet.receive(amount)  # Call the receive method of the wallet.
        elif choice == "3":
            print(f"Balance: {wallet.balance:.2f}")  # Displaying the current wallet balance.
        elif choice == "4":
            print("Exiting.")  # Exiting the program loop.
            break
        else:
            print("Invalid option. Try again.")  # Handle invalid menu choices.

# Entry point of the program: execute the main function if the script is run directly.
if __name__ == "__main__":
    main()
