from django.shortcuts import render

# Create your views here.

def course_list(request):
    return render(request, 'mysite/course_list.html', {})
