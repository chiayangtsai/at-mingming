# mac


def basic_while_loop():
    
    #Example please look at leetcode_sum_up_elements

    return 

def leetcode_shuffle_two_lists():
    #Q: Given two lists a and b, assume len(a) == len(b)
    #.  shuffle the element in a and b following index order, and print out the results.
    a = [5, 4, 1, 3, 2]
    b = [6, 7, 0, 6, 7]
    #.   0. 1. 2. 3. 4
    #. =>  5  6  4 7 1 0 3 6 2 7
    #HW0705


    return 

# HW0620
def leetcode_sum_up_elements():
    # Q: Give a list of numbers, sum up all elements and print out the results
    # NOTE: use list index to form the for loop
    a = [3, 1, 5, 4, 2, 0, 1, 5] #<== input
    elements = 0
    for i in range(0, len(a) ,1) : #[0, 1, 2, 3, .........len(a)-1]
        elements = elements + a[i]

    print("sum = %d" % elements)

    print("=============")

    elements = 0
    i =0 
    while i < len(a):
        #....
        elements += a[i]
        i = i+1

    print("sum = %d" % elements)

    

    
    return


def basic_range():
    """
    range ( starting boundary , ending boundary  , increment )     return "python object with list"
            ^^^^^^^^^^^^^^^^^.  ^^^^^^^^^^^^^^^^.  ^^^^^^^^^
            inclusive              exclusive.         1
                                                  ^^^^^^^^^^^ ignored if increment == 1


            ^^^^^^^^^^^^^^^^^^^ ignored if starting with 0
    """

    # Q: create a list - consecutive numbers from 2 to 10
    a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(a)

    res = list(range(2, 11, 1))
    print(res)

    # Q: create a list - consecutive numbers from -67 to 67
    res = list(range(-67, 68, 1))
    print(res)

    print("====")

    # Q: create a list - consecutive numbers : 3, 4, 5, 6, 7, 8, 9
    res = list(range(3, 10, 1))
    print(res)

    # Q: create a list - consecutive numbers : 5, 7, 9, 11
    res = list(range(5, 13, 2))
    print(res)

    # Q: create a list - consecutive numbers :  6, 5, 4, 3, 2, 1, 0
    res = list(range(6, -1, -1))
    print(res)

    # Q: create a list - consecutive numbers :  0, 1, 2, 3, 4, 5
    res = list(range(0, 6, 1))
    res = list(range(0, 6))
    res = list(range(6))
    print(res)

    # Q: create a list - consecutive numbers :  5, 3, 1, -1
    res = list(range(5, -2, -2))
    print(res)

    return


def leetcode_find_max():
    nums = [41, 67, 67, 67, 67]
    # Q: Find the maximum number in nums, and print it out

    #   print("using max = %d" % ma)

    max_num = nums[0]
    for x in nums:
        if x > max_num:
            max_num = x

    print(max_num)


def basic_print():
    """
    basic data type :
      integer : 3, 1, 2, 0, -3
      floating point : 3.12, -2.5
      string : "a", "ho_...", 'kkkkk'
    """

    print("---- integer -------")
    # Q : print out "my math score is 90"
    # %d is an integer
    score = 67
    print("my math score is %d" % score)

    # Q: print out "my math and english scores are 80 and 70, respectively"
    #                                             ^^.    ^^^
    #                                        scoreM.   scoreE
    scoreM = 41
    scoreE = 67
    print("my math and english scores are %d and %d , respectively" % (scoreM, scoreE))

    print("---- string -------")
    # . --- %s ------
    # Q: print out "Victor's math score is 90"
    #              ^^^^^^.                ^^^
    #                  name                  score
    name = "BOB"
    score = 41
    print("%s's math score is %d" % (name, score))

    print("---- floating point -------")
    # ---- %f ------- default: supporting 6 floating digits.
    pi = 3.141592653589793
    # Q: print out "the value of pi is 3.1415926"
    #                                 ^^^^^^^^^ pi
    print("the value of pi is %.7f" % (pi))
    print("the value of pi is %.2f" % (pi))
    print("the value of pi is %.3f" % (pi))

    pi = 3.14
    print("the value of pi is %f" % (pi))

    print("---- everything can be printed with string -------")
    ss = ""
    print(ss)

    ss = str(999)  # "999"
    print(ss)
    ss = str()  # equivalent to ss = ""
    print("res = %s" % ss)

    pi = 3.141592653589793
    # Q: print out "the value of pi is 3.141592653589793"
    # ss = str(pi) #variable
    print("the value of pi is %s" % str(pi))

    print("------ return/ end of line -----")
    a = 5
    b = 3
    print(a)
    print("\n\n")  # line indentation
    print(b)

    """
    (2+3)x 5 = 25
    3 x 5 = 15

    """


def basic_operators():
    print("--- arithmetic operation ---")
    """
    + - * /
    """

    print("--- logic ---")
    """
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

    """

    print("--- +=, *=, /=, -= ---")

    # Q: calculate "a" plus 1 and print out "the result is 8"
    #                                                     ^ a +1
    a = 8  # "=" : assign the value from right to left
    print("the result is %d" % a)

    # data in "Disk"
    # "CPU" process data : "Disk" -> "DRAM" -> "CPU"
    #                                 ^^^^^ memory

    # Q: add "2" to a
    a = 10  # variable
    a = a + 2  # <== 12
    print("a is %d" % a)

    # Q: add "1" to a
    a = a + 1  # <== 13
    print("a is %d" % a)

    a += 1  # <== 14
    print("a is %d" % a)

    # Q: multiply "2" to a
    a *= 2  # a = a*2 # <== 28
    print("a is %d" % a)

    # Q: divide "a" by 2 and assign back to "a"
    a /= 2
    print("a is %d" % a)

    return


