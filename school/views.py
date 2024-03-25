from django.shortcuts import render

from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import School


def show_homepage(request):
    
    return render(request, 'school/homepage.html')

def show_schools(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/schools.html', {'data': data})


def show_assessment_areas(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/assessment_areas.html', {'data': data})


def show_awards(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/awards.html', {'data': data})


def show_student_class(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/student_class.html', {'data': data})


def show_student(request):
    data_list = School.objects.all()  

    paginator = Paginator(data_list, 100)  

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/student.html', {'data': data})


def show_subject(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/subject.html', {'data': data})
    

def show_answers(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/answers.html', {'data': data})



def show_summery(request):
    data_list = School.objects.all()  # This retrieves all records from the table

    paginator = Paginator(data_list, 100)  # Show 25 records per page

    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)

    return render(request, 'school/summery.html', {'data': data})