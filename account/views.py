from django.shortcuts import redirect, render
from .forms import SignINForm,SignUpForm
from django.contrib.auth import authenticate,login
# from django.contrib.auth.models import User
from account.models import User
from django.contrib.auth import logout
from .forms import UploadImageForm
from .models import User
from .models import Profile_pic

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token import account_activation_token
from django.core.mail import EmailMessage
from django.http import HttpResponse

# Create your views here.
def logout_user(request):
    logout(request)
    return redirect("/")

def index(request):

    login_form = SignINForm(request.POST,None)

    
    context = {
        'login' : login_form
    }
    
    if login_form.is_valid:
        username = request.POST.get("email")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request,username = username, password = password )
        print("jjja",user)
        if user is not None:
        
            login(request,user)
            return redirect("mainapp:index")
        else:
            pass
    return render(request,'signin.html',context)


def signup(request):
    sign_up = SignUpForm(request.POST,None)

    context =  { 
        "form" :sign_up
    }
    if request.method =='POST':
        if sign_up.is_valid:
            username = request.POST.get("username")
            first_name = request.POST.get("first_name")
            last_name =  request.POST.get("last_name")
   
            phone =  request.POST.get("phone")
            email = request.POST.get('email')
            password = request.POST.get("password")
            user = authenticate(request,username = email, password = password )
            if user is not None:
                print("user exists")
                return redirect("account:sign_in")
            else:
                
                user = User.objects.create_user(username = username , email = email , password = password)
                user.last_name = last_name
                user.first_name = first_name
                user.phone = phone
                user.is_active =  False
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()
                return HttpResponse('We have sent you an email, please confirm your email address to complete registration')

    return render(request,'signup.html',context)


def profile_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
  
        if form.is_valid():
            image =  request.FILES["image"]
            if request.user.is_authenticated:
                user =  request.user.id
                user_obj =  User.objects.get(id=  user)
                obj,created =  Profile_pic.objects.get_or_create(user_id = user_obj)
                obj.image = image
                obj.save()

                return redirect("/")


            else:
                return redirect("accounts:sign_in")
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form' : form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        current_site = get_current_site(request)
        email_subject = 'Successfull Registration'
        message = render_to_string('successfull_regestration.html', {
        'user': user,
        'domain': current_site.domain
        })
        to_email = user.email
        email = EmailMessage(email_subject, message, to=[to_email])
        email.send()

        return HttpResponse('Your account has been activate successfully')
        
    else:
        return HttpResponse('Activation link is invalid!')
    

    