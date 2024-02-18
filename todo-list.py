def main():
    todo = {}

    running = True
    while running:
        print("What action would you like to take: ")
        action = input("""Press [A] to add a task, 
                       [V] to view all tasks, 
                       [M] to mark a task as completed,
                       [D] to delete a task,
                       Any other key to quit.""").upper()
        
        if action == "A":
            item = input("What would you like to add? ")
            todo.update({item : " "})
        elif action == "V":
            print("Tasks: ")
            for task in todo.keys():
                print(task + f" [{todo[task]}]")
        elif action == "M":
            item = input("What would you like to mark as completed? ")
            try:
                todo[item] = "X"
            except:
                print("THAT TASK IS NOT IN THE LIST")
        elif action == "D":
            item = input("What item would you like to delete? ")
            try:
                todo.pop(item)
            except:
                print("THAT TASK IS NOT IN THE LIST")
        else:
            running = False


main()