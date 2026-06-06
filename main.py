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
    print("my math score is %d" % score    )
    
    #Q: print out "my math and english scores are 80 and 70, respectively"
    #                                             ^^.    ^^^
    #                                        scoreM.   scoreE
    scoreM = 41
    scoreE = 67
    print("my math and english scores are %d and %d , respectively"   %(scoreM  ,scoreE)   )


    print("---- string -------")
    #. --- %s ------
    #Q: print out "Victor's math score is 90" 
    #              ^^^^^^.                ^^^
    #                  name                  score
    name = "BOB"
    score = 41
    print("%s's math score is %d"%(name,score)) 
    

    print("---- floating point -------")
    # ---- %f ------- default: supporting 6 floating digits. 
    pi = 3.141592653589793
    #Q: print out "the value of pi is 3.1415926"
    #                                 ^^^^^^^^^ pi
    print("the value of pi is %.7f" % (pi))
    print("the value of pi is %.2f" % (pi))
    print("the value of pi is %.3f" % (pi))

    pi = 3.14    
    print("the value of pi is %f" % (pi))


    print("---- everything can be printed with string -------")
    ss = ""
    print(ss)
    
    ss = str(999) # "999"
    print(ss)
    ss = str() # equivalent to ss = ""
    print("res = %s" % ss)


    pi = 3.141592653589793
    #Q: print out "the value of pi is 3.141592653589793"
    #ss = str(pi) #variable
    print("the value of pi is %s" % str(pi) )
    
    print("------ return/ end of line -----")
    a = 5
    b = 3
    print(a)
    print("\n\n") #line indentation
    print(b)
    
    '''
    (2+3)x 5 = 25
    3 x 5 = 15
    
    '''
        
def basic_operators():

    print("--- arithmetic operation ---")
    '''
    + - * /
    '''

    print("--- logic ---")
    '''
    and or

    if "raining" and "floor is wet" => don't go out 


    A , B

    A and B

    True and True => True
    True and False => False
    False and True => False
    False and False => False

    if "raining" or "sunny" => umbrella
    
    A or B => 

    True or True => True
    True or False => True
    False or True => True
    False or False => False
        
    '''


    print("--- +=, *=, /=, -= ---")

    #Q: calculate "a" plus 1 and print out "the result is 8"
    #                                                     ^ a +1
    a = 8 # "=" : assign the value from right to left
    print("the result is %d"% a)


    # data in "Disk"
    # "CPU" process data : "Disk" -> "DRAM" -> "CPU"
    #                                 ^^^^^ memory
    
    #Q: add "2" to a
    a = 10 #variable
    a = a+2 # <== 12
    print("a is %d" % a)


    #Q: add "1" to a
    a = a+1 #<== 13
    print("a is %d" % a)
    
    a += 1 # <== 14
    print("a is %d" % a)

    #Q: multiply "2" to a
    a *=2 # a = a*2 # <== 28
    print("a is %d" % a)

    #Q: divide "a" by 2 and assign back to "a"
    a /=2
    print("a is %d" % a)

    
    return

def basic_list_i():

    a = 5 #<== variable a: object, memory

    b = [3, 1, 2] #<== variable b: address of the list
    #.   ^^ ^^.^^
    #.   0. 1. 2
    print(b[0])
    print(b[1])
    print(b[2])

    #Q: Given a list "a", add "5" to the index-0 element of a
    a = [6, 7, 8]
    #.  ^^ a[0]
    print(a)    
    a[0] = a[0] + 5 # a[0] += 5
    print(a)

    #Q: Given a list "d", multiply 100 to the index-1 element of d
    d = [6, 7]
    #.   0. 1
    
    d[1] = d[1] * 100
    print(d)

    
    # Q: combine two lists a and b to c
    a= [6, 7]
    b= [9, 10, 11]
    # c = [6, 7, 9, 10, 11]
    c = a + b
    print(c)

    print("------ append ------")
    a = [6, 7]
    #.   0  1 
    #Q: append "-1" to a
    #. a=> [6, 7, -1]
    a = a + [-1]
    #a.append(-1)        
    print(a)

    #HW0605 
    #Q: Give 4 lists, comebine them together to a new list "z"
    a= [3, 5]
    b= [0, 2]
    c = [-1]
    d = [7]
    z = [] # => [3, 5, 0, 2, -1, 7]
    z = a + b + c + d
    print(z)
    

# zoom link
# 
if __name__ == '__main__':  # special meaning for Python execution, but we will talk about it later.

    testID = 3

    if testID == 0: #needs :
        print("hello world ") #string
    elif testID == 1:  #elif = else if
        basic_print() #print  
    elif testID == 2:
        basic_operators() #operatioins
    elif testID == 3:
        basic_list_i() # list
    else:
        print("wrong testID, not supported")

    ''' comments

    == basic level class ===
    - Part 1 - basics         
        - print <= done
        - basic operators : arithmetic operations  <= done
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