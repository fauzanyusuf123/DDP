from Animal import Animal

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun

    def cetak_ular(self):
        super().cetak(),
        print("\ndesign \t\t\t:", self.design,
        "\nRacun \t\t\t :", self.racun,
        "\nmakanan \t\t:", self.makanan,
        "\nhidup \t\t\t:", self.hidup,
        "\nberkrmbang_biak \t:", self.berkembang_biak
        )
        
Anaconda = Ular("Anaconda", "kambing", "amazon", "bertelur", "batilk solo", "tidak berbisa")
Anaconda.cetak_ular()
Kobra = Ular("Kobra", "katak", "hutan", "bertelur", "BajuSilat,", "Berbisa")
Kobra.cetak_ular()