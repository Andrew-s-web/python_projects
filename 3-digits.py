import random as r

incorr_digit = " "
partly_right_digit = "W"
right_digit = "C"
tryings = 0
user_guess = 0
right_guess = r.randint(100, 1000)

print("Я загадал число, состоящее из 3 цифр, сможете угадать за 7 попыток?")
user_playing = input("Введите 'да' или 'нет' \n")


def game():
    global user_guess, tryings
    tryings = 0
    user_guess = ""
    print(
        "Каждый раз когда вы угадываете число, если в нем есть такая цифра, но она стоит на другом месте, я буду писать"
        "символ 'W' под этой цифрой \n"
        "Когда цифра верна и стоит на том же месте, что и в цисле, мною загаданном я буду писать символ - 'C' под этой "
        "цифрой")

    while right_guess != user_guess and tryings < 8:
        hint_str = ""
        if tryings > 0:
            print(f"У вас осталось {7 - tryings} попыток")
        while True:
            user_guess = (input("Введите целое число \n"))
            if user_guess.isdigit():
                break
        print(user_guess)
        if user_guess != right_guess:
            for i in range(3):
                if str(user_guess)[i] == str(right_guess)[i]:
                    hint_str += right_digit
                elif str(user_guess)[i] != str(right_guess)[i] and str(user_guess)[i] in str(right_guess):
                    hint_str += partly_right_digit
                else:
                    hint_str += incorr_digit
        else:
            print(f"Поздравляю! Вы угадали число с {tryings} попыток")

        tryings += 1
        print(hint_str)

    game_again = input("Хотите сыграть еще?\n"
                       "Напишите 'да' или 'нет'\n")
    if game_again.lower() == 'да':
        game()
    else:
        print("До встречи!")


if tryings > 7:
    print("Игра окончена")
    game_again = input("Вы не смогли угадать число за 7 попыток, хотите сыграть еще раз?\n"
                       "Напишите 'да' или 'нет'\n")
    if game_again.lower() == 'да':
        game()
    else:
        print("До встречи!")

if user_playing.lower() == 'да':
    game()
else:
    print("Жаль, что вы уходите")
