import time
import os
import random
import sys
import csv
import string
words = string.ascii_letters


#########################################################################


def clear_terminal(): # to clear the terminal
    """Clears the terminal screen."""

    if os.name == "nt": #for Windows
        os.system("cls")
    else:
        os.system("clear") # for Linux and Mac os


#############################################################################

def showBanner():
    banner = '''
                    _______ __  __ 
                 /\|__   __|  \/  |
                /  \  | |  | \  / |
               / /\ \ | |  | |\/| |
              / ____ \| |  | |  | |
             /_/    \_\_|  |_|  |_|
    \n\n'''
    print(banner)



###############################################################################

def main_screen():
    clear_terminal()
    print("\t\t\tBank of Bitches ATM\n\n")
    showBanner()
    card_num = input("Enter card Number: ")
    time.sleep(2)
    if card_num.startswith("11"): # Treat as checking account Debit Card
        debit(card_num)
    elif card_num.startswith("36"):
        pass
        

#################################################################################

def check_balance(acc_num):
    clear_terminal()
    showBanner()
    acc_bal = 0
    with open("acc_details/acc_bal.csv")as file:
        reader = csv.reader(file)
        for row in reader:
            if acc_num in row:
                acc_bal = row[1]
    print(f"Your Account Blance is : {acc_bal}\n")
    input("Press Enter to Continue")
    return

####################################################################################

