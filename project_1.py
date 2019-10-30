import webbrowser
import random
import json
import threading
from time import sleep
import datetime
import sys

payout = [
    100,
    200,
    300,
    500,
    1000,
    2000,
    4000,
    8000,
    16000,
    32000,
    64000,
    125000,
    250000,
    500000,
    1000000,
]
answer_value = {"a": 1, "b": 2, "c": 3, "d": 4}
time_limit = 30

with open("questions_list.json", "r", encoding="utf-8") as myfile:
    data = myfile.read()
questions_list = json.loads(data)


def timer():
    global my_timer
    my_timer = (time_limit * 60) + 1
    for i in range(my_timer):
        my_timer -= 1
        sleep(1)


def game():
    money = 0
    current_list = questions_list
    web_help = 0
    fiftyfifty_help = 0

    for i in range(15):
        question = random.choice(current_list)
        current_list.remove(question)
        print("Time left:", str(datetime.timedelta(seconds=my_timer)))
        print("Question for", payout[i], "\n\n" + question[0])
        sleep(0.3)
        print("a) ", question[1])
        sleep(0.3)
        print("b) ", question[2])
        sleep(0.3)
        print("c) ", question[3])
        sleep(0.3)
        print("d) ", question[4], "\n")
        sleep(0.3)
        answer = input("Enter your answer (a, b, c or d): ")
        if my_timer == 0:
            print("Out of time")
            answer = "quit"

        while answer.lower() not in ["a", "b", "c", "d", "quit"]:
            if my_timer == 0:
                print("Out of time")
                answer = "quit"
            elif answer == "web":
                if web_help == 0:
                    webbrowser.open("http://google.com", new=2)
                    web_help += 1
                    answer = input("Enter your answer (a, b, c or d): ")
                else:
                    print("Time left:", str(datetime.timedelta(seconds=my_timer)))
                    print("You have already used this lifeline")
                    answer = input("Enter your answer (a, b, c or d): ")
            elif answer == "50/50":
                if fiftyfifty_help == 0:
                    random_list = [1, 2, 3, 4]
                    random_list.remove((answer_value[question[5]]))
                    random_list.remove(random.choice(random_list))
                    question[random_list[0]] = ""
                    question[random_list[1]] = ""
                    print(str(datetime.timedelta(seconds=my_timer)))
                    print("Question for", payout[i], "\n\n" + question[0])
                    sleep(0.5)
                    print("a) ", question[1])
                    sleep(0.5)
                    print("b) ", question[2])
                    sleep(0.5)
                    print("c) ", question[3])
                    sleep(0.5)
                    print("d) ", question[4], "\n")
                    sleep(0.5)
                    fiftyfifty_help += 1
                    answer = input("Enter your answer (a, b, c or d): ")
                else:
                    print("Time left:", str(datetime.timedelta(seconds=my_timer)))
                    print("You have already used this lifeline")
                    answer = input("Enter your answer (a, b, c or d): ")

            else:
                print("Time left:", str(datetime.timedelta(seconds=my_timer)))
                print("Unrecognized answer")
                answer = input("Enter your answer (a, b, c or d): ")

        if answer.lower() == question[5]:
            money = payout[i]
            print("Your answer is correct!\n")
        elif answer.lower() == "quit":
            if money > 0:
                print("Congratulations! You won:", money)
                break
            else:
                print("You didn't win anything. Try again.")
                break
        elif money == payout[14]:
            print("Congratulations! You are a Millionaire!!!")
        else:
            if money < payout[4]:
                print("You lost. Correct answer is", question[5])
                break
            elif money < payout[9]:
                print("Congratulations! You won:", payout[4])
                break
            else:
                print("Congratulations! You won:", payout[9])
                break


player_name = input(
    'Welcome to the game "Who Wants to be a Millionaire"!\nPlease enter your name: '
)
print(
    player_name.capitalize() + ", you have",
    time_limit,
    'minutes to answer 15 questions and became a millionaire!\nYou have 2 guarantee points: 1000 and 32000\nThere are 2 lifelines:\n50/50 - enter "50/50"\nSearch in web - enter "web"\n\nEnter\'quit\' to end the game and take the money\n',
)
start_point = input(
    player_name.capitalize() + ", please enter 'start' to start the game: "
)
while start_point.lower() != "start":
    start_point = input(
        player_name.capitalize() + ", please enter 'start' to start the game: "
    )
timer_thread = threading.Thread(target=timer)
timer_thread.setDaemon(True)
timer_thread.start()
game()
sys.exit()

