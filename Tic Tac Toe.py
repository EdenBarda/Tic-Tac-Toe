# Eden Barda, 208932202

import random


def print_game():
    for i in game:
        for j in i:
            print(j, end=" ")
        print("")


def computer_turn():
    """send to recursive function that calculates
    the best turn, then she "beat the crap out of you"."""
    scores = []
    if turn_number == 1:
        if not extreme_case():  # the one case that the recursion didn't solve.
            for i in range(9):
                scores.append(theoretical_o_turn(i, 1))
            max_index = scores.index(max(scores))
            the_row = (max_index // 3)
            the_column = (max_index % 3)
            if game[the_row][the_column] == "e":
                game[the_row][the_column] = "O"
            else:
                random_computer_turn()

    else:
        for i in range(9):
            scores.append(theoretical_o_turn(i, 1))
        max_index = scores.index(max(scores))
        the_row = (max_index // 3)
        the_column = (max_index % 3)
        if game[the_row][the_column] == "e":
            game[the_row][the_column] = "O"
        else:
            random_computer_turn()


def theoretical_o_turn(index, stage_value):
    """checks what would happen if the computer put O in the "index" place."""
    the_row = (index // 3)
    the_column = (index % 3)
    if game[the_row][the_column] != "e":
        return stage_value
    game[the_row][the_column] = "O"
    if is_computer_win():
        game[the_row][the_column] = "e"
        return stage_value * 10
    the_sum = 0
    for i in range(9):
        the_sum += stage_value * theoretical_x_turn(i, stage_value / 3)
    game[the_row][the_column] = "e"
    return the_sum


def theoretical_x_turn(index, stage_value):
    """checks what would happen if the user will put X in the "index" place."""
    the_row = (index // 3)
    the_column = (index % 3)
    if game[the_row][the_column] != "e":
        return 1
    game[the_row][the_column] = "X"
    if is_user_win():
        game[the_row][the_column] = "e"
        return stage_value * (-10)
    the_sum = 0
    for i in range(9):
        the_sum += stage_value * theoretical_o_turn(i, stage_value / 3)
    game[the_row][the_column] = "e"
    return the_sum


def extreme_case():
    """handles a single extreme case where the user does a trick."""
    if game[0][0] == "X":
        game[2][2] = "O"
        return True
    if game[0][2] == "X":
        game[2][0] = "O"
        return True
    if game[2][0] == "X":
        game[0][2] = "O"
        return True
    if game[2][2] == "X":
        game[0][0] = "O"
        return True
    return False


def random_computer_turn():
    """the function choose randomly O place in the computer's turn."""
    turn_is_done = False
    while not turn_is_done:
        x = random.randint(0, 8)
        the_row = (x // 3)
        the_column = (x % 3)
        if game[the_row][the_column] == "e":
            game[the_row][the_column] = "O"
            turn_is_done = True
        else:
            continue


def is_computer_win():
    """the function checks if there is a line or diagonal that is all O's."""
    is_first_diagonal = True
    is_second_diagonal = True
    is_column = False
    is_row = False
    for i in range(3):
        # checks if all the organs in the place (i)x(i) are O.
        is_first_diagonal = game[i][i] == "O" and is_first_diagonal

        # checks if all the organs in the place (2-i)x(i) are O.
        is_second_diagonal = game[2 - i][i] == "O" and is_second_diagonal

        # checks if there is a line with all O's.
        is_row = game[i] == ["O", "O", "O"] or is_row

        # checks if there is a column with all O's.
        is_column = (game[0][i] == game[1][i] == game[2][i] == "O") or is_column

    # if there is something that is true it means that the computer won.
    return is_first_diagonal or is_second_diagonal or is_row or is_column


def is_user_win():
    """the function checks if there is a line or diagonal that is all X's."""
    is_first_diagonal = True
    is_second_diagonal = True
    is_column = False
    is_row = False
    for i in range(3):
        # checks if all the organs in the place (i)x(i) are X.
        is_first_diagonal = game[i][i] == "X" and is_first_diagonal

        # checks if all the organs in the place (2-i)x(i) are X.
        is_second_diagonal = game[2 - i][i] == "X" and is_second_diagonal

        # checks if there is a line with all X's.
        is_row = game[i] == ["X", "X", "X"] or is_row

        # checks if there is a column with all X's.
        is_column = (game[0][i] == game[1][i] == game[2][i] == "X") or is_column

    # if there is something that is true it means that the user won.
    return is_first_diagonal or is_second_diagonal or is_row or is_column


"""The game itself."""
turn_number = 0
game = [["e", "e", "e"], ["e", "e", "e"], ["e", "e", "e"]]
print_game()

# the maximum turn for the user is 5 (if no one wins up to them).
while turn_number < 5:
    num = input("Your turn: ")

    # if the user input something that is not 1 to 9 number,
    # the program ask him again to enter a number.
    if "1" <= num <= "9" and len(num) == 1:
        num = int(num) - 1
        row = (num // 3)
        column = (num % 3)
        if game[row][column] == "e":
            game[row][column] = "X"
            turn_number += 1
            if is_user_win():
                print_game()
                print("You win")
                break

            # if turn_number == 5 there is no space in the game board.
            if turn_number < 5:
                computer_turn()
            if is_computer_win():
                print_game()
                print("You lose")
                break
            print_game()
            if turn_number == 5:
                print_game()
                print("It's a draw")
        else:
            continue
    else:
        continue
