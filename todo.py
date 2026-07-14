tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("View Tasks selected")

    elif choice == "2":
        print("Add Task selected")

    elif choice == "3":
        print("Delete Task selected")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")