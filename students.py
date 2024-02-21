class Student:
    def __init__(self,name,studentNumber,department) -> None:
        self.name=name
        self.studentNumber = studentNumber
        self.department= department
    
    def studentInfo(self):
        print(f"Öğrenci adı: {self.name}, Öğrenci No:{self.studentNumber}, Okuduğu Bölüm: {self.department}")

    def departmentInfo(self):
        print(f"{self.name}, {self.department} bölümünde okuyor.")
        