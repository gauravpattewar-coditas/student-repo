from student_profile.models import Student

class StudentDao:
    def addStudentData(self, first_name, last_name, dob, photo, resume ):
        new_employee = Student(first_name=first_name, last_name=last_name, dob=dob, photo=photo, resume=resume)
        new_employee.save()
        return new_employee
    
    @staticmethod
    def getAllStudentData():
        return Student.objects.all()
    
    def deleteStudentData(self, student_id):
            student = Student.objects.get(id=student_id)
            student.delete()
            return True
               
    def editStudentData(self, student_id, first_name, last_name, dob, photo, resume):
            student = Student.objects.get(id=student_id)
            student.first_name = first_name
            student.last_name = last_name
            student.dob = dob
            student.photo = photo
            student.resume = resume
            student.save()
            return student 