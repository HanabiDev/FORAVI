#encoding: utf-8
from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from FORAVI.auth_validations import is_superuser
from FORAVI.utils import paginate_objects
from cms.forms import PostForm, DocumentForm
from cms.models import Post, Document

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def home(request):
    if request.method == 'GET':
        return render_to_response('cms_home.html',request.session, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def create_post(request):
    if request.method == 'GET':
        form = PostForm()
        return render_to_response('posts/post.html', {'form':form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect(reverse_lazy('cms:posts_index'))
        else:
            return render_to_response('posts/post.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def index_posts(request):
    posts = Post.objects.all().order_by('-date')
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('posts/posts_index.html', {'count':count, 'posts' : posts }, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def search_posts(request):
    key = request.GET.get('key')
    posts = Post.objects.filter(title__contains=key).order_by('-date')
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('posts/posts_index.html', {'key':key,'count':count, 'posts' : posts }, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def update_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'GET':
        form = PostForm(instance=post)
        return render_to_response('posts/post.html', {'editing':True, 'form':form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(reverse_lazy('cms:posts_index'))
        else:
            return render_to_response('posts/post.html', {'editing':True, 'form':form}, context_instance=RequestContext(request))
@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def publish_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.published = True
    post.save()
    return redirect(reverse_lazy('cms:posts_index'))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def unpublish_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.published = False
    post.save()
    return redirect(reverse_lazy('cms:posts_index'))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(reverse_lazy('cms:posts_index'))





""" Documents views """
@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def create_doc(request):
    if request.method == 'GET':
        form = DocumentForm()
        return render_to_response('docs/doc.html', {'form':form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            return redirect(reverse_lazy('cms:docs_index'))
        else:
            return render_to_response('docs/doc.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def index_docs(request):
    docs = Document.objects.all().order_by('-date')
    count = docs.count()
    page = request.GET.get('page')
    docs = paginate_objects(page,docs)
    return render_to_response('docs/docs_index.html', {'count':count, 'docs' : docs }, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def search_docs(request):
    key = request.GET.get('key')
    docs = Document.objects.filter(name__contains=key).order_by('-date')
    count = docs.count()
    page = request.GET.get('page')
    docs = paginate_objects(page,docs)
    return render_to_response('docs/docs_index.html', {'key':key,'count':count, 'docs' : docs }, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def update_doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)

    if request.method == 'GET':
        form = DocumentForm(instance=doc)
        return render_to_response('docs/doc.html', {'editing':True, 'form':form}, context_instance=RequestContext(request))
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES, instance=doc)
        if form.is_valid():
            doc = form.save()
            return redirect(reverse_lazy('cms:docs_index'))
        else:
            return render_to_response('docs/doc.html', {'editing':True, 'form':form}, context_instance=RequestContext(request))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def publish_doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    doc.published = True
    doc.save()
    return redirect(reverse_lazy('cms:docs_index'))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def unpublish_doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    doc.published = False
    doc.save()
    return redirect(reverse_lazy('cms:docs_index'))

@login_required(login_url=reverse_lazy('backend_login'))
@user_passes_test(is_superuser, login_url=reverse_lazy('backend_login'))
def delete_doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    doc.delete()
    return redirect(reverse_lazy('cms:docs_index'))