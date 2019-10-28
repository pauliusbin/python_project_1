import webbrowser
import random
import time
import json


questions_file = "questions1.txt"
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


player_name = input(
    'Welcome to the game "Who Wants to be a Millionaire"!\nPlease enter your name: '
)
print(
    player_name.capitalize() + ", you have",
    time_limit,
    'minutes to answer 15 questions and became a millionaire!\nYou have 2 guarantee points: 1000 and 32000\nThere are 2 lifelines:\n50/50 - enter "50/50"\nSearch in web - enter "web"\n\nEnter\'quit\' to end the game and take the money\n',
)


def game():
    money = 0
    current_list = questions_list
    web_help = 0
    fiftyfifty_help = 0

    for i in range(14):
        question = random.choice(current_list)
        current_list.remove(question)
        print(
            "Question for",
            payout[i],
            "\n" + question[0],
            "\na) ",
            question[1],
            "\nb) ",
            question[2],
            "\nc) " + question[3],
            "\nd) ",
            question[4],
        )
        answer = input("Enter your answer (a, b, c or d): ")
        while answer.lower() not in ["a", "b", "c", "d", "quit"]:
            if answer == "web":
                if web_help == 0:
                    webbrowser.open("http://google.com", new=2)
                    web_help += 1
                    answer = input("Enter your answer (a, b, c or d): ")
                else:
                    print("You have already used this lifeline")
                    answer = input("Enter your answer (a, b, c or d): ")
            elif answer == "50/50":
                if fiftyfifty_help == 0:
                    random_list = [1, 2, 3, 4]
                    random_list.remove((answer_value[question[5]]))
                    random_list.remove(random.choice(random_list))
                    question[random_list[0]] = ""
                    question[random_list[1]] = ""
                    print(
                        "Question for",
                        payout[i],
                        "\n" + question[0],
                        "\na) ",
                        question[1],
                        "\nb) ",
                        question[2],
                        "\nc) " + question[3],
                        "\nd) ",
                        question[4],
                    )
                    fiftyfifty_help += 1
                    answer = input("Enter your answer (a, b, c or d): ")
                else:
                    print("You have already used this lifeline")
                    answer = input("Enter your answer (a, b, c or d): ")
            elif answer.lower() == "quit":
                if money > 0:
                    print("Congratulations! You won:", money)
                    break
                else:
                    print("You didn't win anything. Try again.")
                    break
            else:
                print("Unrecognized answer")
                answer = input("Enter your answer (a, b, c or d): ")

        if answer.lower() == question[5]:
            money = payout[i]
            print("Your answer is correct!\n")
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


start_point = input(
    player_name.capitalize() + ", please enter 'start' to start the game: "
)
while start_point.lower() != "start":
    start_point = input(
        player_name.capitalize() + ", please enter 'start' to start the game: "
    )

game()
