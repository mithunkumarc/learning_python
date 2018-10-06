### convert to list , sort and compare 
#### using builtin fuctions

        word1 = list('silent')
        word2 = list('listen')
        word1.sort()
        word2.sort()
        word1_s = ''.join(word1)
        word2_s = ''.join(word2)
        print(word1_s,word2_s,word1_s == word2_s)


#### without using builtin functions

    def anagramTest(string1,another_string):
    '''if one of the character not found in another string, makes stillOK as false'''
    string2 = list(another_string)
    pos1 = 0
    stillOk = True

    while pos1 < len(string1) and stillOk:
        pos2 = 0
        found = False
        while pos2 < len(string2) and not found:
            if string1[pos1] == string2[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            string2[pos2] = None # replacing found letter with None
        else:
            # if one of the letter not found then stop loop return false
            stillOk = False

        pos1 = pos1 + 1

    return stillOk


    print(anagramTest('silent','listen'))



