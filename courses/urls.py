from django.urls import path
from . import views
from .views import (
    CourseDetailView,
    CategoryView,
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
    path('course', views.search, name="courses"),
    path('entries/', views.entries, name='entries'),
    path('universities/', views.universities, name="universities"),

    path('course/<int:pk>/', CourseDetailView.as_view(), name="course_detail"),
    path('course/new/', CourseCreateView.as_view(), name='course_new'),
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

    # path('courses/', views.coursepageview, name="courses"),
    path('category/', views.CategoryView, name="category"),
    path('qualification', views.qualification, name="qualification"),
    path("points", views.points, name="points"),
    path("consult", views.consult, name="consult"),
    path("querying", views.queries, name='querying'),

    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

]
