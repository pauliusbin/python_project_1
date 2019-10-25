import webbrowser
import random
web_help = 0
fiftyfifty_help = 0
questions_file = 'questions1.txt'
payout = {1:100, 2:200, 3:300, 4:500, 5:1000, 6:2000, 7:4000, 8:8000, 9:16000, 10:32000, 11:64000, 12:125000, 13:250000, 14:500000, 15:1000000}
answer_value = {"a":1, "b":2, "c":3, "d":4}
time_limit = 30
questions_list = [["Knowing that a function named fun() resides in a module named mod, choose the proper way to import it:", "import fun from mod", "import fun", "from mod import fun", "from fun import mod","c"],["Knowing that a function named fun() resides in a module named mod, and it has been imported using the following line: \nimport mod \nchoose the way it can be invoked in your code:", "mod.fun()", "mod::fun()", "fun()", "mod‑>fun()","a"],["A function returning a list of all entities available in a module is called:", "content()", "dir()", "entities()", "listmodule()","b"],["The pyc file contains:", "compiled Python code", "a Python interpreter", "a Python compiler", "Python source code","a"],["When a module is imported, its contents:", "are executed once (implicitly)", "are executed as many times as they are imported", "are ignored", "may be executed (explicitly)","a"],["A predefined Python variable, storing the current module name, is called:", "__modname__", "__name__", "__mod__", "__module__","b"],["The following statement:\nfrom a.b import c\ncauses the import of:", "entity c from module b from package a", "entity a from module b from package c", "entity c from module a from package b", "entity b from module a from package c","a"],["Entering the try: block implies that:", "the block will be omitted", "all of the instructions from this block will be executed", "some of the instructions from this block may not be executed", "none of the instructions from this block will be executed","c"],["The unnamed except: block:", "must be the last one", "cannot be used if any named block has been used", "can be placed anywhere", "must be the first one","a"],["The top‑most Python exception is named:", "BaseException", "Exception", "TopException", "PythonException","a"],["The following statement:\nassert var == 0", "will stop the program when var != 0", "is erroneous", "has no effect", "will stop the program when var == 0","d"],["ASCII is:", "a predefined Python variable name", "a standard Python module name", "a character name", "short for American Standard Code for Information Interchange","d"],["UTF‑8 is:", "a synonym for “byte”", "a form of encoding Unicode code points", "the 9th version of the UTF standard", "a Python version name","b"],["UNICODE is a standard:", "honored by the whole universe", "for coding floating-point numbers", "used by coders from universities", "like ASCII, but much more expansive","d"],["The following code\nx = ‘\\”\nprint(len(x))\nprints:", "1", "0", "3", "2","a"],["The following code:\nprint(ord(‘c’) – ord(‘a’))\nprints:", "3", "2", "0", "1","b"],["The following code\nprint(chr(ord(‘z’) – 2))\nprints:", "x", "a", "z", "y","a"],["The following code\nprint(3 * ‘abc’ + ‘xyz’)\nprints:", "abcabcabcxyz", "abcabcxyzxyz", "xyzxyzxyzxyz", "abcxyzxyzxyz","a"],["The following code\nprint(‘Mike’ > “Mikey”)\nprints:", "0", "False", "1", "True","b"],["The following code:\nprint(float(“1,3”))", "prints 1,3", "prints 1.3", "raises a ValueError exception", "prints 13","c"]]

player_name = input("Welcome to the game \"Who Wants to be a Millionaire\"!\nPlease enter your name: ")
print(player_name.capitalize()+", you have", time_limit, "minutes to answer 15 questions and became a millionaire!\nYou have 2 guarantee points: 1000 and 32000\nThere are 2 lifelines:\n50/50 - enter \"50/50\"\nSearch in web - enter \"web\"\n\nEnter'quit' to end the game and take the money\n")

#with open(questions_file) as file_object:
#    lines = file_object.readlines()
#for line in lines:
#    questions_list.append(line.strip())
#print(questions_list)  
def web():
    if web_help == 0:
        webbrowser.open('http://google.com', new=2)
        web_help +=1
        answer = input("Enter your answer (a, b, c or d): ")
    else:
        print("You have already used this lifeline")
        answer = input("Enter your answer (a, b, c or d): ")

def fiftyfifty():
    if fiftyfifty_help == 0:
        # pabaigti
        fiftyfifty_help += 1
    else:
        print("You have already used this lifeline")
        answer = input("Enter your answer (a, b, c or d): ")

def game():
    money = 0
    current_list = questions_list

    for i in range(14):
        question = random.choice(current_list)
        current_list.remove(question)
        print("Question for", payout[i+1],"\n"+question[0],"\na) ",question[1],"\nb) ",question[2],"\nc) "+question[3],"\nd) ",question[4])
        answer = input("Enter your answer (a, b, c or d): ")

        if answer.lower() == "web":
            web()

        if answer == "50/50":
            fiftyfifty()

        if answer.lower() == "quit":
            if money > 0:
                print("Congratulations! You won:",money)
                break
            else:
                print("You didn't win anything. Try again.")
                break 
        elif answer.lower() == question[5]:
            money = payout[i+1]
            print ("Your answer is correct!\n")
        else:
            if money < payout[5]:
                print("You lost. Correct answer is", question[5])
                break
            elif money < payout[10]:
                print("Congratulations! You won:", payout[5])
                break
            else:
                print("Congratulations! You won:", payout[10])
                break
    print("Congratulations! You are a Millionaire!!!)           


start_point = input(player_name.capitalize()+", please enter 'start' to start the game: ")
if start_point.lower() == "start":
    game()
else:
    start_point = input(player_name.capitalize()+", please enter:'start' to start the game: ")    


#statistics file read write and open
