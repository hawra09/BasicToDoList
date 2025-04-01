def todolist():
    tasks = []
    while True:
        print('      To Do List      ')
        print('Use the following commands:')
        print('1. Add Task')
        print('2. Show Tasks')
        print('3. Mark Task as Done')
        print('4. Exit Application')
        choice = input('Enter the command you would like to execute:')
        if choice == '1':
            n_tasks = int(input('How many tasks would you like to add:'))
            for i in range(n_tasks):
                task = input(f'Please enter task #{i+1}:').strip()
                tasks.append({'Task': task, "Complete": False})
                print(f'{task} has been added!')
        elif choice == '2':
            if not tasks:
                print('There are no tasks available')
            else:
                print(tasks)
        elif choice == '3':
            task_index = int(input('Enter the task number to mark as done:')) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["Complete"] = True
            else:
                print('Invalid task number!')
        elif choice == '4':
            print('Thank you for using the To-Do List Application')
            break
        else:
            print('Invalid selection! Please try again!')
todolist()