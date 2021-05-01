from django.shortcuts import render
from django.http import HttpResponse
from students.models import Studentdetails
from students.models import Courseinfo
from students.models import Registrar
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    context = {'firstname':'Rachel', 'lastname':'Worley'}
    return render(request, 'students/home.html', context)

@login_required
def studentdetails(request):
    students = Studentdetails.objects.all()
    paginator = Paginator(students, 10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)
    return render(request, 'students/studentdetails.html', {'details':studentdata})

@login_required    
def courseinfo(request):
    courses = Courseinfo.objects.all()
    paginator = Paginator(courses, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
    return render(request, 'students/courseinfo.html', {'info':coursedata})

@login_required  
def registrar(request):
    regcourse = Courseinfo.objects.all()
    regstudent = Studentdetails.objects.all()
    regdata = ""
    if('studentid' in request.session):
        regdata = Registrar.objects.filter(studentid = request.session['studentid'])

    if('wizid' in request.GET and 'course' not in request.GET):
        wizid = request.GET.get('wizid')
        request.session['studentid'] = wizid
        return HttpResponse('Success')

    if('wizid' in request.GET and 'course' in request.GET):
        wizid = request.GET.get('wizid')
        course = request.GET.get('course')
        courseregistrar = Courseinfo.objects.filter(coursename=course)
        courseid = courseregistrar.values()[0]['courseid']
        name = courseregistrar.values()[0]['coursename']
        instructor  = courseregistrar.values()[0]['instructorname']
        regdata = Registrar.objects.filter(studentid= wizid)
        count = 0
        for row in regdata:
            count = count+1
            if count >= 3:
                return HttpResponse('Course1')
            if row.coursename == course:
                return HttpResponse('Course2')

        newdata= Registrar(studentid = wizid, courseid=courseid, coursename=name, instructorname=instructor)
        newdata.save()
        
        return HttpResponse('Success')
    return render(request, 'students/registrar.html', {'students': regstudent, 'regcourse': regcourse, 'registrar': regdata})

