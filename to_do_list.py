class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task}' deleted from the to-do list.")
        else:
            print("Invalid task index. No task deleted.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks[task_index - 1]
            print(f"Task '{completed_task}' marked as completed.")
            # You can add additional functionality here, like moving the task to a 'Completed' list.
        else:
            print("Invalid task index. No task marked as completed.")


def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.display_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "3":
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "4":
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "5":
            print("Exiting the to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
