dictionary = [
    {
      "name" : "Elijah",
      "bidprice" : 1
    },
    {
      "name" : "success",
      "bidprice" : 33
    }
]

def bidding(name_of_person, price_of_bid, new_list): 
    new_dictionary = {
      "name" : name_of_person,
      "bidprice" : price_of_bid
    }
    new_list.append(new_dictionary)

while True:
    name = input("What is your name: ")
    bid_price = ((int(input("What is your bidding price: $"))))

    bidding(name, bid_price, dictionary)
    
    max_bidder = max(dictionary, key=lambda x: x["bidprice"] )
        
    res = input(f"Do any other person want to bid? Yes OR No: ")
    if res.lower() == "no":
        break
    
   
max_bidder = max(dictionary, key=lambda x: x["bidprice"] )
print(f"The highest bidder is {max_bidder['name']} with ${max_bidder['bidprice']}")
        