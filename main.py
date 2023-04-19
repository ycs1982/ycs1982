a = int(input("Lado a :"))
b = int(input("Lado b :"))
c = int(input("Lado c :"))


if a < b + c and b < c + a  and c < b + c:
    if a == b and b == c:
        print("Triangulo equilatero")
    if a != b and b != c and c != a:
        print("Triangulo escaleno")
else:
    print("isso não é um triangulo")

if not a !=b and a != c:
    print ("triangulo isoceles")