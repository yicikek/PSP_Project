# ********************************************************* 
# Program: TL03_G4.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN 
# Tutorial Section: TL03 Group: G4
# Trimester: 2215
# Year: 2022/23 Trimester 1 
# Member_1: 1211107063 | KEK YI CI
# Member_2: 1211107030 | AIDEN CHAN KAI MING
# Member_3: 1211107031 | CHUAH YUN SHAN
# Member_4: 1211106628 | KENG JING LI
# ********************************************************* 
# Task Distribution
# Explain which function or which part of Python code you did 
# Member_1: register(), access(),registeradmin(),accessadmin(),deleteuser(),menu(),cart(Username),buy(Username),adninhome(),userhome(),home(),combine all coding 
# Member_2: adminhome(),deletehome(),deleteuser(),deleteadmin(),menu(),quit(),home()
# Member_3: cart(Username),buy(Username),rating(),report()
# Member_4: addLego() , removeLego(), adMenu(), addContent(),addLegoPro(name, promo),displayLegoPro(name),is_percentage(promo),promoMenu(),addPromo(),pc_detail(),adminselect()
# *********************************************************

def register():
    db = open("database.txt","r")#read the database textfile
    print("\n--------------------Sign up-------------------")
    Username = str(input("Create your Username: "))
    Password = str(input("Create Your Password (6-8character): "))
    confPassword = str(input("Confirm Your Password : "))
    
    d = [] #empty list to store Username
    p = [] #empty list to store password
    for i in db: #to split my text in database
        a,b = i.split(",")
        b = b.strip()#to remove the character infront the username so that username can stand alone
        d.append(a)
        p.append(b)
    data = dict(zip(d, p))# make it to the pair and read the data 
    
    if(Password != confPassword): 
        print("Invalid Password Combination.")
        #if password not same to the comfirm password will show invalid password combination
        ask_again = str(input("Do you wish to continue sign up as new user?(y/n): "))
        if ask_again == "y":
            register()
        else:
            home()
        
    else:
        if len (Password)<=6:
            print ("Password too weak,you need to reenter a new password more than 6 alphabet or number.")
            # if the password less than 6 alphabet or number will print password is too weak
            ask_reg = str(input("Do you wish to continue sign up as new user?(y/n): "))
            if ask_reg == "y":
                register()
            else:
                home()
                
        elif Username in d:
            print("Username has been used")
            #if the username in the d list will print username has been used
            ask_reg_1 = str(input("Do you wish to continue sign up as new user?(y/n): "))
            if ask_reg_1 == "y":
                register()
            else:
                home()
            
        else:
            db = open("database.txt", "a+") 
            # Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. 
            # If the file does not exist, it creates a new file for reading and writing.
            db.write(Username+", "+Password+"\n") #\n a type of escape character that will create a new line when used. 
            db.close()
            print("Success!")
            suc_1 = input("Do you want to back to main page or login?(h/l): ")
            if suc_1 == "l":
                access()
            else:
                home()

def access(): 
    db = open("database.txt","r")
    global Username
    print("\n------------------Login-----------------")
    Username = str(input("Enter Your Username : "))
    Password = str(input("Enter Your Password : "))
    
    # if your input username or password number is bigger than one 
    if not len(Username or Password)<1:
        d = [] #empty list to store Username
        p = [] #empty list to store Password
        for i in db: #to split my text in database
            a,b = i.split(",")
            b = b.strip()#to remove the character infront the username so that username can stand alone
            d.append(a)
            p.append(b)
        data = dict(zip(d, p))
        
        try:
            if data[Username]:
            #if data contain the username try following
                try: 
                    if Password == data[Username]:
                    #check if password and username is it match
                        print("\nLogin success!")
                        print("Hi,", Username)
                        menu()  
                        
                    else:
                        print("Password or Username incorrect")
                        ask = str(input("Do you wish to continue login as user?(y/n): "))
                        if ask == "y":
                            access()
                        else:
                            home()
                except: 
                    print("Incorrect password or username")
                    ask1 = str(input("Do you wish to continue login as user?(y/n): "))
                    if ask1 == "y":
                        access()
                    else:
                        home()
            else:
                print("Username or password doesn't exist")
                ask2 = str(input("Do you wish to continue login as user?(y/n): "))
                if ask2 == "y":
                    access()
                else:
                    home()
        except:
            print("Username or password doesn't exist")
            ask3 = str(input("Do you wish to continue login as user?(y/n): "))
            if ask3 == "y":
                access()
            else:
                home()  
    else:
        print("Please enter a value")
        access()

