from django.shortcuts import render_to_response

# Create your views here.
from django.template.context import RequestContext
from FORAVI.utils import paginate_objects
from cms.models import Post


def home(request):
    return render_to_response('index.html', request.session, context_instance=RequestContext(request))


def index_news(request):
    posts = Post.objects.all().order_by('-date')
    count = posts.count()
    page = request.GET.get('page')
    posts = paginate_objects(page,posts)
    return render_to_response('articles.html', {'count':count, 'articles' : posts }, context_instance=RequestContext(request))


def show_post(request, slug):
    post = Post.objects.filter(slug=slug)
    return render_to_response('article.html', {'post' : post }, context_instance=RequestContext(request))


