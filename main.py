# zad1
# liczby1 = [x for x in range(31)]
# #print(liczby1)
# liczby2 = [x*2 for x in liczby1]
# #print(liczby2)
# plik = open("liczby.txt", "w")
# plik.writelines(str(liczby2))
# plik.close()

# zad2
# plik = open("liczby.txt", "r")
# linie = plik.readlines()
# plik.close()
# print(linie)

# zad3
# tekst = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. In porttitor aliquam lectus. ' \
#         'Mauris ornare laoreet finibus. Sed euismod congue dictum. Etiam elementum velit mi, ' \
#         'eget convallis ante euismod non. Morbi efficitur porttitor velit, et egestas eros ornare ut. ' \
#         'Aliquam imperdiet sagittis lorem a vestibulum. Pellentesque nec lectus imperdiet, tincidunt turpis eget, ' \
#         'imperdiet velit. Praesent elementum massa purus, vel bibendum erat pellentesque ac. Cras ac mattis odio, ' \
#         'eget vehicula sapien. Nullam faucibus nulla vitae faucibus maximus. '
# with open("tekst.txt", "w") as plik:
#     plik.writelines(str(tekst))
# plik = open("tekst.txt", "r")
# linie = plik.readlines()
# plik.close()
# with open("tekst.txt", "r") as plik:
#     for linie in plik:
#         print(linie, "")

# zad4
# class NaZakupy:
#     def __init__(self, nazwa, ilosc, jednostka, cena):
#         self.nazwa = nazwa
#         self.ilosc = ilosc
#         self.jednostka = jednostka
#         self.cena = cena
#
#     def wyswietl_produkt(self):
#         return self.nazwa, self.ilosc, self.jednostka, self.cena
#
#     def ile_produktu(self):
#         return self.ilosc, self.jednostka
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena
# produkt = NaZakupy('banan', 10, 'kg', 4)
# print(produkt.wyswietl_produkt())
# print(produkt.ile_produktu())
# print(produkt.ile_kosztuje())

# zad5
# class Ciagi:
#     def __init__(self, a1, r, ile):
#         self.a1 = a1
#         self.ile = ile
#         self.r = r
#
#     def wyswietl_dane(self):
#         print(self.a1)
#         for x in range(1, self.ile):
#             self.a1 += self.r
#             print(self.a1)
#
#     def policz_sume(self):
#         suma = self.a1
#         for x in range(1, self.ile):
#             self.a1 += self.r
#             suma += self.a1
#         return suma
#
#
# ciag = Ciagi(2, 1, 5)
# print(ciag.wyswietl_dane())
# ciag = Ciagi(2, 1, 5)
# print(ciag.policz_sume())
