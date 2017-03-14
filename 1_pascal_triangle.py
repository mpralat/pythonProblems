def get_pascal(row, position):
    '''
    Given the number of row and position, calculates the value of the Pascal triangle.
    '''
    if (position < 0 or row < 0) or (position > row):
        print("Please check the provided values!")
        return None
    if position == 0 and row == 0:
        return 1
    elif position == 0:
        return get_pascal(row - 1, position)
    elif position == row:
        return get_pascal(row - 1, position - 1)
    else:
        return get_pascal(row - 1, position - 1) + get_pascal(row - 1, position)


# Check
for i in range(7):
    print(get_pascal(6, i))
