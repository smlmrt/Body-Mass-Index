print(("-" * 30) + "\nVücut Kütle indeksi Hesaplayıcı\n" + ("-" * 30))

boy = int(input("Lütfen boyunuzu giriniz(cm cinsinden): "))
kilo = float(input("Lütfen kilonuzu giriniz: "))
sonuc = kilo/((boy/100) ** 2)

print("Vücut kitle indeksiniz {}".format(sonuc))

if sonuc >= 0 and sonuc <= 18.4:
    print("Zayıf")
elif sonuc >= 18.5 and sonuc <= 24.9:
    print("Normal")
elif sonuc >= 25 and sonuc <= 29.9:
    print("Fazla kilolu")
elif sonuc >= 30 and sonuc <= 34.9:
    print("Şişman. Birinci derece obez.")
elif sonuc >= 35 and sonuc <= 44.9:
    print("Şişman. İkinci derece obez.")
else:
    print("Aşırı Şişman.Üçüncü derece obez.")
