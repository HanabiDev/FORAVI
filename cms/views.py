#encoding: utf-8

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from cms.forms import PostForm
from cms.models import Post


def paginate_objects(page, objects):
    paginator = Paginator(objects,15)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects



def home(request):
    if request.method == 'GET':
        return render_to_response('cms_home.html',request.session, context_instance=RequestContext(request))

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


def index_posts(request):
    posts = Post.objects.all()
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('posts/posts_index.html', {'count':count, 'posts' : posts }, context_instance=RequestContext(request))


def search_posts(request):
    key = request.GET.get('key')
    posts = Post.objects.filter(title__contains=key)
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('posts/posts_index.html', {'key':key,'count':count, 'posts' : posts }, context_instance=RequestContext(request))


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

def publish_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.published = True
    post.save()
    return redirect(reverse_lazy('cms:posts_index'))


def unpublish_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.published = False
    post.save()
    print post.published
    return redirect(reverse_lazy('cms:posts_index'))


def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(reverse_lazy('cms:posts_index'))