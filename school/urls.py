from django.urls import path

from . import views



urlpatterns = [

    path('', views.show_homepage, name='homepage'),

    path('schools/', views.show_schools, name='schools'),

    path('assessment_areas/', views.show_assessment_areas, name='assessment_areas'),

    path('awards/', views.show_awards, name='awards'),

    path('student_class/', views.show_student_class, name='student_class'),

    path('student/', views.show_student, name='student'),

    path('subject/', views.show_subject, name='subject'),

    path('answers/', views.show_answers, name='answers'),

    path('summery/', views.show_summery, name='summery'),


]
