# Namespaces_in_Python
Emulation of the work of the namespace in Python

### Reference to:
[1] Valentyn N Sichkar. Emulation of the work of the namespace in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Namespaces_in_Python (date of access: XX.XX.XXXX)

## Description
In this task, each namespace has a unique text identifier – its name.
<br/>The following requests are submitted to the program for entry:
<br/><b>create < namespace > < parent ></b> - create a new namespace named < namespace > inside the <parent> space
<br/><b>add < namespace > < var> </b> - add the < var >variable to the <namespace> 
<br/><b>get < namespace > < var ></b> - get the name of the space from which the < var > variable will be taken when queried from the < namespace > space, or None if no such space exists

Input format:
<br/>9
<br/>add global a
<br/>create foo global
<br/>add foo b
<br/>get foo a
<br/>get foo c
<br/>create bar foo
<br/>add bar a
<br/>get bar a
<br/>get bar b

<br/>Output:
<br/>global
<br/>None
<br/>bar
<br/>foo

## MIT License
## Copyright (c) 2018 Valentyn N Sichkar
## github.com/sichkar-valentyn
### Reference to:
[1] Valentyn N Sichkar. Emulation of the work of the namespace in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Namespaces_in_Python (date of access: XX.XX.XXXX)
