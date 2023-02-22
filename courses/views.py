import math
from django.views.generic import ListView, DetailView

from .models import Course, University, Entry, Category
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import QuestionsForm
from django.urls import reverse_lazy


def index(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories":categories})

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'career_type_detail.html'
    context_object_name= "category"


def category_courses(request, pk):
    category_name = get_object_or_404(Category, pk=pk)
    career = Course.objects.filter(category=category_name)
    context = {
        'courses': career,

    }
    return render(request, 'search/courses.html',  context)

class CareerCourseView(DetailView):
    model = Course
    template_name = 'search/courses.html'
    context_object_name= "courses"

class CourseListView(DetailView):
    model = Category
    template_name = 'search/courses.html'
    context_object_name= "categories"



def realistic_courses(request):
    course_list = Course.objects.filter(category = 2)
    return render(request, 'search/courses.html',  {'courses': course_list})

def investigative_courses(request):
    course_list = Course.objects.filter(category = 3)
    return render(request, 'search/courses.html',  {'courses': course_list})  

def artistic_courses(request):
    course_list = Course.objects.filter(category = 4)
    return render(request, 'search/courses.html',  {'courses': course_list})

def social_courses(request):
    course_list = Course.objects.filter(category = 5)
    return render(request, 'search/courses.html',  {'courses': course_list})

def enterprising_courses(request):
    course_list = Course.objects.filter(category = 6)
    return render(request, 'search/courses.html',  {'courses': course_list})

def conventional_courses(request):
    course_list = Course.objects.filter(category = 7)
    return render(request, 'search/courses.html',  {'courses': course_list}) 


def entry_list_view(request, pk):
    entry_list = Entry.objects.all()
    return render(request, "search/entries.html", {'entries':entry_list})


# def course_entries(request, slug):
#     course_name = get_object_or_404(Course, slug=slug)
#     career = Entries.objects.filter(course=course_name)
#     context = {
#         'entries': career,

#     }
#     return render(request, 'search/entries.html',  context)



def private_universities_view(request):
    universities = University.objects.filter(category = "private")
    return render(request, 'university/universities.html', {'universities': universities})


def public_universities_view(request):
    universities = University.objects.filter(category = "public")
    return render(request, 'university/universities.html', {'universities': universities})
   


class EntryDetailView(DetailView):
    model = Entry
    template_name = 'entry_detail.html'


class EntryCreateView(CreateView):
    model = Entry
    template_name = 'entry_new.html'
    fields = '__all__'


class EntryUpdateView(UpdateView):
    model = Entry
    template_name = 'entry_edit.html'
    fields = ['course', 'cut_off', 'university']


class EntryDeleteView(DeleteView):
    model = Entry
    template_name = 'university_delete.html'
    success_url = reverse_lazy('course:entries')


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'




class UniversityDetailView(DetailView):
    model = University
    template_name = 'university_detail.html'




def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('entries')
    return render(request, 'login/login.html')


def qualification(request):
    return render(request, "calculation/qualification.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def points(request):
    group1 = int(request.POST['A'])
    group2 = int(request.POST['B'])
    group3 = int(request.POST['C'])
    group4 = int(request.POST['D'])
    arg = int(request.POST['AGR'])
    sum_points = group1 + group2 + group3 + group4
    val1 = sum_points / 48
    val2 = arg / 84
    x = val1 * val2
    square = math.sqrt(x)
    res = math.floor(square * 48)
    context = {
        'result': res,
        'first_subject': group1,
        'second_subject': group2,
        'third_subject': group3,
        'fourth_subject': group4,
        'Aggregate_points': arg,

    }
    return render(request, "calculation/points.html", context)


def queries(request):
    context = {}
    context['form'] = QuestionsForm

    return render(request, "consult/querying.html", context)


