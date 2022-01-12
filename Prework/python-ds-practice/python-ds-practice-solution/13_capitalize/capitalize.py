def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    # there's a built-in method for this!
    return phrase.capitalize()

    # or, doing it by hand:
    # return phrase[:1].upper() + phrase[1:]
