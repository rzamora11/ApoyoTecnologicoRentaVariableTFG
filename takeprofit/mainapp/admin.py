from django.contrib import admin

# Register your models here.
from .models import Empresa
admin.site.register(Empresa)

from .models import Empresa_ESG
admin.site.register(Empresa_ESG)