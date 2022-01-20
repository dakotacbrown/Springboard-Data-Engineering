def vowel_count(phrase):

    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = {}
    for char in phrase.lower():
        if char in 'aeiou':
            if char not in vowels:
                vowels[char] = 1
            elif char in vowels:
                vowels[char] += 1
    return vowels

   ## method for counting all vowels not one at a time
   ## vowels = {}.fromkeys('aeiou',0)
   ## for char in phrase.lower():
   ##     if char in vowels:
   ##         vowels[char] += 1