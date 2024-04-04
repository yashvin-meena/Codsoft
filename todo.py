class TODO():
    list = []
    def create_todo(self):
        task = input('Enter your task:')
        self.list.append(task)
        print('added !!')
        
    def update_todo(self):
        task = input('Enter previous task:')
        for i in range(len(self.list)):
            if self.list[i] == task:
                new_task = input('Enter new task to update:')
                self.list[i] = new_task
                print('updated !!')
                break
        else:
            print('No such task !!')
    
    def delete_todo(self):
        task = input('Enter the task to delete:')
        if task in self.list:
            self.list.remove(task)
            print('deleted !!')
        else:
            print('No such task !!')

    def view_todo(self):
        task_list = self.list
        if task_list:
            for i in task_list:
             print(i)
        else:
           print('You do not have any task !!')

ch = 'Y'
print('******TODO-LIST******')
while ch == 'Y':
    print('''
    1. press 1 to add task
    2. press 2 to update task
    3. press 3 to view task list
    4. press 4 to delete
    5. press 5 to exit
    ''')
    choice = int(input('Enter choice:'))
    td = TODO()
    if choice == 1:
        td.create_todo()
    elif choice == 2:
        td.update_todo()
    elif choice == 3:
        td.view_todo()
    elif choice == 4:
        td.delete_todo()
    elif choice >= 5:
        break
    ch = input('press Y to continue:')[0]
    ch = ch.upper()
    