def registeradmin():
    db = open("admindatabase.txt","r")
    print("\n------------------Admin Sign up -----------------")
    print("Please fill in:")
    Username = str(input("Create your Username: "))
    Password = str(input("Create Your Password (6-8charac1): "))
    confPassword = str(input("Confirm Your Password : "))
    
    d = [] #empty list to store Username
    p = [] 
    for i in db: #to split my text in admindatabase
        a,b = i.split(",")
        b = b.strip()#to remove the character infront the username so that username can stand alone
        d.append(a)
        p.append(b)
    data = dict(zip(d, p))
    
    if(Password != confPassword):
        print("Invalid Password Combination.")
        ask_admin_1 = str(input("Do you wish to continue sign up as new admin?(y/n): "))
        if ask_admin_1 == "y":
            registeradmin()
        else:
            home()
        
    else:
      if len (Password)<=6:
        print ("Password too weak, you need to reenter a new password more than 6 alphabet or number")
        ask_admin_2 = str(input("Do you wish to continue sign up as new admin?(y/n): "))
        if ask_admin_2 == "y":
            registeradmin()
        else:
            home()
            
      elif Username in d:
        print("Username has been used")
        ask_admin_3 = str(input("Do you wish to continue sign up as new admin?(y/n): "))
        if ask_admin_3 == "y":
            registeradmin()
        else:
            home()
      else:
        db = open("admindatabase.txt", "a+")
        db.write(Username+", "+Password+"\n")
        db.close()
        
        print("Success!")
        suc_2 = str(input("Do you want to back to home or continue login?(h/l): "))
        if suc_2 == "l":
            accessadmin()
        else:
            home()           

def accessadmin():
    db = open("admindatabase.txt","r")
    print("\n------------------Admin Login-----------------")
    Username = str(input("Enter Your Username : "))
    Password = str(input("Enter Your Password : "))
    
    # if your username or password isnt true
    if not len(Username or Password)<1:
    
        d = [] #empty list to store Username
        p = [] #empty list to store Password
        for i in db: #to split my text in admindatabase
            a,b = i.split(",")
            b = b.strip()#to remove the character infront the username so that username can stand alone
            d.append(a)
            p.append(b)
        data = dict(zip(d, p))
        
        try:
            if data[Username]:
            #if data contain the username try following
                try: 
                    if Password == data[Username]:
                    #check if password and username is it match
                        print("Login success")
                        print("Hi,", Username)
                        adminselect()
                    else:
                        print("Password or Username incorrect")
                        ask_adminacc = str(input("Do you wish to continue?(y/n): "))
                        if ask_adminacc == "y":
                            accessadmin()
                        else:
                            home()

                except: 
                    print("Incorrect password or username")
                    ask_adminacc_1 = str(input("Do you wish to continue?(y/n): "))
                    if ask_adminacc_1 == "y":
                        accessadmin()
                    else:
                        home()

            else:
                print("Username or password doesn't exist")
                ask_adminacc_2 = str(input("Do you wish to continue?(y/n): "))
                if ask_adminacc_2 == "y":
                    accessadmin()
                else:
                    home()

        except:
            print("Username or password doesn't exist")
            ask_adminacc_3 = str(input("Do you wish to continue?(y/n): "))
            if ask_adminacc_3 == "y":
                accessadmin()
            else:
                home()

    else:
        print("Please enter a value")
        accessadmin()
 
