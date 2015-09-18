from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginate_objects(page, objects):
    paginator = Paginator(objects,15)

    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)

    return objects
