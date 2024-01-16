# davlat = [ 'Uzb', 'UK','USA', 'Rus', 'AAA', 'INDIA', 'QOZOQ']
# print(len(davlat))
# davlat.sort()
# print(davlat)
# davlat.sort(reverse=True)
# print(davlat)
# davlat.reverse()
# print(davlat)
# sonlar = list(range(120,1200,2))
# print(sum(sonlar))
# minn = min(sonlar)
# maxx= max(sonlar)
# print(minn+maxx)
# print(len(sonlar))
# boshi = sonlar[:20]
# print(boshi)
# urt = sonlar[260:280]
# ox = sonlar[520 :]
# print(urt)
# print(ox)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan']
# for n in mehmonlar:
#     print(f" Hurmatli {n},")
#     print("sizni 20 - mart kuni toyga taklif qilamiz ")
#

# kub = list(range(11,100,2))
# for n in kub :
#     print(f"{n+1} - {n**3}")
#
# son = int(input("son kiriting = "))
# if son >0:
#     print(" son musbat")
# else:
#     print("son manfiy")

# yosh = int(input(" Yoshingizni kiriting : "))
# if yosh <7:
#     print("Sizga bepul kirish")
# elif  yosh<=18 :
#     print(" Kirish puli 5000 som ")
# elif yosh >=18:
#      print("sizga kirish 10000 som")
#

# kun = input(" bugun kun nima : ")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("bugun dam olish kuni")
# else:
#     print("bugun ish kuni...")
#

# menyu = ['osh', 'norin', 'somsa','shashlik']
# buyurtma = ['osh', 'salat','somsa']
# for n in buyurtma:
#     if n in menyu:
#         print(f"menyuda {n} bor")
#     else:
#         print(f"kechirasiz menyuda {n} yoq")
#
# son = 1
# while son <=5:
#     print(son)
#     son=son+1
#

# print(" kiritilgan sonninig kvadiratini qaytaruvchi dastyr.")
# savol = "Istalgan son kiritng "
# savol += "(toxtatish uchun 'exit' dep yozing "
# qiymat = ''
# while qiymat!='exit':
#     qiymat = input(savol)
#     if qiymat!='exit':
#         print(float(qiymat)**2)
#
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadirati {son**2} ga teng")
#
#
# son = 0
# while son <10:
#     son+=1
#     if son%2!=0:
#         continue
#     else:
#         print(son, end=" ")
#

# ismlar = []
# print("Yaqin dostlaringiz royxatini tuzamiz ")
# n =1
# while True:
#     savol = f"{n} - do'stingizni kiritng - "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qoshasizmi ? ha/yoq - ")
#     if javob == "ha":
#         n+=1
#         continue
#     else:
#         break
# print("royxat tuzildi")
# print(ismlar)
#
#
