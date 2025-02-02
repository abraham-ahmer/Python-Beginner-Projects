task = []
while True: #for infinite input, condition = always true.
    task_name = input("Write Task: ").lower()

    # To exit code
    if task_name == "done":
        break #exit if the use types 'done'

        #removing completed tasks before appending.
    if task_name.startswith("completed "):
        remove_task = task_name.replace("completed ", "", 1) #extracts the actual task by replacing 'remove' with task
        if remove_task in task: 
            task.remove(remove_task) #if found 'remove', then remove it 
            print("Completed:", remove_task)

    else:
        task.append(task_name) #append in the end, so that exit and removing cond wont be counted as part of append.
        #print(f"Task list: {task}")

print(f"Your Final Tasks: {task}")