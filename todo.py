def task():
    tasks = [] #empty list
    print("----Welcome to the task management app----")
    

    total_task =int(input("Enter how many task you want to add ="))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} =")
        tasks.append(task_name)

    print(f"Today's tasks are\n{tasks}")

    while True:
        operation = int (input("\Enter\n1:Add=\n2:Update\n3:Delete\n4:Mark\n5:Stop/"))
        if operation ==1:
            add =input("Enter task you want to add =")
            tasks.append(add)
            print(f"Task {add} has been added...")
            print(f"Today's tasks are\n{tasks}")

        elif operation == 2:
            updated_val =input("Enter the task that you update =")
            if updated_val in tasks:
                up = input("Enter new task =")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task{up}")
                print(f"Today's tasks are\n{tasks}")
                
           
        elif operation == 3:
            del_val = input("Which task that you want to delete =")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks [ind]
                print(f"Task {del_val} has been deleted")
                print(f"Today's tasks are\n{tasks}")
            else:
                print("Task not found!")
                
        elif operation == 4:
            marks_val = input("Which task do you want to mark as done =")
            if marks_val in tasks:
                ind = tasks.index(marks_val)
                tasks[ind] =tasks[ind] +"Done"
                print(f"Task {marks_val} has been marked as done") 
                print(f"Today's tasks are\n{tasks}")
            else:
                print("Task not found!")    

        elif operation == 5:
            print("Closing the program...")
            break
        else:
            print("Invaild option! Please try again.")  

task() 