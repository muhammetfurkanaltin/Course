class Teacher:
    def __init__(self,id,branch,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else : 
            self.id = id 
        self.name = name 
        self.branch = branch
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender