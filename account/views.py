from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AccountAuthenticationForm
# from django.contrib.auth import authenticate, login
# from .models import user_type, User

# def signup(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         st = request.POST.get('student')
#         te = request.POST.get('teacher')
        
#         user = User.objects.create_user(
#             email=email,
#         )
#         user.set_password(password)
#         user.save()
        
#         usert = None
#         if st:
#             usert = user_type(user=user,is_student=True)
#         elif te:
#             usert = user_type(user=user,is_teach=True)
        
#         usert.save()
#         #Successfully registered. Redirect to homepage
#         return redirect('explore')
#     return render(request, 'register.html')
    
# def login(request):
#     if (request.method == 'POST'):
#         email = request.POST.get('email') #Get email value from form
#         password = request.POST.get('password') #Get password value from form
#         user = authenticate(request, email=email, password=password)
        
#         if user is not None:
#             login(request, user)
#             type_obj = user_type.objects.get(user=user)
#             if user.is_authenticated and type_obj.is_student:
#                 return redirect('shome') #Go to student home
#             elif user.is_authenticated and type_obj.is_teach:
#                 return redirect('thome') #Go to teacher home
#         else:
#             # Invalid email or password. Handle as you wish
#             return redirect('home')

#     return render(request, 'home.html')


# def shome(request):
#     if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
#         return render(request,'student_home.html')
#     elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
#         return redirect('thome')
#     else:
#         return redirect('login')
                      
# def thome(request):
#     if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
#         return render(request,'teacher_home.html')
#     elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
#         return redirect('shome')
#     else:
#         return redirect('explore')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('for_explore')
        else:
            context['registration_form'] = form
    
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)

def logout_view(request):
    logout(request)
    return redirect('for_explore')

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('for_explore')
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect("for_explore")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)
    