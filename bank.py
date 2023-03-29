import csv
import time
import sys
import random
import os
from getpass import getpass
import string
import colorama
from colorama import Fore


###################################################

#Function to take password input as *****
def get_password(prompt):
    password = ""
    print(prompt, end="", flush=True)
    if os.name == 'nt':
        import msvcrt
        while True:
            key = msvcrt.getch() 
            if key == b"\r" or key == b"\n":
                print()
                return password
            elif key == b"\b":
                if password:
                    password = password[:-1]
                    print("\b \b", end="", flush=True)
            elif key == b"\x03":
                raise KeyboardInterrupt
            else:
                password += key.decode("utf-8")
                print("*", end="", flush=True)
    else:
        password = getpass('')
        return password

############################################################

def clear_terminal(): # to clear the terminal
    """Clears the terminal screen."""

    if os.name == "nt": #for Windows
        os.system("cls")
    else:
        os.system("clear") # for Linux and Mac os

    banner = '''

  ____              _             __   ____  _ _       _          _     
 |  _ \            | |           / _| |  _ \(_) |     | |        ( )    
 | |_) | __ _ _ __ | | __   ___ | |_  | |_) |_| |_ ___| |__   ___|/ ___ 
 |  _ < / _` | '_ \| |/ /  / _ \|  _| |  _ <| | __/ __| '_ \ / _ \ / __|
 | |_) | (_| | | | |   <  | (_) | |   | |_) | | || (__| | | |  __/ \__ \\
 |____/ \__,_|_| |_|_|\_\  \___/|_|   |____/|_|\__\___|_| |_|\___| |___/
                                                                        
                                                                        
                                                            By Tamimul Ahsan                                                            
    '''
    print(f"\n\n{banner}")

##############################################################

words = string.ascii_letters
r_words = random.choices(words,k=5)


