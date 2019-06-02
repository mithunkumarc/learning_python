### convert to list , sort and compare 
#### using builtin fuctions

        def check_anagram(word1,word2):
            #check the length of two words first
            if len(word1) == len(word2):
                #sort word1
                sorted_word1 = sorted(word1)
                #return type of sorted is list, so convert back to string
                sorted_word1_str = ''.join(sorted_word1)
                #sort word2
                sorted_word2 = sorted(word2)
                # return type of sorted is list, so convert back to string
                sorted_word2_str = ''.join(sorted_word2)
                #compare
                if sorted_word1_str == sorted_word2_str:
                    return True
                else:
                    return False
            else:
                return False

        result = check_anagram("mithun","kumar")
        print(result)


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



