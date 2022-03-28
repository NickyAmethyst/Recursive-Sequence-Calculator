# this script computes the first 'n' terms of a recursively defined sequence
# x1 value is a rational number and the inductive step is composed of arithmatic opperations

from fractions import Fraction
import sys
x1 = Fraction(input("enter a rational number, e.g. 5 or 5/7: "))
#x1 = Fraction("4")

numberOfTerms = int(input("Enter number of terms to be calculated: "))
#numberOfTerms = 50

# The numerator and denominator variables are later used to define the inductive step
# Prompt user to enter a list of integers for the numerator and denominator
numerator = input("Enter the coefficients and exponents of the numorator polynomial \n as a comma separated list with an \n even number of terms e.g. 3,2,2,0 which represents 3x^2 + 2x^0: ").split(',')
#numerator = [3,3,2,0]
denominator = input("Enter the coefficients and exponents of the denominator polynomial \n as a comma separated list with \n an even number of terms e.g. 5,0 which represents the constant 5: ").split(',')
#denominator = [2,2,1,1]   # 5

# funcion takes in a list and returns a polynomial
# lists must have even numbers of terms
def poly_gen(coefs, y):
    #maybe use fraction modual in here
    """Returns the value of a polynomial variable = 'y' with coefficients and powers given by 'coefs'"""
    p = Fraction("0")
    for i in range(0,len(coefs), 2):
        x = coefs[i+1]
        a = coefs[i]
        p += Fraction(a)*(Fraction(y)**Fraction(x))
        #print(coefs[i],"* y^",coefs[i+1])
    #p = int(p)
    return p

# a rule to define the nth term in terms of the previous term
def inductive_step(nMinusOneTh):
    nTh = poly_gen(numerator, Fraction(nMinusOneTh)) / poly_gen(denominator, Fraction(nMinusOneTh))
    return nTh

# returns the first n terms of the sequence by a list of these 2-tuples

def compute_head(n, x1, inductive_step):
    sequenceHead = [x1]
    count = 1
    width = len(str(numberOfTerms))
    for i in range(1, n):
        sequenceHead.append(inductive_step(sequenceHead[i - 1]))
        # (**) print one at a time to see when it overflows
        t = inductive_step(sequenceHead[i - 1])
        output = f"x_{count:{width}}: {t.numerator:.10e} / {t.denominator:.10e}  |  {float(t)}"
        print(output)
        count +=1
        # (**)
    return sequenceHead


compute_head(numberOfTerms, x1, inductive_step)


# # (**)
# ans = compute_head(numberOfTerms, x1, inductive_step)


# width = len(str(numberOfTerms))
# count = 1
# for t in ans:
#     output = f"x_{count:{width}}: {t.numerator:.10e} / {t.denominator:.10e}  |  {float(t)}"
#     print(output)
#     count +=1
# # (**)