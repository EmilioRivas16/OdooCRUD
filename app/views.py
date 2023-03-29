from django.shortcuts import render, redirect
from django.http import HttpResponse
import xmlrpc.client
import requests



server_url = 'http://localhost:8069'
db_name = 'odoodb'
username = 'emiliorivas918@gmail.com'
password = '1234'
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(server_url))
uid = common.authenticate(db_name, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(server_url))


def get(request):
    try:
        partner_ids = models.execute_kw(db_name, uid, password, 'res.partner', 'search', [[('id', '>', 6)]])
        partner_records = models.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['name', 'street', 'street2', 'zip']})
        
        return HttpResponse(str(partner_records))
    except Exception as e:
        return HttpResponse('Hubo un error')

def listado(request):
    
    try:
        partner_ids = models.execute_kw(db_name, uid, password, 'res.partner', 'search', [[('id', '>', 6)]], {'order': 'id ASC'})
        partner_records = models.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id', 'name', 'street', 'street2', 'zip']})

    except Exception as e:
        partner_records = []

    context = {'partner_records': partner_records}
    return render(request, 'index.html', context)

def agregar(request, name, precio, existencia, descripcion):
    try:
        partner_id = models.execute_kw(
            db_name,
            uid,
            password,
            'res.partner',
            'create',
            [{'name': name, 'street': precio, 'street2': existencia, 'zip': descripcion}]
        )
        return redirect('http://127.0.0.1:8000/index')
    except Exception as e:
        return HttpResponse('Hubo un error')

def modificar(request, id, name, precio, existencia, descripcion):
    try:
        models.execute_kw(
            db_name,
            uid,
            password,
            'res.partner',
            'write',
            [[id], {'name': name, 'street': precio, 'street2': existencia, 'zip': descripcion}]
        )
        return redirect('http://127.0.0.1:8000/index')
    except Exception as e:
        return HttpResponse('Hubo un error')

def eliminar(request, id):
    try:
        models.execute_kw(
            db_name,
            uid,
            password,
            'res.partner',
            'unlink',
            [[id]]
        )
        return redirect('http://127.0.0.1:8000/index')
    except Exception as e:
        return HttpResponse('Hubo un error')

def detallado(request, id):
    
    try:
        partner_ids = models.execute_kw(db_name, uid, password, 'res.partner', 'search', [[('id', '=', id)]])
        partner_records = models.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id', 'name', 'street', 'street2', 'zip']})

    except Exception as e:
        partner_records = []

    context = {'partner_records': partner_records}
    return render(request, 'detallado.html', context)


def form_agregar(request):
    return render(request, 'agregar.html')

def form_modificar(request, id):
    try:
        partner_ids = models.execute_kw(db_name, uid, password, 'res.partner', 'search', [[('id', '=', id)]])
        partner_records = models.execute_kw(db_name, uid, password, 'res.partner', 'read', [partner_ids], {'fields': ['id', 'name', 'street', 'street2', 'zip']})

    except Exception as e:
        partner_records = []

    context = {'partner_records': partner_records}
    return render(request, 'modificar.html', context)