#############################################################################
def register(): # Create new account 

    clear_terminal()
    print(f"\t\t\tRegister\n\n")


    def savings(): # Savings account creation

        acc_num = '547136'+ str(random.randint(1111111,9999999))
        acc_balance = 0
        name = input('Full Name: ')
        fath_name = input("Father's Name: ")
        moth_name = input("Mother's Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        contact = input("Contact Number: ")
        nid = input("National ID no: ")
        email = input("E-mail: ")
        address = input('Address: ')
        duration = ""
        while True:
            acc_duration = input('Select Account Duration:\n1. 2 Years\n2. 5 Years\n3. 10 Years\n > ')
            if acc_duration == '1':
                duration = '2 Years'
                break
            elif acc_duration == '2':
                duration = '5 Years'
                break
            elif acc_duration == '3':
                duration = "10 years"
                break
            else:
                print("\nInvalid Choice\n")
                time.sleep(1)
        time.sleep(2)
        clear_terminal()

        print('Review Your Final Info\n\n')
        print(f'Name: {name}\nNational ID: {nid}\nE-mail: {email}\nContact: {contact}')
        input('\nPress Enter to Continue')
        clear_terminal()
        print('Creating Account......')
        time.sleep(5)

        username = name.split()[0]+contact[-4:]+random.choice(words)+'s'
        k = ""
        for i in r_words:
            k+=i
        password = k+contact[:5]


        with open("CSVs/savings.csv","a",newline='') as file: # Append the infos of account in the co-responding csv file 
            writer = csv.writer(file)
            writer.writerow([username,acc_num,name,fath_name,moth_name,dob,contact,nid,email,address,duration])
        
        with open('CSVs/all_visible.csv',"a",newline="") as file: # append the infos to the public csv file that is accessible to everyone
            writer = csv.writer(file)
            writer.writerow([acc_num,name,'Savings',email])


        with open("acc_details/username_password.txt","a") as file: # store username and password
            file.write(f"{username}:{password}\n")

        with open("acc_details/acc_bal.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,acc_balance])

        
        print('Account Created SuccessFully\n')
        time.sleep(5)

        print(f'Account Number: {acc_num}\nRouting Number: {55254}\nUser id: {username}\nPassword: {password}\nChange the password after logging in.')
        input('\nPress Enter to continue')
        time.sleep(2)



    def checking(): # Checking account registration

        acc_num = '361572'+str(random.randint(1111111,9999999))
        acc_balance = 0
        name = input('Full Name: ')
        fath_name = input("Father's Name: ")
        moth_name = input("Mother's Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        contact = input("Contact Number: ")
        nid = input("National ID no: ")
        email = input("E-mail: ")
        address = input('Address: ')
        monthly_tnx = input('Monthly expected Transaction amount: ')
        clear_terminal()

        print('Review Your Final Info')
        print(f'Name: {name}\nNational ID: {nid}\nE-mail: {email}\nContact: {contact}')
        input("Press Enter To Continue\n")
        time.sleep(2)
        clear_terminal()

        
        username = name.split()[0]+contact[-4:]+random.choice(words)+'c'
        k = ""
        for i in r_words:
            k+=i
        password = k+contact[:5]


        with open("CSVs/checking.csv","a",newline='') as file: # store the infos in a private co-responding csv
            writer = csv.writer(file)
            writer.writerow([username,acc_num,name,fath_name,moth_name,dob,contact,nid,email,address,monthly_tnx])
        
        with open('CSVs/all_visible.csv',"a",newline="") as file: # publically accessible csv
            writer = csv.writer(file)
            writer.writerow([acc_num,name,'checking',email])


        with open("acc_details/username_password.txt","a") as file: # store username and password
            file.write(f"{username}:{password}\n")

        with open("acc_details/acc_bal.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,acc_balance])

        
        print('\nCreating Account..')
        time.sleep(2)
        print("\nAccount Created SuccessFully")
        time.sleep(2)

        print(f'Account Number: {acc_num}\nRouting Number: {55254}\nUser id: {username}\nPassword: {password}\nChange the password after logging in.')
        input('\nPress Enter to continue')
        time.sleep(2)


    def student(): # student account registration
        acc_num = '573942'+ str(random.randint(1111111,9999999))
        acc_balance = 0
        name = input('Full Name: ')
        fath_name = input("Father's Name: ")
        fath_mobile = input("Father's Mobile Number: ")
        fath_nid = input("Father's National ID no: ")
        moth_name = input("Mother's Name: ")
        dob = input("Date of Birth (DD/MM/YYYY): ")
        contact = input("Contact Number: ")
        nid = input("National ID no: ")
        stud_id = input("Student ID no: ")
        inst = input("Institution Name: ")
        email = input("E-mail: ")
        address = input('Address: ')
        clear_terminal()

        print('Review Your Final Info\n\n')
        print(f'Name: {name}\nNational ID: {nid}\nE-mail: {email}\nContact: {contact}')
        input("Press Enter To Continue\n")
        time.sleep(2)
        clear_terminal()

        username = name.split()[0]+contact[-4:]+random.choice(words)+'t'
        k = ""
        for i in r_words:
            k+=i
        password = k+contact[:5]


        with open("CSVs/student.csv","a",newline='') as file: # private csv file
            writer = csv.writer(file)
            writer.writerow([username,acc_num,name,fath_name,fath_mobile,fath_nid,moth_name,dob,contact,nid,stud_id,inst,email,address])
        
        with open('CSVs/all_visible.csv',"a",newline="") as file: # public csv file
            writer = csv.writer(file)
            writer.writerow([acc_num,name,'student',email])


        with open("acc_details/username_password.txt","a") as file: # username and password
            file.write(f"{username}:{password}\n")

        with open("acc_details/acc_bal.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,acc_balance])

        print('\nCreating Account...')
        time.sleep(2)

        print('\nAccount Created Successful')

        print(f'Account Number: {acc_num}\nRouting Number: {55254}\nUser id: {username}\nPassword: {password}\nChange the password after logging in.')
        input('\nPress Enter to continue')
        time.sleep(2)


    while True:
        acc_type = input('Select Account Type\n1. Savings\n2. Checking\n3. Student\n0. Main Menu\n > ')
        
        if acc_type == '1':
            savings()
            welcome_menu()
        elif acc_type == '2':
            checking()
            welcome_menu()
        elif acc_type == '3':
            student()
            welcome_menu()
        elif acc_type == '0':
            clear_terminal()
            welcome_menu()
        else:
            print("Invalid Choice")
            clear_terminal()
            register()

#######################################################################################


def login(): # login function
    global usrnm
    clear_terminal()

    print(f"\t\t\tLogin\n\n") 

    username = input('Enter Username: ')
    password = get_password("Enter Password: ")

    with open("acc_details/username_password.txt","r")as file:

        for line in file:
            if line.strip() == f"{username}:{password}":
                identifier = username[-1]
                usrnm = username
                print("login Successful")
                time.sleep(2)

                if identifier == 'c':
                    checking_dashboard()
                elif identifier == 's':
                    savings_dashboard()
                elif identifier == 't':
                    student_dashboard()

        else:
            print("\nInvalid Username or Password\n")
            time.sleep(2)

            x = input("Try Again? (y/n): ")
            if x.lower()=='y':
                login()
            elif x.lower() == 'n':
                welcome_menu()

########################################################################################


def welcome_menu():  # The main menu after starting the program
    clear_terminal()

    print("\t\t\tHome\n\n")
    time.sleep(2)

    while True:
        x = input(f'1. Login\n2. Register\n3. Account Types\n4. About Us\n5. Contact Us\n0. Exit\n > ')#Total users count at the bottom right of the box
        if x == '1':
            login()
        elif x == '2':
            register()
        elif x == '3':
            account_type()
        elif x == '4':
            about_us()
        elif x == '5':
            contact_us()
        elif x == '0':
            sys.exit()
        else:
            print('\nInvalid Choice')
            time.sleep(1)
            welcome_menu()


##############################################################################

def account_type(): # types and benifits of different accounts
    clear_terminal()

    print("\t\t\tAccount Types\n\n")
    print('\t\tSavings\n\nSave money on a monthly Basis for a certain amount of time.\nGet interes on your money On a yearly Basis.')
    print('Minimum Deposit amount: 10000\nWithdrawl Available after 2 Years\nYearly Charge (1500)\nFree Debit/ATM Card')

    print('\n\n\n\t\tChecking\n\nSpend,Deposit,Withdraw,Pay anytime you want.\nExcellent Interest Rate.\nDirect Deposit, Credit Card, Fund Transfer, Overdraft.')
    print('Use Cashless Banking. Yearly Charge (2500)')

    print('\n\n\n\t\tStudent\n\nAccounts Exclusively for Students.\nDirect Deposit, Withdraw, Payment, Overdraft, Credit Card, Fund Transfer.')
    print('Cashless Banking, No ATM Charge, Yearly Charge (500).\nAccount will automatically convert to Checking account after 5 Years.')
    
    input('\n\nPress Enter to Continue')
    welcome_menu()

#####################################################################################################
def about_us():
    print("About us")

#######################################################################################################

def contact_us():
    print('Contact Us')

##############################################################################################

def send_money(acc_num):
    clear_terminal()
    print("\t\t\tSend Money\n\n")
    input_filename = "acc_details/acc_bal.csv"

    dest_acc = input("Enter Recipient's Account Number: ")
    amount = input("Enter Amount: ")

    acc_bal = 0
    rec_bal = 0

    flag = False

    with open(input_filename,"r") as f:
        reader = csv.reader(f)
        for row in reader:
            if dest_acc in row:
                flag = True

    if not flag:
        print("Recipient's Account Not Found")
        time.sleep(2)
        return
    else:
        with open(input_filename,"r") as file:
            reader = csv.reader(file)
            rows = []

            for row in reader:
                if acc_num in row:
                    acc_bal = int(row[1])
                    if acc_bal < int(amount):
                        print("Not Enough Balance")
                        return
                    row[1] = str(acc_bal - int(amount))

                elif dest_acc in row:
                    rec_bal = int(row[1])
                    row[1] = str(rec_bal + int(amount))

                rows.append(row)

        # write updated rows to temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # replace original file with temporary file
        os.replace(temp_filename, input_filename)

        print("Money sent successfully.")
        time.sleep(2)
        return


###############################################################################################

def deposit(acc_num):
    clear_terminal()
    print("\t\t\tDeposit\n\n")
    input_filename = "acc_details/acc_bal.csv"

    amount = input("Enter Deposit Amount: ")

    acc_bal = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if acc_num in row:
                acc_bal = int(row[1])
                row[1] = str(acc_bal+ int(amount))

            rows.append(row)

        # write updated rows to temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    # replace original file with temporary file
    os.replace(temp_filename,input_filename)

    print("Deposit Successful.")
    time.sleep(2)
    return


##############################################################################################

def withdrawl(acc_num):
    clear_terminal()
    print("\t\t\tWithdrawl\n\n")
    input_filename = "acc_details/acc_bal.csv"

    amount = input("Enter Withdrawl Amount: ")

    acc_bal = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if acc_num in row:
                acc_bal = int(row[1])
                row[1] = str(acc_bal - int(amount))

            rows.append(row)

        # write updated rows to temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    # replace original file with temporary file
    os.replace(temp_filename,input_filename)

    print("Successful.")
    time.sleep(2)
    return


###############################################################################################

def checking_dashboard(): # check the csv file for name and account number to greet and display info
    clear_terminal()    
    ac_num = ""

    def in_checking():
        while True:
            action = input("1. Money_stuff\n2. Account Info\n3. User info\n4. Apply for Card\n5. Log Out\n0. Exit\n >  ")
            if action == '1':
                clear_terminal()
                print("\t\t\tMoney Stuff\n\n")
                x = input("1. Send\n2. Deposit\n3. Withdraw\n4. Go Back\n0. Exit > ")
                if x == '1':
                    send_money(ac_num)
                elif x == '2':
                    deposit(ac_num)
                elif x == '3':
                    withdrawl(ac_num)
                elif  x == '4':
                    checking_dashboard()
                elif x == '0':
                    sys.exit()
                else:
                    print(f"\nInvalid Choice\n")

            elif action == '2':
                clear_terminal()
                print("\t\t\tAccount Information\n\n")

                with open("acc_details/acc_bal.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if ac_num in row:
                            ac_bal = row[1]

                cc_num = ""
                cc_exp = ""
                cc_cvv = ""
                dc_num = ""
                dc_pin = ""

                with open("acc_details/cc.csv") as c:
                    reader = csv.reader(c)
                    for row in reader:
                        if ac_num in row:
                            cc_num = row[1]
                            cc_exp = row[2]
                            cc_cvv = row[3]
                    
                with open("acc_details/dc.csv") as d:
                    reader = csv.reader(d)
                    for row in reader:
                        if ac_num in row:
                            dc_num = row[1]
                            dc_pin = row[2]

                with open("CSVs/checking.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if usrnm in row:
                            print(f"Account Type: Checking\t\t\t Name    : {row[2]}")
                            print(f"Account No  : {row[1]} \t\t Balance : {ac_bal} ")
                            print("'\n\n\t\t\tCard Information\n")
                            print(f"Credit Card")
                            print("Card Number: "+ (cc_num if cc_num!="" else "N/A"))
                            print("Expiery: "+ (cc_exp if cc_exp !="" else "N/A"))
                            print("CVV: "+ (cc_cvv if cc_cvv !="" else "N/A"))
                            print("\nDebit Card")
                            print("Card Number: "+ (dc_num if dc_num!="" else "N/A"))
                            print("Pin: "+ (dc_pin if dc_pin !="" else "N/A"))
                            
                            input("\n\nPress Enter to Continue.")
                            time.sleep(2)
                            checking_dashboard()

            elif action == '3':
                clear_terminal()
                print("\t\t\tUser Information\n\n")

                with open("CSVs/checking.csv") as file:
                    reader = csv.reader(file)

                    for row in reader:
                      if usrnm in row:
                        print(f"Name    : {row[2]}\t\t\t Date Of Birth: {row[5]}")
                        print(f"Father  : {row[3]}\t\t Mother       : {row[4]}")
                        print(f"Contact : {row[6]}\t\t\t National ID  : {row[7]}")
                        print(f"E-mail  : {row[8]}\t Address      : {row[9]}")

                        input("\nPress Enter to continue")
                        time.sleep(2)

                        checking_dashboard()

            elif action == '4':
                clear_terminal()
                print("\t\t\tGet A Card")
                z = input("Card Type:\n1. Credit\n2. Debit\n > ")
                if z == '1':
                    flag = False
                    with open("acc_details/cc.csv") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if ac_num in row:
                                flag = True
                    if flag:
                        print("\nYou already have a credit card agains't your account")
                        time.sleep(5)
                        checking_dashboard()
                    else:     
                        with open("acc_details/cc.csv","a",newline='') as file:
                            writer = csv.writer(file)
                            cc_num = '415628'+str(random.randint(1111111,9999999))
                            cc_exp = str(random.randint(1, 28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(2027, 2029))
                            cc_cvv = str(random.randint(111,999))
                            writer.writerow([ac_num,cc_num,cc_exp,cc_cvv])
                            print("\nGetting Your Card Ready. Please Wait......")
                            time.sleep(5)
                            clear_terminal()
                            print("Card Generated Successfully\n\n")
                            time.sleep(2)
                            print(f"Card Type: Credit\nCard Number: {cc_num}\nExpiery Date: {cc_exp}\nCvv: {cc_cvv}\nOverdraft: 20000\n")
                            file.close()

                        with open("acc_details/overdraft.csv","a",newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([ac_num,20000])
                            file.close()
                            time.sleep(2)
                            input("Press Enter to Continue")
                            checking_dashboard()
                
                elif z == '2':
                    flag = False
                    with open("acc_details/cc.csv") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if ac_num in row:
                                flag = True
                    if flag:
                        print("\nYou already have a debit card agains't your account")
                        time.sleep(5)
                        checking_dashboard()
                    else:
                        with open("acc_details/dc.csv") as f:
                            reader = csv.reader(f)
                            for row in reader:
                                if ac_num in row:
                                    print("\n\nYou Already have A Debit card against your account")
                                    time.sleep(5)
                                    checking_dashboard()
                                else:
                                    with open("acc_details/dc.csv","a",newline='') as file:
                                        writer = csv.writer(file)
                                        dc_num = '11752'+str(random.randint(111111,999999))
                                        dc_pin = str(random.randint(111,999))
                                        writer.writerow([ac_num,dc_num,dc_pin])
                                        print("\nGetting Your Card Ready. Please Wait......")
                                        time.sleep(5)
                                        clear_terminal()
                                        print("Card Generated Successfully\n\n")
                                        time.sleep(2)
                                        print(f"Card Type: Debit\nCard Number: {dc_num}\nPin: {dc_pin}\n")
                                        input("Press Enter to Continue")
                                        file.close()
                                        time.sleep(2)
                                        checking_dashboard()

                else:
                    print("\nInvalid Choice")
                    time.sleep(2)
                    checking_dashboard()
            
            elif action == '5':
                time.sleep(2)
                welcome_menu()
            elif action == '0':
                sys.exit()
            else:
                print("\nInvalid Choice")
                time.sleep(2)
                in_checking()


    with open("CSVs/checking.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            if usrnm in row:
                print(f"Welcome {row[2]}\n")
                time.sleep(2)
                ac_num = row[1]
                
    in_checking()

#########################################################################################


def savings_dashboard(): # check the csv file for name and account number to greet and display info
   
    ac_num = ""
    clear_terminal()

    def in_savings():
        while True:
            action = input("1. Money_stuff\n2. Account Info\n3. User info\n4. Log Out\n5. Exit\n >  ")
            if action == '1':
                clear_terminal()
                print("\t\t\tMoney Stuff\n\n")
                x = input("1. Send\n2. Deposit\n3. Go Back\n0. Exit > ")
                if x == '1':
                    send_money(ac_num)
                elif x == '2':
                    deposit(ac_num)
                elif  x == '3':
                    savings_dashboard()
                elif x == '0':
                    sys.exit()
                else:
                    print("Invalid Choice")

            elif action == '2':
                clear_terminal()
                print("\t\t\tAccount Information\n\n")

                with open("acc_details/acc_bal.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if ac_num in row:
                            ac_bal = row[1]

                with open("CSVs/savings.csv") as f:
                    reader = csv.reader(f)

                    for row in reader:
                        if usrnm in row:
                            print(f"Account Type: Savings\t\t\t Name    : {row[2]}")
                            print(f"Account No  : {row[1]} \t\t Balance : {ac_bal} ")
                            input("\n\nPress Enter to Continue.")
                            time.sleep(2)
                            in_savings()

            elif action == '3':
                clear_terminal()
                print("\t\t\tUser Information\n\n")

                with open("CSVs/savings.csv") as file:
                    reader = csv.reader(file)

                    for row in reader:
                      if usrnm in row:
                        print(f"Name    : {row[2]}\t\t\t Date Of Birth: {row[5]}")
                        print(f"Father  : {row[3]}\t\t Mother       : {row[4]}")
                        print(f"Contact : {row[6]}\t\t\t National ID  : {row[7]}")
                        print(f"E-mail  : {row[8]}\t Address      : {row[9]}")
                        print(f"Duration: {row[10]}")

                        input("\nPress Enter to continue")
                        time.sleep(2)

                        savings_dashboard()
            
            elif action == '4':
                welcome_menu()
            elif action == '0':
                sys.exit()
            else:
                print("\nInvalid Choice")
                time.sleep(2)
                in_savings()


    with open("CSVs/savings.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            if usrnm in row:
                print(f"Welcome {row[2]}\n")
                time.sleep(2)
                ac_num = row[1]
                
    in_savings()


###########################################################################################

def student_dashboard(): # check the csv file for name and account number to greet and display info
    clear_terminal()
    ac_num = ""

    def in_student():
        while True:
            action = input("1. Money_stuff\n2. Account Info\n3. User info\n4. Apply for a Card\n5. Log Out\n0. Exit >  ")
            if action == '1':
                clear_terminal()
                print("\t\t\tMoney_Stuff\n\n")
                x = input("1. Send\n2. Deposit\n3. Withdraw\n4. Go Back\n0. Exit\n > ")
                if x == '1':
                    send_money(ac_num)
                elif x == '2':
                    deposit(ac_num)
                elif x == '3':
                    withdrawl(ac_num)
                elif  x == '4':
                    student_dashboard()
                elif x == '0':
                    sys.exit()
                else:
                    print("Invalid Choice")

            elif action == '2':
                clear_terminal()
                print("\t\t\tAccount Information\n\n")

                cc_num = ""
                cc_exp = ""
                cc_cvv = ""
                dc_num = ""
                dc_pin = ""

                with open("acc_details/cc.csv") as c:
                    reader = csv.reader(c)
                    for row in reader:
                        if ac_num in row:
                            cc_num = row[1]
                            cc_exp = row[2]
                            cc_cvv = row[3]
                    
                with open("acc_details/dc.csv") as d:
                    reader = csv.reader(d)
                    for row in reader:
                        if ac_num in row:
                            dc_num = row[1]
                            dc_pin = row[2]

                with open("acc_details/acc_bal.csv") as f:
                    reader = csv.reader(f)
                    for row in reader:
                        if ac_num in row:
                            ac_bal = row[1]

                with open("CSVs/student.csv") as f:
                    reader = csv.reader(f)

                    for row in reader:
                        if usrnm in row:
                            print(f"Account Type: Student\t\t\t Name    : {row[2]}")
                            print(f"Account No  : {row[1]} \t\t Balance : {ac_bal} ")
                            print("\n\n Card Information\n")
                            print(f"Credit Card")
                            print("Card Number: "+ (cc_num if cc_num!="" else "N/A"))
                            print("Expiery: "+ (cc_exp if cc_exp !="" else "N/A"))
                            print("CVV: "+ (cc_cvv if cc_cvv !="" else "N/A"))
                            print("\nDebit Card")
                            print("Card Number: "+ (dc_num if dc_num!="" else "N/A"))
                            print("Pin: "+ (dc_pin if dc_pin !="" else "N/A"))
                            input("\n\nPress Enter to Continue.")
                            time.sleep(2)
                            student_dashboard()

            elif action == '3':
                clear_terminal()
                print("\t\t\t\tUser Information\n\n")
                with open("CSVs/student.csv") as file:
                    reader = csv.reader(file)

                    for row in reader:
                      if usrnm in row:
                        print(f"Name        : {row[2]}\t\t\t Date Of Birth   : {row[7]}")
                        print(f"Father      : {row[3]}\t\t\t Mother          : {row[6]}")
                        print(f"Father's ID : {row[5]}\t\t\t Father's Contact: {row[4]}")
                        print(f"Contact     : {row[8]}\t\t\t National ID     : {row[9]}")
                        print(f"E-mail      : {row[12]}\t\t Address         : {row[13]}")
                        print(f"Student ID  : {row[10]}\t\t\t Institution     : {row[11]} ")
                        time.sleep(2)

                        y = input("\n\n1.Edit Info\n2.Go Back\n > ")

                        if y == '1':
                            print("Under Development")
                            time.sleep(5)
                        else:
                            student_dashboard()

            elif action == '4':
                clear_terminal()
                print("\t\t\tGet A Card")
                z = input("Card Type:\n1. Credit\n2. Debit(Free Transaction for Students)\n > ")
                if z == '1':
                    flag = False
                    with open("acc_details/cc.csv") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if ac_num in row:
                                flag = True
                    if flag:
                        print("\nYou already have a credit card agains't your account")
                        time.sleep(5)
                        student_dashboard()
                    else:
                        with open("acc_details/cc.csv","a",newline='') as file:
                            writer = csv.writer(file)
                            cc_num = '415628'+str(random.randint(1111111,9999999))
                            cc_exp = str(random.randint(1, 28))+"/"+str(random.randint(1,12))+"/"+str(random.randint(2027, 2029))
                            cc_cvv = str(random.randint(111,999))
                            writer.writerow([ac_num,cc_num,cc_exp,cc_cvv])
                            print("\nGetting Your Card Ready. Please Wait......")
                            time.sleep(5)
                            clear_terminal()
                            print("Card Generated Successfully\n\n")
                            time.sleep(2)
                            print(f"Card Type: Credit\nCard Number: {cc_num}\nExpiery Date: {cc_exp}\nCvv: {cc_cvv}\nOverDraft: 20000\n")
                            file.close()

                        with open("acc_details/overdraft.csv","a",newline='') as f:
                            writer = csv.writer(f)
                            writer.writerow([ac_num,20000])
                            file.close()
                            time.sleep(2)
                            input("Press Enter to Continue")
                            student_dashboard()
                
                elif z == '2':
                    flag = False
                    with open("acc_details/dc.csv") as f:
                        reader = csv.reader(f)
                        for row in reader:
                            if ac_num in row:
                                flag = True
                    if flag:
                        print("\nYou already have a debit card agains't your account")
                        time.sleep(5)
                        student_dashboard()
                    else:
                        with open("acc_details/dc.csv","a",newline='') as file:
                            writer = csv.writer(file)
                            dc_num = '11750'+str(random.randint(111111,999999))
                            dc_pin = str(random.randint(111,999))
                            writer.writerow([ac_num,dc_num,dc_pin])
                            print("\nGetting Your Card Ready. Please Wait......")
                            time.sleep(5)
                            clear_terminal()
                            print("Card Generated Successfully\n\n")
                            time.sleep(2)
                            print(f"Card Type: Debit\nCard Number: {dc_num}\nPin: {dc_pin}\n")
                            input("Press Enter to Continue")
                            file.close()
                            time.sleep(2)
                            student_dashboard()

                else:
                    print("\nInvalid Choice")
                    time.sleep(2)
                    student_dashboard()

            elif action == '5':
                welcome_menu()
            elif action == '0':
                sys.exit()
            else:
                print("\nInvalid Choice")
                time.sleep(2)
                student_dashboard()


    with open("CSVs/student.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            if usrnm in row:
                print("Welcome",row[2])
                time.sleep(2)
                ac_num = row[1]
                
    in_student()


welcome_menu()