def basic_list_i():
    a = 5  # <== variable a: object, memory

    b = [3, 1, 2]  # <== variable b: address of the list
    # .   ^^ ^^.^^
    # .   0. 1. 2
    print(b[0])
    print(b[1])
    print(b[2])

    # Q: Given a list "a", add "5" to the index-0 element of a
    a = [6, 7, 8]
    # .  ^^ a[0]
    print(a)
    a[0] = a[0] + 5  # a[0] += 5
    print(a)

    # Q: Given a list "d", multiply 100 to the index-1 element of d
    d = [6, 7]
    # .   0. 1

    d[1] = d[1] * 100
    print(d)

    # Q: combine two lists a and b to c
    a = [6, 7]
    b = [9, 10, 11]
    # c = [6, 7, 9, 10, 11]
    c = a + b
    print(c)

    print("------ append ------")
    a = [6, 7]
    # .   0  1
    # Q: append "-1" to a
    # . a=> [6, 7, -1]
    a = a + [-1]
    # a.append(-1)
    print(a)

    # HW0605
    # Q: Give 4 lists, comebine them together to a new list "z"
    a = [3, 5]
    b = [0, 2]
    c = [-1]
    d = [7]
    z = []  # => [3, 5, 0, 2, -1, 7]
    z = a + b + c + d
    print(z)

    print("------- += for variable-----------")
    x = 5
    # Q: add "1" to x and assign it back to x
    x = x + 1
    # or
    x += 1

    print("------- += for list-----------")
    a = [6, 7]
    # Q: append -1 to a
    a = a + [-1]  # 拆掉重蓋
    # or
    a += [-1]  # 加蓋

    print("--------- length of list ------")
    nums = [3, 5, 1, 4, 2]
    # len(list)

    l = len(nums)
    print(l)

    print("--------- locate ------")
    nums = [3, 5, 1, 4, 2]
    # .      0  1. 2. 3. 4   <== last index = len(nums) -1
    # .      -5 -4 -3 -2 -1
    print(nums[2])

    print("last element = %d" % nums[len(nums) - 1])
    print("last element = %d" % nums[-1])


def basic_loop():
    # Q: 1+2+3+4+5
    sum = 0

    sum += 1
    sum += 2
    sum += 3
    sum += 4
    sum += 5

    print(sum)
    print("=====")

    # Q: 1+2+3+4+5+6.....+10
    sum = 0

    for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print("x= %d" % x)
        sum += x
        print("sum= %d" % sum)
        print("\n")

    print(sum)

    print("------------")

    # Q: Given a list, sum up all values and print out the sum
    a = [3, 1, 5, 4, 2]
    sum = 0

    for x in a:
        sum += x

    print("sum= %d" % sum)

    print("------------")
    # Q: Given a list of numbers, print out negative values
    nums = [3, -1, 2, -5, -3, 6, 8]
    # => -1
    # .   -5
    # .   -3

    for n in nums:
        if n < 0:
            print(n)

    print("------------")
    # Q: Given a list, sum up all values and print out the sum
    # NOTE: use list index to implement the solution
    a = [3, 1, 5, 4, 2, -1]
    #.   0. 1. 2. 3. 4.  5. 6<== index (list index, container index)
    # print(a[0])
    # print(a[1])
    # print(a[2])
    # print(a[3])
    # print(a[4])

    # .   0. 1. 2. 3. 4
    # .  a[0] a[1] a[2] a[3] a[4]
    sum = 0
    for i in range(0,  len(a)  ,1): #[0, 1, 2, 3, 4]:
        sum += a[i]
        
    print(sum)

    return
    
    print("------------")
    # Q: Given a list of numbers, if the number is negative, reset it to 0. Print out the results
    nums = [3, -1, 2, -5, -3, 6, 8]
    # .      0.  1. 2.  3.  4. 5. 6
    #    nums = [3, 0, 2, 0, 0, 6, 8]

    # # Debug
    # for n in nums:
    #     if n<0:
    #         n=0
    for i in [0, 1, 2, 3, 4, 5, 6]:
        if nums[i] < 0:
            nums[i] = 0

    print(nums)

    print("------ the length of the list --")
    # Q: Given a list a = [3, 1, 5, 4, 2], what is the length of a
    a = [3, 1, 5, 4, 2]
    # .   0. 1. 2. 3. 4
    l = len(a)

    print(l)

    return


def leetcode_9x9_multiplications():
    # Q: print out 2's 九九乘法表
    # 2x1 = 2
    # 2x2 = 4
    # 2x3 = 6
    # 2x4 = 8
    # 2x5 = 10
    # 2x6 = 12
    # 2x7 = 14
    # 2x8 = 16
    # 2x9 = 18

    for x in range(1, 10, 1):  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print("2x%d = %d" % (x, 2 * x))

    print("=====")

    # Q: print out 2's, 3's, 4's, .....'s 九九乘法表
    # 2x1= 2
    # ...
    # 2x9 = 18
    # 3x1 = 3
    # ....
    # 3x9 = 27
    # 4x1..
    # ..
    # 9x1 = 9
    # ...
    # 9x9 = 81
    # HINT : double loop (two layers)
    # HW0612

    for i in range (2,10,1):#[2, 3, 4, 5, 6, 7, 8, 9]:
        for x in range (1,10,1):#[1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("%dx%d=%d" % (i, x, i * x))
    #
    return