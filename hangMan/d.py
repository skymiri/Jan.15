def print_hello(nb_repeat=1):
    for _ in range(nb_repeat):
        print("Hello")


def mainFunc(name, repeats):

    print_hello()
    print("Nice meet")

    if repeats > 0:
        print_hello()


if __name__ == "__main__":
    mainFunc("Tim")
    mainFunc("Sky", 10)