def deletehome(delete_option=None):
#Here we define the function for "Delete" process
    delete_option = input("Delete User account type 1, delete admin account type 2: ")
    #Asks user to choose to delete type of account 
    if delete_option == "1":
        deleteuser()
    #If user inputs 1 then we redirect them to deleteuser() function
    elif delete_option == "2":
        deleteadmin()
    #Else if user inputs 2 then we redirect them to deleteadmin() function
    else:
        print("Invalid choice. Please pick again")
        deletehome()
    #Else we tell user they had input an invalid choice and pick again 
    
def deleteuser():
#Here we define a function for user to continue their delete process
    db_del = open("database.txt", "r")
    #Here we will open our database and start reading the account information from it
    
    print("Please enter the account details that you want to delete")
    del_user = str(input("Username: "))
    del_pass = str(input("Password: "))
    #Then we ask users to insert the account details they chose to delete
    
    if not len(del_user or del_pass)<1:
    
        d = [] #empty list to store Username
        p = [] #empty list to store Password
        for i in db_del: #to split my text in database
            a,b = i.split(",")
            b = b.strip()#to remove the character infront the username so that username can stand alone
            d.append(a)
            p.append(b)
        data = dict(zip(d, p))
   
        try:
            if data[del_user]:
            #if data contain the username try following
                try: 
    
                    if del_pass == data[del_user] :
                        confirm1 = str(input("Are you really sure you want to remove your account (y/n): "))
                        #We make sure the user wants to remove their account
                        confirm2 = confirm1.lower()
                        #Lower case the input in case user inputs their answer in upper case
                        if confirm2 == "y":
                        #If user confirmed they want to remove their account then we proceed with the procedure
                            try:
                                fileHandle = open("database.txt", "r")
                                lines = fileHandle.readlines()
                                fileHandle.close()
                                
                                try:
                                    fileHandle = open("database.txt", "w")
                                    lineText = del_user+", "+del_pass
                                  
                                    chk=0
                                    for line in lines:
                                      if line.strip("\n") != lineText:
                                        fileHandle.write(line)
                                        
                                      else:
                                        chk=1
                                    fileHandle.close()
                                    if chk==1:
                                      print("\nAccount has been deleted succesfully! We're sorry to see you go :-(")
                                    else:
                                        print("\nThe account doesn't exist!")
                                        ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                                        if ask1 == "y":
                                            deleteuser()
                                        else:
                                            home()  
                                except IOError:
                                    print("\nError Occurred !")
                                    ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                                    if ask1 == "y":
                                        deleteuser()
                                    else:
                                        home()  
                            except:
                                print("Oops! Error occured!")
                                ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                                if ask1 == "y":
                                    deleteuser()
                                else:
                                    home()  
                        else:
                            print("We're glad that you chose to stay with us!")
                            home()
                            #If user made a mistake and dont want to remove their account then we bring them back to the home page
                            #If the account and password match with the database then the system will remove the accounts they desired for
                    else:
                        print("Incorrect password or username")
                        ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                        if ask1 == "y":
                            deleteuser()
                        else:
                            home()  
                except:
                    print("Incorrect password or username")
                    ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                    if ask1 == "y":
                        deleteuser()
                    else:
                        home()  
            else:
                print("Username or password doesn't exist")
                ask1 = str(input("Do you wish to continue delete as user?(y/n): "))
                if ask1 == "y":
                    deleteuser()
                else:
                    home()  
        except:
            print("Username or password doesn't exist. Please try again")
            ask_del_user = str(input("Do you wish to continue?(y/n): "))
            if ask_del_user == "y":
                deleteuser()
            else:
                home()            
    else:
        print("Please enter a value")
        deleteuser()       
        

