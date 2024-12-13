from Animal import Animal

class Buaya(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, rahang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.rahang = rahang
    def cetak_Buaya(self):
        super().cetak(),
        print("\ndesign \t\t\t:", self.design,
        "\nrahang \t\t\t:", self.rahang,
        "\nmakanan \t\t:", self.makanan,
        "\nhidup \t\t\t:", self.hidup,
        "\nberkembang_biak \t:", self.berkembang_biak
        )

BuayaRawa = Buaya("BuayaRawa", "daging", "amfhibi", "bertelur", "besar", "kuat")
BuayaRawa.cetak_Buaya()