#function for different task
def add_task(tasks):
    task=input("Enter the task you want to add:  ")
    tasks.append(task)
    print("Task added  successfully")

def update_task(tasks):
    view_tasks(tasks)
    task_index=int(input("Enter the task number you want to update:  "))-1
    if 0<=task_index < len(tasks):
        new_task=input("Enter the new task:  ")
        tasks[task_index]=new_task
        print("Task updated to",new_task)
    else:
        print("Invalid task number")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        print("Your tasks:\n")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}.{task}")


def delete_task(tasks):
    view_tasks(tasks)
    task_index=int(input("Enter the task number you want to delete:  "))-1
    if 0<=task_index < len(tasks):
        removed_task=tasks.pop(task_index)
        print(f"Task'{removed_task}' deleted successfully")
    else:
        print("Invalid task number")


tasks=[]
reagain=True
while True:
    print("\n================================TO DO LIST================================")
    print("To-Do list Menu:")
    print("1-Add a task")
    print("2-Update a task")
    print("3-View Tasks")
    print("4-Delete a task")
    print("5-Exit")
    choice=int(input("Choose an Option which you want...(1-5):"))
    if choice==1:
        add_task(tasks)
    elif choice==2:
        update_task(tasks)
    elif choice==3:
        view_tasks(tasks)
    elif choice==4:
        delete_task(tasks)
    elif choice==5:
        print("Exiting the To-Do List Program...")
        print("\nThanks for interacting with me😍😍===================\n VISIT AGAIN")
        break
    else:
        print("----------Invalid Choice------------\nPLEASE TRY AGAIN------------")
        