from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.


def index(res):
    return HttpResponse('<h1>Hello world!</h1>')


# def student_by_id(res, student_id):
#     student = Student.objects.get(pk=student_id)
#     return HttpResponse(f"id: {student.id}, Họ tên: {student.name}, MSSV: {student.mssv}, Ngày sinh: {student.bday}")

# render template
def student_by_id(res, student_id):
    student = Student.objects.get(pk=student_id)
    return render(res, 'student_details.html', {'student': student})
