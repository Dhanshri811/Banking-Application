#!/usr/bin/env python
# coding: utf-8

# # Login Details

# In[ ]:


def OpenAcc():
    n= input('Enter the name: ')
    ac= input('Enter account number: ')
    add= input('Enter the address: ')
    cn= input('Enter the contact number: ')
    ob= int(input('Enter opening balance: '))
    data1 = (n, ac, add, cn, ob)
    data2= (n,ac,ob)
    
    sql1=('Insert into ACCOUNT values (%s, %s, %s, %s, %s)')
    sql2= ('Insert into AMOUNT values(%s,%s,%s)')
   
    mycursor = mydb.cursor()
    mycursor.execute(sql1,data1)
    mycursor.execute(sql2,data2)
    mydb.commit()
    print('Data Entered successfully')
    main()
    
    
def Deposit_amount():
    amount= int(input('Enter the amount you want to deposit: '))
    ac= input('Enter the account number: ')
    a= 'select Balance from AMOUNT where AccNo= %s'
    data= (ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result=mycursor.fetchone()
    t=result[0]+amount
    sql=('update AMOUNT set Balance =%s where AccNo =%s')
    d=(t, ac)
    mycursor.execute(sql,d)
    mydb.commit()
    main()
    
    
def WithDraw_amount():
    amount= int(input('Enter the amount you want to withdraw: '))
    ac= input('Enter the account number: ')
    a= 'select Balance from AMOUNT where AccNo= %s'
    data= (ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result=mycursor.fetchone()
    t=result[0]- amount
    sql=('update AMOUNT set Balance=%s where AccNo =%s')
    d=(t, ac)
    mycursor.execute(sql,d)
    mydb.commit()
    main()
    
    
    
def Add_beneficiary():
    Benef= input('Enter the beneficiary name: ')
    ac= input('Enter the account number: ')
    a= 'select balance from AMOUNT where AccNo= %s'
    data= (ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    mydb.commit()
    main()
    
def Details():
    ac=input('Enter the account number: ')
    a='select * from AMOUNT where AccNo=%s'
    data=(ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result= mycursor.fetchone()
    for i in result:
        print(i)
    
    main()
    
    
def main():
    print('''
    1.Open New Account
    2.Deposit Amount
    3.Withdraw Amount
    4.Display Details
    ''')
    choice= input('Enter the task you want to perform: ')
    if (choice== '1'):
        OpenAcc()
    elif(choice == '2'):
        Deposit_amount()
    elif(choice=='3'):
        WithDraw_amount()
    elif(choice=='4'):
        Details()
    else:
        print('Invalid Choice')
        main()
main()


# # Add Beneficiary

# In[ ]:


def AddBenef():
    
    ac= input('Enter account number: ')
    add= input('Enter the Beneficiary name: ')
    tf = int(input('Enter transfer amount: '))
    data1 = (ac, add, tf)
   
    
    sql1=('Insert into Beneficiaries values (%s, %s, %s)')
    
    mycursor = mydb.cursor()
    mycursor.execute(sql1,data1)
    mydb.commit()
    print('Data Entered successfully')
    main()



def Details():
    ac=input('Enter the account number: ')
    a='select * from Beneficiaries where AccNo=%s'
    data=(ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result= mycursor.fetchone()
    for i in result:
        print(i)
    main()


def main():
    print('''
    1.Add Beneficary
    
    2.Display Details
    ''')
    choice= input('Enter the task you want to perform: ')
    if (choice== '1'):
        AddBenef()
    elif(choice=='2'):
        Details()
    else:
        print('Invalid Choice')
        main()
main()


# In[ ]:





# # Registration of Cards- Credit Card

# In[ ]:


def AddCard():
    
    ac= input('Enter account number: ')
    cn= input('Enter the Card number(8 digit): ')
    pin = input('Enter Pin: ')
    cvv = int(input('Enter Cvv: '))
    data1 = (ac, cn, pin,cvv)
   
    
    sql1=('Insert into Credit_Cards values (%s, %s, %s, %s)')
    
    mycursor = mydb.cursor()
    mycursor.execute(sql1,data1)
    mydb.commit()
    print('Data Entered successfully')
    main()  
    

def Details():
    ac=input('Enter the account number: ')
    a='select * from Credit_Cards where AccNo=%s'
    data=(ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result= mycursor.fetchone()
    for i in result:
        print(i)
    main()


def main():
    print('''
    1.Add Credit Card
    
    2.Display Details
    ''')
    choice= input('Enter the task you want to perform: ')
    if (choice== '1'):
        AddCard()
    elif(choice=='2'):
        Details()
    else:
        print('Invalid Choice')
        main()
main()


# # Debit Card

# In[ ]:


def AddCard():
    
    ac= input('Enter account number: ')
    cn= input('Enter the Card number(8 digit): ')
    pin = input('Enter Pin: ')
    cvv = int(input('Enter Cvv: '))
    
    data1 = (ac, cn, pin,cvv)
   
    
    sql1=('Insert into Debit_Cards values (%s, %s, %s, %s)')
    
    mycursor = mydb.cursor()
    mycursor.execute(sql1,data1)
    mydb.commit()
    print('Data Entered successfully')
    main()



def Details():
    ac=input('Enter the account number: ')
    a='select * from Debit_Cards where AccNo=%s'
    data=(ac, )
    mycursor =mydb.cursor()
    mycursor.execute(a,data)
    result= mycursor.fetchone()
    for i in result:
        print(i)
        main()



def main():
    print('''
    1.Add Debit Card
    
    2.Display Details
    ''')
    choice= input('Enter the task you want to perform: ')
    if (choice== '1'):
        AddCard()
    elif(choice=='2'):
        Details()
    else:
        print('Invalid Choice')
        main()
main()


# In[ ]:





# In[ ]:




