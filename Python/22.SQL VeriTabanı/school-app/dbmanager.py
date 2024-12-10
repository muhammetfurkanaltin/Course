import mysql.connector
from connection import connection
from datetime import datetime 
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager :
    def __init__(self):
        self.connection = connection 
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "Select * from student where id = %s"
        value = (id,)
        self.cursor.execute(sql ,value)
        try :
            obj = self.cursor.fetchone()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def deleteStudent(self,studentid):
        sql = "delete from student where id =%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane ögrenci silindi.')
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def getClasses(self):
        sql = "Select * from class "
        self.cursor.execute(sql)
        
        try :
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def getStudentClassId(self,classid):
        sql = "Select * from student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql ,value)
        try :
            obj = self.cursor.fetchall()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kyıt olusturuldu')
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def editStudent(self, student: Student):
        sql = "UPDATE student SET studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s, classid =%s WHERE id=%s "
        value = (student.studentNumber, student.name, student.surname, student.birthdate, student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} tane kayıt güncellendi')
        except mysql.connector.Error as err :
            print("Hata: ", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass
    
    def __del__(self):
        self.connection.close()
        print("db silindi")

db = DbManager()
student = db.getStudentById(7)

student[0].name = "ahmet"


#db.addStudent(student[0])
db.editStudent(student[0])


#students = db.getStudentClassId(1)
#print(students[0].name)
#print(students[4].name)