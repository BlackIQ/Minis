import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    """Load tasks from file"""
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

tasks = load_tasks()

while True:
    print("\n" + "=" * 40)
    print("    To-Do List")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Done")
    print("4. Delete Task")
    print("5. Exit")
    print("=" * 40)
    
    choice = input("Your choice (1-5): ")
    
    if choice == '1':
        task = input("Task: ")
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added!")
        
    elif choice == '2':
        if not tasks:
            print("No tasks!")
        else:
            print("\n" + "-" * 30)
            for i, t in enumerate(tasks, 1):
                status = "Done" if t["done"] else "Pending"
                print(str(i) + ". " + status + " - " + t["task"])
            print("-" * 30)
            
    elif choice == '3':
        if not tasks:
            print("No tasks!")
        else:
            for i, t in enumerate(tasks, 1):
                print(str(i) + ". " + t["task"])
            try:
                num = int(input("Task number: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done!")
                else:
                    print("Error: Invalid number!")
            except ValueError:
                print("Error: Invalid input!")
                
    elif choice == '4':
        if not tasks:
            print("No tasks!")
        else:
            for i, t in enumerate(tasks, 1):
                print(str(i) + ". " + t["task"])
            try:
                num = int(input("Task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print("Task deleted: '" + removed["task"] + "'")
                else:
                    print("Error: Invalid number!")
            except ValueError:
                print("Error: Invalid input!")
                
    elif choice == '5':
        print("Goodbye!")
        break
        
    else:
        print("Error: Invalid choice!")