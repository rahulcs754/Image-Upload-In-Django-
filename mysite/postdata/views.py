from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.files.storage import FileSystemStorage #image upload code

# Create your views here.
from .forms import ProfileForm
from .models import Profile


def index(request):
    alldata = Profile.objects.all()
    return render(request, 'index.html',{ 'data':alldata })

#@csrf_protect
def result(request):
    saved = False
    if request.method == 'POST' and request.FILES['picture']:
        #Get the posted form
        myfile = request.FILES['picture']
        ''' 
        Start code | move file to project folder scripts
        '''
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        saved = True
        if saved == True:
            output = "Your file is upload"
        ''' 
        End code
        '''    

        #*********************************
        #*********************************

        ''' Start Code Here '''
        title = request.POST.get('description','')
        myfile1 = request.FILES['picture'] 

        obj = Profile(name=title, picture=myfile1)
        # obj.name = title
        # obj.picture = myfile1
        obj.save()
        #return redirect('/')
        output += "save data"
        ''' End code '''
        alldata = Profile.objects.all()

    #return HttpResponse(upimage)
    return render(request,'index.html', { 'result': output,'data':alldata })

