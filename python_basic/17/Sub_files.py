print(f"Sub file is:{__name__}")


def input_name():
    name = input("Nhap vao ten cua ban: ")
    print(f"Ten cua ban la {name}")


def input_age():
    age = input("Nhap vao tuoi cua ban: ")
    print(f"Tuoi cua ban la {age}")


def main():
    input_name()
    input_age()


if __name__ == "__main__":
    main()
