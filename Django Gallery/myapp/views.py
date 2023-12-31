from django.shortcuts import render,redirect
from .models import Image
from .forms import ImageForm

# Create your views here.

def home(request):
    if request.method=='POST':
        form=ImageForm(request.POST,request.FILES)#request.FILES as it is a file
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ImageForm()
    img=Image.objects.all()
    return render(request,'myapp/home.html',{'form':form,'img':img})
