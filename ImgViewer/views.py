from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import loader
from django.core.files.storage import FileSystemStorage

from ImgViewer.models import MyImage
from ImgViewer.forms import ImageForm
from PIL import Image
from posixpath import basename
# Create your views here.

def home(request):
    return render(request, 'home.html', {'idpic' : MyImage.objects.all().order_by("id")[0].id})
    

def listing(request):
    pictures = MyImage.objects.all()
    return render(request, 'listing.html', {'object_list' : pictures})

def ViewPicture(request, id_picture):
    picture = MyImage.objects.get(id=id_picture)
    return render(request, 'picture.html', { 'img' : picture.image.name })


def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
           
        if form.is_valid():
            form.save()
            return render(request, 'upload/model_form_upload.html', {
                'form': form, 'uploaded_file_url' : "File uploaded"
            })
    else:
        form = ImageForm()
    return render(request, 'upload/model_form_upload.html', {
        'form': form
})


def keepPicture(request):
    prev = request.META.get('HTTP_REFERER')
    if prev:
        imgid = int(basename(request.META.get('HTTP_REFERER')))
        myimg = MyImage.objects.get(id=imgid)
        myimg.verified = True
        myimg.rejected = False
        myimg.save()
        return redirect(prev)
    return HttpResponse("fail")

def rejectPicture(request):
    prev = request.META.get('HTTP_REFERER')
    if prev:
        imgid = int(basename(request.META.get('HTTP_REFERER')))
        myimg = MyImage.objects.get(id=imgid)
        myimg.verified = True
        myimg.rejected = True
        myimg.save()
        return redirect(prev)
    return HttpResponse("fail")

def prevPic(request):
    prev = request.META.get('HTTP_REFERER')
    if prev:
        imgid = int(basename(request.META.get('HTTP_REFERER')))
        if imgid == 1:
            return redirect(prev)
        if MyImage.objects.filter(id=imgid-1).exists():
            myimg = MyImage.objects.get(id=imgid-1)
            if myimg:
                return redirect("/picture/"+str(imgid-1))
            return redirect(prev)
        else:
            i = 2
            while imgid - i != 0:
                if MyImage.objects.filter(id=imgid-i).exists():
                    return redirect("/picture/"+str(imgid-1))
                ++i;
            return redirect(prev)
    return HttpResponse("fail")

def nextPic(request):
    prev = request.META.get('HTTP_REFERER')
    if prev:
        imgid = int(basename(request.META.get('HTTP_REFERER')))
        if (imgid == MyImage.objects.all().order_by("-id")[0].id):
            return redirect(prev)
        if MyImage.objects.filter(id=imgid+1).exists():
            myimg = MyImage.objects.get(id=imgid+1)
            if myimg:
                return redirect("/picture/"+str(imgid+1))
            return redirect(prev)
        else:
            i = 2
            while imgid + i != MyImage.objects.all().order_by("-id")[0].id:
                if MyImage.objects.filter(id=imgid+i).exists():
                    return redirect("/picture/"+str(imgid+1))
                ++i;
            return redirect(prev)
    return HttpResponse("fail")
