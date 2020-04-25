from django.db import models

# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    Updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    file_number=models.CharField(max_length=255)
    address=models.TextField()
    profile_pic=models.FileField()
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()
    
class Grades(models.Model):
    id=models.AutoField(primary_key=True)
    grade_name=models.CharField(max_length=255)
    stream=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Subjects(models.Model):
    id=models.AutoField(primary_key=True)
    subject_name=models.CharField(max_length=255)
    grade_id=models.ForeignKey(Grades,on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField()
    address=models.TextField()
    grades_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    subject_id=models.ForeignKey(Subjects,on_delete=models.DO_NOTHING)
    attendance_date=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class AttendanceReport(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.DO_NOTHING)
    attendance_id=models.ForeignKey(Attendance,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StudentLeaveReport (models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students, on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StaffLeaveReport (models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs, on_delete=models.CASCADE)
    leave_date=models.CharField(max_length=255)
    leave_message=models.TextField()
    leave_status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StudentFeeback(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    feedback=models.TextField()
    feedback_reply=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StaffFeeback(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    feedback=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StudentNotification(models.Model):
    id=models.AutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()

class StaffNotification(models.Model):
    id=models.AutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=models.Manager()



    





 