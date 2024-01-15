def obscure_text():

    text = input("Type a string : ")
    string = " "
    # Return the string with some letters replaced by numbers
    for char in text:
        if char == "o" or char == "O":
            string += "0"
        elif char == "e" or char == "E":
            string += "3"
        elif char == "i" or char == "I":
            string += "1"
        else:
            string += char
        
    return string

result = obscure_text()
print(result)

def main():
    with open("/Users/sky/Desktop/ACIT2515/Jan.15/Unittest/demo2/demo.py", "w") as f:
        f.write(obscure_text())
        f.close()

    f = open("/Users/sky/Desktop/ACIT2515/Jan.15/Unittest/demo2/demo.py", "r")
    print(f.read())



if __name__ == "__main__":
    main()

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
