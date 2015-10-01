from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.shortcuts import render_to_response, redirect

# Create your views here.
from django.template.context import RequestContext
from FORAVI.utils import paginate_objects
from cms.models import Post, Comment, Document, Content


def home(request):
    return render_to_response('index.html', request.session, context_instance=RequestContext(request))


def index_news(request):
    posts = Post.objects.filter(published=True).order_by('-date')
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('articles.html', {'count':count, 'articles' : posts }, context_instance=RequestContext(request))


def show_post(request, slug):
    post = Post.objects.get(slug=slug)
    return render_to_response('article.html', {'post' : post }, context_instance=RequestContext(request))

def add_comment(request, content_id):
    content = Content.objects.get(id=content_id)
    url = ''
    try:
        content = content.post
        url = 'frontend:post'
    except:
        content = content.document
        url = 'frontend:doc'

    new_comment = Comment(content =content, message=request.POST.get('comment'), author=request.user)
    new_comment.save()

    return redirect(reverse_lazy(url,args=(content.slug,)))

def update_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.message = request.POST.get('comment')
    comment.save()
    return HttpResponse(comment.message)

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    content = None
    url = ''
    try:
        content = comment.content.post
        url = 'frontend:post'
    except:
        content = comment.content.document
        url = 'frontend:doc'

    comment.delete()
    return redirect(reverse_lazy(url,args=(content.slug,)))


def index_documents(request):
    docs = Document.objects.filter(published=True).order_by('-date')
    count = docs.count()
    page = request.GET.get('page')
    docs = paginate_objects(page,docs)
    return render_to_response('documents.html', {'count':count, 'documents' : docs }, context_instance=RequestContext(request))


def show_document(request, slug):
    document = Document.objects.get(slug=slug)
    return render_to_response('document.html', {'document' : document }, context_instance=RequestContext(request))
