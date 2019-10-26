"""
> Implementation of integer multiplication algorithm
> Restriction to only multiplying by single digits
> Options for implentation:
>> Grade school long hand multiplication
>> Karatsuba's Algorithm
>> recursive integer multiplication
>> good explanation and learning source here: https://www.cs.umd.edu/class/spring2016/cmsc351-0101/int_mult.pdf
"""

class product_calculator():
    '''
    Implement product multiplication.
    1) Karatsuba
    2) Recursive integer multiplication
    3) gradeschool math implementation
    '''
    def karatsuba(x, y):
        '''
        1) convert A and B to strings
        2) check string length
        3) if string length is 1, sort and combine
        4) if string length >1
        5) call function again on smaller pairs
        '''
        #Assume lendth of
        lenx = len(str(x))
        leny = len(str(y))
        try:
            y = (lenx == leny)
        except y is False:
            print("x and y are not the same length")
        return None

    def ksplit():
        A = None
        B = None
        C = None
        return (A,B,C)

    def recursive_integer_multiplication(a,b):
        return None


if __name__ == "__main__":
    testA = 3141592653589793238462643383279502884197169399375105820974944592
    testB = 2718281828459045235360287471352662497757247093699959574966967627
    return int_product(testA, testB)
