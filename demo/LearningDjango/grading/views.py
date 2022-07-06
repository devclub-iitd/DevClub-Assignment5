from django.shortcuts import render, get_object_or_404
from .models import Grade
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        studentid = request.user.id
        grade = get_object_or_404(Grade, student_id=studentid)
        course = grade.course
        marks = grade.marks
        return HttpResponse(f"You have scored {marks} marks in {course} course!")
    else:
        return HttpResponse("You are not logged in")
