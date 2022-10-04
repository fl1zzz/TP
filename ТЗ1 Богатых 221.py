class Contacts:
    def __init__(self):
        self.database = [[], [], [], [], [], []]

    def __add__(self, contact):
        self.database[0].append(len(self.database[0]) + 1)
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.database[1].append(fio[0])
        self.database[2].append(fio[1])
        self.database[3].append(fio[2])
        if contact.phone != '':
            self.database[4].append(contact.phone)
        else:
            self.database[4].append(None)
        if contact.mail != '':
            self.database[5].append(contact.mail)
        else:
            self.database[5].append(None)

    def getContact(self, id):
        ans = "ID - " + str(self.database[0][id]) + "\n"
        if self.database[1][id] != None:
            ans += "ФИО: " + self.database[1][id]
        if self.database[2][id] != None:
            ans += " " + self.database[2][id]
        if self.database[3][id] != None:
            ans += " " + self.database[3][id]
        if self.database[4][id] != None:
            ans += "\n" + "Номер телефона: " + self.database[4][id]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.database[5][id] != None:
            ans += "\n" + "Почта: " + self.database[5][id] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def phoneSearch(self, phone):
        if self.database[4].__contains__(phone):
            id = self.database[4].index(phone)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")

    def mailSearch(self, mail):
        if self.database[5].__contains__(mail):
            id = self.database[5].index(mail)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")

    def search(self, fio):
        ids = []
        if fio[0] != None:
            for i in range(len(self.database[1])):
                if fio[0] == self.database[1][i]:
                    ids.append(self.database[0][i] - 1)
        if fio[1] != None:
            if fio[0] != None:
                for id in ids:
                    if fio[1] != self.database[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.database[2])):
                    if fio[1] == self.database[2][i]:
                        ids.append(self.database[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in ids:
                    if fio[2] != self.database[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.database[3])):
                    if fio[2] == self.database[3][i]:
                        ids.append(self.database[0][i] - 1)

        if len(ids) == 0:
            print("Ничего не найдено")
        else:
            for id in ids:
                print(self.getContact(id))

    def getWithoutPhoneOrMail(self, num):
        # 1 без номера, 2 без почты, 3 без обоих
        if num == 1:
            for i in range(len(self.database[4])):
                if self.database[4][i] == None:
                    print(self.getContact(i))
            return
        if num == 2:
            for i in range(len(self.database[5])):
                if self.database[5][i] == None:
                    print(self.getContact(i))
            return
        if num == 3:
            for i in range(len(self.database[4])):
                if self.database[4][i] == None and self.database[5][i] == None:
                    print(self.getContact(i))
            return

    def change(self, id, contact):
        id -= 1
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.database[1][id] = fio[0]
        self.database[2][id] = fio[1]
        self.database[3][id] = fio[2]
        if len(contact.phone) > 0:
            self.database[4][id] = contact.phone
        else:
            self.database[4][id] = None
        if len(contact.mail) > 0:
            self.database[5][id] = contact.mail
        else:
            self.database[5][id] = None

    def printAll(self):
        for i in range(len(self.database[0])):
            print(self.getContact(i))

class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

def printCommands():
    print("Команды: ")
    print("1 - Вывести все контакты", "2 - Поиск по телефону", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - поиск по отсутствию номера/почты", "6 - Изменение контакта", "7 - Остановить программу", sep="\n")


print("Введите имя файла")
fileName = input()
file = open(fileName, encoding='utf-8')
base = Contacts()
for list in file:
    arr = list.split(",")
    contact = Contact(arr[0],arr[1].replace(" ",""),arr[2].replace(" ","").replace("\n",""))
    base.__add__(contact)
print("База готова")
printCommands()
vvod = int(input())
while vvod!="akdna@@@kdn":
    if vvod==1:
        base.printAll()
    elif vvod==2:
        print("Введите телефон")
        phone = input()
        base.phoneSearch(phone)
    elif vvod == 3:
        print("Введите почту")
        mail = input()
        base.mailSearch(mail)
    elif vvod == 4:
        fio = []
        print("Введите фамилию, либо оставьте пустую строку")
        f = input()
        if f=='':
            fio.append(None)
        else:
            fio.append(f)
        print("Введите имя, либо оставьте пустую строку")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Введите отчество, либо оставьте пустую строку")
        o = input()
        if o == '':
            fio.append(None)
        else:
            fio.append(o)
        base.search(fio)
    elif vvod == 5:
        print("Введите по чему хотите искать: ", "1 - без номера", "2 - без почты", "3 - без обоих", sep="\n")
        num = int(input())
        base.getWithoutPhoneOrMail(num)
    elif vvod == 6:
        print("Введите id контакта, который хотите изменить и новые данные для него", "(в две разные строки)", sep="\n")
        id = int(input())
        newinfo = input().split(",")
        contact = Contact(newinfo[0], newinfo[1].replace(" ", ""), newinfo[2].replace(" ", "").replace("\n", ""))
        base.change(id, contact)
    elif vvod == 7:
        "Программа закрыта"
        break
    print()
    printCommands()
    vvod = int(input())