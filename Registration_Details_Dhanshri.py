#!/usr/bin/env python
# coding: utf-8

# In[28]:


import mysql.connector


# In[30]:


mydb=mysql.connector.connect(host= 'localhost', user='root', password = 'nineleaps',database='python_connector')


# In[29]:


mycursor =mydb.cursor()


# In[ ]:





# In[ ]:





# In[4]:


import re


    
def registration_details():
        """This method takes all the user information as input 
        and stores in the table Registration_details"""

        

        user_id=int(input("\nEnter user_id:"))
        password =check_password()
        data1= (user_id,password )
        sql1=('Insert into Registration values (%s, %s)')
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute(sql1,data1)
        mydb.commit()
        print('Data Entered successfully')
        main()


# In[3]:


def check_password():
    password=input("Enter password : ")
    r=re.compile("^(?=.*[a-z])(?=." +
     "*[A-Z])(?=.*\\d)" +
     "(?=.*[-+_!@#$%^&*., ?]).+$")

    if re.search(r,password) and len(password)>=7:
        b=True
    else:
        b=False
    while not b:
        print("Password must contain 1  letter in upper case, 1 letter in lower case, a number and a special character. Please enter again!")
        password=input("Enter password : ")
        if re.search(r,password) and len(password)>=7:
            b=True
    return password     
    


# In[12]:


def cursor_connection(command,data):
    mycursor =mydb.cursor(buffered=True)
    mycursor.execute(a,data)
    


# In[17]:


def Details():
    ui=input('Enter the user_id: ')
    a='select * from Registration where User_id=%s'
    data=(ui, )
    mycursor =mydb.cursor(buffered=True)
    mycursor.execute(a,data)
    result= mycursor.fetchall()
    print(result)
  

#     for i in re1sult:
#         print(i)
#         main()


# In[ ]:


def main():
    print('''
    1.New User registration
    2.Display Details
   
    ''')
    choice= input('Enter the task you want to perform: ')
    if (choice== '1'):
        registration_details()

    elif(choice=='2'):
        Details()
    else:
        print('Invalid Choice')
        main()
main()


# In[ ]:





# In[ ]:




