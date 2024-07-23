tasks = []
def addTask():
  title = input("Enter task title: ")
  tasks.append({"title": title, "completed": False})
  print(f"Task '{title}' added!")
def viewTasks():
  if not tasks:
    print("There are no tasks on your list.")
  else:
    print("Tasks:")
    counter = 1
    for task in tasks:
      completion = "completed" if task["completed"] else ["pnding"]
      print(f"{counter} {task['title']} ({completion})")
      counter = counter+1
def markTaskCompleted():
  taskNumber = int(input("Enter task number to mark complete: ")) - 1
  if 0 <= taskNumber < len(tasks):
    tasks[taskNumber]["completed"] = True
    print(f"Task '{tasks[taskNumber]['title']}' marked complete!")
  else:
    print("Invalid task number. Please try again.")
def deleteTask():
  taskNumber = int(input("Enter task number to delete: ")) - 1
  if 0 <= taskNumber < len(tasks):
    for i in range(taskNumber, len(tasks) - 1):
      tasks[i] = tasks[i + 1]
    tasks = tasks[: len(tasks) - 1]
    print(f"Task deleted successfully!")
  else:
    print("Invalid task number. Please try again.")
while True:
  print("To-Do List Menu:")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Completed")
  print("4. Delete Task")
  print("5. Exit")
  choice = input("Enter your choice (1-5): ")
  if choice == "1":
    addTask()
  elif choice == "2":
    viewTasks()
  elif choice == "3":
    markTaskCompleted()
  elif choice == "4":
    deleteTask()
  elif choice == "5":
    print("rahet aalek")
    break
  else:
    print("invalid choice. please try again.")