def simpl(a, b):
    i = 1
    c = a
    d = b
    a = abs(a)
    b = abs(b)
    while i < a + 1:
        if a % i == 0:
            if b % i == 0:
                a //= i
                b //= i
                i = 1
        i += 1
    if (c > 0 and d > 0) or (c < 0 and d < 0):
        if a == b:
            return "1"
        else:
            if b == 1:
                return str(a)
            return "(" + str(a) + "/" + str(b) + ")"
    else:
        if a == b:
            return " -1"
        else:
            if b == 1:
                return "-" + str(a)
            return " -(" + str(a) + "/" + str(b) + ")"


poly = []
int_poly = []
print("This is a program that integrates any polynomial")
j = int(input("Type the number of terms in your polynomial: "))
i = 0

while j - i > 0:
    # Adds parts for the original function
    k = j - i

    if k != 0:
        coeff = int(input("Type in the coefficient of term " + str(i+1) + ": "))
        expo = int(input("Type in the exponent of  term " + str(i+1) + " (input zero if it is a constant term): "))

    if coeff > 0 and i != 0:
        poly.append("+" + str(coeff) + "x^" + str(expo))
    elif coeff > 0:
        poly.append(str(coeff) + "x^" + str(expo))
    else:
        poly.append(str(coeff) + "x^" + str(expo))

    # Adds parts for the integrated function
    int_expo = expo + 1
    int_coeff = simpl(coeff, int_expo)

    #General Case
    if expo != -1:
        if coeff > 0 and i != 0:
            int_poly.append("+" + str(int_coeff) + "x^" + str(int_expo))
        elif coeff > 0:
            int_poly.append(str(int_coeff) + "x^" + str(int_expo))
        else:
            int_poly.append(str(int_coeff) + "x^" + str(int_expo))
    else:
        if coeff > 0 and i != 0:
            int_poly.append("+" + str(coeff) + "ln(x)")
        elif coeff > 0:
            int_poly.append(str(coeff) + "ln(x)" )
        else:
            int_poly.append(str(coeff) + "ln(x)" )

    i += 1


print()
print("The original function is: ")
for i in range(len(poly)):
    if not ("^0" in poly[i]):
        print(poly[i], end='')
    else:
        print(poly[i].removesuffix("x^0"), end='')

print()
print("The integrated function is: ")
for i in range(len(int_poly)):
    print(int_poly[i], end='')
print("+C")
