class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
      self.nama = nama
      self.makanan = makanan
      self.hidup = hidup
      self.berkembang_biak = berkembang_biak
    def cetak(self):
       print("nama \t\t\t:", self.nama,
             "makanan \t\t:", self.makanan,
             "hidup \t\t\t:", self.hidup,
             "berkembang_biak \t:", self.berkembang_biak
             ) 
#object = Animal("Buaya", "Daging", "Amfibi", "bertelur")
#object.cetak_(self)