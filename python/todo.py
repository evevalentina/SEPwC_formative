import argparse
import os

fileTASK_FILE = ".tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a" encoding= "utf-8") as file
    #inputting items into a task
    #manual task file wtitten as a list
    list[Item_1, Item_2 , Item_3, Item_4, Item_5]:
     print(list)
     
     
     
Input - a task to add to the list
    Return - nothing 
    
def list_tasks():
    
    with open(TASK_FILE, "r", encoding= "utf-8") as file:
        tasks = file.readlines()
        counter = 1
      for tasks in tasks:
            output_string = output_string + str(counter) + ","+ tasks
            counter = counter + 1
            

    return


def remove_task(index):
    return

def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
