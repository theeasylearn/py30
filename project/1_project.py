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
        print("I will do bill management")
        #task develop menu for bill management 
        
    elif choice == 0:
        print("Thank you for yousing Saral software... ")
        break # stop loop 
    else:
        print("invalid choice ")