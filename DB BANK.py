#Initially create a DataBase in MySQL
#Create a table with AccNo,Name,Deposit,Withdraw
#Give a AccNo,Name, Deposit,Withdraw for Initials
#Next follow below process
#Note:  Transaction is a table name in database


import mysql.connector
import sys

#BANK DETAILS;
class Bank:
    def __init__(self):
        self.bankname="STATE BANK OF INDIA"
        connection=mysql.connector.connect(user="manu317",password="manu317@ROBOT",host="127.0.0.1",database="Bank")
       
    def deposit(self,amt):
        try:
            connection=mysql.connector.connect(user="manu317",password="manu317@ROBOT",host="127.0.0.1",database="Bank")
            x=input("Enter your ACCOUNT NUMBER as per your account :")
            query2="select * from Transactions where ID='{}'".format(x)
            c=connection.cursor()
            c.execute(query2)
            record=c.fetchall()
            #print(record[0][2])
        
            self.deposited=record[0][2]
          
            self.deposited+=amt
            query3="update Transactions set Deposit={} where ID='{}'".format(self.deposited,x)
            c.execute(query3)
            connection.commit()
            print("Your Account Balance is:",self.deposited)
        except Exception as msg:
            print("Exception:",msg)
        
    def withdraw(self,amt):
        try:
            connection=mysql.connector.connect(user="manu317",password="manu317@ROBOT",host="127.0.0.1",database="Bank")
            x=input("Enter your ACCOUNT NUMBER as per your account :")
            query2="select * from Transactions where ID='{}'".format(x)
            c=connection.cursor()
            c.execute(query2)
            record=c.fetchall()
            #print(record[0][2])
        
            self.deposited=record[0][2]
        
     
            if self.deposited>amt:
                self.deposited-=amt
                print("Collect Cash")
                print("Your Balance is:",self.deposited)
                print("Thank you")
                query3="update Transactions set  Withdraw={} where ID='{}'".format(self.deposited,x)
                query4="update Transactions set  Deposit={} where ID='{}'".format(self.deposited,x)
                c.execute(query3)
                c.execute(query4)
                connection.commit()
            else:
                print("Sorry,insufficient Balance")
                sys.exit()

        except Exception as msg:
            print("Exception:",msg)

    def BalanceEnquiry(self):
            connection=mysql.connector.connect(user="manu317",password="manu317@ROBOT",host="127.0.0.1",database="Bank")
            x=input("Enter your ACCOUNT NUMBER as per your account :")
            query2="select * from Transactions where ID='{}'".format(x)
            c=connection.cursor()
            c.execute(query2)
            record=c.fetchall()
            print("Your Balance is:",record[0][3])

class CustomerGuidance:
    def main():
        print("Press-1 for Deposit")
        print("Press-2 for WithDraw")
        print("Press-3 for BalanceEnquiry")
        x=int(input("Enter a number to Withdraw or Deposit or BalanceEnquiry"))
        if x==1:
                b=Bank()
                amt=float(input("Enter amount to Deposit"))
                b.deposit(amt)

        elif x==2:
            b=Bank()
            amt=float(input("Enter amount to WithDraw"))
            b.withdraw(amt)

        elif x==3:
            b=Bank()
            b.BalanceEnquiry()
            
b=Bank()
print("Welcome to",b.bankname)
CustomerGuidance.main()           

