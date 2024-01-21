from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .profileDao import StudentDao 

@csrf_exempt
def student(request):
    if request.method == 'POST':
        first_name= request.POST.get('firstName')
        last_name= request.POST.get('lastName')
        dob= request.POST.get('dob')
        photo= request.FILES.get('photo')
        resume= request.FILES.get('resume')
        student = StudentDao()
        studentDetails=student.addStudentData(first_name,last_name,dob,photo,resume)
        students = StudentDao.getAllStudentData()
        return render(request, 'student_list.html', {'students': students})
                      
    else:
        return render(request,'student_form.html')

@csrf_exempt
def student_list(request):
    student = StudentDao()
    students= student.getAllStudentData()
    return render(request, 'student_list.html', {'students': students})

@csrf_exempt
def delete_student(request, pk):
    student = StudentDao()
    student.deleteStudentData(pk)
    return redirect('student_list')


@csrf_exempt
def edit_student(request,pk):
    if request.method == 'POST':
        first_name= request.POST.get('firstName')
        last_name= request.POST.get('lastName')
        dob= request.POST.get('dob')
        photo= request.FILES.get('photo')
        resume= request.FILES.get('resume')
        student = StudentDao()
        studentDetails=student.editStudentData(pk,first_name,last_name,dob,photo,resume)
        students = StudentDao.getAllStudentData()
        return render(request, 'student_list.html', {'students': students})
                      
    else:
        return render(request,'edit_form.html')
