# Initial list of bids
dictionary = [
    {
        "name": "Elijah",
        "bidprice": 1  # Change to integer
    },
    {
        "name": "success",
        "bidprice": 33  # Change to integer
    }
]

def bidding(name_of_person, price_of_bid, bids_list):
    new_dictionary = {
        "name": name_of_person,
        "bidprice": price_of_bid
    }
    bids_list.append(new_dictionary)

while True:
    name = input("What is your name: ")
    bid_price = int(input("What is your bidding price: $"))

    bidding(name, bid_price, dictionary)

    # Find the highest bid
    max_bid = max(dictionary, key=lambda x: x["bidprice"])
    
    res = input(f"Do any other person want to bid? Yes OR No: ")
    if res.lower() == "no":
        break

# Final highest bid result
max_bid = max(dictionary, key=lambda x: x["bidprice"])
print(f"The highest bidder is {max_bid['name']} with ${max_bid['bidprice']}")