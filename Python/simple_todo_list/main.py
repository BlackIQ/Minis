tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    choice = input("Enter choice: ")
    
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
        
    elif choice == '2':
        if not tasks:
            print("No tasks!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(str(i) + ". " + task)
                
    elif choice == '3':
        print("Goodbye!")
        break
        
    else:
        print("Error: Invalid choice!")