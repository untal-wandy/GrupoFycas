from django import forms
from . import models  # Asegúrate de importar correctamente el modelo

class CustomerForm(forms.ModelForm):
  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.CheckboxInput):
                          field.widget.attrs.update({'class': 'form-check-input'})
                          

    class Meta:
      model = models.Customer
      fields = ['fines', 'monto_requerido', 'saldar_deudas', 'hijos', 'fue_recomendado', 'familiar_en_fycas', 'tierra', 'vehiculo', 'casa', 'name', 'last_name', 'number', 'address',  'work_information',  'dni',  "img2", "img1", "name_r1", "name_r2", "number_r1", "number_r2",
        'lat', 'lon',
        # Datos personales
        'type_input',
        'sexo',
        'estado_civil',
        'ocupacion',
        'code_customer',
        'nacimiento',
        'nacionalidad',
        'direccion',
        'sector',
        'calle_numero',
        'municipio',
        'ciudad',
        'provincia',
        'pais',
        'dir_referencia',
        'phone',
        
        # # Datos de trabajo
        'empresa_trabaja',
        'cargo',
        'direccion_trabajo',
        'sector',  # Renombrado para evitar conflicto de nombres
        'calle_numero_trabajo',
        'municipio_trabaja',
        'ciudad_trabaja',
        'provincia_trabajo',
        'pais_trabajo',
        'dir_referencia_trabajo',
        'salario_m',
        'moneda',
        
        'relacion_tipo',
        'fecha_apertura',
        'fecha_vencimiento',
        'fecha_ultimo_pago',
        'numeoro_cuenta',  # Corregido de 'numeoro_cuenta'
        'estatus',
        'tipo_prestamo',
        'moneda_prestamo',
        'credito_aprovado',  # Corregido de 'credito_aprovado'
        'balance_corte',
        'monto_adeudado',
        'pago_mandatorio_cuota',
        'monto_ultimo_pago',
        'total_atraso',
        'tasa_interes',
        'forma_pago',
        'cantidad_cuota',
        'atraso1_30',
        'atraso31_60',
        'atraso61_90',
        'atraso91_120',
        'atraso121_150',
        'atraso151_180',
        'atraso181_o_mas',
        
        'company',

    ]
      
 

      #       'name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre Completo"}),
      #       'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
      #       'name_r1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Nombre" }),
            
      #       'name_r2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Apellidos" }),
            
      #       'number': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'number_r1': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'number_r2': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Numero"}),
            
      #       'address': forms.TextInput(attrs={'class': 'form-control address', "placeholder": "Donde Recide"}),
       
      #       'work_information': forms.Textarea(attrs={'class': 'form-control textarea', "placeholder": "Informacion Laboral"}),

      #       'dni': forms.TextInput(attrs={'class': 'form-control',  "placeholder": "232-3232-3232", }),

      #   }
      
      
class CreditForm(forms.ModelForm):
  class Meta:
      model = models.Credit
      fields = [
        "customer", "name", "price_feed", "no_account", 'date', 'tasa',
         "mode_pay", "day_pay", "dni", "amount", "amount_feed",
      ]
      widgets = {
        'customer': forms.TextInput(attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'dni': forms.TextInput(attrs={'class': 'form-control'}),
        'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'date': forms.DateInput(attrs={'class': 'form-control'}),
        'tasa': forms.NumberInput(attrs={'class': 'form-control'}),

        'price_feed': forms.NumberInput(attrs={'class': 'form-control'}),
        'no_account': forms.TextInput(attrs={'class': 'form-control'}),
        'day_pay': forms.NumberInput(attrs={'class': 'form-control'}),
        'amount_feed': forms.TextInput(attrs={'class': 'form-control'}),

      }
      
      
class PayCreditForm(forms.ModelForm):
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = models.PayCredit
        fields = ['credit',  'img', ]
        widgets = {
            'img': forms.FileInput(attrs={'accept': 'image/*'})
        }
        
        
class CustomerDebit(forms.ModelForm):
    class Meta:
        model = models.CustomerDebit
        fields = ['name', 'number', 'dni', 'day_created']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'day_created': forms.DateInput(attrs={'class': 'form-control'}),
        }
        
        
        
class CuotaForm(forms.ModelForm):
    class Meta:
        model = models.Cuota
        fields = ['credito', 'cuota', 'capital', 'capital_restante', 'creado', 'pago', 'estado']
        widgets = {
            'creado': forms.DateInput(attrs={'type': 'date'}),  # Para un selector de fecha
            'pago': forms.TextInput(attrs={'placeholder': 'Día del pago'}),  # Campo de texto
        }
        
        
class CashControlForm(forms.ModelForm):
    class Meta:
        model = models.CashControl
        fields = ['date', 'opening_balance', 'closing_balance', 'total_income', 'total_expenses', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha'}),
            'opening_balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Saldo de apertura'}),
            'closing_balance': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Saldo de cierre'}),
            'total_income': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresos totales'}),
            'total_expenses': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Gastos totales'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Notas'}),
        }