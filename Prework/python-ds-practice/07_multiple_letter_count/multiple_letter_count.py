def multiple_letter_count(phrase):

    dictionary = {}

    for letter in phrase:
        dictionary[letter] = phrase.lower().count(letter.lower())

    return dictionary

    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """