from os import*
from colorama import*
from pwinput import*
import pymysql
from tqdm import*
import time

 #login page coding

while True:
    system("color 8f")
    system("cls")
    print("\n"*5)
    user=input(Fore.WHITE+Style.BRIGHT+" "*80+"enter the username:")
    print()
    pas=pwinput(prompt=" "*80+"enter the password:",mask="*")
    con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp")
    cur=con.cursor()
    q="SELECT * FROM emps WHERE username=%s and password=%s"
    val=(user,pas)
    cur.execute(q,val)
    row=cur.fetchone()
    print()
    if row==None:
        print(Fore.RED+" "*80+"invalid username or password")
        choice=input(Fore.WHITE+" "*80+"try again y/n?")
        if choice in "Yy":
            continue
        else:
            sys.exit()
    else:
        break

#splash  screen coding

system("cls")
print("\n"*5)
print(Fore.WHITE+" "*80+"E M P L O Y E E  M A N A G E M E N T")
print()
print(Fore.WHITE+" "*90+"S Y S T E M")
print("\n"*5)
print(Fore.GREEN+" "*90+"Version 1.0")
print()
print(Fore.WHITE+" "*80+"Developed By:Ansh Choudahry")
print("\n"*5)
print(Fore.GREEN)
for i in tqdm(range(10),desc="please wait"):
    time.sleep(0.1)
print(Fore.WHITE)
system("pause")

# add employee page coding

def add_employee():
    system("cls")
    print("Add employee record")
    print("------------------------")
    empid=int(input("enter the employee id:"))
    name=input("enter the employee name:")
    email=input("enter the employee email:")
    phone=int(input("enter the employee phone number:"))
    address=input("enter the address:")
    post=input("enter the post:")
    salary=int(input("enter the salary:"))
    con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
    cur=con.cursor()
    q="insert into employee values(%s,%s,%s,%s,%s,%s,%s)"
    val=(empid,name,email,phone,address,post,salary)
    cur.execute(q,val)
    print("Data save successfully")
    system("pause")
    main_menu()

#delete employee page coding
def delete_employee():
   system("cls")
   print("Delete Employee Record")
   print("-------------------------")
   empid=int(input(Fore.WHITE+"enter employee id:"))
   print()
   print(Fore.WHITE+"Employee Record")
   print("------------------------------")
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM employee WHERE id=%s"
   val=(empid,)
   cur.execute(q,val)
   row=cur.fetchone()
   if row==None:
      print(Fore.RED+"Not found")
   else:
      print("employee id:",row[0])
      print("Name:",row[1])
      print("email:",row[2])
      print("phone:",row[3])
      print("address:",row[4])
      print("post:",row[5])
      print("salary:",row[6])
      print("------------------")
      choice=input("Do you want to delete y/n?")
      if choice in "yY":
         q="DELETE FROM employee WHERE id=%s"
         cur.execute(q,val)
         print()

      print(Fore.WHITE+"successfully deleted")
      system('pause')
      main_menu() 

# search page coding
def search_employee():
   system("cls")
   print(Fore.WHITE+"Serach Employee")
   print("-----------------------------")
   empid=int(input("enter the employee id:"))
   print()
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM employee WHERE id=%s"
   val=(empid,)
   cur.execute(q,val)
   row=cur.fetchone()
   if row==None:
      print(Fore.RED+"Not found")
   else:
      print(Fore.WHITE+"Employee Record")
      print("-----------------------------")
      print("Employee id:",row[0])
      print("Employee Name:",row[1])
      print("Employee email:",row[2])
      print("Employee phone:",row[3])
      print("Employee address:",row[4])
      print("Employee post:",row[5])
      print("Employee salary:",row[6])
      system('pause')
      main_menu()

#Edit employee page coding
def edit_employee():
   system("cls")
   print(Fore.WHITE+"Edit Employee Record")
   print("-----------------------------------")
   empid=int(input("enter the employee id:"))
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM employee WHERE id=%s"
   val=(empid,)
   cur.execute(q,val)
   row=cur.fetchone()
   if row==None:
      print()
      print(Fore.RED+"Not Found")
   else:
      print()
      print(Fore.WHITE+"Employee Record")
      print("-----------------------------")
      print("Employee id:",row[0])
      print("Employee Name:",row[1])
      print("Employee email:",row[2])
      print("Employee phone:",row[3])
      print("Employee address:",row[4])
      print("Employee post:",row[5])
      print("Employee salary:",row[6])
      print("---------------------------")
      choice=input("Do you want to edit Y/N?:")
      print()
      if choice in "Yy":
         name=input("enter name:")
         email=input("enter email:")
         phone=int(input("enter phone no.:"))
         address=input("enter address:")
         post=input("enter post:")
         salary=int(input("enter salary:"))
         con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
         cur=con.cursor()
         q="UPDATE employee SET name=%s,email=%s,phone=%s,address=%s,post=%s,salary=%s WHERE id=%s"
         val=(name,email,phone,address,post,salary,empid)
         cur.execute(q,val)
         print()
         print("Successfully Updated")
         system('pause')
         main_menu()


