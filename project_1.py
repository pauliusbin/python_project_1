import webbrowser
import random

questions_file = 'questions1.txt'
money = 0
web_help = 1
fiftyfifty_help = 1
questions_list= [["Knowing that a function named fun() resides in a module named mod, choose the proper way to import it:", "import fun from mod", "import fun", "from mod import fun", "from fun import mod"],["Knowing that a function named fun() resides in a module named mod, and it has been imported using the following line: \n\nimport mod \nchoose the way it can be invoked in your code:", "mod.fun()", "mod::fun()", "fun()", "mod‑>fun()"],["A function returning a list of all entities available in a module is called:", "content()", "dir()", "entities()", "listmodule()"],["The pyc file contains:", "compiled Python code", "a Python interpreter", "a Python compiler", "Python source code"],["When a module is imported, its contents:", "are executed once (implicitly)", "are executed as many times as they are imported", "are ignored", "may be executed (explicitly)"],["A predefined Python variable, storing the current module name, is called:", "__modname__", "__name__", "__mod__", "__module__"],["The following statement:\nfrom a.b import c\ncauses the import of:", "entity c from module b from package a", "entity a from module b from package c", "entity c from module a from package b", "entity b from module a from package c"],["Entering the try: block implies that:", "the block will be omitted", "all of the instructions from this block will be executed", "some of the instructions from this block may not be executed", "none of the instructions from this block will be executed"],["The unnamed except: block:", "must be the last one", "cannot be used if any named block has been used", "can be placed anywhere", "must be the first one"],["The top‑most Python exception is named:", "BaseException", "Exception", "TopException", "PythonException"],["The following statement:\nassert var == 0", "will stop the program when var != 0", "is erroneous", "has no effect", "will stop the program when var == 0"],["ASCII is:", "a predefined Python variable name", "a standard Python module name", "a character name", "short for American Standard Code for Information Interchange"],["UTF‑8 is:", "a synonym for “byte”", "a form of encoding Unicode code points", "the 9th version of the UTF standard", "a Python version name"],["UNICODE is a standard:", "honored by the whole universe", "for coding floating-point numbers", "used by coders from universities", "like ASCII, but much more expansive"],["The following code\nx = ‘\”\nprint(len(x))\nprints:", "1", "0", "3", "2"],["The following code:\nprint(ord(‘c’) – ord(‘a’))\nprints:", "3", "2", "0", "1"],["The following code\nprint(chr(ord(‘z’) – 2))\nprints:", "x", "a", "z", "y"],["The following code\nprint(3 * ‘abc’ + ‘xyz’)\nprints:", "abcabcabcxyz", "abcabcxyzxyz", "xyzxyzxyzxyz", "abcxyzxyzxyz"],["The following code\nprint(‘Mike’ > “Mikey”)\nprints:", "0", "False", "1", "True"],["The following code:\nprint(float(“1,3”))", "prints 1,3", "prints 1.3", "raises a ValueError exception", "prints 13"]]
player_name = input("Welcome to the game!\nPlease enter your name: ")
print (player_name.capitalize()+", please enter:\n'start' if you want to start the game\n'quit' if you want to end game and take the money\n'help' if you need help" )

#with open(questions_file) as file_object:
#    lines = file_object.readlines()
#for line in lines:
#    questions_list.append(line.strip())
#print(questions_list)    
    
answer = input("Enter your answer: ")
if answer.lower() == "stop":
    print(money)
elif answer.lower() == "browse":
    webbrowser.open('http://google.com', new=2)
else:
    print("wrong input")

#statistics file read write and open
