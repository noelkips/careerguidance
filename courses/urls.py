from django.urls import path
from . import views
from .import knowlege_base
from .views import (
    CourseDetailView,
    CategoryDetailView,
    CourseUpdateView,
    CourseCreateView,
    CourseDeleteView,
    UniversityDetailView,
    UniversityCreateView,
    UniversityUpdateView,
    UniversityDeleteView,
    EntryDetailView,
    EntryCreateView,
    EntryDeleteView,
    EntryUpdateView,
)

app_name = 'course'
urlpatterns = [
    path('', views.index, name="index"),
    path('career-types/<int:pk>/', CategoryDetailView.as_view(), name="career_type_detail"),
    path('career-types/<int:pk>/courses/', views.category_courses, name="categories"),
     path('career-types/<int:pk>/courses/entries/', views.entry_list_view, name='entries'),

    path('<slug:slug>/<int:pk>/', views.CareerCourseView.as_view(), name="category_courses"),
    path('realistic_courses/', views.realistic_courses, name="realistic_courses"),
    path('investigative_courses/', views.investigative_courses, name="investigative_courses"),
    path('artistic_courses/', views.artistic_courses, name="artistic_courses"),
    path('social_courses/', views.social_courses, name="social_courses"),
    path('enterprising_courses/', views.enterprising_courses, name="enterprising_courses"),
    path('conventional_courses/', views.conventional_courses, name="conventional_courses"),
    
   

    
    path('private_universities/', views.private_universities_view, name="private_universities"),
    path('public_universities/', views.public_universities_view, name="public_universities"),
  

    path('course/<int:pk>/', CourseDetailView.as_view(), name="course_detail"),
    path('course/new/', CourseCreateView.as_view(), name='course_new'),
    path('<slug:slug>/', views.CourseListView.as_view(), name='career_course'),
    path('course/<int:pk>/edit/',CourseUpdateView.as_view(), name='course_edit'),
    path('course/<int:pk>/delete/',CourseDeleteView.as_view(), name='course_delete'),

    path('entries/<int:pk>/',EntryDetailView.as_view(), name="entry_detail"),
    path('entries/new/',EntryCreateView.as_view(), name='entry_new'),
    
    path('entries/<int:pk>/edit/',EntryUpdateView.as_view(), name='entry_edit'),
    path('entries/<int:pk>/delete/',EntryDeleteView.as_view(), name='entry_delete'),

    path('universities/<int:pk>/', UniversityDetailView.as_view(), name="university_detail"),
    path('universities/new/', UniversityCreateView.as_view(), name='university_new'),
    path('universities/<int:pk>/edit/',UniversityUpdateView.as_view(), name='university_edit'),
    path('universities/<int:pk>/delete/',UniversityDeleteView.as_view(), name='university_delete'),


    
    
    path('qualification', views.qualification, name="qualification"),
    path("points", views.points, name="points"),
    path("consult", knowlege_base.consult, name="consult"),
    path("querying", views.queries, name='querying'),

    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

]
