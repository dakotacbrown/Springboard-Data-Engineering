def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    repeated = ''
    if isinstance(num, int) and num >= 0:
        while num > 0:
            repeated = repeated + str(phrase)
            num -= 1
    else:
        return None
    return repeated

## Seems better timewise
##  if not isinstance(num, int) or num < 0:
##      return None
##  return phrase * num