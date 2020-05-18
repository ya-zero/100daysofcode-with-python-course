def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n > 0:
       
       return (string[n:]+string[0:n])
    return  (string[-abs(n):]+string[0:len(string)-abs(n)])

print (rotate('pybites loves julian and bob!',-15))