def deleteadmin():
#Here we define a function for admin to continue their delete process
    db_del_admin = open("admindatabase.txt", "r")
    #Here we will open our database and start reading the account information from it
    
    print("Please enter the account details that you want to delete")
    del_admin = str(input("Username: "))
    del_pass_admin = str(input("Password: "))
    #Then we ask users to insert the account details they chose to delete
    
    if not len(del_admin  or del_pass_admin)<1:
    
        d = [] #empty list to store Username
        p = [] #empty list to store Password
        for i in db_del_admin: #to split my text in database
            a,b = i.split(",")
            b = b.strip()#to remove the character infront the username so that username can stand alone
            d.append(a)
            p.append(b)
        data = dict(zip(d, p))
        
        try:
            if data[del_admin]:
            #if data contain the username try following
                try: 
    
                    if del_pass_admin == data[del_admin] :
                        confirm1 = str(input("Are you really sure you want to remove your account (y/n): "))
                        #We make sure the user wants to remove their account
                        confirm2 = confirm1.lower()
                        #Lower case the input in case user inputs their answer in upper case
                        if confirm2 == "y":
                        #If user confirmed they want to remove their account then we proceed with the procedure
                            try:
                                fileHandle = open("admindatabase.txt", "r")
                                lines = fileHandle.readlines()
                                fileHandle.close()
                                
                                try:
                                    fileHandle = open("admindatabase.txt", "w")
                                    lineText = del_admin+", "+del_pass_admin
                                    
                                    chk=0
                                    for line in lines:
                                      if line.strip("\n") != lineText:
                                        fileHandle.write(line)
                                        
                                      else:
                                        chk=1
                                    fileHandle.close()
                                    if chk==1:
                                      print("\nAccount has been deleted succesfully! We're sorry to see you go :-(")
                                    else:
                                        print("\nThe account doesn't exist!")
                                        ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                                        if ask_del_admin == "y":
                                            deleteadmin()
                                        else:
                                            home()
                                except IOError:
                                    print("\nError Occurred ")  
                                    ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                                    if ask_del_admin == "y":
                                        deleteadmin()
                                    else:
                                        home()
                                    
                            except:
                                print("Oops! something error")
                                ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                                if ask_del_admin == "y":
                                    deleteadmin()
                                else:
                                    home()
                        else:
                            print("We're glad that you chose to stay with us!")
                            home()
                            #If user made a mistake and dont want to remove their account then we bring them back to the home page
                            #If the account and password match with the database then the system will remove the accounts they desired for
                    else:
                        print("Incorrect password or username")
                        ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                        if ask_del_admin == "y":
                            deleteadmin()
                        else:
                            home()
                except:
                    print("Incorrect password or username")
                    ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                    if ask_del_admin == "y":
                        deleteadmin()
                    else:
                        home()
            else:
                print("Username or password doesn't exist")
                ask_del_admin = str(input("Do you wish to continue?(y/n): "))
                if ask_del_admin == "y":
                    deleteadmin()
                else:
                    home()
        except:
            print("Username or password doesn't exist")
            ask_del_admin_2 = str(input("Do you wish to continue?(y/n): "))
            if ask_del_admin_2 == "y":
                deleteadmin()
            else:
                home()
    else:
        print("Please enter a value")
        deleteadmin()



def menu():

    while True:

        print("\nWelcome to our LEGO Store. How may we assist you?")
        print("1) Theme")
        print("2) Hot Sales")
        print("3) Upcoming Promotion")
        print("4) Cart")
        print("5) Buy")
        print("6) Sign Out")
        #Here we print the options that are available in menu
        choice_menu = str(input("Enter choice: "))
        print("")
        
        #Then we let users to choose anything they're interested in 
    
        if choice_menu == "1":
            print("LEGO theme:")
            # Open the file in reading mode
            with open('legocontent.txt', 'r') as menur:
                # Read the lines of the file
                lines = menur.readlines()
                # Initialize a counter variable
                counter = 1
                # Iterate through the lines and print them with the line number and data items
                for line in lines:
                    # Split the line into a list of data items
                    data = line.strip().split('\n')
                    # Print the line number and data items
                    print(f'{counter}. {data}')                    # Increment the counter
                    counter += 1
                 
                  
        #Else if user pick choice one then we will provide the themes that are in store
        
        elif choice_menu == "2":
            print("LEGO top sales in previous month:")
            print("Top Seller: Tecnic")
            print("Second Best Seller: Marvel")
            print("Third Best Seller: Duplo")
        #Else if the user pick choice two then we will provide the statistic on seller ranking
    
        elif choice_menu == "3":
            print("Upcoming LEGO Promotion:")
            with open('legopromo.txt', 'r') as menur:
                # Read the lines of the file
                lines = menur.readlines()
                # Initialize a counter variable
                counter = 1
                # Iterate through the lines and print them with the line number and data items
                for line in lines:
                    # Split the line into a list of data items
                    
                    a,b = line.split(",")
                    b = b.strip()
                    a = a.title()
                    # Print the line number and data items
                    print(f'{counter}. {b+" off"}:{a}')                    
                    # Increment the counter
                    counter += 1          
                   
        #If the user pick choice 3 then we show them which themes are currently having a discount
        
        elif choice_menu == "4":
            cart(Username)
            
        elif choice_menu == "5":
            buy(Username)
            
        elif choice_menu == "6":
            print("You have sign out succesfully. Have a nice day <3")
            home()
            break
            
        #Else if user pick choice 6 then we break the loop
        
        else:
            print("Invalid option. Please try again")
            
        #Else we just end the session since use pick something invalid
        
        
