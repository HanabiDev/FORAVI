#encoding: utf-8

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from FORAVI.utils import paginate_objects
from backend.models import SiteUser


def home(request):
    if request.method == 'GET':
        return render_to_response('finantial_home.html',request.session, context_instance=RequestContext(request))

def load_reports(request):
    if request.method == 'GET':
        return render_to_response('load_reports.html',request.session, context_instance=RequestContext(request))

def load_clients(request):
    datafile = request.FILES.get('datafile')
    reader = unicode_csv_reader(datafile, delimiter=";")

    for row in reader:
        dni = row[0].strip()
        full_name = row[1]
        first_name, last_name = clean_name(full_name)
        password = last_name
        user = None

        try:
            user = SiteUser.objects.get(username=dni)
            user.update()
        except:
            if not user:
                new_client = SiteUser.objects.create_user(
                    username=dni, password=password,
                    first_name=first_name, last_name=last_name,
                )
                new_client.save()

import csv
def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'UTF-8') for cell in row]

def clean_name(full_name):
    print repr(full_name)
    encoded_name = full_name.replace(u'\xb4',u'').replace(u'\xa5', u'Ñ').strip().split('/')
    last_name = encoded_name[0]+' '+encoded_name[1] if encoded_name[1]!='' else encoded_name[0]
    first_name = encoded_name[2]

    return first_name,last_name



