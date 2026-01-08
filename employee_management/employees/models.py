from django.db import models

class Employee(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        INACTIVE = 'inactive', 'Inactive'

    employee_id = models.AutoField(
        primary_key=True,
        help_text="System generated unique employee ID"
    )

    name = models.CharField(
        max_length=100,
        help_text="Full name of the employee"
    )

    email = models.EmailField(
        unique=True,
        help_text="Official company email address used for identification"
    )

    department = models.CharField(
        max_length=100,
        help_text="Department where the employee works (HR, IT, Finance, etc.)"
    )

    designation = models.CharField(
        max_length=100,
        help_text="Job title or role of the employee"
    )

    date_of_joining = models.DateField(
        help_text="Date when the employee joined the organization"
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ACTIVE,
        help_text="Current employment status"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Timestamp when the employee record was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp when the employee record was last updated"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.name} - {self.designation}"
