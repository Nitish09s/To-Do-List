class TodoList:
    def __init__(self, file_name='todo_list.txt'):
        """Initialize the TodoList with a file to store tasks."""
        self.file_name = file_name
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from a file into the list."""
        try:
            with open(self.file_name, 'r') as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Save the current list of tasks to the file."""
        with open(self.file_name, 'w') as file:
            for task in self.tasks:
                file.write(task + '\n')

    def add_task(self, task):
        """Add a task to the list and save the changes."""
        self.tasks.append(task)
        self.save_tasks()
        print(f'Task "{task}" added.')

    def view_tasks(self):
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks in the list!")
        else:
            print("\nTo-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def remove_task(self, task_number):
        """Remove a task by its number and save the changes."""
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")


def menu():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Remove a task")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            task = input("Enter a new task: ")
            todo_list.add_task(task)
        elif choice == '3':
            todo_list.view_tasks()
            task_num = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_num)
        elif choice == '4':
            print("Exiting the to-do list.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    menu()
