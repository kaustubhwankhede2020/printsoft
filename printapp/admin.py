from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Employee)
admin.site.register(PaperType)
admin.site.register(PaperColor)
admin.site.register(PaperSize)
admin.site.register(PaperGsm)
admin.site.register(PaperConfiguration)
admin.site.register(PlateSize)
admin.site.register(PlateConfiguration)
admin.site.register(PrintingSize)
admin.site.register(PrintingConfiguration)
admin.site.register(BindingConfiguration)
admin.site.register(CustomerConfiguration)
admin.site.register(JobConfiguration)
admin.site.register(LaminationConfiguration)
