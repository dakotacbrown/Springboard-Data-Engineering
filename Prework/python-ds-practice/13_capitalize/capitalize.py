def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    lst = list(phrase)
    lst[0] = lst[0].capitalize()

    return ''.join(lst)