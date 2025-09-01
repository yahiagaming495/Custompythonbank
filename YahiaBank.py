import os
import time
import requests
print("Welcome to CustomBank")
found = False
current_name = ""
current_id = ""
current_reg = ""
money = 0
Name = input("What is your bank name?: ")
ID = input("What is your id?: ")
Reg = input("What is your Registration key:? ")
filename = f"CustomBank_{Name}_{ID}_{Reg}.txt"
if not os.path.exists("accounts.txt"):
    os.system("touch accounts.txt") ## I did it using the "os" library because i like to do it that way    
                
with open("accounts.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Name: "):
            current_name = line[6:].strip()
    
        elif line.startswith("ID: "):
            current_id = line[4:].strip()
    
        elif line.startswith("Registration key: "):
            current_reg = line[17:].strip()
    
        if Name == current_name and ID == current_id and Reg == current_reg:
           ## requests.post("https://ntfy.sh/bankntfy",
             ##   data=f"{current_name} with id {current_id} signed in".encode(encoding='utf-8'))
            found = True
            break
            

if not found:
    print("Account not found")
    exit()

if found:
    if not os.path.exists(filename):
        with open(filename, "w") as u:
            u.write("Name: " + Name + "\n")
            u.write("ID: " + ID + "\n")
            u.write("REG: " + Reg + "\n")
            u.write(f"Balance: {money}\n")
            u.write("\n")
            u.close()
    print("Account found")
    with open(filename) as f:
        for line in f:
            if line.startswith("Balance: "):
                money = int(line[9:].strip())

    while True:
        print("[1] Deposit")
        print("[2] Delete money")
        print("[3] Show money")
        print("[4] Transfer money")
        print("[5] Exit")
        options = input("What Option do you want to select?: ")


        if options == "1":
            deposit = int(input("How much do you want to deposit?: "))
            money += deposit
            os.system("clear")
            with open(filename, "w") as g:
                g.write("Name: " + current_name + "\n")
                g.write("ID: " + current_id + "\n")
                g.write("REG: " + current_reg + "\n")
                g.write(f"Balance: {money}\n")
                g.write("\n")
                g.close()
                print(f"Your new balance is {money}")
                ## requests.post("https://ntfy.sh/bankntfy",
                                       ## data=f"{current_name} deposited {deposit}$ his money is {money}$ with id {current_id}".encode(encoding='utf-8'))                   
                    

        elif options == "2": ##-
            withdraw = int(input("How much do you want to withdraw?: "))
            if money < withdraw:
                print("Insufficant funds")


            else:
                money -= withdraw
                ## requests.post("https://ntfy.sh/bankntfy",
                   ## data=f"{current_name} withdrawed {withdraw} his Money is now {money}$ with id {current_id}".encode(encoding='utf-8'))
                    
                print(f"Your new balance is {money}$")
                with open(filename, "w") as g:
                    g.write("Name: " + current_name + "\n")
                    g.write("ID: " + current_id + "\n")
                    g.write("REG: " + current_reg + "\n")
                    g.write(f"Balance: {money}\n")
                    g.write("\n")
                    g.close()
                    print(f"Your new balance is {money}$")
                

        elif options == "3":
            print(f"Your money is {money}")
            time.sleep(3.5) 
            os.system("clear")

        elif options == "4":
            tuser = input("What is the name of the person?: ")
            treg = input("What is the REG of that person: ")
            tid = input("What is the id of the person?: ")
            tamount = int(input("How much do you want to transfer?: "))
            tfilename = f"CustomBank_{tuser}_{tid}_{treg}.txt"
            if not os.path.exists(tfilename):
                print("Reciver's account not found")

            elif tamount > money:
                print("Insufficant funds")


            else:
                with open("accounts.txt") as f:
                        for line in f:
                                line = line.strip()
                                if line.startswith("Name: "):
                                        tcurrent_name = line[6:].strip()
                
                                                
                                elif line.startswith("ID: "):
                                        tcurrent_id = line[4:].strip()
                
                                                
                                elif line.startswith("Registration key: "):
                                        tcurrent_reg = line[17:].strip()
                money -= tamount
                with open(filename, "w") as h: ## Writing user's data
                            h.write("Name: " + current_name + "\n")
                            h.write("ID: " + current_id + "\n")
                            h.write("REG: " + current_reg + "\n")
                            h.write(f"Balance: {money}\n")
                            h.write("\n")
                                        
                with open(tfilename) as tf: ## Writing reciver's data
                            for line in tf:
                                if line.startswith("Balance: "):
                                        t_money = int(line[9:].strip())
                                        t_money += tamount
                with open(tfilename, "w") as h:
                            h.write("Name: " + tcurrent_name + "\n")
                            h.write("ID: " + tcurrent_id + "\n")
                            h.write("REG: " + tcurrent_reg + "\n")
                            h.write(f"Balance: {t_money}\n")
                            h.write("\n")
                print(f"Succesfly send {tamount} to {tuser} your new balance is {money}")
                                        
                                            
                                                  
        elif options == "5":
            exit()

