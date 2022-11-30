from django.shortcuts import render

# Create your views here.
def honey(request):
    return render(request,'honey.html')
