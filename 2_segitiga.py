class luasSegitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = self.alas * self.tinggi / 2

x = luasSegitiga(3,5)
print(x.luas)