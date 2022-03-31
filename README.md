This code is meant to be run from the command line.


This code calculates the first n terms of a recursively defined sequence based on 3 user definded variables:
1) numberOfTerms is an integer value which spesifies the number of terms to be calculated
2) x1 a rational number represented by the Fraction type from the fractions modual
3) numorator is list of integers whose length is an even number. It is generated from a comma separated list without brackets entered by the user. this list is used to genorate a polynomial whose coefisients and exponents are given by the elements of the list for example:

    nicky@nicky-MacBookPro:~/Projects/recursive-sequence-calculator$ python3 main.py
    Enter the coefficients and exponents of the numorator polynomial 
    as a comma separated list with an even number of terms e.g. 1,1,2,0: 3,2,2,0 

will yield:
    numerator
    ['3','2','2','0']
    
and this will be used to generate the polynomial:
    3x^2 + 2x^0

the '0' is necisary to represenyt the constant term in the polynomial
4) denominator is the same as numerator but it represtents the denominator polynomial

given:
numberOfTerms = 5
x1 = Fraction("4")
numerator = ['1','1','2','0']
denominator = ['5','0']

the inductive step will be x_n+1 = (x_n + 2)/(5)
which gives:
x_1: 4.0000000000e+00 / 1.0000000000e+00  |  4.0
x_2: 3.0000000000e+00 / 1.0000000000e+01  |  0.3
x_3: 2.3000000000e+01 / 1.5000000000e+01  |  1.5333333333333334
x_4: 5.3000000000e+01 / 1.1500000000e+02  |  0.4608695652173913
x_5: 2.8300000000e+02 / 2.6500000000e+02  |  1.0679245283018868


I also want to add a feature that allows a user to request a specific term or to export the data.

