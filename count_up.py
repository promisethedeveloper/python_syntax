def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    x = list(range(start, stop+1))
    for y in x:
        print(y)


count_up(5, 7)   
count_up(2, 20)     
