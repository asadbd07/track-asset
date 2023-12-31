from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact_no = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class DeviceStatus(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Device Status"
        verbose_name_plural = "Device Status"


class Device(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000)
    status = models.ForeignKey(DeviceStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class DeviceLog(models.Model):
    TYPE_CHOICES = [
        ('checkin', 'Check In'),
        ('checkout', 'Check Out'),
    ]
    type = models.CharField(choices=TYPE_CHOICES, max_length=20, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assigned_till = models.DateTimeField(null=True, blank=True)
    check_out_at = models.DateTimeField(null=True, blank=True)
    check_in_at = models.DateTimeField(null=True, blank=True)
    status_when_checked_out = models.ForeignKey(
        DeviceStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="device_checkin_status")
    status_when_returned = models.ForeignKey(
        DeviceStatus, on_delete=models.CASCADE, null=True, blank=True, related_name="device_return_status")

    def __str__(self):
        return f"{self.device}"
