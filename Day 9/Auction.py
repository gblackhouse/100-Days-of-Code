from art import logo
print(logo)

def highest_bid(auction):
    winner = max(auction)
    highest_amount = auction[winner]
    print(f"{winner} has won with a bid of ${highest_amount}")

bids = {}
bidding = True

while bidding:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bids[name] = bid

    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if continue_bidding == 'no':
        bidding = False
        highest_bid(bids)
    elif continue_bidding == 'yes':
        print("\n" * 20)
