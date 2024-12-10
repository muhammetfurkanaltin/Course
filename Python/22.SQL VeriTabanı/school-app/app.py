from dbmanager import DbManager
from Student import Student
import datetime 
class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "****\n1-Ögrenci Listesi\n2-Ögrenci Ekle\n3-Ögrenci Güncelle\n4-Ögrenci sil\n5-Ögretmen Ekle\n6-Siniflara Göre Dersler\n7-Çikiş(E\Ç)"

        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "E" or islem == "Ç":
                break
            else :
                print ("Yanliş Seçim")

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('Ögrenci id : '))
        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()

        studentid = int(input('Ögrenci id : '))

        student = self.db.getStudentById(studentid)
        student[0].name= input('name: ') or student[0].name
        student[0].surname= input('surname: ') or student[0].surname
        student[0].gender= input('cinsiyet(E/K): ') or student[0].gender
        student[0].classid= input('sinif: ') or student[0].classid

        year = input('yil: ') or student[0].birthdate.year
        month = input('ay: ') or student[0].birthdate.month
        day = input('gün: ') or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])

    def addStudent(self):
        self.displayClasses()
        classid = int(input("hangi sinif: "))
        number  = input('Numara: ')
        name    = input('Ad: ')
        surname = input('Soyad: ')
        year    = int(input('Yıl: '))
        month   = int(input('Ay: '))
        day     = int(input('Gün: '))
        birthdate = datetime.datetime(year,month,day)
        gender =input('cinsiyet (E/K)')

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()

        classid = int(input("hangi sinif: "))

        students = self.db.getStudentClassId(classid)
        print("Ögrenci Listesi")

        for std in students:
            print(f'{std.id} {std.name} {std.surname}')
        return classid

app = App()
app.initApp()
