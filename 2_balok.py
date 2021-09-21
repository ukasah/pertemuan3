class volumeBalok:
    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.volume = self.panjang * self.lebar * self.tinggi

y = volumeBalok(5, 8, 9)
print(y.volume)