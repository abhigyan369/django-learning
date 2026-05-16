from django.shortcuts import render
from .forms import StudentForm
from .models import Course

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    return render(request, 'register.html', {'form': form})


def course_students(request):
    courses = Course.objects.all()
    students = []

    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(id=course_id)
        students = course.student_set.all()

    return render(request, 'course_students.html', {
        'courses': courses,
        'students': students
    })