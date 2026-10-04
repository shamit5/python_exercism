def square(number):
    """A module for calculating the number of grains of wheat on a          chessboard."""
    if  not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1 )


def total():
    return (2 ** 64) - 1
