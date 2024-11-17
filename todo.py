# Initialize an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    if task:  # Check if the task is not an empty string
        tasks.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("Task cannot be empty!")

# Function to list all tasks
def list_tasks():
    if tasks:  # Check if the task list is not empty
        print("Here are your tasks:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("No tasks to display. Your to-do list is empty.")

# Function to remove a task by its index
def remove_task(index):
    try:
        task = tasks.pop(index - 1)  # Pop the task at the given index (adjusting for 0-based index)
        print(f"Task '{task}' removed successfully.")
    except IndexError:
        print("Error: Invalid task number. Please try again.")
        
# Main menu function to interact with the user
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()  # Show the tasks before asking for a task number
            try:
                task_number = int(input("Enter the task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Run the program
if __name__ == "__main__":
    main()
