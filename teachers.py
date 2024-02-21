class Teacher:
    def __init__(self,name,teacherId,department) -> None:
        self.name=name
        self.teacherId = teacherId
        self.department= department
    
    def teacherInfo(self):
        print(f"Öğretmen adı: {self.name}, Öğretmen id:{self.teacherId}, Çalıştığı Bölüm: {self.department}")

    def departmentInfo(self):
        print(f"{self.name}, {self.department} bölümünde çalışıyor.")
        