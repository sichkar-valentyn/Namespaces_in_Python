# File: Namespaces_in_Python.py
# Description: Emulation of the work of the namespace in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Emulation of the work of the namespace in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Namespaces_in_Python (date of access: XX.XX.XXXX)

# Number of input lines
n = int(input())
spaces = {'global': {'features': [], 'variables': []}}

# Function to add new variable into the namespace
def adding_to_the_namespace(spaces, name_space, value):
    if name_space not in spaces:
        spaces[name_space] = {}
        spaces[name_space]['variables'] = []
        spaces[name_space]['variables'].append(value)
    else:
        if 'variables' not in spaces[name_space]:
            spaces[name_space]['variables'] = []
            spaces[name_space]['variables'].append(value)
        else:
            spaces[name_space]['variables'].append(value)

# Function to create new namespace
def create_namespace(spaces, name_space, parent_namespace):
    if name_space not in spaces:
        spaces[name_space] = {}
        spaces[name_space]['features'] = []
        spaces[name_space]['variables'] = []
        spaces[parent_namespace]['features'].append(name_space)
        spaces[name_space]['parent'] = parent_namespace
    else:
        if 'features' not in spaces[name_space]:
            spaces[name_space]['features'] = []
            spaces[name_space]['parent'] = parent_namespace
            spaces[parent_namespace]['features'].append(name_space)
        else:
            spaces[name_space]['features'].append(name_space)
            spaces[parent_namespace]['features'].append(name_space)

# Function to search variable in the namespases
def search_namespace(spaces, namespace, value):
    if value in spaces[namespace]['variables']:
        return namespace
    else:
        try:
            upper_namespace = spaces[namespace]['parent']
        except KeyError:
            return None
        return search_namespace(spaces, upper_namespace, value)

# Showing the results
for i in range(n):
    input_string = input().split()
    if input_string[0] == 'adding_to_the_namespace':
        adding_to_the_namespace(spaces, input_string[1], input_string[2])
    elif input_string[0] == 'create_namespace':
        create_namespace(spaces, input_string[1], input_string[2])
    elif input_string[0] == 'get':
        print(search_namespace(spaces, input_string[1], input_string[2]))
