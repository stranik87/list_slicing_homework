def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    x = list1 + list1[::-1]
    return x

print(main(['a', 'b', 'c', 'd']))