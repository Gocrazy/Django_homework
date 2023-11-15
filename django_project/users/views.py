from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from django.template.loader import render_to_string
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.core.mail import EmailMessage, send_mail
from .models import CustomUser
from .tokens import generate_token


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def signup(request):
    current_site = get_current_site(request) 
    print('domain ', current_site.domain)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): 
            print('signup post ', form.is_valid())
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  

            current_site = get_current_site(request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('acc_active_email.html', {  
                'user': user,  
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return redirect('login')
        
    else:  
        form = CustomUserCreationForm()   
    return render(request, "signup.html", {'form': form})

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = CustomUser.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('login')
    else:
        return render(request,'activation_failed.html')