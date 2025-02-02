shop = {
    "apple" : 2,
    "banana" : 1.5,
    "carrot" : 1
}
cart_val = 0 #initializing val as 0, so that we can add value afterwards.

while True: #infinite True, so that user can put as many items he can.

    items = input("Add items on your cart: ").lower()
    if items == "done": #stopping condition
        break
    elif items in shop: 
            cart_val += shop[items] #if items found in shop, then add their val with each others using cart_value
    else:
        print("Not Availble. Kindly Choose From The Available Items.") #if items arent in shop, ask them again.

print(f"Final Cart Value = {cart_val}") #final spending
