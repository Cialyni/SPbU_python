from mergesort import sort

if __name__ == "__main__":
    try:
        array = list(map(int, input("Enter array that you want to sort.\n").split()))
        print("Result is:", *sort(array))
    except ValueError:
        print("!ERROR!\nEnter array of integer numbers using space as separator")
