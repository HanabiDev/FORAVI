#encoding: utf-8
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from FORAVI.auth_validations import is_superuser
from backend.forms import AccountForm, CustomPasswordChangeForm


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def home(request):
    return render_to_response('backend_index.html', request.session, context_instance=RequestContext(request))



def login_user(request):
    logout(request)
    username = password = ''
    error = False

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active and user.is_superuser:
                    login(request, user)
                    return redirect(reverse_lazy('backend_home'))
                else:
                    if not user.is_superuser:
                        error = 'No posee permisos de administrador'
                    else:
                        error = 'Usuario no activo'
            else:
                error = 'Credenciales no válidas'
        else:
            error = 'Usuario y contraseña requeridos'
    return render_to_response('admin_login.html', {'error':error, 'site_user':username}, context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('backend_login'))

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
            return render_to_response('admin_login.html', {'message':message, 'restoring':True}, context_instance=RequestContext(request))
        finally:
            error = 'El usuario no existe'

    else:
        error = 'Email o usuario requerido'
    return render_to_response('admin_login.html', {'rest_error':error, 'restoring':True}, context_instance=RequestContext(request))

def manage_account(request):
    user = request.user
    if request.method == 'GET':
        form = AccountForm(instance=user)
        return render_to_response('account.html', {'form':form}, context_instance=RequestContext(request))

    if request.method == 'POST':

        form = AccountForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            form = AccountForm(instance=user)
            message = 'Tu cuenta ha sido actualizada.'
            return render_to_response('account.html', {'form':form, 'message':message}, context_instance=RequestContext(request))

        return render_to_response('account.html', {'form':form}, context_instance=RequestContext(request))


def update_password(request):
    if request.method == 'GET':
        form = CustomPasswordChangeForm(request.user, None)
        return render_to_response('update_password.html', {'form':form}, context_instance=RequestContext(request))

    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse_lazy('backend_login'))
        return render_to_response('update_password.html', {'form':form}, context_instance=RequestContext(request))

def send_password_restore_mail(user, password):
    send_mail(
		subject=u'Recuperación de contraseña',
		message=u"""Se ha solicitado recuperar la contraseña para esta cuenta.
		           Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión recuerde cambiar su
		           contraseña desde la configuracion de su cuenta. La nueva contraseña es:"""+password+''.decode('utf-8'),
		html_message=u"""<p><b>Señor </b><br>"""+user.first_name+' '+user.last_name+u"""</b></p>
		            <p>Se ha solicitado recuperar la contraseña para su cuenta de administración en FORAVI.<p>
		            <p>Se le ha generado un nueva contraseña de ingreso. Una vez iniciada la sesión, recuerde cambiar su
		            contraseña desde la configuracion de su cuenta.</p> La nueva contraseña es: <b>"""+password+'</b>'.decode('utf-8'),
		from_email='FORAVI <notificaciones@foravi.com>',
		recipient_list=[user.email],
		fail_silently=False
	)
