from django.contrib import admin
from asset.models import Company, Employee, DeviceStatus, Device, DeviceLog


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_at')
    list_filter = ('name', 'created_at')
    search_fields = ('name', 'address')


admin.site.register(Company, CompanyAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'email',
                    'contact_no', 'designation', 'company')
    list_filter = ('name', 'designation', 'company')
    search_fields = ('name', 'employee_id', 'email')


admin.site.register(Employee, EmployeeAdmin)


class DeviceStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(DeviceStatus, DeviceStatusAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'description', 'status')
    list_filter = ('name', 'status',)
    search_fields = ('name', 'serial_number',)


admin.site.register(Device, DeviceAdmin)


class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'device', 'employee', 'check_out_at', 'check_in_at',
                    'status_when_checked_out', 'status_when_returned')
    list_filter = ('type', 'device', 'employee',)
    search_fields = ('device', 'employee',)


admin.site.register(DeviceLog, DeviceLogAdmin)
