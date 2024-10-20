from . import models
from . import forms
from django.http import JsonResponse
from datetime import datetime
from twilio.rest import Client  
import time
from .mixing import Options
from num2words import num2words
from django.contrib.humanize.templatetags.humanize import intcomma


def SearchCustomer(request):
      list_cutomers = []
      for c in models.Customer.objects.all():
            dict_customer = { 
                    'id': c.id,
                    'filter':    c.name + " " + c.last_name + c.dni + c.calle_numero + "," + c.municipio +  ',' + c.sector +  ',' + c.ciudad +  c.work_information + c.number,
                    'name': c.name + " " + c.last_name,
                    "dni": c.dni,
                    "ubication": c.calle_numero + "," + c.municipio +  ',' + c.sector +  ',' + c.ciudad, 
                    "inf": c.work_information,
                    "refers": c.name_r1 + " " + " " + str(c.number_r1) + " - " + c.name_r2 + " " + str(c.number_r2) ,
                    "recide": c.address,
            }
            list_cutomers.append(dict_customer)
      return JsonResponse(list_cutomers,  safe=False)


def CustomerVerify(request):
        # cus = models.Customer.objects.all()
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.customer_verify == False:
            c.customer_verify = True
        c.save()
        print(c.customer_verify)
        # for cm in cus:
        #     cm.customer_verify = False 
        #     cm.save()
        return JsonResponse(list(),  safe=False)
    
def CustomerNoVerify(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.customer_verify == True:
            c.customer_verify = False
        c.save()
        return JsonResponse(list(),  safe=False)
    


def TurnDebeit(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit_visit == False:
            c.debit_visit = True
        else:
            c.debit_visit = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def TurnDebeitFollow(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit_follow == False:
            c.debit_follow = True
        else:
            c.debit_follow = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def TurnDebeitActive(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.debit == False:
            c.debit = True
        else:
            c.debit = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
def DisableCustomer(request):
        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        if c.is_active == False:
            c.is_active = True
        else:
            c.is_active = False
        c.save()
        return JsonResponse(list(),  safe=False)    
    
    
def MensajeCustomerDebit(request):
        customer_debit = models.CustomerDebit.objects.filter(debit = True)
        for cb in customer_debit:
            print(f'Recordatorio enviado a: {cb.name}, {cb.number}')
            Send_WhatsApp_Message(cb.name, cb.number)
            time.sleep(20) 
            
        def Send_WhatsApp_Message(name, number):
            account_sid = 'AC32b5e94ce632aabd0a278a56e16bd44a'
            auth_token = 'a61c8b622e93ada5958d69dacef7c461'
            client = Client(account_sid, auth_token)

            Msm = f"Recordatorio de Pago - Grupo FyCas \n \nEstimado {name}: \n\nPor medio del presente mensaje, le recordamos que tiene una cuota pendiente. Su puntualidad en los pagos es muy importante para nosotros, por lo que le solicitamos amablemente que realice su pago lo antes posible. \n \nSi ya ha realizado su pago, por favor ignore este mensaje."
            message = client.messages.create(
                  body= Msm,
                  from_= '+13344384583',
                  to= f'+1{number}' )
            return True
        
        return JsonResponse(list(),  safe=False)    
    
    

def CreateCreditAjax(request):
        from datetime import datetime

        c = models.Customer.objects.get(id=request.GET.get('customer_id'))
        credit = models.Credit.objects.create( 
            customer = c,
            dni = c.dni,
            name = c.name + " " + c.last_name,
            amount= int(request.GET.get('monto')),
            amount_feed = request.GET.get('monto_pagar'),
            no_account = int(0),
            price_feed = request.GET.get('cuotas'),
            day_pay = int(request.GET.get('dia')),
            mont = Options.MontNow(),
            day = Options.GetDayWeek(),
            day_number =  datetime.now().day,
            year = num2words(datetime.now().year, lang='es'),
            year_number = datetime.now().year,
        )
        c.monto_requerido =  intcomma(int(request.GET.get('monto')))
        c.save()
        print(num2words(datetime.now().year))
        data = {'monto_requerido':  intcomma(credit.amount)}
        return JsonResponse(data,  safe=False)    
    
    
def AplicarPago(request):
    cu = models.Cuota.objects.get(id=request.GET.get('id'))
    cu_ta = models.Cuota.objects.get(id=request.GET.get('id'))
    # print(request.GET.get('input'), 'soii')
    credit = models.Credit.objects.get(id=cu.credito.id)
    cuotas_o =  credit.credito.all()
    p_x_c = 1
    c_p = 0
        
    for cuo in cuotas_o:
        p_x_c += cu.cuota
        if cuo.abonado > 0:
            c_p += cuo.abonado
    print(c_p, 'siuuu')
    if  cu.estado == False:
        if cu.cuota != cu.abonado:
            monto_abonado = int(request.GET.get('input'))
            cu.abonado += monto_abonado
            cu.restante = max(cu.cuota - cu.abonado, 0)

            if cu.abonado >= cu.cuota:
                cu.abonado = cu.cuota


            if cu.cuota == cu.abonado:
                cu.estado = True
            cu.save()
        else:
            cu.estado = True
            cu.save()
    else:
        cu.estado = False
        cu.credito.estado = False
        # cu.save()
    D = {
        'id': cu_ta.id
    }
    
    return JsonResponse(D,  safe=False)    
    
""""
from django.shortcuts import render
from .models import Contacto
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

def migrar_contactos(request):
    # Leer contactos de la base de datos
    contactos = Contacto.objects.all()

    # Transformar datos
    contactos_google = []
    for contacto in contactos:
        contacto_google = {
            "givenName": contacto.nombre,
            "familyName": contacto.apellido,
            "emails": [{"value": contacto.correo_electronico}],
            "phones": [{"value": contacto.numero_telefono}],
        }
        contactos_google.append(contacto_google)

    # Autenticarse con la API de Google Contacts
    credenciales = Credentials.from_service_account_file('credentials.json')
    cliente = build('people', 'v1', credentials=credenciales)

    # Crear o actualizar contactos en Google Contacts
    for contacto_google in contactos_google:
        persona = cliente.people().resource().create(body=contacto_google).execute()
        print(f"Contacto creado: {persona.resourceName}")

    return render(request, 'contacto/migracion_exitosa.html')

"""""
