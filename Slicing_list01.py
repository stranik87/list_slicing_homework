def main(numbers):
    """
    A list called numbers is given. Return the items in the even index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    x = numbers[::2]
    return x

print(main([1, 2, 3, 4, 5]))