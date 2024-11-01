from django.contrib import admin
from api.models import Company, Employee, Student, Manager

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'aim')


# Register models with their respective admin classes
admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Manager, ManagerAdmin)
