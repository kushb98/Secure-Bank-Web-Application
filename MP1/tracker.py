from datetime import datetime
import json
import os

tasks = []
# constant, don't edit, use .copy()
TASK_TEMPLATE = {
    "name":"",
    "due": None, # datetime
    "lastActivity": None, # datetime
    "description": "",
    "done": False # False if not done, datetime otherise
}

# don't edit, intentionaly left an unhandled exception possibility
def str_to_datetime(datetime_str):
    """ attempts to convert a string in one of two formats to a datetime
    Valid formats (visual representation): mm/dd/yy hh:mm:ss or yyyy-mm-dd hh:mm:ss """
    try:
        return datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')
    except:
        return datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')

def save():
    """ writes the tasks list to a json file to persist changes """
    f = open("tracker.json", "w")
    f.write(json.dumps(tasks, indent=4, default=str))
    f.close()

def load():
    """ loads the task list from a json file """
    if not os.path.isfile("tracker.json"):
        return
    f = open("tracker.json", "r")
    
    data = json.load(f)
    # Note about global keyword: https://stackoverflow.com/a/11867510
    global tasks
    tasks = data
    f.close()
    print(f"data {data}")    

def list_tasks(_tasks):
    """ List a summary view of all tasks """
    i = 0
    for t in _tasks:
        print(f"{i+1}) [{'x' if t['done'] else ' '}] Task: {t['name']} (Due: {t['due']})")
        i += 1
    if len(_tasks) == 0:
        print("No tasks to show")

# edits should happen below this line

def add_task(name: str, description: str, due: str):
    """ Copies the TASK_TEMPLATE and fills in the passed in data then adds the task to the tasks list """
    task = TASK_TEMPLATE.copy() # don't delete this
    # update lastActivity with the current datetime value
    task["lastActivity"] = datetime.now()
    # set the name, description, and due date (all must be provided)
    if name == "" or description == ""  or due == "" :
        print("Your addtion was not completed due to empty input! Please make sure all 3 values are entered")
    else:
        task["name"] = name 
        task["description"] = description
        task["due"] = str_to_datetime(due)
        tasks.append(task)
        print("Your task was added successfully!")
    # due date must match one of the formats mentioned in str_to_datetime()
    # add the new task to the tasks list
    # output a message confirming the new task was added or if the addition was rejected due to missing data
    # make sure save() is still called last in this function
    #kb97 , 15th February 2023
    save()

def process_update(index):
    """ extracted the user input prompts to get task data then passes it to update_task() """
    if index in range(len(tasks)):
        print(tasks[index])
        task1 =tasks[index]["name"]
        task2 =tasks[index]["description"]
        task3 =tasks[index]["due"]
        name = input(f"What's the name of this task? ({task1})\n").strip()
        desc = input(f"What's a brief descriptions of this task? ({task2}) \n").strip()
        due = input(f"When is this task due (format: m/d/y H:M:S) ({task3}) \n").strip()
        update_task(index, name=name, description=desc, due=due)
    else:
        print("Out of Bounds")    
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # show the existing value of each property where the TODOs are marked in the text of the inputs (replace the TODO related text)
    # kb97 , 15th February 2023
    
    

def update_task(index: int, name: str, description:str, due: str):
    """ Updates the name, description , due date of a task found by index if an update to the property was provided """
    flag = 0

    if index in range(len(tasks)):
        if(name!=""):
            flag = 1
            tasks[index]["name"] = name

        if(description!=""):
            flag = 1
            tasks[index]["description"] = description

        if(due!=""):
            flag = 1
            tasks[index]["due"] = str_to_datetime(due)

        if(flag == 1):
            print("Your task was successfully updated!")

        if(flag ==0):
            print("Your task was not updated since no changes were provided!")       

    else:
        print("Index out of Bounds")          

    tasks[index]["lastActivity"] =datetime.now()
    # find the task by index          
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # update incoming task data if it's provided (if it's not provided use the original task property value)
    # update lastActivity with the current datetime value
    # output that the task was updated if any items were changed, otherwise mention task was not updated
    # make sure save() is still called last in this function
    # kb97 , 16th February 2023
    
    save()

def mark_done(index):
    """ Updates a single task, via index, to a done datetime"""
    if index in range(len(tasks)):
        if tasks[index]["done"] == False:
            tasks[index]["done"] = datetime.now()
            print("Task marked as Done")
        else:
            print("Task is already completed") 
    else:
        print("Index is out of Bounds") 
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # if it's not done, record the current datetime as the value
    # if it is done, print a message saying it's already completed
    # make sure save() is still called last in this function
    # kb97 , 16th February 2023

    save()

def view_task(index):
    """ View more info about a specific task fetch by index """ 
    # find task from list by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # utilize the given print statement when a task is found
    # kb97 , 17th February 2023
    if index in range(len(tasks)):
        task = { 
                "name":tasks[index]["name"],
                "due" :tasks[index]["due"],
                "lastActivity":tasks[index]["lastActivity"],
                "description":tasks[index]["description"],
                "done" :tasks[index]["done"]
    }
        print(f"""
        [{'x' if task['done'] else ' '}] Task: {task['name']}\n 
        Description: {task['description']} \n 
        Last Activity: {task['lastActivity']} \n
        Due: {task['due']}\n
        Completed: {task['done'] if task['done'] else '-'} \n
        """.replace('  ', ' '))
    
    else:
        print("Index out of bounds")



