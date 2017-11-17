from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    courses = Course.objects.all()
    courses_list = []
    for course in courses:
        name = course.course_name
        course_id = course.id
        created_at = course.created_at
        description = course.description.description
        courses_list.append({'course_name': name, 'description': description, 'created_at': created_at, 'id': course_id})
    context = {
        "courses_list": courses_list
    }
    return render(request, 'courses/index.html', context)

def create(request):

    errors = Course.objects.validate(request.POST)
    description_errors = Description.objects.validate(request.POST)
    errors.update(description_errors)

    if len(errors):
        print(errors)
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        c = Course.objects.create(course_name=request.POST['course_name'])
        Description.objects.create(description=request.POST['description'],course=c)
        return redirect('/')
    return redirect('/')

def destroy_request(request, course_id):
    c = Course.objects.get(id=course_id)
    course = {}
    course['name'] = c.course_name
    course['description'] = c.description.description
    course['id'] = course_id
    context = {
        "course": course
    }
    return render(request, 'courses/delete.html', context)

def destroy(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/')