import logging

logger = logging.getLogger(__name__)


def armenian_latinisation(input_string):
    # For example, you can use Flask to create a route that accepts POST requests with user input

    wordChars = list(input_string)

    # exception
    if wordChars[0] == "o" and wordChars[1] == "d" and len(wordChars) == 2:
        wordChars = ["օդ"]

    for index, _ in enumerate(wordChars):
        # Capitalize chars

        if (
            index < len(wordChars) - 1
            and wordChars[index] == "T"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "Թ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "T"
            and wordChars[index + 1] == "s"
        ):
            wordChars[index] = "Ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "Z"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "Ծ"
            wordChars[index + 1] = ""

        elif index < len(wordChars) - 1 and (
            wordChars[index] == "t" and wordChars[index + 1] == "z"
        ):
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""

        elif index < len(wordChars) - 1 and (
            wordChars[index] == "g" and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "T"
            and wordChars[index + 1] == "z"
        ):
            wordChars[index] = "Ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "G"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "Ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "R"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "Ր"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "O"
            and wordChars[index + 1] == "o"
        ):
            wordChars[index] = "Ու"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "O"
            and wordChars[index + 1] == "w"
        ):
            wordChars[index] = "Ու"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "o"
            and wordChars[index + 1] == "o"
        ):
            wordChars[index] = "ու"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "O"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "O"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "o"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "o"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "G"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "Ղ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "g"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "ղ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "K"
            and wordChars[index + 1] == "h"
        ):  # 13
            wordChars[index] = "Խ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "D"
            and wordChars[index + 1] == "z"
        ):  # 17
            wordChars[index] = "Ձ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "S"
            and wordChars[index + 1] == "h"
        ):  # 24
            wordChars[index] = "Շ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "C"
            and wordChars[index + 1] == "h"
        ):  # 19
            wordChars[index] = "Ճ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "Z"
            and wordChars[index + 1] == "H"
        ):
            wordChars[index] = "Ժ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "Z"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "Ժ"
            wordChars[index + 1] = ""

        elif wordChars[index] == "@":
            wordChars[index] = "ը"

        # lower case chars
        elif index < len(wordChars) - 1 and (
            wordChars[index] == "t"
            and wordChars[index + 1] == "z"
            and wordChars[index + 2] == "’"
        ):
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""
            wordChars[index + 2] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "z"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "o"
            and wordChars[index + 1] == "o"
        ):
            wordChars[index] = "ու"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "t"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "թ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "t"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "թ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "T"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "Թ"
            wordChars[index + 1] = ""

        elif index < len(wordChars) - 1 and (
            wordChars[index] == "t" and wordChars[index + 1] == "s"
        ):  # 14
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""

        elif index < len(wordChars) - 1 and (
            wordChars[index] == "c" and wordChars[index + 1] == "’"
        ):  # 14
            wordChars[index] = "ծ"
            wordChars[index + 1] = ""

        elif index < len(wordChars) - 1 and (
            wordChars[index] == "C" and wordChars[index + 1] == "’"
        ):  # 14
            wordChars[index] = "Ծ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "r"
            and wordChars[index + 1] == "’"
        ):
            wordChars[index] = "ռ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "z"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "ժ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "k"
            and wordChars[index + 1] == "h"
        ):
            wordChars[index] = "խ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "d"
            and wordChars[index + 1] == "z"
        ):  # 17
            wordChars[index] = "ձ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "g"
            and wordChars[index + 1] == "h"
        ):  # 18
            wordChars[index] = "ղ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "s"
            and wordChars[index + 1] == "h"
        ):  # 24
            wordChars[index] = "շ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "c"
            and wordChars[index + 1] == "h"
        ):  # 26
            wordChars[index] = "չ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "e"
            and wordChars[index + 1] == "v"
        ):  # 38
            wordChars[index] = "և"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "v"
            and wordChars[index + 1] == "o"
        ):  # 25
            wordChars[index] = "ո"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "e"
            and wordChars[index + 1] == "’"
        ):  # 7
            wordChars[index] = "է"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "e"
            and wordChars[index + 1] != "’"
        ):  # 5
            wordChars[index] = "ե"

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "u"
            and wordChars[index + 1] == "’"
        ):  # 8
            wordChars[index] = "ը"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "y"
            and wordChars[index + 1] == "a"
        ):  # 8
            wordChars[index] = "ը"

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "U"
            and wordChars[index + 1] == "’"
        ):  # 8
            wordChars[index] = "Ը"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "U"
            and wordChars[index + 1] == "’"
        ):  # 8
            wordChars[index] = "Ը"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "t"
            and wordChars[index + 1] == "’"
        ):  # 9
            wordChars[index] = "թ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "j"
            and wordChars[index + 1] == "’"
        ):  # 28
            wordChars[index] = "ճ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "p"
            and wordChars[index + 1] == "’"
        ):  # 36
            wordChars[index] = "փ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "E"
            and wordChars[index + 1] != "’"
        ):  # 5
            wordChars[index] = "Ե"

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "E"
            and wordChars[index + 1] == "’"
        ):  # 7
            wordChars[index] = "Է"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "J"
            and wordChars[index + 1] == "’"
        ):  # 28
            wordChars[index] = "Ճ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars)
            and wordChars[index] == "R"
            and wordChars[index + 1] == "’"
        ):  # 29
            wordChars[index] = "Ռ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "P"
            and wordChars[index + 1] == "’"
        ):  # 36
            wordChars[index] = "Փ"
            wordChars[index + 1] = ""

        elif (
            index < len(wordChars) - 1
            and wordChars[index] == "P"
            and wordChars[index + 1] == "h"
        ):  # 36
            wordChars[index] = "Փ"
            wordChars[index + 1] = ""

        elif wordChars[index] == "r":  # 33
            wordChars[index] = "ր"

        elif wordChars[index] == "L":  # 12
            wordChars[index] = "Լ"

        elif wordChars[index] == "x":
            wordChars[index] = "խ"

        elif wordChars[index] == "X":
            wordChars[index] = "Խ"

        # ??????
        elif wordChars[index] == "y":
            wordChars[index] = "ը"

        elif wordChars[index] == "z":  # 6
            wordChars[index] = "զ"

        elif wordChars[index] == "a":  # 1
            wordChars[index] = "ա"

        elif wordChars[index] == "b":  # 2
            wordChars[index] = "բ"

        elif wordChars[index] == "g":  # 3
            wordChars[index] = "գ"

        elif wordChars[index] == "d":  # 4
            wordChars[index] = "դ"

        elif wordChars[index] == "o":
            wordChars[index] = "ո"

        elif wordChars[index] == "U":
            wordChars[index] = "Ու"

        elif wordChars[index] == "u":
            wordChars[index] = "ու"

        elif wordChars[index] == "Z":  # 6
            wordChars[index] = "Զ"

        elif wordChars[index] == "i":  # 11
            wordChars[index] = "ի"

        elif wordChars[index] == "l":  # 12
            wordChars[index] = "լ"

        elif wordChars[index] == "k":  # 15
            wordChars[index] = "կ"

        elif wordChars[index] == "h":  # 16
            wordChars[index] = "հ"

        elif wordChars[index] == "m":  # 21
            wordChars[index] = "մ"

        #!!!!
        elif wordChars[index] == "y":  # 22
            wordChars[index] = "յ"

        elif wordChars[index] == "n":  # 23
            wordChars[index] = "ն"

        elif wordChars[index] == "u":  # 35
            wordChars[index] = "ո"

        elif wordChars[index] == "p":  # 27
            wordChars[index] = "պ"

        elif wordChars[index] == "W":  # 27
            wordChars[index] = "Ւ"

        elif wordChars[index] == "w":
            wordChars[index] = "ւ"

        elif wordChars[index] == "R":  # 30
            wordChars[index] = "Ռ"

        elif wordChars[index] == "j":  # 28
            wordChars[index] = "ջ"

        elif wordChars[index] == "v":  # 31
            wordChars[index] = "վ"

        elif wordChars[index] == "t":  # 32
            wordChars[index] = "տ"

        elif wordChars[index] == "c":  # 34
            wordChars[index] = "ց"

        elif wordChars[index] == "q":  # 37
            wordChars[index] = "ք"

        elif wordChars[index] == "f":  # 40
            wordChars[index] = "ֆ"

        # Higher case letters here.

        elif wordChars[index] == "A":  # 1
            wordChars[index] = "Ա"

        elif wordChars[index] == "B":  # 2
            wordChars[index] = "Բ"

        elif wordChars[index] == "G":  # 3
            wordChars[index] = "Գ"

        elif wordChars[index] == "D":  # 4
            wordChars[index] = "Դ"

        elif wordChars[index] == "J":  # 10
            wordChars[index] = "Ջ"

        elif wordChars[index] == "I":  # 11
            wordChars[index] = "Ի"

        elif wordChars[index] == "K":  # 15
            wordChars[index] = "Կ"

        elif wordChars[index] == "H":  # 16
            wordChars[index] = "Հ"

        elif wordChars[index] == "M":  # 21
            wordChars[index] = "Մ"

        # !!!
        elif wordChars[index] == "Y":  # 22
            wordChars[index] = "Ը"  # Ը

        elif wordChars[index] == "N":  # 23
            wordChars[index] = "Ն"

        elif wordChars[index] == "P":  # 27
            wordChars[index] = "Պ"

        elif wordChars[index] == "V":  # 31
            wordChars[index] = "Վ"

        elif wordChars[index] == "T":  # 32
            wordChars[index] = "Տ"

        elif wordChars[index] == "C":  # 34
            wordChars[index] = "Ց"

        elif wordChars[index] == "Q":  # 37
            wordChars[index] = "Ք"

        elif wordChars[index] == "O":  # 39
            wordChars[index] = "Ո"

        elif wordChars[index] == "F":  # 40
            wordChars[index] = "Ֆ"

        elif wordChars[index] == "S":  # 30
            wordChars[index] = "Ս"

        elif wordChars[index] == "s":
            wordChars[index] = "ս"

        elif wordChars[index] == "T":
            wordChars[index] = "Տ"

        elif wordChars[index] == "t":
            wordChars[index] = "տ"

    wordChars = [i for i in wordChars if i]

    return "".join(wordChars)
