# Day 201 365 #AnAlgorithmAday2018
# Problem is from CTCI 1.5
#
#One Away
#
#WThere are three type of edits that can be made, insert a char, remove a char or replace a char.  given two strings, 
#see if there are one edit away
########################################################################################################################


def oneAway(str1, str2):
    
    concat = str1 + str2

    letter_count = {}

    for char in concat:
        letter_count[char] = letter_count.get(char, 0) + 1


    values = letter_count.values()

    odd_count = 0

    for value in values:
        if value % 2 != 0:
            odd_count += 1

    return odd_count <= 2



