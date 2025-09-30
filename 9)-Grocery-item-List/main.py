#  Grocery item list --

def Grocery ():
    item_list = []  #add all item in this list --
    
    print('My-Grocery-item-list')
    
    much_item = int(input('Enter how many items you add :-'))
    for i in range(1 , much_item + 1):
        item_name = input(f'Enter a item :-{i}') 
        item_list.append(item_name)
        print(f"you'r  item list{item_list}")
    
    while True:
        task_opreation = int(input("1-add \n 2-delet \n 3-view \n 4-exit \n Enter a :-"))
        
        # item add--
        if task_opreation == 1:
            add_item = input("Add item :-")
            item_list.append(add_item)
            print(item_list)
            
        # item delet --
        elif task_opreation == 2:
            del_item = input('Which item you want delet :-')
            if  del_item in item_list :
                remo_item = item_list.index(del_item)
                del item_list[remo_item]
                print(f'task was delet {item_list}')
                print(item_list)
                
                
        # show  my list
        elif task_opreation == 3:
            print(f"my Total item is :-{item_list}")
            
        elif task_opreation == 4:
            print(" you exit from you list :--")
            break
        
        else:
            print("worng pattern :-")
Grocery()