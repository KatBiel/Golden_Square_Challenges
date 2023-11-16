1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

2. Design the Class Interface
Include the initializer, public properties, and public methods with all parameters, return values, and side-effects.

class ToDo
# User-facing properties:
#    name: string

    def __init__(self):
        self.todo_list = []
# Parameteres: n/a
# Side effects: initilizes the to do list 
    pass

    def add(self, task):
# Parameters: task: a string representing a single task
# Returns: Nothing
# Side effects: Saves the task to the self object
#   Throws an exception if the task is already on the list
    pass

    def remove(self, task):
# Parameters:  a string representing a single task
# Returns: Nothing
# Side effects: Removes the task from the self object
#   Throws an exception if the task is not on the list

    def show_all_to_dos(slef):
# Parameteres: n/a
# Returns: a list of updated to do-s
# Side effects: Print the final list 


3. Create Examples as Tests
Make a list of examples of how the class will behave in different situations.

# EXAMPLE

'''
Add a task to the list and assert that list is updated 
'''

test_add_(task) --> [Do laundry]

'''
Add a task to the list and assert that list is updated 
'''
test_add_multiple_tasks(task1, task2, task3) --> [task1, task2, task3]

'''
Test add empty task
'''
test_add_empty_sting() --> rasises error 'Cannot add empty task!'

'''
Remove completed tasks from the list 
'''
test_remove_completed_tasks(task2) --> [task1, task3]




4. Implement the Behaviour
After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.