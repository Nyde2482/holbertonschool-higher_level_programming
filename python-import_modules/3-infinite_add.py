#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_count = len(sys.argv) - 1
    print(sum(int(sys.argv[i]) for i in range(1, args_count + 1)))
