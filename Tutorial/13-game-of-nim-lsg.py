# to be able to specify type annotations and static type checker mypy
from typing import List, Any, Set, Dict, Tuple, Optional
from functools import reduce
from operator import __xor__, __or__
from random import randint

"""
This game of NIM consists of 16 matches in 4 rows arranged as follows:

          1-   |
          2-   | | |
          3-   | | | | |
          4-   | | | | | | |

The players alternately pick a certain number of matches (at least 1) in only one row,
and the one who takes the last matches wins.

A winning game (for the player who has to play) is a game for which the result of
the Vertical XOR is Non False (True value are in the result of the Vertical XOR),
otherwise it is a loosing game (only False value in the result of the Vertical XOR).
From any winning game the current player can obtain a loosing game for the other player ;-).
From any loosing game one obtains a winning game for the other player what ever one does :-(.

         Rows  Matches        Binary Conversion
          1-                        ===>          F F F
          2-   | | |                ===>          F T T
          3-   | | | | |            ===>          T F T
          4-   | | | | | | |        ===>          T T T

                                                  | | |   Vertical XOR
                                                  V V V

                                                  F T T   Non False = "winning"
          F = False, T = True

The Game is represented by a list of integers and the Binary Convertion is done with a 
list of booleans. A the beginning the pyramid of matches, the Rows of a Game is [1,3,5,7] for example.
"""


def int_to_bin_three_bit(matches: int) -> List[bool] :
    """
    Converts an integer into binary over 3 bits (modulo 8).
    Each bit is represented by a boolean. It is more logical to represent
    the bits with true/false values rather than with 0/1 integer value.
    For the sake of simplicity every constant is converted explicitly.
    :param matches: the number of matches per row to convert into binary
    :return: the list of booleans, each boolean represents a bit (Most Significant Bit on the left)
    """
    bin_converter = {
        0: [False, False, False],    # 000
        1: [False, False, True],     # 001
        2: [False, True,  False],    # 010
        3: [False, True,  True],
        4: [True , False, False],
        5: [True,  False, True],
        6: [True,  True,  False],    # 110
        7: [True,  True,  True]      # 111
    }
    dic_length = len(bin_converter)  # how many entries in the dictionary
    matches = matches % dic_length   # modulo avoids out of bounds
    return bin_converter[matches]


def game_to_bin(game : List[int]) -> List[List[bool]]:
    """
    Converts a game into binary, i.e. each row of the game is converted into binary,
    it means that a list of list of booleans is required (each element of the outer list
    is a row converted into binary).
    :param game: the game to convert
    :return: a list of list of Booleans
    """
    return list(map(int_to_bin_three_bit, game))
    # equivalent to
    # converted_game = []
    # for line in game:
    #     converted_game.append(int_to_bin_three_bit(line))
    # return converted_game


def row_to_col(lst_lst: List[List[Any]]) -> List[List[Any]]:
    """
    Transforms a list of lists into another list of lists as follows
       [x1,x2,x3],[y1,y2,y3], ...] --> [[x1,y1,...],[x2,y2,...],[x3,y3,...]]
    The function assumes that all the lists in the input list have the same number of
    elements (this assumption is important for the termination of the recursion).
    This implementation takes advantage of map function and recursion and which makes the
    the implemention easer to develop and understand.
    :param lst_lst: the list of lists (row - col) to transform
    :return: the transformed list of lists (col - row)
    """
    head = (lambda x: x[0])
    tail = (lambda x: x[1:])
    if not lst_lst or not head(lst_lst):  # c.f. the remark about recursion termination
        return []
    else:
        return [list(map(head, lst_lst))] + (row_to_col(list(map(tail, lst_lst))))


def is_winning(game: List[int]) -> bool:
    """
    Determines whether a game is a "winning" game or not.  A game is winning
    if the result of the Vertical XOR contains some bits set to True.
    :param game: the game to check
    :return: True if winning, False otherwise
    """
    # performs the Vertical XOR by reducing as list of bool (lst) with xor lambda
    reduce_xor = (lambda lst: reduce(__xor__, lst, False))

    # converts game into binary and the converts/permutes the row and col
    game_bin_row_col = row_to_col(game_to_bin(game))

    # performs Vertical XOR on every column
    res_vert_xor = list(map(reduce_xor, game_bin_row_col))

    return reduce(__or__, res_vert_xor, False)