# list of employee page coding
def list_of_employee():
   system("cls")
   print()
   print(" "*85+"List Of Employee")
   print()
   print("="*210)
   print("%25s %25s %25s %25s %25s %25s %25s"%("ID","NAME","EMAIL","PHONE","ADDRESS","POST","SALARY"))
   print("="*210)
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM employee"
   cur.execute(q)
   rows=cur.fetchall()
   for row in rows:
      print("%25s %25s %25s %25s %25s %25s %25s"%(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
   system('pause')
   main_menu()


#promote employee page coding
def promote_employee():
   system("cls")
   print(Fore.WHITE+"PROMOTE EMOLOYEE")
   print("--------------------------------")
   empid=int(input("enter the employee id:"))
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM employee WHERE id=%s"
   val=(empid,)
   cur.execute(q,val)
   row=cur.fetchone()
   print()
   print("salary=",row[6])
   newsalary=int(input(Fore.WHITE+"enter the new salary:"))
   if newsalary==row[6]:
      print(Fore.RED+"New salary is equal to the current salary")
   elif newsalary<row[6]:
      print(Fore.RED+"New salary less than the current salary")
   elif newsalary>row[6]:
      q="UPDATE employee SET salary=%s WHERE id=%s"
      val=(newsalary,empid)
      cur.execute(q,val)
      print()
      print("promoted successfully")
      system('pause')
      main_menu()


# change password coding
def change_password():
   system("cls")
   print(Fore.WHITE+" "*75+"CHANGE PASSWORD")
   print("="*210)
   print("\n"*5)
   currpass=input("enter current password:")
   print()
   con=pymysql.connect(host="localhost",user="root",password="ansh123",db="emp",autocommit=True)
   cur=con.cursor()
   q="SELECT * FROM emps WHERE password=%s"
   val=(currpass,)
   cur.execute(q,val)
   row=cur.fetchone()
   if row==None:
      print()
      print(Fore.RED+" "*75+"Incorrect password")
      choice=input(Fore.WHITE+" "*75+"try again y/n?")
      if choice in "Yy":
         change_password()
      else:
         newpass=input(Fore.WHITE+" "*75+"enter new password:")
         conpass=input(Fore.WHITE+" "*75+"enter confirm password:")
         if newpass!=conpass:
            print(Fore.RED+" "*75+"Password Mismatched")
            choice=input(Fore.WHITE+" "*75+"try again y/n?")
            if choice in "Yy":
              change_password()
            else:
               q="UPDATE emps SET password=%s"
               val=(newpass,)
               cur.execute(q,val)
               print(Fore.WHITE+" "*75+"successfully updated")
            system('pause')
            main_menu()


#main page coding
def main_menu():
  print("\n")
  system("cls")
  print("\n"*5)
  print(Fore.GREEN+" "*80+"MAIN MENU")
  print(" "*70+"-"*40)
  print()
  print(Fore.WHITE+" "*80+"1 Add Employee Details")
  print()
  print(Fore.WHITE+" "*80+"2 Delete Employee Details")
  print()
  print(Fore.WHITE+" "*80+"3 Search Employee Details")
  print()
  print(Fore.WHITE+" "*80+"4 Edit Employee Details")
  print()
  print(Fore.WHITE+" "*80+"5 List of Employee Details")
  print()
  print(Fore.WHITE+" "*80+"6 Promote Employee")
  print()
  print(Fore.WHITE+" "*80+"7 Change Password")
  print()
  print(Fore.WHITE+" "*80+"8 Exit")
  print(" "*70+"-"*40)
  choice=int(input(" "*80+"enter your choice?:"))

  if choice==1:
     add_employee()
  elif choice==2:
     delete_employee()
  elif choice==3:
     search_employee()
  elif choice==4:
     edit_employee()
  elif choice==5:
    list_of_employee()
  elif choice==6:
   promote_employee()
  elif choice==7:
    change_password()
   
main_menu()