def cart (Username):
    #print the item that available right now
    print("Items available:")
    print("a) Ideas RM100")
    print("b) Harry Potter RM200")
    print("c) Marvel RM250")
    print("d) Duplo RM150")
    print("e) Technic RM150")
    cart = []
    sum = 0
    #This is the loop if you want add item to cart select yes, if no the loop will stop it immediately and print the item and total price
    while True:
        select = input("Do you want to add item to your cart?(y/n): ")
        select = select.strip()
        
        if select == "y":
            print("Which item would you like to add to cart?")
            choice_cart = input("Enter choice: ")
            choice_cart = choice_cart.strip()
            
            if choice_cart == "a":
                a = "Ideas"
                sum = sum + 100
                cart.append(a)
                print("Your item added to the cart Successfully!\n")
                
            elif choice_cart == "b":
                b = "Harry Potter"
                sum = sum + 200
                cart.append(b)
                print("Your item added to the cart Successfully!\n")
                
            elif choice_cart == "c":
                c = "Marvel"
                sum = sum + 250
                cart.append(c)
                print("Your item added to the cart Successfully! \n")
                
            elif choice_cart == "d":
                d = "Duplo"
                sum = sum + 150
                cart.append(d)
                print("Your item added to the cart Successfully! \n")
                
            elif choice_cart == "e":
                e = "Technic"
                sum = sum + 150
                cart.append(e)
                print("Your item added to the cart Successfully! \n")
               
            else:
                print("Invalid choice, please try again.\n")
                    
        elif select == "n":
            showsum = sum
            #the join is to combine all the item that added to cart list into one line by using the comma
            product = ",".join(cart)
            
            if sum == 0 :
                print ("\nThere no item added. Take your time to continue shopping")
                break
            
            else :
                # create a variable to check if the username exists or not
                username_exists = False
                with open("cart.txt", "r+") as cartfile:
                    lines = cartfile.readlines()
                    # Iterate over the lines 
                    # i represent the index of the current element
                    # line represent the username item that added to cart
                    # enumerate the function return an iterator that generate pair containing i and line
                    # lines is the data inside the cart file
                    for i, line in enumerate(lines):
                        if line.startswith(Username):
                            productParts = line.split(":")
                            #[1] is used to access the second element of the list 
                            existing_product = productParts[1].strip()
                            new_product = existing_product + f",{product}"
                            new_line = f"{Username}:{new_product}\n"
                            lines[i] = new_line
                            # Set the flag to True
                            username_exists = True
                            break
                    if not username_exists:
                        cartfile.write(f"{Username}:{product}\n")
                    else:
                        # Go to the beginning of the file
                        cartfile.seek(0)
                        # Write the lines back to the file
                        cartfile.writelines(lines)
                        cartfile.close()
                        
                with open("buy.txt", "r+") as buyfile:
                    lines = buyfile.readlines()
                    # Iterate over the lines
                    for i, line in enumerate(lines):
                        if line.startswith(Username):
                            priceParts = line.split(":")
                            existing_price = priceParts[1].strip()
                            new_price = int(existing_price) + sum
                            new_line = f"{Username}:{new_price}\n"
                            lines[i] = new_line
                            # Set the flag to True
                            username_exists = True
                            break
                    if not username_exists:
                        buyfile.write(f"{Username}: {showsum}\n")
                    else:
                        # Go to the beginning of the file
                        buyfile.seek(0)
                        # Write the lines back to the file
                        buyfile.writelines(lines)
                        buyfile.close()

                print("\nAll item added to cart successfully.")
                print("Item you added to cart:", product)
                print("Total amount: RM",sum)
                break
        else:
            print("Invalid choice, please try again")
            
