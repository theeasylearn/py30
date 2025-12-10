import connection as con 
print("Saral Billing software")
while True:
    print("Press 1 for Product management")
    print("Press 2 for Bill management")
    print("Press 0 for Exit ")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print("welcome to Product management")
        while True:
            print("press 1 to view/search product")
            print("Press 2 to edit product")
            print("Press 3 to add new product")
            print("Press 4 to delete product ")
            print("Press 0 to return to main manu")
            product_choice = int(input("Enter your choice (0 to 4)"))
            if product_choice == 1:
                 search = input("Enter product name to search(press enter to search all)")
                 start = 0
                 
                 while True:
                    if len(search) == 0:
                        sql = "select id,name,price,stock,description,weight,size from product order by name limit %s,10"
                        values = [start]
                    else:
                        sql = "select id,name,price,stock,description,weight,size from product where name=%s order by name limit %s,10"
                        values = [search,start]
                    table = con.fetch(sql,values)
                    if len(table)>0:
                        print(f"{'ID':<4}{'NAME':<48}{'PRICE':<8}{'STOCK':<6}{'WEIGHT':<6}{'SIZE':<10}{'DESCRIPTION':<4}")
                        print("_"*100)
                        for row in table:
                            output = f"{row['id']:<4}{row['name']:<48}{row['price']:<8}{row['stock']:<6}{row['weight']:<6}{row['size']:<10}{row['description']:<4}"
                            print(output)  
                        start+=10
                        key = input("Press enter to see other products")
                    else:
                        break 
            elif product_choice == 2:
                print("I will edit product")
            elif product_choice == 3:
                sql = "insert into product(name,price,stock,description,weight,size) values (%s,%s,%s,%s,%s,%s)"
                try:
                    name = input("Enter product name: ")
                    price = float(input("Enter price: "))
                    stock = int(input("Enter stock quantity: "))
                    description = input("Enter description: ")
                    weight = float(input("Enter weight: "))
                    size = input("Enter size: ")
                    values = [name,price,stock,description,weight,size] #list
                    con.run(sql,values,'new product added')
                except ValueError as error:
                    print("invalid input (price stock, weight must be numbers)")
            elif product_choice == 4:
                print("I delete product")
            elif product_choice == 0:
                print("I will return to main menu")
                break 
            else:
                print("invalid input")    
    elif choice == 2:
        print("Welcome to bill management")
        while True:
            print("press 1 to add product into bill ")
            print("press 2 to view bill items ")
            print("press 3 to delete product from non printed bill ")
            print("press 4 to save and print bill ")
            print("press 5 to get details of bill between given date ")
            print("press 6 to search for specific bill by customer name ")
            print("Press 0 to exit to main menu")
            bill_choice = int(input("Enter your choice"))
            if bill_choice == 1:
                print("i will add product into bill")
            elif bill_choice == 2:
                print("i will view bill items")
            elif bill_choice == 3:
                print("i will delete product from non printed bill")
            elif bill_choice == 4:
                print("i will save and print bill")
            elif bill_choice == 5:
                print("i will get details of bill between given date")
            elif bill_choice == 6:
                print("i will search for specific bill by customer name")
            elif bill_choice == 0:
                break #will break inner loop
            else:
                print("invalid bill choice")
    elif choice == 0:
        print("Thank you for yousing Saral software... ")
        break # stop loop 
    else:
        print("invalid choice ")