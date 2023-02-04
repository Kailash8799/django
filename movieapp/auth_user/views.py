from django.shortcuts import render, redirect
from .models import User,Contact
from django.contrib.auth.hashers import make_password, check_password
# from django.core.mail import send_mail
# Create your views here.


def login(request):
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        return redirect('/')
    params = {'success': False}
    if (request.method == 'POST'):
        u_email = request.POST.get('u_email', '')
        u_password = request.POST.get('u_password', '')
        if (len(u_email) > 5 and len(u_password) > 4):
            usr1 = User.objects.filter(user_email=u_email)
            print(usr1.values_list)
            if (usr1):
                upass = ""
                for item in usr1:
                    upass = item.user_password
                if (check_password(u_password,upass)):
                     responce = redirect('/')
                     responce.set_cookie('u_logincred',u_email)
                     return responce
                else:
                    params = {
                        'message': "Invalid credentials", 'success': True}
                    return render(request, 'auth_user/login.html', params)
            else:
                params = {'message': "User does not exist", 'success': True}
                return render(request, 'auth_user/login.html', params)
        else:
            params = {
                'message': "Enter a minimum 5 character in every fields", 'success': True}
    else:
        params = {'message': "Some error accured!", 'success': False}
        return render(request, 'auth_user/login.html', params)
    return render(request, 'auth_user/login.html',params)


def signup(request):
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        return redirect('/')
    params = {'success': False}
    if (request.method == 'POST'):
        u_name = request.POST.get('u_name', '')
        u_email = request.POST.get('u_email', '')
        u_password = request.POST.get('u_password', '')
        if (len(u_name) > 3 and len(u_email) > 5 and len(u_password) > 4):
            usr1 = User.objects.filter(user_email=u_email)
            if (usr1):
                params = {'message': "Invalid credentials", 'success': True}
                return render(request, 'auth_user/signup.html', params)
            else:
                pass_hash = make_password(u_password)
                u1 = User(user_name=u_name, user_email=u_email,
                          user_password=pass_hash)
                u1.save()
                params = {'message': "Account Successfully created",
                          'success': True}
                return render(request, 'auth_user/signup.html', params)
        else:
            params = {
                'message': "Enter a minimum 5 character every fields", 'success': False}
    else:
        params = {'message': "Some error accured!", 'success': False}
        return render(request, 'auth_user/signup.html', params)
    return render(request, 'auth_user/signup.html', params)


def forgot(request):
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        return redirect('/')
    return render(request, 'auth_user/forgot.html')

def about(request):
    params = {'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        params = {'loggedin':True}
    return render(request, 'auth_user/about.html',params)

def contact(request):
    name = request.POST.get('cname','')
    email = request.POST.get('cemail','')
    message = request.POST.get('cmessage','')
    params = {'loggedin':False}
    u_cookie = request.COOKIES.get('u_logincred','')
    if(u_cookie != ''):
        params = {'loggedin':True}
    if(len(message) > 6 and len(name) > 2 and len(email) > 5):
        m1 = Contact(m_u_name=name,m_email=email,u_message=message)
        m1.save()
        return redirect('/user_auth/contact')
    return render(request, 'auth_user/contact.html',params)

def logout(request):
    responce = redirect('/')
    responce.delete_cookie('u_logincred')
    return responce