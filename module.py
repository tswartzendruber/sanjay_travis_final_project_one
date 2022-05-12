def one(n) -> int:
    """
    Function to add an integer and the integer one less than it
    :param n: Input number
    :return: The sum of the integer and the integer one less than it
    """
    if type(n) == int:
        if n > 0:
            if n == 1:
                return 1
            else:
                return n + one(n-1)
        else:
            raise ValueError('Input not positive')
    else:
        raise TypeError('Input not an integer')


def two(num, power) -> int:
    """
    Function to take the first integer to the power of the second integer
    :param num: First integer (base)
    :param power: Second integer (exponent)
    :return: 'base' to the power of 'exponent'
    """
    if type(num) == int and type(power) == int:
        if num > 0 and power > 0:
            if num == 1:
                return 1
            elif power == 1:
                return num
            else:
                return num * two(num, power-1)
        else:
            raise ValueError('Input not positive')
    else:
        raise TypeError('Input not an integer')


def three(n) -> str:
    """
    Function to display the integer followed by the next descending integers down to 1
    :param n: Starting number that was input
    :return: String of first integer followed by the next descending integers down to 1
    """
    if type(n) == int:
        if n > 0:
            if n == 1:
                return '1'
            else:
                return f'{n} {three(n - 1)}'
        else:
            raise ValueError('Input not positive')
    else:
        raise TypeError('Input not an integer')
