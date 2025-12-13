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
                print("I will view/search product")
            elif product_choice == 2:
                print("I will edit product")
            elif product_choice == 3:
                print("I add new product")
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
    