def buy(Username):
    cartcontents = open ("cart.txt", "r")  
    contents = cartcontents.read()
    # check if the file is empty
    if len(contents) == 0:
        print("There no Item in the cart list. Please add some product to cart.") 
    
    else:
        cart = open ("cart.txt", "r")
        for line in cart:
            if line.startswith(Username):   
                buyerProduct = line.split(":")[1]
                buyerItem = buyerProduct.strip()

                #read the cart text file
                #if the line start with the username that input, than it will split the line with this :
                #buyerItem is to remove any leading space at the first and the end
                buy = open ("buy.txt","r")
                for line in buy:
                    if line.startswith(Username):
                        priceProduct = line.split(":")[1]
                        priceItem = priceProduct.strip()

                    print ( "Item you added to cart:", buyerItem )
                    print ( "Total amount: RM",priceItem)
                    print("This is your cart item\n")
                    print("Do you wish to buy this item")
                    choice_buy = str(input("If yes put y, If no put n: "))
                    choice_buy = choice_buy.strip()
                    if choice_buy == "y":
                        purDetail  = open("purchaseDetail.txt", "a+") 
                        purDetail.write(f"{Username}:{buyerItem} = RM{priceItem}\n")
                        purDetail.close()
                        #write the purachase detail into the text file so that the admin know what item that user buy 
                        
                        with open("cart.txt", "r") as cartr:
                            cartlines = cartr.readlines()
                            # create a new list with the modified cartlines
                            modified_cartlines = []
                            for line in cartlines:
                                if not line.startswith(Username) or not line.endswith(buyerProduct):
                                #using buyerProduct but not buyerItem is because the buyerItem remove all any leading space at the front and at the back 
                                  modified_cartlines.append(line)
                                  
                            # write the modified list back to the file
                            with open("cart.txt", "w") as cartw:
                                cartw.writelines(modified_cartlines)
                                cartw.close()
                        #remove the cart item so that the item wont repeat print out the old item when the user add new item in cart
                                
                        with open ("buy.txt","r") as buyr:
                            buylines = buyr.readlines()
                            modified_buylines = []
                            for line in buylines:
                                if not line.startswith(Username) or not line.endswith(priceProduct):
                                    modified_buylines.append(line)
                            
                            with open("buy.txt","w") as buyw:
                                buyw.writelines(modified_buylines)
                                buyw.close()    
                                
                        print("You buy the item successfullly","\n")
                        rating()
                        
                    elif choice_buy == "n":
                        print("Take your time to continue shopping")
                        

                    else:
                        print("Invalid option.")
            else:
                print("There no Item in the cart list. Please go to the cart add some product.") 
                
def rating():
    print("Please rate the our service")
    print("From the rating scale of 1-5")
    choice_rate = float(input("Rating: "))

    if choice_rate <= 1:
        Reason = str(input("\nwhat should we improve for our service: "))
        print("Thanks for the rating and comment, we will improve our service!")
        
    elif choice_rate <=2 and choice_rate>=1:
        Reason = str(input("\nwhat should we improve for our service: "))
        print("Thanks for the rating and comment, we will improve our service!")
        
    elif choice_rate <=3 and choice_rate>=2:
        Reason = str(input("\nwhat should we improve for our service: "))
        print("Thanks for the rating and comment, we will improve our service!")
        
    elif choice_rate <=4 and choice_rate>=3:
        Reason = str(input("\nwhat should we improve for our service: "))
        print("Thanks for the rating and comment, we will improve our service!")
        
    elif choice_rate <=5 and choice_rate>=4:
        Reason = str(input("\nwhat should we improve for our service: "))
        print("Thanks for the rating and comment, we will improve our service!")
    
    elif choice_rate == None:
        print("Invalid Number, please try again\n")
        rating()
        #the none is used to define  a null valuse or no value at all

    else:  
        print("Invalid Number, please try again\n")
        rating()


