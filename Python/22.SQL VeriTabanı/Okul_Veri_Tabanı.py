import mysql.connector
from connection import connection
from datetime import datetime 

ogrenciler=[ 
    ("101","Ahmet"  ,"Yılmaz",datetime(2005, 5, 17),"E"),
    ("102","Ali"    ,"Can",datetime   (2005, 6, 17)   ,"E"),
    ("103","Canan"  ,"Tan",datetime   (2005, 7, 7)    ,"K"),
    ("104","Ayşe"   ,"Taner",datetime (2005, 9, 23) ,"K"),
    ("105","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("106","Ali"    ,"Cenk",datetime  (2003, 8, 25)  ,"E")
]

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else : 
            self.id = id 
        self.name = name 
        self.studentNumber = studentNumber
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kyıt olusturuldu')
        except mysql.connector.Error as err :
            print("Hata: ", err)
        finally:
            Student.connection.close()

    @staticmethod        
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} tane kyıt olusturuldu')
        except mysql.connector.Error as err :
            print("Hata: ", err)
        finally:
            Student.connection.close()       

#ahmet = Student("131","Ahmet","Yılmaz",datetime(2005, 5, 17),"E")
#ahmet.saveStudent()
#Student.saveStudents(ogrenciler)   

    @staticmethod
    def StudentInfo():
        sql = "select * from student LIMIT 5"
        #sql = 'Select StudentNumber,Name,Surname From student '
        #sql = "select * from student where Gender LIKE '%K%' " 
        #sql = "select * from student where YEAR(birthdate) = 2003" #MOUTH() DAY()
        #sql = "select * from student where YEAR(birthdate) = 2005 name = 'Ali' " 
        #sql = "select * from student where name like '%an%' or surname like '%an%'"
        #sql = "select COUNT(*) from student where gender = 'E' "
            #result = Student.mycursor.fetchone()
        #sql = "select * from student where Gender LIKE '%K%' order by name,surname" 

        Student.mycursor.execute(sql)
        try:  
            result = Student.mycursor.fetchall()
            
            for product in result :
               print(f'no: {product[0]} Name: {product[1]} \a Surname: {product[2]} \a Birthdate: {product[3]}')

        except mysql.connector.Error as err :
            print("Hata: ", err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id = %s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try :
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err :
            print('Error', err)


    def updateStudent(self):
        sql = "UPDATE student SET studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s WHERE id=%s"
        values = (self.studentNumber, self.name, self.surname, self.birthdate, self.gender, self.id)

        Student.mycursor.execute(sql,values)

        try :
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount}tane kayıt güncellendi.')
        except mysql.connector.Error as err :
            print ("Hata: " ,err)

    @staticmethod
    def updateStudents(liste):
        sql = "UPDATE student SET studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s WHERE id=%s"
        values = []
        order =[1,2,3,4,5,0]
        for item in liste :
            item = [item[i]for i in order ]
            values.append(item)
        Student.mycursor.executemany(sql,values)

        try :
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount}tane kayıt güncellendi.')
        except mysql.connector.Error as err :
            print ("Hata: " ,err)

    @staticmethod
    def getStudentGender(gender):
        sql = "select * from student where gender = %s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try :
            return Student.mycursor.fetchall()
            
        except mysql.connector.Error as err :
            print('Error', err)
            
#student = Student.getStudentById(7)
#student.name = 'Çınar'
#student.surname = 'Turan'
#student.updateStudent()


students = Student.getStudentGender('E')
print(students)
liste=[]
for std in students:
    std = list(std)
    std [2] = 'Mr ' + std[2]
    liste.append(std)
Student.updateStudents(liste)
