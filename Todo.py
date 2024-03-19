class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a task to the to-do list."""
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        """Remove a task from the to-do list."""
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def show_tasks(self):
        """Show all tasks in the to-do list."""
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("To-Do List is empty.")

def main():
    todo_list = TodoList()  # Create a to-do list object

    print("Welcome to To-Do List Manager!")
    while True:
        print("\nSelect operation:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            todo_list.show_tasks()
        elif choice == '4':
            print("Thank you for using To-Do List Manager!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
