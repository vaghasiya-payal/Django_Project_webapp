from django.contrib import admin
from EMSapp.models import Company,Employee
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display =['cName','cEmail','cLogo','cUrl']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eFname','eLname','eCompany','eEmail','ePhone']