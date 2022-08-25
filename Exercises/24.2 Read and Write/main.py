import os


def main():
    with open(file=os.path.join(os.sys.path[0], "my_file.txt"), mode="a") as file:
        file.write("\nA")


if __name__ == "__main__":
    main()
