# 1 - misol
shakl = input("Shakl nomini kiriting (uchburchak, kvadrat, to'rtburchak, doira): ").lower()

match shakl:
    case "uchburchak":
        asos = float(input("Asosini kiriting: "))
        balandlik = float(input("Balandligini kiriting: "))
        yuza = (asos * balandlik) / 2
        print("Uchburchak yuzasi:", yuza)

    case "kvadrat":
        tomon = float(input("Tomonini kiriting: "))
        yuza = tomon ** 2
        print("Kvadrat yuzasi:", yuza)

    case "to'rtburchak":
        uzunlik = float(input("Uzunligini kiriting: "))
        kenglik = float(input("Kengligini kiriting: "))
        yuza = uzunlik * kenglik
        print("To'rtburchak yuzasi:", yuza)

    case "doira":
        radius = float(input("Radiusini kiriting: "))
        pi = 3.14
        yuza = pi * radius ** 2
        print("Doira yuzasi:", yuza)

    case _:
        print("Noto‘g‘ri shakl nomi kiritildi")




# 2 - misol
kunlar = int(input('Hafta kunlarini kiriting: '))

match kunlar:
    case 1:
        print('Dushanba')
    case 2:
        print('Seshanba')
    case 3:
        print("Chorshanba")
    case 4:
        print('Payshanba')
    case 5:
        print("Juma")
    case 6:
        print('Shanba')
    case 7:
        print('Yakshanba')

    case kunlar if 1 <= 5:
        print('Ish kunlari')
    case kunlar if 5 <= 7:
        print('Dam olish kuni')




# 3 - misol
mahsulot = input('Mahsulot turini kiriting (meva , sabzavot, gosht, sut): ').lower()
kg = float(input('Ogirligini kiriting: '))

match mahsulot:
    case "meva":
        narx = 10_000
    case "sabzavot":
        narx = 15_000
    case "go`sht":
        narx = 100_000
    case "sut":
        narx = 15_000

if narx > 0:
    umumiy = narx * kg
    print(f"{mahsulot.title()}ning {kg} kg narxi: {umumiy} so'm")




# 4 - misol
transport = input("Transport turini kiriting: ")
time = float(input('Vaqtni kiriting: '))

match transport:
    case 'mashina':
        masofa = 1_000
    case 'velosiped':
        masofa = 5_000
    case 'poyezd':
        masofa = 100_000
    case 'samolyot':
        masofa = 200_000
    case 'piyoda':
        masofa = 2_000
    case 'avtobus':
        masofa = 10_000

if masofa > 0:
    umumiy = masofa * time
    print(f"{transport.title()}ning {time} vaqti: {umumiy}")
