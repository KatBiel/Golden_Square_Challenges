class ToDo:

    def __init__(self):
        self.todo_list = []

    def add(self, task):
        if task == '':
            raise Exception('Cannot add empty task!')
        self.todo_list.append(task)

    def remove(self, task):
        self.todo_list.remove(task)

    def show_all_to_dos(self):
        return self.todo_list
        