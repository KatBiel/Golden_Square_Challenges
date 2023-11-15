1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

2. Design the Function Signature

def include_todo(text):

parameters: text
returns: True or False
side effects: no side effects

pass

3. Create Examples as Tests

'''
Given a text with #TODO 
returns true
'''
include_todo('This is a #TODO item.) --> True

'''
Given a sentence with no #TODO
returns false
'''
include_todo('There is nothing to do today.') --> False

'''
Given an empty string
raises an error
'''
incluse_todo('') --> Raises an error 'No text to evaluate'

4. Implement the Behaviour

# Example

import pytest
from lib.include_todo import *

'''
Given a text with #TODO 
returns true
'''
def test_include_todo():
    result = include_todo('This is a #TODO item.')
    assert result == True