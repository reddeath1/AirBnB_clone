# AirBnB_clone

For this project, we expect you to look at these concepts:

Python packages
AirBnB clone


Background Context
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object
Resources
Read or watch:

cmd module
cmd module in depth
packages concept page
uuid module
datetime
unittest module
args/kwargs
Python test cheatsheet
cmd module wiki page
python unittest
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General<br>
How to create a Python package<br>
How to create a command interpreter in Python using the cmd module<br>
What is Unit testing and how to implement it in a large project<br>
How to serialize and deserialize a Class<br>
How to write and read a JSON file<br>
How to manage datetime<br>
What is an UUID<br>
What is *args and how to use it<br>
What is **kwargs and how to use it<br>
How to handle named arguments in a function<br>
Copyright - Plagiarism<br>
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.<br>
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.<br>
You are not allowed to publish any content of this project.<br>
Any form of plagiarism is strictly forbidden and will result in removal from the program.<br>
## Requirements<br>
Python Scripts<br>
Allowed editors: vi, vim, emacs<br>
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)<br>
All your files should end with a new line<br>
The first line of all your files should be exactly #!/usr/bin/python3<br>
A README.md file, at the root of the folder of the project, is mandatory<br>
Your code should use the pycodestyle (version 2.8.*)<br>
All your files must be executable<br>
The length of your files will be tested using wc<br>
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')<br>
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')<br>
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')<br>
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)<br>
## Python Unit Tests<br>
Allowed editors: vi, vim, emacs<br>
All your files should end with a new line<br>
All your test files should be inside a folder tests<br>
You have to use the unittest module<br>
All your test files should be python files (extension: .py)<br>
All your test files and folders should start by test_<br>
Your file organization in the tests folder should be the same as your project<br>
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py<br>
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py<br>
All your tests should be executed by using this command: python3 -m unittest discover tests<br>
You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py<br>
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')<br>
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')<br>
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')<br>
We strongly encourage you to work together on test cases, so that you don’t miss any edge case<br>
## GitHub
There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.<br>

More Info
Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash
<br>
AUTHORS<br>
FRANK GALOS <https://github.com/reddeath1/><br>
Alabi Abdulmateen Bukola <https://github.com/AbdulmateenAl>


