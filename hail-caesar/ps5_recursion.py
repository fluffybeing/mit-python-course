# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    ### TODO.
    if aStr == '':
        return aStr
    else:
        return aStr[-1:] + reverseString(aStr[:-1])

#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    ###TODO
    if x is '':
        return True
    elif word is '':
        return False
    if x in word:
        return True
    if x[0] == word[0]:
        return x_ian(x[1:], word[1:])
        return True
    else:
        return x_ian(x, word[1:])
        return False

#
# Problem 5: Typewriter

def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text) <= lineLength:
            return text
    if text[lineLength]== ' ':
            return text[:lineLength+1]+ '\n' + insertNewlines(text[lineLength:], lineLength)
    else:
            tmp = text.find(" ", lineLength, len(text))
            return text[:tmp+1]+ '\n' + insertNewlines(text[tmp:], lineLength)
        