def deposit(acc_num,card_num):
    clear_terminal()
    showBanner()
    print("\t\t\tDeposit\n\n")
    input_filename = "acc_details/acc_bal.csv"

    amount = input("Enter Deposit Amount: ")

    acc_bal = 0
    new_bal = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if acc_num in row:
                acc_bal = int(row[1])
                new_bal = str(acc_bal+ int(amount))
                row[1] = new_bal

            rows.append(row)

        # write updated rows to temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    k = ""
    for i in random.choices(words,k=3):
        k+=i
    tnx_id = k+str(random.randint(100,999))


    if card_num.startswith("11"):
        with open("atm/debit_tnx.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,tnx_id,card_num,"Deposit",amount,acc_bal,new_bal])
            file.close()

    elif card_num.startswith("41"):
        with open("atm/debit_tnx.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,tnx_id,card_num,"Deposit",amount,acc_bal,new_bal])
            file.close()

    print(f"\nDeposit Successful.")
    clear_terminal()
    showBanner()
    print("\n\n\t\tTransaction Details")
    print(f"\n\nAccount Number: {acc_num}\nCard Number: {card_num}\nDeposit Amount: {amount}\nPrevious Balance: {acc_bal}\nNew Balance : {new_bal}\nTransaction ID: {tnx_id}\n")


    # replace original file with temporary file
    os.replace(temp_filename,input_filename)


    input("Press Enter To Continue")
    time.sleep(2)
    clear_terminal()
    return

################################################################################################


def debit_withdrawal(acc_num,card_num):
    clear_terminal()
    showBanner()
    print("\t\t\t Withdrawal")
    input_filename = "acc_details/acc_bal.csv"

    amount = input("Enter Withdrawal Amount: ")

    acc_bal = 0
    new_bal = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if acc_num in row:
                acc_bal = int(row[1])
                new_bal = str(acc_bal - (int(amount)+12))
                row[1] = new_bal
            rows.append(row)

        # write update ingo to the temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename,"w",newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
            file.close()

    k = ""
    for i in random.choices(words,k=3):
        k+=i
    tnx_id = k+str(random.randint(100,999))


    if card_num.startswith("11"):
        with open("atm/debit_tnx.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,tnx_id,card_num,"Withdraw",amount,acc_bal,new_bal])
            file.close()


    # replace original file with temporary file
    os.replace(temp_filename,input_filename)

    print(f"\nWithdrawal Successful.")
    clear_terminal()
    showBanner()
    print("\n\n\t\tTransaction Details")
    print(f"\n\nType: Withdrawal\nAccount Number: {acc_num}\nCard Number: {card_num}\nWithdrawal Amount: {amount}\nCharges: {12}\nPrevious Balance: {acc_bal}\nNew Balance : {new_bal}\nTransaction ID: {tnx_id}\n")
    input("Press Enter To Continue")
    time.sleep(2)
    clear_terminal()
    return



#################################################################################################


def debit_withdrawal_student(acc_num,card_num):
    clear_terminal()
    showBanner()
    print("\t\t\tWithdrawl\n\n")
    input_filename = "acc_details/acc_bal.csv"

    amount = input("Enter Withdrawl Amount: ")

    acc_bal = 0
    new_bal = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        rows = []

        for row in reader:
            if acc_num in row:
                acc_bal = int(row[1])
                new_bal = str(acc_bal - int(amount))
                row[1] = new_bal

            rows.append(row)

        # write updated rows to temporary file
        temp_filename = "acc_details/acc_bal_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    
    k = ""
    for i in random.choices(words,k=3):
        k+=i
    tnx_id = k+str(random.randint(100,999))


    if card_num.startswith("11"):
        with open("atm/debit_tnx.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([acc_num,tnx_id,card_num,"Withdraw",amount,acc_bal,new_bal])
            file.close()

    # replace original file with temporary file
    os.replace(temp_filename,input_filename)

    print(f"\nWithdrawal Successful.")
    clear_terminal()
    showBanner()
    print("\n\n\t\tTransaction Details")
    print(f"\n\nType: Withdrawal\nAccount Number: {acc_num}\nCard Number: {card_num}\nWithdrawal Amount: {amount}\nPrevious Balance: {acc_bal}\nNew Balance : {new_bal}\nTransaction ID: {tnx_id}\n")
    input("Press Enter To Continue")
    time.sleep(2)
    clear_terminal()
    return



def credit_withdrawal(acc_num,card_num):
    clear_terminal()
    showBanner()
    print("\t\t\t Withdrawal")
    input_filename = "acc_details/overdraft.csv"

    amount = input("Enter Withdrawal Amount: ")

    final_overdraft = 0
    overdraft = 0

    with open(input_filename,"r") as file:
        reader = csv.reader(file)
        for row in reader:
            if acc_num in row:
                overdraft = int(row[1])
        file.close()

    if int(amount)+12 > overdraft:
        print("Limit Exceeded")
        time.sleep(2)
        return
    else:
        final_overdraft = str(overdraft - (int(amount) + 12))
        with open(input_filename,"r") as file:
            reader = csv.reader(file)
            rows = []
            for row in reader:
                if acc_num in row:
                    row[1] = final_overdraft
                rows.append(row)
        
        # write updated rows to temporary file
        temp_filename = "acc_details/overdraft_temp.csv"

        with open(temp_filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    

        k = ""
        for i in random.choices(words,k=3):
            k+=i
        tnx_id = k+str(random.randint(100,999))


        if card_num.startswith("41"):
            with open("atm/credit_tnx.csv","a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([acc_num,tnx_id,card_num,"Withdraw",amount,overdraft,final_overdraft])
                file.close()

        # replace original file with temporary file
        os.replace(temp_filename,input_filename)

        print(f"\nWithdrawal Successful.")
        clear_terminal()
        showBanner()
        
        print("\n\n\t\tTransaction Details")
        print(f"\n\nType: Withdrawal\nAccount Number: {acc_num}\nCard Number: {card_num}\nWithdrawal Amount: {amount}\nPrevious Overdraft: {overdraft}\nAvailable Overdraft : {final_overdraft}\nTransaction ID: {tnx_id}\n")
        input("Press Enter To Continue")
        time.sleep(2)
        clear_terminal()
        return




def debit(card_number):
    flag = False

    card_pin = ""
    ac_num = ""

    with open("acc_details/dc.csv") as file:
        reader = csv.reader(file)

        for row in reader:
            if card_number in row:
                flag = True # Card Found
                card_pin = row[2] # Fetch the card Pin
                ac_num = row[0] # Fetch the Account Number

    if not flag:
        clear_terminal()
        showBanner()
        print("Invalid Card Number")
        time.sleep(2)
        return
    else:
        counter = 0
        max_try = 3
        while counter < max_try: 
            pin = input(f"\n{max_try-counter} tries left\nEnter Pin: ")
            if pin!=card_pin:
                print("\nInvalid Pin")
                counter+=1
                time.sleep(1)
                if counter == 3:
                    return

            else:
                clear_terminal()
                showBanner()
                print("Pin Verified. Redirecting...")
                time.sleep(2)
                def in_ch_d():
                    clear_terminal()
                    showBanner()
                    action = input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n > ")
                    if action == "1":
                        deposit(ac_num,card_number)
                        in_ch_d()
                    elif action == "2":
                        if card_number.startswith("11750"):
                            debit_withdrawal_student(ac_num, card_number)
                            in_ch_d()
                        else:
                            debit_withdrawal(ac_num,card_number)
                            in_ch_d()
                    elif action == '3':
                        clear_terminal()
                        showBanner()
                        print("Checking Account Balance... Please Wait........")
                        time.sleep(3)
                        check_balance(ac_num)
                        in_ch_d()
                    elif action == '4':
                        clear_terminal()
                        showBanner()
                        print("Thank you for using the ATM Service......")
                        time.sleep(2)
                        sys.exit()
                    else:
                        print("\nInvalid Choice")
                        time.sleep(2)
                        in_ch_d()
                in_ch_d()

                                 
main_screen()



