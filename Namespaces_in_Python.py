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

def add(spaces, current_namespace, what):
    if current_namespace not in spaces:
        spaces[current_namespace] = {}
        spaces[current_namespace]['variables'] = []
        spaces[current_namespace]['variables'].append(what)
    else:
        if 'variables' not in spaces[current_namespace]:
            spaces[current_namespace]['variables'] = []
            spaces[current_namespace]['variables'].append(what)
        else:
            spaces[current_namespace]['variables'].append(what)

def create(spaces, current_namespace, parent_namespace):
    if current_namespace not in spaces:
        spaces[current_namespace] = {}
        spaces[current_namespace]['features'] = []
        spaces[current_namespace]['variables'] = []
        spaces[parent_namespace]['features'].append(current_namespace)
        spaces[current_namespace]['parent'] = parent_namespace
    else:
        if 'features' not in spaces[current_namespace]:
            spaces[current_namespace]['features'] = []
            spaces[current_namespace]['parent'] = parent_namespace
            spaces[parent_namespace]['features'].append(current_namespace)
        else:
            spaces[current_namespace]['features'].append(current_namespace)
            spaces[parent_namespace]['features'].append(current_namespace)

def search(spaces, namespace, what):
    if what in spaces[namespace]['variables']:
        return namespace
    else:
        try:
            upper_namespace = spaces[namespace]['parent']
        except KeyError:
            return None
        return search(spaces, upper_namespace, what)

for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(spaces, command[1], command[2])
    elif command[0] == 'create':
        create(spaces, command[1], command[2])
    elif command[0] == 'get':
        print(search(spaces, command[1], command[2]))
