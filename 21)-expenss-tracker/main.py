#  mini project Expenses tracker--

print("🛼 --Welcome to Expenses tracker--🛼")
store_Expenses = []

while True:
    print('''
        1. Add Expense
        2. View All Expenses
        3. View Total Expense
        4. Exit

       ''')
    

    user_choise = int(input("Enter your choise :-"))
    
#  1. Add Expense
    if user_choise == 1:
        name = input("Enter name here :-")
        amount = int(input("Enter a amount here :-"))
        category = input("Enter a category here :-")
        
        store_Expenses.append([name , amount , category])
        print("Expenses added succesfully") 
        print(store_Expenses)
        
#  2. View All Expenses        
    elif user_choise == 2:
        print("view your all expenses")
        print(store_Expenses)


#  3. View Total Expense   
    elif user_choise == 3:
     total_amount = 0
     for expenses in store_Expenses:
         total_amount += expenses[1]
         print("Total Expenses :-" , total_amount)
         
         
# 4. exit 
     break