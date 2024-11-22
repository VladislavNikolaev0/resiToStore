from django.contrib import admin
from .models import Processor, MotherBroad, Ram, PowerUnit

# Register your models here.

admin.site.register(Processor)
admin.site.register(MotherBroad)
admin.site.register(Ram)
admin.site.register(PowerUnit)