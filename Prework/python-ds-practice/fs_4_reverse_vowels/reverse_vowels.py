def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    wordlst = list(s)
    palindrome = list("".join([letter for letter in wordlst[::-1] if letter in "aeiouAEIOU"]))
    for iterator, i in enumerate(wordlst):
        if i in 'aeiouAEIOU':
            wordlst.pop(iterator)
            wordlst.insert(iterator, palindrome[0])
            palindrome.pop(0)
    return "".join(wordlst)