from app.wsgi import *
from container.erp.models import Type

# Listar
#Type.objects.all()

# insertar

#t = Type(name='Presidente').save()

#Editar
#t =Type.objects.get(pk=1)
#t.name='Accionista'
#t.save()

#Eliminar
#t=Type.objects.get(pk=1)
#t.delete()

#Listar con filtros incluyendo mayusculas y minusculas

#obj = Type.objects.filter(name__icontains='Ac')
#print(obj)