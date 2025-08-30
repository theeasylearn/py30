# write a program to find out profit or loss amount from given purcharse price and sales price 
#accept input 
purchase_price = input("Enter purcharse price")
sales_price = input("Enter sales price")
#convert variables into integer 
purchase_price = int(purchase_price)
sales_price = int(sales_price)
if sales_price>purchase_price:
    print("profit = ",sales_price - purchase_price)
else:
    print("Loss = ",purchase_price - sales_price)
# print("Good bye.")