def report():
    print("\nHello! Welcome to our LEGO store!")
    print("How may we assist you?")
    print("1) New sets with missing part")
    print("2) New sets with damage part")
    print("If you have any other reports please press 3")
    
    choice_chat = input("\nEnter choice: ")
    choice_chat = choice_chat.strip()

    if choice_chat == "1":
        print("\nWe're really sorry to hear that something was missing from your new LEGO set. We do our best to make every set perfect and we take it very seriously when a faulty one sneaks through. Don't worry though, we can send you the parts you need!")
        home()
    elif choice_chat == "2":
        print("\nWe take it very seriously if your LEGO set isn't perfect and we'd like to send you a replacement as soon as possible.")
        home()
    elif choice_chat == "3":
        report = str(input("Comment here: "))
        print("\nYour report has been submitted. We will try to get back to you ASAP!")
        home()
    else: 
        print("\nPlease enter a given option")
        home()

       
def addLego(newName):    # add new lego item
    newName = newName.upper()   # convert newName to upper case, matching regardless of the case of the characters.
    LegoList = []       # empty list to store lego name
    LegoFile = open('legocontent.txt', "r")     # open txt file in read mode 
    LegoList = [line.strip().upper() for line in LegoFile]      # .strip() to remove whitespace from line       # .upper() to convert line into uppercase
    LegoFile.close()
    
    if newName not in LegoList:     # check if newName in list or not
        LegoList.append(newName)    # add newName in list       # .append() to add newName at the end of the list
        LegoFile = open("legocontent.txt", "a")     # save info in file 
        LegoFile.write( newName +"\n")      # open txt file and write the name 
        LegoFile.close()    
        print("LEGO® " +newName+ " successfully ADDED.")
        return LegoList
    else:
        print("LEGO® " +newName+ " already exists. Please enter a different LEGO item.")
        return LegoList

def removeLego(delName):      # remove lego item      
    delName = delName.upper()
    LegoList = []
    LegoFile = open('legocontent.txt', "r")
    LegoList = [line.strip().upper() for line in LegoFile]   
    LegoFile.close()

    if delName in LegoList:    # check if delName is in the file
        LegoList.remove(delName)   # remove delName from the list
        LegoFile = open("legocontent.txt", "w")     # open txt file in write mode    
        for name in LegoList:   
            LegoFile.write(name + "\n") # rewrite the updated list to file
        LegoFile.close()
        print("LEGO® " + delName + " successfully REMOVED.")
        return LegoList

    else:
        print("LEGO® " + delName + " not found.")
        return LegoList

def adMenu():
    print("==========================")
    print("1 - Add new LEGO item")
    print("2 - Remove LEGO item")
    print("3 - Exit")
    print("==========================")

def addProduct():
    runProgram = True
    while runProgram:
        invalidOption = False
        adMenu()
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)
            
            if option == 1:
                newName = input("Enter new LEGO to add: ")
                addLego(newName) 

            elif option == 2:
                delName = input("Enter LEGO to remove: ")
                removeLego(delName)
                
            elif option == 3:
                runProgram = False
                print("---------Bye---------\n")
                adminselect()

            else:
                invalidOption = True
        else:
            invalidOption = True
            
        if invalidOption:
            print("INVALID option. Please select another option.\n")
            addProduct()

