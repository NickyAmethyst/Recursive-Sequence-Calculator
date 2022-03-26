# this script computes the first 'n' terms of a recursively defined sequence
# x1 value is a rational number and the inductive step is composed of arithmatic opperations

from fractions import Fraction
#x1 = input("enter a rational number, i.e. 5 or 5/7: ")
#x1 = Fraction("3/5")
#x1 = Fraction(input("enter a rational number, e.g. 5 or 5/7: "))
x1 = Fraction("4")

# now how to define the inductive step?
# Prompt user to enter a list of integers for the numerator and denominator
#numerator = [1,1,2,0] # 1x^1 + 2x^0
numerator = input("Enter the coefficients and exponents of the numorator polynomial \n as a comma separated list with an even number of terms e.g. 1,1,2,0: ").split(',')
#numerator = [1,1,2,0]
print(numerator)
#denominator = input("Enter the coefficients and exponents of the denominator polynomial as a comma separated list with an even number of terms e.g. 1,1,2,0:").split(',')
denominator = [5,1]   # 5
#numberOfTerms = int(input("Enter number of terms to be calculated: "))
numberOfTerms = 100
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

def inductive_step(nMinusOneTh):
    #nTh = (2*nMinusOneTh + 1)/5
    nTh = poly_gen(numerator, Fraction(nMinusOneTh)) / poly_gen(denominator, Fraction(nMinusOneTh))
    #nTh = (nMinusOneTh[0] + 2*nMinusOneTh[1], 5*nMinusOneTh[1])
    return nTh

# then define the first n terms of the sequence by a list of these 2-tuples
def compute_head(n, x1, inductive_step):
    sequenceHead = [x1]
    for i in range(1, n):
        sequenceHead.append(inductive_step(sequenceHead[i - 1]))
    return sequenceHead
ans = compute_head(numberOfTerms, x1, inductive_step)
#print(ans)

# chage the output format to scientific notation
# is there a table output format?
#use string formating
#when the num and denom get to long, more than 10 dig. switch to approx scientic notation wit
# presision 10
width = len(str(numberOfTerms))
count = 1
for t in ans:
    output = f"{count:{width}}: {t.numerator:.10e} / {t.denominator:.10e}  |  {float(t)}"
    print(output)
    count +=1
    #print(t, float(t))
print(type(x1))