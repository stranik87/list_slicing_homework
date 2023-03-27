def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    x = list1[-1:0:-n]
    return x

print(main(['a', 'b', 'c', 'd', 'e', 'f'], -1))