import random


def game_result(option, user, dictionary, name):
    doubled_option = option * 2
    start = doubled_option.index(user) + 1
    end = doubled_option.index(user, start + 1)

    all_between = doubled_option[start:end]
    length = len(all_between)
    middle_index = length // 2
    stronger = all_between[:middle_index]
    weaker = all_between[middle_index:]

    if computer in stronger:
        print(f'Sorry, but the computer chose {computer}')
    elif computer in weaker:
        print(f'Well done. The computer chose {computer} and failed')
        dictionary[name] = int(dictionary[name])
        dictionary[name] += 100
    else:
        print(f'There is a draw {computer}')
        dictionary[name] = int(dictionary[name])
        dictionary[name] += 50


name = input('Enter your name:')
print(f'Hello, {name}')

names = []
numbers = []

with open("rating.txt") as f:
    for line in f:
        if line.strip():
            names.append(line.split()[0][0:])

with open("rating.txt") as f:
    for item in f.readlines():
        scores = ""
        for sub_item in item.split():
            if sub_item.isdigit():
                scores += sub_item
        numbers.append(scores)

dictionary = dict(zip(names, numbers))

option_user = input('Please enter the options: ')

if option_user != "":
    option = option_user.split(',')
else:
    option = ["rock", "paper", "scissors"]

print("Okay, let's start!")

while True:
    user = input("Your turn: ")
    computer = random.choice(option)
    if user == "!exit":
        print('Bye!')
        with open("rating.txt", 'w') as f:
            for key, value in dictionary.items():
                f.write('%s %s\n' % (key, value))
            f.close()
        break

    elif user == "!rating":
        for item in dictionary.keys():
            if item == name:
                print('Your rating: ' + str(dictionary[name]))
                break
        else:
            dictionary[name] = '0'
            print('Your rating: ' + dictionary[name])

    elif user in option:
        game_result(option, user, dictionary, name)

    else:
        print("Invalid input")