def addLegoPro(name, promo): 
    name = name.upper()
    promoList = []  # read data from file and store it in promoList    
    with open("legopromo.txt", "r") as promoFile:
        promoList = promoFile.readlines()       # read the file line by line

    for i in promoList:
        n, p = i.strip().split(", ")    # .strip() to remove whitespace     # .split(", ") to split the comma and space
        if n.upper() == name:        
            promoList.remove(i)     # if n same with name remove i in list
            promoList.append(f"{name}, {promo}\n")          
            break
    else:
        promoList.append(f"{name}, {promo}\n")
        
    with open("legopromo.txt", "w") as promoFile:
        promoFile.writelines(promoList)     # write the updated list line by line in file
    
    print(f"{promo} OFF for LEGO® {name}.")
    return promoList

def displayLegoPro(name):
    name = name.upper()
    with open("legopromo.txt", "r") as promoFile:
        for line in promoFile:
            n, p = line.strip().split(", ")
            if n.upper() == name:
                print("LEGO® " +name+ " has a " + p +" OFF promotion.")
                return
        else:
            print("There is no promotion for LEGO® "+name+".")

def is_percentage(promo):   # check if input is a percentage 
    if promo.endswith('%') and promo[:-1].isdigit():
        return True
    return False

def promoMenu():
    print("==========================")
    print("1 - Add LEGO's promotion")
    print("2 - Check LEGO's promotion")
    print("3 - Exit")
    print("==========================")

def addPromo():
    runProgram = True
    while runProgram:
        invalidOption = False
        promoMenu()
        option = input("\nSelect a menu option: ")
        if option.isdigit():
            option = int(option)

            if option == 1:
                name = input("Add which LEGO's promotion? ")
                promo = input("Enter " + name +"'s promotion: ")
                if is_percentage(promo):  
                    addLegoPro(name, promo)
                else:
                    print("Please enter a valid percentage (e.g. 10%).")
             
            elif option == 2:
                name = input("Check which LEGO's promotion? ")
                displayLegoPro(name)
            
            elif option == 3:
                runProgram = False
                print("---------Bye---------\n")
                adminselect()

            else:
                invalidOption = True
        else:
            invalidOption = True
            
        if invalidOption:
            print("INVALID option. Please select another option.\n")
            addPromo()

def pc_detail():    # check purchase detail
    f = open('purchaseDetail.txt', "r")
    detail = f.read()    # read the entire contents of the file 
    print(detail + "\n")
    f.close()
    return adminselect()

def adminselect():
    print("Press 1: Add product")
    print("Press 2: Add promotion")
    print("Press 3: Check purchase detail")
    print("Press 4: Sign out")

    option = input ("\nSelect a number: ")

    if option == "1":
        addProduct()
        
    elif option == "2":
        addPromo()

    elif option == "3":
        pc_detail()
    
    elif option == "4":
        print("You have sign out succesfully. Have  a nice day <3")
        home()
        
    else:
        print("INVALID option. Please select another option.\n")
        adminselect()
def userhome():
    print("\nWelcome to User section:")
    print("1. Login ")
    print("2. Sign up")
    print("3. Delete User acccount")
    option = input ("Select a number: ")
    
    if option == "1":
        access()
        
    elif option == "2":
        register()

    elif option == "3":
        deleteuser()
        
    else:
        print(" Please enter an option.\n")
        userhome()

def adminhome(adminoption=None ):
    print("\nWelcome to Admin section:")
    print("1. Login ")
    print("2. Sign up")
    print("3. Delete Admin acccount")
    adminoption = input ("\nSelect a number: ")
    print("")
    
    if adminoption == "2":
        registeradmin()
        
    elif adminoption == "1":
        accessadmin()
        
    elif adminoption == "3":
        deleteadmin()
        
    else:
        print("Please enter an option.")
        adminhome()    
        
def quit():
    print("Thank you for your visit! See you again")
    
    
            
def home(option=None ):
#Here we define the function for users to pick their choice of function in the program
    print ("Welcome to our LEGO home pages")
    print ("1. User")
    print ("2. Admin")
    print ("3. Report")
    print ("4. Quit")
    option = str(input ("Please select a number: "))
    #Then we let user the pick any functions from the list

    if option == "1":
        userhome()

    elif option == "2":
        adminhome()
    
    elif option == "3":
        report()
        
    elif option == "4":
        quit()
        
    else:
        print("Please enter an option")
        home()
     
home()

