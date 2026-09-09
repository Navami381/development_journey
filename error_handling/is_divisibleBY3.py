def is_divisibly_bythree(num):

    result= True

    if num%3==0:

        result=True
    else:
        result=False

    return result

assert is_divisibly_bythree(9)==True,"test case 1 failed"
assert is_divisibly_bythree(16)==False,"test case 2 failed"