#encoding: utf-8

from django.core.urlresolvers import reverse_lazy
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from FORAVI.utils import paginate_objects
from backend.models import SiteUser
from finantial.models import CreditLine, ClientCreditProduct, ClientSavingProduct, SavingLine
from datetime import datetime


def home(request):
    if request.method == 'GET':
        return render_to_response('finantial_home.html',request.session, context_instance=RequestContext(request))

def load_reports(request):
    if request.method == 'GET':
        return render_to_response('load_reports.html',{'tab':'clients'}, context_instance=RequestContext(request))

def load_clients(request):
    if request.method == 'GET':
        return render_to_response('load_reports.html',{'tab':'clients'}, context_instance=RequestContext(request))
    if request.method == 'POST':
        datafile = request.FILES.get('datafile')
        reader = unicode_csv_reader(datafile, delimiter=";")
        dni_consolidate = []

        for row in reader:
            if len(row) > 0:
                dni = row[0].strip()
                dni_consolidate.append(dni)
                user = None
                try:
                    user = SiteUser.objects.get(username=dni)
                except:
                    if not user:
                        full_name = row[1]
                        first_name, last_name = clean_name(full_name)
                        password = last_name
                        new_client = SiteUser.objects.create_user(
                            username=dni, password=password,
                            first_name=first_name, last_name=last_name,
                        )
                        new_client.save()

        SiteUser.objects.exclude(is_superuser=True).update(is_active=False)
        SiteUser.objects.filter(username__in=dni_consolidate).update(is_active=True)

        return render_to_response('load_reports.html', {'tab':'clients', 'loaded_cli':True}, context_instance=RequestContext(request))

def load_credits(request):
    if request.method == 'GET':
        return render_to_response('load_reports.html', {'tab':'pres', 'loaded':False}, context_instance=RequestContext(request))
    if request.method == 'POST':
        datafile = request.FILES.get('datafile')
        reader = unicode_csv_reader(datafile, delimiter=";")

        for row in reader:
            credit_data = clean_credit_row(row[:10])

            new_user_product, created = ClientCreditProduct.objects.update_or_create(
                credit_line = credit_data[2],
                client = credit_data[0],
                defaults={
                    'promisory_note': credit_data[1],
                    'quota': credit_data[3],
                    'amount': credit_data[4],
                    'remaining_amount': credit_data[5],
                    'amortized_percent': credit_data[6],
                    'remaining_payments': credit_data[7],
                    'start_date': datetime.date(datetime.strptime(credit_data[8], '%d/%m/%Y')),
                    'end_date': datetime.date(datetime.strptime(credit_data[9], '%d/%m/%Y'))
                }
            )

            new_user_product.save()
        return render_to_response('load_reports.html', {'tab':'pres', 'loaded_cre':True}, context_instance=RequestContext(request))


def load_deposits(request):
    if request.method == 'GET':
        return render_to_response('load_reports.html', {'tab':'depo', 'loaded':False}, context_instance=RequestContext(request))
    if request.method == 'POST':
        datafile = request.FILES.get('datafile')
        reader = unicode_csv_reader(datafile, delimiter=";")

        for row in reader:
            deposit_data = clean_deposit_row(row)
            new_savings_line, created = ClientSavingProduct.objects.update_or_create(
                saving_line = deposit_data[1],
                client = deposit_data[0],
                defaults = {
                    'savings_total': deposit_data[2],
                    'quota': deposit_data[3],
                    'salary_percent': deposit_data[4]
                }
            )

            new_savings_line.save()

        return render_to_response('load_reports.html', {'tab':'depo', 'loaded_depo':True}, context_instance=RequestContext(request))


import csv
def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'windows-1252') for cell in row]

def clean_name(full_name):
    encoded_name = full_name.replace(u'\xb4',u'').replace(u'\xa5', u'Ñ').strip().replace('  ', ' ').split('/')
    last_name = encoded_name[0]+' '+encoded_name[1] if encoded_name[1]!='' else encoded_name[0]
    first_name = encoded_name[2]
    return first_name,last_name

def clean_credit_row(row):
    new_row = []
    for cell in row:
        encoded_cell = cell.replace(u'\xb4',u'').replace(u'\xa5', u'Ñ').strip().replace('  ', ' ')
        new_row.append(encoded_cell)

    new_row[0] = SiteUser.objects.get(username=new_row[0])
    new_row[2] = CreditLine.objects.get(name=new_row[2])

    return new_row

def clean_deposit_row(row):
    new_row = [cell.strip().replace('  ',' ') for cell in row]
    new_row[0] = SiteUser.objects.get(username=new_row[0])
    new_row[1] = SavingLine.objects.get(name=new_row[1])

    return new_row
