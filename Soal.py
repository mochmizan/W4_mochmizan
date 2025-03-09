#Soal 1
class Orang:
    def __init__(self, nama_depan, nama_belakang, no_id):
      self.nama_depan = nama_depan
      self.nama_belakang = nama_belakang
      self.no_id = no_id

#Soal 2
class Mahasiswa(Orang):
  SARJANA, MASTER, DOKTOR = range(3)

  def __init__(self, jenjang, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.jenjang = jenjang
    self.matkul = []

  def enrol(self, mata_kuliah):
    self.matkul.append(mata_kuliah)

#Soal 3
class Karyawan(Orang):
  TETAP, TDK_TETAP = range(2)

  def __init__(self, status, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.status = status

#Soal 4
class Dosen(Karyawan):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.matkul_diajar = []

  def mengajar(self, mata_kuliah):
    self.matkul_diajar.append(mata_kuliah)

#Soal 5
Bowo = Mahasiswa(Mahasiswa.SARJANA, "Bowo", "Nugroho", "987654")
Bowo.enrol("Basis Data")
print(Bowo.matkul)

#Soal 6
rizki = Dosen(Dosen.TETAP, "Rizki", "Setiabudi", "456789")
rizki.mengajar("Statistik")
print(rizki.matkul_diajar)

#Soal 7
class Pelajar:
  def __init__(self):
    self.matkul = []
  
  def enrol(self, mata_kuliah):
    self.matkul.append(mata_kuliah)

#Soal 8
class Pengajar:
  def __init__(self):
    self.matkul_diajar = []

  def mengajar(self, mata_kuliah):
    self.matkul_diajar.append(mata_kuliah)

#Soal 9
class Asdos(Orang, Pelajar, Pengajar):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    Pelajar.__init__(self)
    Pengajar.__init__(self)

#Soal 10
uswatun = Asdos("Uswatun", "Hasanah", "456456")
uswatun.enrol("Big Data")
uswatun.mengajar("Kecerdasan Artifisial")
print(uswatun.matkul)
print(uswatun.matkul_diajar)
