import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a", encoding= "utf-8") as file:
      file.write(task + "\n")
     
     

#Input - a task to add to the list
    #Return - nothing
    
def list_tasks(): 
    
    with open(TASK_FILE, "r", encoding= "utf-8") as file: 
        tasks = file.readlines()
        output_string = ""
        counter = 1
        for tasks in tasks:
            output_string = output_string

def remove_task(index):ng + str(counter) + ". "+ tasks
            counter = counter + 1
            output_string = string.rstrip("\n")


            
    return output_string


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"import argparse
            import os

            TASK_FILE = ".tasks.txt"

            def add_task(task):
                with open(TASK_FILE, "a", encoding= "utf-8") as file:
                  file.write(task + "\n")
                 
                 

            #Input - a task to add to the list
                #Return - nothing 
                
                 def list_tasks():
                
                with open(TASK_FILE, "r", encoding= "utf-8") as file: 
                    tasks = file.readlines()
                    output_string = "" 
                    counter = 1
                    for tasks in tasks:
                        output_string = output_string

            def remove_task(index):ng + str(counter) + ". "+ tasks
                        counter = counter + 1
                        output_string = string.rstrip("\n")


                        
                return output_string()


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
    main()WORDS
