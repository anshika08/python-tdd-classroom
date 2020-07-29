def reverse_list(mylist):
    """
    Reverses order of elements in list input_list.
    """
    newlist=[]
    for i in reversed(mylist):
        newlist.append(i)
    return newlist

def count_digits(number):
    """
    Return count of digits
    """
    count=0
    while(number>0):
        count=count+1
        number=number//10

    return count
