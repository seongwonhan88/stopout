from django.shortcuts import render

# Create your views here.
from .models import School


def school_list(request):
    schools = School.objects.all()

    context = {
        'schools': schools
    }

    return render(request, 'school/school_list.html', context)


def school_detail(request, school_id):
    school = School.objects.get(id=school_id)
    context = {
        'school': school
    }

    return render(request, 'school/school_detail.html', context)

