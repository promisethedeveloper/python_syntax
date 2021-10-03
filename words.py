def print_upper_words(words):
    """This function will print all the words in the list, in a seperate and in uppercase"""

    for word in words:
        print(word.upper())



    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

def print_upper_words2(words):
    """This function will print all the words in the list, in a seperate and in uppercase"""

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())



def print_upper_words3(words, starting_words):
    """Print each word on a seperate line, uppercased, if starts with one of the starting_words

        >>> print_upper_words3(["Daddy", "Edward", "Bernard", "zope"],
        ...                   must_start_with=["B", "D"])
        BERNARD
        DADDY
    """
    for word in words:
        for letter in starting_words:
            if word.startswith(letter):
                print(word.upper())
                break