todo_list=[]
def load_tasks():
    try:
        with open(r"C:\Users\BrighTec Com\Documents\tasks.txt","r") as file:
            for line in file:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass

def save_tasks():
    with open(r"C:\Users\BrighTec Com\Documents\tasks.txt","w") as file:
        for task in todo_list:
            file.write(task + "\n")

def add_task():
    task=input("What is the new work:")
    todo_list.append(task)
    save_tasks()
    print("Added and Saved!")
def view_tasks():
    if not todo_list:
        print("There arenot works,stay free!")
        return
    print("\n----Your works ----")
    for i, task in enumerate(todo_list,1):
        print(f"{i}.{task}")

def delete_task():
    view_tasks()
    try:
        num=int(input("The number which you want remove"))
        todo_list.pop(num-1)
        save_tasks()
        print("Deleted!")
    except:
      print ("Number is wrong")
load_tasks()
while(True):
    print("\n1.Add | 2.View |3.Delete |4.Exit")
    choice=input('What is your choice:')
    if choice =="1":
        add_task()
    elif choice=="2":
       view_tasks()
    elif choice=="3":
       delete_task()
    elif choice =="4":
        print("Your number is wrong")
        break
       
      
       
    else:
       print("enter a number (1-4)")
    
    
    



