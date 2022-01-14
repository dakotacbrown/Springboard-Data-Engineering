def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    newPhrase = list(phrase)

    for iterator, letter in enumerate(newPhrase):
        swap_upper = to_swap.isupper()
        swap_lower = to_swap.islower()
        letter_upper = letter.isupper()
        letter_lower = letter.islower()
        if letter.lower() == to_swap.lower():
            if swap_upper:
                if letter_upper:
                    newPhrase.pop(iterator)
                    newPhrase.insert(iterator, to_swap.lower())
                elif letter_lower:
                    newPhrase.pop(iterator)
                    newPhrase.insert(iterator, to_swap.upper())
            elif swap_lower:
                if letter_lower:
                    newPhrase.pop(iterator)
                    newPhrase.insert(iterator, to_swap.upper())
                elif letter_upper:
                    newPhrase.pop(iterator)
                    newPhrase.insert(iterator, to_swap.lower())
                    
    return ''.join(newPhrase)