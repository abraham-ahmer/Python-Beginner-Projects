
# Implement a class TodoList with methods to add, remove, mark complete, and list tasks.

class ToDoList:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def add_task(self, **kwargs):
          self.tasks.append(kwargs)
       
    def __str__(self): # displaying all the tasks with title, desc, status
        output = ""
        for i in self.tasks:
            output += f"Title: {i["title"]} | Description: {i["description"]} | Status: {i["status"]}\n"
        return output.strip()
    
        # return str(self.tasks) raw form
    

    def all_tasks(self):  # displaying only tasks
        only_tasks  = [i["title"] for i in self.tasks]
        return f"All Tasks: {only_tasks}"
    

    def completed_tasks(self):  # tasks that are completed
                   
        completed = [i["title"] for i in self.tasks if i['status'] == "completed"]
        return f"Completed tasks: {completed}"


    def remove_task(self):  # remove task after completion

        self.tasks = [task for task in self.tasks if task["status"] != "completed"] 
        return f"After removing completed tasks: {self.tasks}"

# put the whole dictionary (task) into the new list after iterating and checking the condition


t1 = ToDoList([])

t1.add_task(title="Practicing", description="practicing coding", status="completed")
t1.add_task(title="Reading", description="Reading Biography", status="pending")
t1.add_task(title="Playing", description="Playing videogame", status="completed")

print(t1)

print(t1.all_tasks())

print(t1.completed_tasks())

print(t1.remove_task())
