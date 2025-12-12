import connection as con 
import shutil
columns = shutil.get_terminal_size().columns
def input_with_default(prompt, current_value):
    user_input = input(f"{prompt} [{current_value}]: ").strip()
    return current_value if user_input == "" else user_input
def display_no_record_found():
    print("*"*columns)
    temp = "No records found"
    # print message in center of screen                            
    print(temp.center(columns)) 
    print("*"*columns)
def display_products():
    search = input("Enter product name to search(press enter to search all)")
    start = 0      
    while True:
        if len(search) == 0:
            sql = "select id,name,price,stock,description,weight,size from product where isdeleted=0 order by name limit %s,10"
            values = [start]
        else:
            search = f"%{search}%"
            sql = "select id,name,price,stock,description,weight,size from product where isdeleted=0 and name like %s order by name limit %s,10"
            values = [search,start]
        table = con.fetch(sql,values)
        if len(table)>0:
            print(f"{'ID':<4}{'NAME':<48}{'PRICE':<8}{'STOCK':<6}{'WEIGHT':<6}{'SIZE':<10}{'DESCRIPTION':<4}")
            print("_"*columns)
            for row in table:
                output = f"{row['id']:<4}{row['name']:<48}{row['price']:<8}{row['stock']:<6}{row['weight']:<6}{row['size']:<10}{row['description']:<4}"
                print(output)  
            start+=10
            key = input("Press enter to see other products")
        else:
            if start == 0:
                display_no_record_found()
            break 
def product_management():
    print("welcome to Product management")
    while True:
        print("press 1 to view/search product")
        print("Press 2 to edit product")
        print("Press 3 to add new product")
        print("Press 4 to delete product ")
        print("Press 0 to return to main manu")
        product_choice = int(input("Enter your choice (0 to 4)"))
        if product_choice == 1:
            display_products()
        elif product_choice == 2:
            display_products()
            productid = int(input("Enter product id to edit"))
            sql = 'select id,name,price,stock,weight,size,description from product where id = %s'
            values = [productid]
            table = con.fetch(sql,values)
            if len(table) == 0:
                display_no_record_found()
            else:
                #product id found
                name = table[0]['name']
                price = table[0]['price']
                stock = table[0]['stock']
                weight = table[0]['weight']
                size = table[0]['size']
                description = table[0]['description']
                try:
                    name = input_with_default("Enter name", table[0]['name'])
                    price = float(input_with_default("Enter price", table[0]['price']))
                    stock = int(input_with_default("Enter stock", table[0]['stock']))
                    weight = float(input_with_default("Enter weight", table[0]['weight']))
                    size = input_with_default("Enter size", table[0]['size'])
                    description = input_with_default("Enter description", table[0]['description'])
                    #update row 
                    print(name,price,stock,weight,size,description)
                    sql = "update product set name=%s,price=%s,stock=%s,weight=%s,size=%s,description=%s where id=%s"
                    values = [name,price,stock,weight,size,description,productid]
                    con.run(sql,values,"product updated")
                except ValueError as error:
                    print("invalid input (price stock, weight must be numbers)")
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
            display_products()
            productid = int(input("Enter product id to edit"))
            sql = 'select id,name,price,stock,weight,size,description from product where id = %s'
            values = [productid]
            table = con.fetch(sql,values)
            if len(table) == 0:
                display_no_record_found()
            else:
                sql = "update product set isdeleted=1 where id=%s"
                values = [productid]
                con.run(sql,values,"product deleted")
        elif product_choice == 0:   
            print("I will return to main menu")
            break 
        else:
            print("invalid input")    
def bill_management():
    print("welcome to bill management")
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
            display_products()
            productid = int(input("Enter product id"))
            sql = 'select id,price,stock from product where id = %s'
            values = [productid]
            table = con.fetch(sql,values)
            if len(table) == 0:
                display_no_record_found()
            else:
                qty = int(input("Enter quantity"))
                if qty>table[0]['stock']:
                    print("not enough stock, available stock is ",table[0]['stock'])
                else:
                    sql = "insert into item (productid,qty,price) values (%s,%s,%s)"
                    values = [productid,qty,table[0]['price']]
                    con.run(sql,values,'Item added into bill')

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
print("Saral Billing software")
while True:
    try:
        print("Press 1 for Product management")
        print("Press 2 for Bill management")
        print("Press 0 for Exit ")
        choice = int(input("Enter your choice"))
        if choice == 1:
            product_management()
        elif choice == 2:
            bill_management()
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
    except ValueError as e:
        print("invalid input, choice must be integer")