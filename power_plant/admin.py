from django.contrib import admin

# Register your models here.

from power_plant.models import System
from power_plant.models import Entry

admin.site.register(System)
admin.site.register(Entry)
