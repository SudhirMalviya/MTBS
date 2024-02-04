from django.contrib import admin
from .models import Address
from .models import *

admin.site.register(Language)
admin.site.register(Movie)
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

