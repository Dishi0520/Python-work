def main():
    x = get_int()
    print(f"x is {x}")

     
def get_int():
    while True:
        try:
            x = int(input("What's X? "))
            break
        except ValueError:
            print("X is not an integer")

    return x

main()