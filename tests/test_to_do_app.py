from lib.to_do_app import *
import pytest


# '''
# Add a task to the list and assert that list is updated 
# '''

def test_add_one_task():
    todo = ToDo()
    todo.add('Do laundry')
    assert todo.show_all_to_dos() == ['Do laundry']

def test_add_multiple_tasks():
    todo = ToDo()
    todo.add('Wash dishes')
    todo.add('Walk the dog')
    todo.add('Feed cats')
    assert todo.show_all_to_dos() == ['Wash dishes', 'Walk the dog', 'Feed cats']

def test_add_empty_task():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add('')
    error = str(e.value)
    assert error == 'Cannot add empty task!'

def test_remove_completed_task():
    todo = ToDo()
    todo.add('Wash dishes')
    todo.add('Walk the dog')
    todo.add('Feed cats')
    todo.remove('Walk the dog')
    assert todo.show_all_to_dos() == ['Wash dishes', 'Feed cats']

