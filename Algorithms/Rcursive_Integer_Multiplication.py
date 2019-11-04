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
    def karatsuba(x, y=None):
        '''
        1) convert A and B to strings
        2) check string length
        3) if string length is 1, sort and combine
        4) if string length >1
        5) call function again on smaller pairs
        '''
        #Assume length of x and y are the same
        lenx = len(str(x))
        leny = len(str(y))
        try:
            y = (lenx == leny)
        except y is False:
            print("x and y are not the same length")

        if lenx == 1:
            #if the length of strings are 1, then we are done
            return xy
        else:
            (Acomp, Bcomp, Ccomp) = ksplit(x,y)
            A = karatsuba(Acomp)
            B = karatsuba(Bcomp)
            C = karatsuba(Ccomp)
            product = ((10**lenx)*A) + ((10**(lenx/2))*B) + C
        return product

    def ksplit(x,y):
        strignx = str(x)
        lenx = len(stringx)
        stringy = str(y)
        leny = len(stringy)
        constituent0 = stringx[0:(lenx/2)]
        constituent1 = stringx[(lenx/2)+1:lenx]
        constituent2 = stringy[0:(leny/2)]
        constituent3 = stringy[(leny/2)+1:leny]
        A = None
        B = None
        C = None
        #Ksplit should use karatsuba
        return (A,B,C)

    def recursive_integer_multiplication(a,b):
        return None


if __name__ == "__main__":
    testA = 3141592653589793238462643383279502884197169399375105820974944592
    testB = 2718281828459045235360287471352662497757247093699959574966967627
    return int_product(testA, testB)
