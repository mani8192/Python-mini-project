# Task managment app in python --

def task ():
    tasks = [] # empty list
    
    print("--welcome to you'r  daily tasks app-- ")
    
    total_task = int(input("How many task you want :-"))
    for i in range(1 , total_task + 1):
        task_name = input(f'Enter task {i} :-')
        tasks.append(task_name)
    print(f'Today task is {tasks} :-')
    
    while True:
        opreation = int(input("1-Add \n 2-update \n 3-delet \n 4-view \n 5 - exit/stop \n Enter a :- "))
        
        if opreation == 1:
            add_task = input("Enter a task :-")
            tasks.append(add_task)
            print(f"task {add_task} has been succesfully added..")           
            
        elif opreation == 2:
            update_task = input("Enter a task you want to update :-") 
            if update_task in tasks:
                up_value = input('Update with new value :-')
                ind  = tasks.index(update_task)
                tasks[ind] = up_value
                print(f"Task update {up_value}")
                
        elif opreation == 3:
            del_value = input("which task you want to deleted :-")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task deleted :-{del_value}")
            print(tasks)
            
        elif opreation == 4:
            print(f"You daily task list is :- {tasks}")
            
        elif opreation == 5:
            print('you out from page :-')
            print('Thanku ')
            break
        
        else:
            print('worng number :-')
task()

