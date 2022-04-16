from .models import Course, University, Entry
import django_filters


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = ['category', ]


class EntryFilter(django_filters.FilterSet):
    class Meta:
        model = Entry
        fields = ['course', 'university', ]



class CutOffFilter(django_filters.FilterSet):
    class Meta:
        model = Entry
        fields = ['cut_off', 'cut_off_max',]


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = ['category','name', ]
