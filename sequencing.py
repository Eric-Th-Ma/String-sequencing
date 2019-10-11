#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:53:07 2018

@author: ericthompson-martin
"""
def align(seq2, seq1):
    '''
    Returns the length of the lcs and the both sequences with '-'
    characters inserted in order to make them the same length with
    their lcs characters alligned in the same order.
    >>> align("human", "chimpanzee")
    (4, '-h-um-an---', 'chi-mpanzee')
    '''
    # create a list of all the character in the lcs and store the lcs length
    lcsVal = lcs(seq1,seq2)[0]
    lcsStringList = list(lcs(seq1,seq2)[2])
    lcsList = list(filter(lambda a: a != '#', lcsStringList))
    lcsList.append("")
    # get the sequence as a list and prepare an empty list to be turned into the new aligned sequence
    seq1Old = list(seq1)
    seq1New = []
    seq2Old = list(seq2)
    seq2New = []
    indexOverall = 0
    for char1 in seq1Old:
        # check if each member of sequence of seq1 is the same as the next element of the lcs
        testChar = lcsList[indexOverall]
        if char1!=testChar:
            #if testChar is not the next character in in the first sequence
            #add to the other list to show there is a nonmatching character here
            seq1New.append(char1)
            seq2New.append('-')
        else:
            indexOverall+=1
            #if the characters match see if this is where the character is in the other list
            #and if not add '-' to seq1 until it aligns the character in the lcs with its
            #location in seq2
            numToRemove=0
            for char2 in seq2Old:
                seq2New.append(char2)
                numToRemove+=1
                if char2==testChar:
                    seq1New.append(char2)
                    break
                else:
                    seq1New.append('-')
            for _ in range(numToRemove):
                seq2Old.pop(0)
    for extraChar in seq2Old:
        # add any extra characters not dealt with in seq2 as characters in seq2 and '-' in seq1
        seq2New.append(extraChar)
        seq1New.append('-')
    return (lcsVal, "".join(seq2New), "".join(seq1New))

def lcs(seq1, seq2):
    '''
    Returns the length of the longest common subsequence of seq1 and seq2,
    and the sequences with all characters not in the lcs replaced by '#'s
    >>> lcs("x", "y")
    (0, '#', '#')
    >>> lcs("spam", "")
    (0, '####', '')
    >>> lcs("spa", "m")
    (0, '###', '#')
    >>> lcs("cat", "car")
    (2, 'ca#', 'ca#')
    >>> lcs("cat", "lca")
    (2, 'ca#', '#ca')
    >>> lcs("human", "chimpanzee")
    (4, 'h#man', '#h#m#an###')
    '''

    # make a table with all 0s with a width one bigger than the length of seq1
    # and a height one bigger than the length of seq2
    table = [(len(seq1)+1)*[0] for x in range(len(seq2)+1)]
    
    #initialize a new seq for each seq but with only #s
    newSeq1 = "#"*len(seq1)
    newSeq2 = "#"*len(seq2)
    for column in range(1,(len(seq1)+1)):
        for row in range(1,(len(seq2)+1)):
            #if the current row and column correspond to characters in the strings that don't match
            # the value is just the max of the previous adjascent squares values
            table[row][column] = max(table[row-1][column], table[row][column-1], table[row-1][column-1])
            if seq1[column-1]==seq2[row-1]:
                # if the row and column correspond to the same character
                # unhashtage the character in both new sequences
                newSeq1list = list(newSeq1)
                newSeq1list[column-1] = seq1[column-1]
                newSeq1 = "".join(newSeq1list)
                newSeq2list = list(newSeq2)
                newSeq2list[row-1] = seq2[row-1]
                newSeq2 = "".join(newSeq2list)
                # hashtag out the character in the original sequnce in order to not double count it
                seq1list = list(seq1)
                seq1list[column-1]  = "#"
                seq1 = "".join(seq1list)
                seq2list = list(seq2)
                seq2list[row-1] = "#"
                seq2 = "".join(seq2list)
                # the value of the lcs in this location is the lcs of the sequences
                # without the letteer currently being counted plus 1
                table[row][column] = table[row-1][column-1]+1

    return (table[len(seq2)][len(seq1)], newSeq1, newSeq2)

if __name__ == '__main__':
 import doctest
 print(doctest.testmod())