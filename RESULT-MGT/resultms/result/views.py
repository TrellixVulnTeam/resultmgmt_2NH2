from django.shortcuts import *
from .models import *

# Create your views here.
def home(request):
    context = {}
    if request.POST.get('rollno') is not None:
        try:
            student = Student.objects.get(rollNo=request.POST.get('rollno').lower())
            print(student)
            context = {
                'Student': student,
                'Results': Result.objects.filter(student=student)
            }
        except Student.DoesNotExist:
            context = {
                "ERROR": 'student does not Exist'
            }
    return render(request, 'home.html', context)