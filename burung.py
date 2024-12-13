from Animal import Animal

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, sayap):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.sayap = sayap

    def cetak_Burung(self):
        super().cetak(),
        print("design \t\t\t:", self.design,
        "\nSayap \t\t\t:", self.sayap,
        "\nMakanan \t\t:", self.makanan,
        "\nHidup \t\t\t:", self.hidup,
        "\nBerkembang_biak \t:", self.berkembang_biak)
        
Garuda = Burung("Garuda", "Ular", "Udara", "bertelur", "Panca Sila", "Bisa terbang")
Garuda.cetak_Burung()
MuraiBatu = Burung("MuaraiBatu", "jangkrik", "Udara", "bertelur", "BatikJawa", "bisaTerbang")
MuraiBatu.cetak_Burung()