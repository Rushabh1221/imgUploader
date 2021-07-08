from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == 'POST':
        fm = ImageForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
        fm = ImageForm()
        imge = Image.objects.all()
    return render(request, 'img/home.html', {'imge':imge, 'form':fm})


