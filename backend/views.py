from django.shortcuts import render
from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.template import loader
from django.contrib.auth import authenticate, login
from .forms import CustomSigninForm, CustomSignupForm,FileUploadForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import CustomUser
# Create your views here.

def isauthenticated(request):
    my_data = request.session.get('user', None)
    if my_data:
       return True
    else:
        return False


@api_view(['GET'])
def index(request):
    template = loader.get_template('index.html')
    print("Database failure")
    return render(request, 'index.html', {'isauthenicated': isauthenticated(request=request)})


@api_view(['GET'])
def login(request):
    if not isauthenticated(request=request):   
        form = CustomSigninForm()
        return render(request, 'login1.html', {'form': form})
    else:
        return redirect('homepage')


@api_view(['GET'])
def signup(request):
    if not isauthenticated(request=request):   
        form = CustomSignupForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('homepage')

@api_view(['POST'])
def authenticate(request):
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user =CustomUser.objects.create_user(email=email, password=password)
            request.session['user']=email
            # Redirect or return JSON response indicating success
            return redirect('homepage')
        else:
            print(form.errors)
            # Return JSON response with form errors
            return redirect('signup')
        
@api_view(['POST'])
def custom_login(request):
    form = CustomSigninForm(request.POST)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            user = CustomUser.objects.get(email=email)
            request.session['user']=email
            # Redirect to a success page.
            return redirect('homepage')
        except:
            print('hello')
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        print(form.errors)
        # Return JSON response with form errors
        return redirect('login')
        

@api_view(['GET'])
def homepage(request):
    if isauthenticated(request):
       form = FileUploadForm()
       return render(request, 'homepage.html',{'isauthenicated': isauthenticated(request=request),'form':form})
    else:
        return redirect('signup')

@api_view(['POST'])    
def upload_file(request):
    form = FileUploadForm(request.POST, request.FILES)
    if form.is_valid():
        # Handle the file
        uploaded_file = form.cleaned_data['file']
        file_name = uploaded_file.name
        file_extension = file_name.split('.')[-1].lower()
        if file_extension == 'csv':
            # Handle CSV file
            pass
        elif file_extension == 'xlsx':
            # Handle XLSX file
            pass
        else:
            # Invalid file type, return error response
            return JsonResponse({'error': 'Invalid file type'}, status=500)
        return JsonResponse({'message':'successful'})
    else:
        return JsonResponse({'imessage':'unsuccessful'})


@api_view(['GET'])
def aboutus(request):
    template = loader.get_template('aboutus.html')
    print("Database failure")
    return render(request, 'aboutus.html', {'isauthenicated': isauthenticated(request=request)})


@api_view(['GET'])
def logout(request):
    try:
        del request.session['user']
        return redirect('signup')
    except:
        return redirect('signup')
