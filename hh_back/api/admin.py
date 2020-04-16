from django.contrib import admin

# Register your models here.
from django.contrib import admin

from api.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')