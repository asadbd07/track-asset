from django.test import TestCase

from .models import Company, Employee, DeviceStatus, Device, DeviceLog


class ModelTestCase(TestCase):
    def setUp(self):
        # dummy test data
        self.company = Company.objects.create(
            name="ABC Company Ltd", address="Uttara, Dhaka")
        self.device_status = DeviceStatus.objects.create(name="Good")

    def test_company_model(self):
        company = Company.objects.get(name="ABC Company Ltd")
        self.assertEqual(company.name, "ABC Company Ltd")
        self.assertEqual(company.address, "Uttara, Dhaka")

    def test_employee_model(self):
        employee = Employee.objects.create(
            name="Kashem Mia",
            employee_id="E11232",
            email="kashemmia@company.com",
            contact_no="01231232131",
            designation="Manager",
            company=self.company,
        )
        self.assertEqual(employee.name, "Kashem Mia")
        self.assertEqual(employee.employee_id, "E11232")
        self.assertEqual(employee.email, "kashemmia@company.com")
        self.assertEqual(employee.contact_no, "01231232131")
        self.assertEqual(employee.designation, "Manager")
        self.assertEqual(employee.company, self.company)

    def test_device_status_model(self):
        device_status = DeviceStatus.objects.get(name="Good")
        self.assertEqual(device_status.name, "Good")

    def test_device_model(self):
        device = Device.objects.create(
            name="Dell Laptop",
            serial_number="12345",
            description="Core i3, 8GB RAM, 256 SSD",
            status=self.device_status,
        )
        self.assertEqual(device.name, "Dell Laptop")
        self.assertEqual(device.serial_number, "12345")
        self.assertEqual(device.description, "Core i3, 8GB RAM, 256 SSD")
        self.assertEqual(device.status, self.device_status)

    def test_device_log_model(self):
        employee = Employee.objects.create(
            name="Lorem Ipsum",
            employee_id="E54321",
            email="lorem@company.com",
            contact_no="102301023",
            designation="Asst. Manager",
            company=self.company,
        )
        device = Device.objects.create(
            name="HP Desktop",
            serial_number="54321",
            description="Core i5, 12GB RAM",
            status=self.device_status,
        )
        device_log = DeviceLog.objects.create(
            type="checkin",
            employee=employee,
            device=device,
            assigned_till=None,
            check_out_at=None,
            check_in_at=None,
            status_when_checked_out=None,
            status_when_returned=None,
        )
        self.assertEqual(device_log.type, "checkin")
        self.assertEqual(device_log.employee, employee)
        self.assertEqual(device_log.device, device)
        self.assertIsNone(device_log.assigned_till)
        self.assertIsNone(device_log.check_out_at)
        self.assertIsNone(device_log.check_in_at)
        self.assertIsNone(device_log.status_when_checked_out)
        self.assertIsNone(device_log.status_when_returned)
