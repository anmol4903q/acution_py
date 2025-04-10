# 🎉 Welcome to the Auction 🏆
print("Welcome to Auction! 🎉")

# 🗳️ Auction dictionary to store bids
dict = {}
ch = 'YES'  # Initial choice to start bidding

# 🏅 Function to determine the highest bidder
def highest(dict):
    winner = ""  # Variable to store the winner's name
    high = 0  # Variable to store the highest bid
    for i in dict:
        amm = dict[i]  # Get the bid amount for each bidder
        if amm > high:  # Check if current bid is higher than the previous highest
            high = amm  # Update the highest bid
            winner = i  # Update the winner's name
    print(f"The winner is {winner} with a bid of {high} 💰. 🏆")  # Show the winner and the winning bid

# 🏁 Auction loop
while ch == "YES":
    # 📢 Prompt for bidder's name and bid amount
    name = input("Enter your name: 🧑‍💻 ")
    bid = int(input("Enter your bid: 💸 "))

    # 📊 Ask if there are more bidders
    ch = input("Are there more bidders? Type (YES/NO): ").upper()

    # 💼 Store the name and bid in the dictionary
    dict[name] = bid

    # ⏹️ If no more bidders, display the winner
    if ch == "NO":
        highest(dict)  # Call the function to find the highest bid
        break  # Exit the loop after the auction ends

    # 🌪️ Clear screen for a fresh entry (optional)
    elif ch == "YES":
        print("\n" * 100)
