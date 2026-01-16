#!/usr/bin/python3
def main():
    import hidden_4

    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    main()
