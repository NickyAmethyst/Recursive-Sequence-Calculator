This code calculates the first n terms of a recursively defined sequence based on 3 user definded variables:
1) numberOfTerms is an integer value which spesifies the number of terms to be calculated
2) x1 a rational number represented by the Fraction type from the fractions modual
3) numorator is list of integers whose length is an even number. It is generated from a comma separated list without brackets entered by the user. this list is used to genorate a polynomial whose coefisients and exponents are given by the elements of the list for example:

    nicky@nicky-MacBookPro:~/Projects/recursive-sequence-calculator$ python3 main.py
    Enter the coefficients and exponents of the numorator polynomial 
    as a comma separated list with an even number of terms e.g. 1,1,2,0: 3,2,2,0 

will yield:
    numerator
    ['1','1','2','0']
    
and this will be used to generate the polynomial:
    3x^2^ + 2x^0^