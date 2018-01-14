# Day 13/365 #AnAlgorithmAday2018
# Problem is from codefights
#
# Amend the sentence
#
#You have been given a string s, which is supposed to be a sentence. However, someone forgot to put spaces between the different words, #and for some reason they capitalized the first letter of every word. Return the sentence after making the following amendments:
#
#Put a single space between the words.
#Convert the uppercase letters to lowercase.
#Example
#
#For s = "CodefightsIsAwesome", the output should be
#amendTheSentence(s) = "codefights is awesome";
#For s = "Hello", the output should be
#amendTheSentence(s) = "hello".
########################################################################################################################

def amendTheSentence(s):

    result = ""

    for char in s:
        if char.isupper():
            result += " " + char.lower()
        else:
            result += char

    return result.strip()
