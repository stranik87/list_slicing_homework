def main(list1):
    """
    A list of several elements is given. Return the three elements from the beginning.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    x = list1[:3]
    return x

print(main(['a', 'b', 'c', 'd']))