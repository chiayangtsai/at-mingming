# mac

def basic_print():
    '''
    basic data type :
      integer : 3, 1, 2, 0, -3
      floating point : 3.12, -2.5
      string : "a", "ho_...", 'kkkkk'
    '''

    print("---- integer -------")
    #Q : print out "my math score is 90"
    #%d is an integer
    score = 67
    print("my math score is %d" % (score)    )
    
    #Q: print out "my math and english scores are 80 and 70, respectively"
    #                                             ^^.    ^^^
    #                                        scoreM.   scoreE
    scoreM = 41
    scoreE = 67
    print("my math and english scores are %d and %d , respectively"   %(scoreM  ,scoreE)   )


    print("---- string -------")
    #Q: print out " Victor's math score is 90" 
    # HW0516(VK) start from here next time

    

    print("---- floating point -------")




    return
    




if __name__ == '__main__':  # special meaning for Python execution, but we will talk about it later.

    testID = 1

    if testID == 0: #needs :
        print("hello world ") #string
    elif testID == 1:  #elif = else if
        basic_print() #print    
    else:
        print("wrong testID, not supported")

    ''' comments

    == basic level class ===
    - Part 1 - basics         
        - print
        - basic operators : arithmetic operations
        - list_i : basics
        - for loop / while loop 
        - list_ii : append, pop, del
        - sliding window algorithm
        - string
    
    - Part 2 - dict (dictionary)    


    - Part 3 - dynamic programming (DP) and miscs    


    == AI coding introduction ===
    - Claude code / codex / cursor
    

    == Advanced level class === (optional)
    
    
    
    '''