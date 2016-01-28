#encoding: utf-8
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from backend.forms import AccountForm, CustomPasswordChangeForm
from backend.models import SiteUser

@login_required(login_url=reverse_lazy('clients:login'))
def home(request):
    if request.method == 'GET':
        user = SiteUser.objects.get(username=request.user.username)
        return render_to_response("clients_home.html", {'user':user}, context_instance=RequestContext(request))


def login_client(request):
    logout(request)
    username = password = ''
    error = False

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse_lazy('clients:home'))

                error = 'Usuario no activo'
            else:
                error = 'Credenciales no válidas'
        else:
            error = 'Usuario y contraseña requeridos'
    return render_to_response('client_login.html', {'error':error, 'site_user':username}, context_instance=RequestContext(request))


def logout_client(request):
    logout(request)
    return redirect(reverse_lazy('clients:login'))

@login_required(login_url=reverse_lazy('clients:login'))
def restore_password(request):
    username = request.POST.get('user')
    error = False
    if username:
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            password = User.objects.make_random_password()
            user.set_password(password)
            user.save()
            send_password_restore_mail(user, password)
            message = 'Se ha enviado un mensaje a su cuenta de correo con la información para restablecer la contraseña.'
            return render_to_response('client_login.html', {'message':message, 'restoring':True}, context_instance=RequestContext(request))
        finally:
            error = 'El usuario no existe'

    else:
        error = 'Email o usuario requerido'
    return render_to_response('client_login.html', {'rest_error':error, 'restoring':True}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('clients:login'))
def manage_account(request):
    user = request.user
    if request.method == 'GET':
        form = AccountForm(instance=user)
        return render_to_response('client_account.html', {'form':form}, context_instance=RequestContext(request))

    if request.method == 'POST':

        form = AccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            form = AccountForm(instance=user)
            message = 'Tu cuenta ha sido actualizada.'
            return render_to_response('client_account.html', {'form':form, 'message':message}, context_instance=RequestContext(request))

        return render_to_response('client_account.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('clients:login'))
def update_password(request):
    if request.method == 'GET':
        form = CustomPasswordChangeForm(request.user, None)
        return render_to_response('client_update_password.html', {'form':form}, context_instance=RequestContext(request))

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse_lazy('clients:login'))
        return render_to_response('client_update_password.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('clients:login'))
def simulators(request):
    if request.method == 'GET':
        return render_to_response("client_simulators.html", request, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('clients:login'))
def send_request(request):
    if request.method == 'GET':
        return render_to_response("client_pqr.html", request, context_instance=RequestContext(request))

def send_password_restore_mail(user, password):
    send_mail(
		subject=u'Recuperación de contraseña',
		message=u"""Se ha solicitado recuperar la contraseña para esta cuenta.
		           Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión recuerde cambiar su
		           contraseña desde la configuracion de su cuenta. La nueva contraseña es:"""+password+''.decode('utf-8'),
		html_message=u"""<p><b>Señor </b><br>"""+user.first_name+' '+user.last_name+u"""</b></p>
		            <p>Se ha solicitado recuperar la contraseña para su cuenta de asociado en FORAVI.<p>
		            <p>Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión, recuerde cambiar su
		            contraseña desde la configuracion de su cuenta.</p> La nueva contraseña es: <b>"""+password+'</b>'.decode('utf-8'),
		from_email='FORAVI <notificaciones@foravi.com>',
		recipient_list=[user.email],
		fail_silently=False
	)


