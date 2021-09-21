class Segitiga:
    def __init__(self):
        self.size = 5


def print_segitiga(n):
        for i in range(1, n+1):
            print((n-i+1) * "*")

x = Segitiga()
print_segitiga(x.size)