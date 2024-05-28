def read_file():
    with open("file1.txt", "r") as f:
        text_from_file = f.read()
        print(text_from_file)


def write_file():
    with open("file2.txt", "a") as f:
        f.write("1\n")


if __name__ == "__main__":
    read_file()
    write_file()
