def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    x = list1[::3]
    return x

print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4]))