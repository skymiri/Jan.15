import pytest


def test_obscure_text():
    assert obscure_text("hello world") == "h3ll0 w0rld"
    assert obscure_text("indigo") == "1nd1g0"
    assert obscure_text("Apple") == "@ppl3"


def obscure_text(string):

    result = ""
    # Return the string with some letters replaced by numbers
    for char in string:
        if char == "o" or char == "O":
            result += "0"
        elif char == "e" or char == "E":
            result += "3"
        elif char == "i" or char == "I":
            result += "1"
        elif char == "a" or char == "A":
            result += "@"
        else:
            result += char

    return result


# if __name__ == "__main__":
#     string = input("Type a string : ")
#     result = obscure_text(string)
#     print(result)

# for i in text(len(string)):
#     if string[i] == "o":
#         string[i] = 0
#     elif string[i] == "O":
#         string[i] = 0
#     elif string[i] == "e":
#         string[i] = 3
#     elif string[i] == "E":
#         string[i] = 3
#     elif string[i] == "i":
#         string[i] = 1
#     elif string[i] == "I":
#         string[i] = 1