def delete_task(index):
    """ deletes a task from the tasks list by index """
    if index in range(len(tasks)):
        tasks.pop(index)
        print("Your task was successfully deleted")
    else:
        print("Task was not removed since index out bounds")
    # delete/remove task from list by index
    # message should show if it was successful or not
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # make sure save() is still called last in this function
    # kb97 , 16th February 2023
    
    save()

def get_incomplete_tasks():
    """ prints a list of tasks that are not done """
    _tasks = []
    for i in range(len(tasks)):
        if tasks[i]["done"] == False:
            _tasks.append(tasks[i])  
    # generate a list of tasks where the task is not done
    # pass that list into list_tasks()
    # kb97 , 16th February 2023
    
    list_tasks(_tasks)

def get_overdue_tasks():
    """ prints a list of tasks that are over due completion (not done and expired) """
    # generate a list of tasks where the due date is older than now and that are not complete
    # pass that list into list_tasks()
    # kb97 , 17th February 2023
    _tasks = []
    for i in range(len(tasks)):
        due_date = str_to_datetime(str(tasks[i]["due"]))
        if (datetime.now() > due_date) and (tasks[i]["done"] == False): 
            _tasks.append(tasks[i])
    list_tasks(_tasks)

def get_time_remaining(index):
    """ outputs the number of days, hours, minutes, seconds a task has before it's overdue otherwise shows similar info for how far past due it is """
    if index in range(len(tasks)):
        if datetime.now() > str_to_datetime(tasks[index]["due"]) :
            time_passed =  datetime.now() - str_to_datetime(tasks[index]["due"])
            print( f"The task is overdue by {time_passed}" )

        elif datetime.now() < str_to_datetime(tasks[index]["due"]) :
            time_remaining = str_to_datetime(tasks[index]["due"]) - datetime.now()
            print( f"The remaing time to due date is {time_remaining}" )    


    else:
        print("Index out of bounds")    
    # get the task by index
    # consider index out of bounds scenarios and include appropriate message(s) for invalid index
    # get the days, hours, minutes, seconds between the due date and now
    # display the remaining time via print in a clear format showing days, hours, minutes, seconds
    # if the due date is in the past print out how many days, hours, minutes, seconds the task is over due (clearly note that it's over due, values should be positive)
    # include your ucid and date as a comment of when you implemented this, briefly summarize the solution
    task = {}

# no changes needed below this line

command_list = ["add", "view", "update", "list", "incomplete", "overdue", "delete", "remaining", "help", "quit", "exit", "done"]
def print_options():
    """ prints a readable list of commands that can be typed when prompted """
    print("Choices")
    print("add - Creates a task")
    print("update - updates a specific task")
    print("view - see more info about a task by number")
    print("list - lists tasks")
    print("incomplete - lists incomplete tasks")
    print("overdue - lists overdue tasks")
    print("delete - deletes a task by number")
    print("remaining - gets the remaining time of a task by number")
    print("done - marks a task complete by number")
    print("quit or exit - terminates the program")
    print("help - shows this list again")

def run():
    """ runs the program until terminated or a quit/exit command is used """
    print("Welcome to Task Tracker!")
    load()
    print_options()
    while(True):
        opt = input("What would you like to do?\n").strip() # strip removes whitespace from beginning/end
        if opt not in command_list:
            print("That's not a valid option")
        elif opt == "add":
            name = input("What's the name of this task?\n").strip()
            desc = input("What's a brief descriptions of this task?\n").strip()
            due = input("When is this task due (visual format: mm/dd/yy hh:mm:ss)\n").strip()
            add_task(name, desc, due)
        elif opt == "view":
            num = int(input("Which task do you want to view? (hint: number from 'list') ").strip())
            index = num-1
            view_task(index)
        elif opt == "update":
            num = int(input("Which task do you want to update? (hint: number from 'list') ").strip())
            index = num-1
            process_update(index)
        elif opt == "done":
            num = int(input("Which task do you want to complete? (hint: number from 'list') ").strip())
            index = num-1
            mark_done(index)
        elif opt == "list":
            list_tasks(tasks)
        elif opt == "incomplete":
            get_incomplete_tasks()
        elif opt == "overdue":
            get_overdue_tasks()
        elif opt == "delete":
            num = int(input("Which task do you want to delete? (hint: number from 'list') ").strip())
            index = num-1
            delete_task(index)
        elif opt == "remaining":
            num = int(input("Which task do you like to get the duration for? (hint: number from 'list') ").strip())
            index = num-1
            get_time_remaining(index)
        elif opt in ["quit", "exit"]:
            print("Good bye.")
            quit()
        elif opt == "help":
            print_options()
        
if __name__ == "__main__":
    run()