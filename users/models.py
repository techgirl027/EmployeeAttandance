from django.db import models
from datetime import datetime

# Create your models here.


class Staff(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=255, unique=True)
    info = models.TextField(blank=True, null=True)
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def str(self) -> str:
        return self.first_name


class Position(models.Model):
    type = models.CharField(max_length=255)
    info = models.TextField(blank=True, null=True)

    def str(self) -> str:
        return self.type


class Shift(models.Model):
    start_time = models.DateTimeField(verbose_name="boshlanish vaqti")
    end_time = models.DateTimeField(verbose_name="tugash vaqti")

    def str(self) -> str:
        return f"{self.start_time} - {self.end_time}"


class StaffShift(models.Model):
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    status_choice = (
        ("plannet", "rejalashtirilgan"),
        ("inprogress", "in progress"),
        ("done", "bajarildi"),
        ("fail", "bajarilmadi"),
    )
    status = models.CharField(max_length=35, choices=status_choice, default="plannet")

    class Meta:
        verbose_name = "Navbatchilik"
        verbose_name_plural = "Navbatchiliklar"
        unique_together = ("employee", "shift")

    def str(self) -> str:
        return f"{self.employee} - {self.shift}"


class StaffAttandance(models.Model):
    date = models.DateField(default=datetime.today)
    is_come = models.BooleanField(default=False)
    employee = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def str(self) -> str:
        return f"{self.employee}"
