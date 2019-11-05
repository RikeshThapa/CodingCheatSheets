"""
> Implementation of integer multiplication algorithm
> Restriction to only multiplying by single digits
> Options for implentation:
>> Grade school long hand multiplication
>> Karatsuba's Algorithm
>> recursive integer multiplication
>> good explanation and learning source here: https://www.cs.umd.edu/class/spring2016/cmsc351-0101/int_mult.pdf
"""

"""
> y = 9876
> x = 1234
a = 12
b = 34
c = 98
d = 76

y = 10^(n/2)*c + d
x = 10^(n/2)*a + b
xy = (10^n)ac + (10^(n/2))(ad+bc) +bd

"""


class product_calculator():
    '''
    Implement product multiplication.
    1) Karatsuba
    2) Recursive integer multiplication
    3) gradeschool math implementation
    '''
    def karatsuba(x,y):
        #convert to string because most manipulations are string oriented
        hx = str(x)
        hy = str(y)
        n = len(hx)
        if len(hx) != len(hy):
            print("Lengths are not the same between x and y")
            return None
        C = int(hx[0:len(hx)])
        D = int(hx[(len(h)+1):len(h)])
        A = int(hy[0:len(hy)])
        B = int(hy[len(hy)+1:len(hy)])
        product = (10**n)*A*C + (10**(n/2))((A*D)+(B*C)) + B*D
        return product


    def recursive_integer_multiplication(a,b):
        return None

def karatsuba(x,y):
    #convert to string because most manipulations are string oriented
    hx = str(x)
    hy = str(y)
    nx = len(hx)
    ny = len(hy)
    if nx%2 == 1:
        print("hx:" + hx)
        hx = "0"+hx
        nx = nx+1
    if ny%2 == 1:
        print("hy:" + hy)
        hy = "0"+hy
        ny = ny+1
    C = (hx[0:nx/2])
    print(C)
    D = (hx[(nx/2):nx])
    print(D)
    A = (hy[0:ny/2])
    print(A)
    B = (hy[(ny/2):ny])
    print(B)

    #if len(c) is not 1 none of the components are since they are all of equal lengths
    if len(C)!=1:
        #component 1
        print("A="+A)
        print("B="+B)
        print("C="+C)
        print("D="+D)
        print("this should be the last message")
        comp1 = karatsuba(int(A),int(C))
        print("comp1:"+str(comp1))
        #component 2
        comp2 = karatsuba(int(A),int(D))
        print("comp2:"+str(comp2))
        #component 3
        comp3 = karatsuba(int(B),int(C))
        print("comp3:"+str(comp3))
        #component 4
        comp4 = karatsuba(int(B),int(D))
        print("comp4:"+str(comp4))
        #product = (10**n)*comp1+(10**(n/2))(comp2+comp3)+comp4
        product = ((10**nx)*comp1)+(10**(nx/2))*(comp2+comp3)+comp4
        print("prod="+str(product))
    else:
        #actually calculate the bit sized prods
        product = x*y
    return product


if __name__ == "__main__":
    testA = 3141592653589793238462643383279502884197169399375105820974944592
    testB = 2718281828459045235360287471352662497757247093699959574966967627
    karatsuba(testA, testB)
