# def salomber(ism):
#     """Salom beruvchi funksiya """
#     print(f"Assalomualaykum. {ism.title()}")
#
# print(salomber('hasan'))
#
# def salom(firstname, lastname):
#     "Ism va familya qabul qiluvchi funksiya."
#     print(f"{firstname.title()} {lastname.title()} ")
#
# print(salom("abdulxoliq", "mirzayev"))
#


# def tyil(tugilgan, joriy_yil=2024):
#     """Tug'ilgan yildan yoshini hisoblovchi dastur.."""
#     print(f"Siz {joriy_yil-tugilgan} yoshdasiz..")
#
# print(tyil(int(input("Tug'ilgan yilingizni kiriting - "))))

# def son_kiriting(son1,son2):
#     """Sonlarni kattasini aniqlovchi dastur."""
#     if son1>son2:
#         print(f"{son1} katta.")
#     else:
#         print(f"{son2} katta")
# print(son_kiriting(son1=int(input("son kiriting - ")), son2=int(input("Son kiriting - "))))


# def ismyasa(ism, familya):
#     """Toliq ism qaytaruvchi funksiya."""
#     toliq_ism = f"{ism.title()} {familya.title()}"
#     return toliq_ism
#
# print(ismyasa("abdulxoliq", "mirzayev"))

# def avto_info(make, model, color,karobka, yili, narxi= None):
#     avto = {'kompany' : make,
#             'model': model,
#             'color':color,
#             'karobka': karobka,
#             'yili': yili,
#             'narx' : narxi}
#     return avto
# avto1 = avto_info('GM', "Malibu", "Qora", "Avtomat",2024)
# avto2 = avto_info('GM', "Malibu", "Oq", "Mexanika",2024,30000)
# avtolar= [avto1,avto2]
# print("onlayin bozordagi avto mashinalar")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx= 'Nomalum'
#     print(f'{avto['color']} {avto['model']}. Narxi = {narx}')



# def oraliq(min, max):
#     sonlar = []
#     while min <max:
#         sonlar.append(min)
#         min+=1
#     return sonlar
# print(oraliq(0,10))


# print("Sayitimizdagi avtolar royxatini shakillantiramiz. ")
# avtolar = []
# while True:
#     print("Quyidagi malumotlarni kiriting . - ", end='\n ')
#     kompaniya = input("ishlab chiqaruvchi - ")
#     modeli = input(" Modeli - ")
#     rangi = input(" Rangi - ")
#     karobka = input(" Karobka - ")
#     yili = input(" Yilini kiriting - ")
#     narxi = input(" Nairxini kiriting - ")
#     avtolar.append(avto_info(kompaniya,modeli,rangi, karobka,yili,narxi))
#     javob = input("Yana qo'shasizni yes/no - ")
#     if javob == "yes":
#         continue
#
#     else:
#         print("Avtomabillar royxatga qo'shildi.. ")
#         # for avto in avtolar:
#         #     print(f'{avto['rangi']} {avto['modeli']} {avto['narxi']}')
#         print(avtolar)
#     break



# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"{ism.title} ning bahosini kiriting: ")
#         baholar[ism]= baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
#


# def summa(*sonlar):
#     """Kiritilgan sonlar yigindisini qaytaruvchi funksiya."""
#     yogindi = 0
#     for son in sonlar:
#         yogindi +=son
#     return yogindi
#
# print(summa(1,2,4))
#

# def summ(x,y,*sonlar):
#     return x+y+sum(sonlar)
#
# print(summ(5,6,6,7,8,8,5))
#




