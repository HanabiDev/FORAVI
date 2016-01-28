from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from FORAVI.auth_validations import is_superuser
from FORAVI.utils import paginate_objects
from users.forms import AddUserForm, UpdateUserForm

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def create_user(request):
    if request.method == 'GET':
        form = AddUserForm()
        return render_to_response('user.html', {'form':form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse_lazy('users:edit_user',kwargs={'user_id':str(user.id)}))
        else:
            return render_to_response('user.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def index_users(request):
    if request.method == 'GET':
        users = User.objects.filter(~Q(is_superuser=True)).order_by('first_name')
        count = users.count()
        page = request.GET.get('page')
        users = paginate_objects(page,users)
        return render_to_response('users_index.html', {'count':count, 'users' : users }, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def search_users(request):
    key = request.GET.get('key')
    users = User.objects.filter(Q(username__contains=key) | Q(email__contains=key) | Q(first_name__contains=key) | Q(last_name__contains=key)).order_by('first_name')
    count = users.count()
    page = request.GET.get('page')
    users = paginate_objects(page,users)
    return render_to_response('users_index.html', {'key':key,'count':count, 'users' : users }, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def update_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'GET':
        form = UpdateUserForm(instance=user)
        return render_to_response('user.html', {'form':form, 'editing':True, 'avatar':user.avatar, 'id':user.id}, context_instance=RequestContext(request))

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect(reverse_lazy('users:users_index'))
        else:
            return render_to_response('user.html', {'form':form, 'editing':True, 'avatar':user.avatar, 'id':user.id}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def update_user_password(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'GET':
        form = AdminPasswordChangeForm(user, None)
        return render_to_response('update_password.html', {'form':form, 'editing':True, 'site_user':user}, context_instance=RequestContext(request))

    if request.method == 'POST':
        form = AdminPasswordChangeForm(user,request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('users:edit_user',kwargs={'user_id':str(user.id)}))
        return render_to_response('update_password.html', {'form':form, 'editing':True, 'site_user':user}, context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def enable_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = True
    user.save()
    print user.is_active
    return redirect(reverse_lazy('users:users_index'))


@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def disable_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect(reverse_lazy('users:users_index'))