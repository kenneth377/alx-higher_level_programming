#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    
    ln = len(sys.argv)
    
    if ln > 2:
        print(ln-1, "arguments:")
        for i in range(1,ln):
            print("{}: {}".format(i, sys.argv[i]))

    elif ln == 2:
        print(1, "argument:")
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print(0, "arguments.")