def is_finished(game: List[int]) -> bool :
    """
    Determines if a game is over by doing the sum of the rows.
    A game is over whenever there is no matches anymore.
    :param game: the current game
    :return: True is the game is over, False otherwise.
    """
    return sum(game) == 0


def remove_matches(game: List[int], row: int, matches: int) -> None:
    """
    Removes some matches on a given row of a given game.
    This function is not a pure function because it changes the matches of the game parameter.
    :param game: the game to modify
    :param row: the row on which the matches have to be removed
    :param matches: the number of matches to remove
    """
    game[row] -= matches


def display_game(game: List[int]) -> None:
    """
    Displays the current game as rows of matches.
    For every row the row number is displayed followed by the matches.
    :param game: the game to display
    """
    print()
    row = 0
    while(row < len(game)):
        print(row+1, end="- ")
        m = game[row]
        while m > 0:
            print("| ", end='')
            m -= 1
        row += 1
        print()
    print()


def remove_one_match_random(game: List[int]) -> None:
    """
    Finds randomly a row on which one match can be removed.
    The game parameter is updated.
    :param game:
    """
    # a way to simulate REPEAT ... UNTIL cond
    while True:
        row = randint(1, len(game))
        if game[row-1] >= 1:
            game[row-1] -= 1
            break
    print("1 match on row {} has been removed.".format(row))


def remove_from_winning(game: List[int]) -> None:
    """
    Find randomly some matches and a row to provide a loosing game to the other player.
    The game parameter is updated.
    :param game: the current game
    """
    while True:
        game_copy = game.copy()
        row = randint(1, len(game_copy))
        if game_copy[row-1] < 1:
            continue
        matches = randint(1, game_copy[row-1])
        remove_matches(game_copy, row - 1, matches)
        if not is_winning(game_copy):
            remove_matches(game, row - 1, matches)
            break
    print("{} matches on row {} have been removed.".format(matches, row))

def computer_turn(game: List[int]) -> None:
    """
    The strategy is as follows:
    If the current game is winning then find a row and some matches to remove such that a loosing
    game can be provided to the other player. It is guaranteed that from a winning game a loosing
    game exist.
    If the current game is loosing we cannot always remove matches on a row to find a losing game.
    Actually only one match is randomly removed to maximise the mistakes of the other player.
    :param game: current game
    """
    if is_winning(game):
        remove_from_winning(game)
    else:
        remove_one_match_random(game)


def user_turn(game: List[int]) -> None:
    """
    Ask the player on which row and how many matches he/she wants to remove.
    The game parameter is updated.
    :param game: the current game
    """
    while True:
        matches = int(input("Enter the number of matches to remove            : "))
        if matches < 1:
            print("   You must remove at least one match")
            continue
        row     = int(input("Enter the row on which matches have to be removed: "))
        # verify that row and matches are OK (not out-of-bounds)
        if row < 1 or row > len(game):
            print("   The row {} is out of bound".format(row))
            continue
        if matches > game[row-1]:
            print("   There are not enough matches on row {}.".format(row))
            continue
        break
    remove_matches(game, row-1, matches)


def main() -> None:
    """ Main program of the game of Nim. """
    # the current game is initialized with 1, 3, 5, 7 matches on the 4 rows.
    game: List[int] = [1, 3, 5, 7]

    print("\nGame of Nim")
    print(  "===========")
    display_game(game)
    start = input("Do you want to start? (y/n) ")
    print()
    if start=="y" or start=="Y":
        print("Your turn")
        user_turn(game)
        display_game(game)
    while True:
        print("My turn")
        computer_turn(game)
        display_game(game)
        if is_finished(game):
            print("I WON\n")
            break
        print("Your turn")
        user_turn(game)
        display_game(game)
        if is_finished(game):
            print("YOU WON\n")
            break


if __name__ == '__main__':
    main()
