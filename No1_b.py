class Jajar_Genjang:
    def __init__(self, panjang):
        self.panjang = panjang

def print_jajar_genjang(n):
    temp = n-1
    for i in range(0, n):
        print(temp*" "+n*"*")
        temp -= 1

x = Jajar_Genjang(5)
print_jajar_genjang(x.panjang)