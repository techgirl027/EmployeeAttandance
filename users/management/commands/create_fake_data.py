from django.core.management.base import BaseCommand
from faker import Faker
from users.models import (
    Staff,
    Position,
    Shift,
    StaffShift,
    StaffAttandance,
)  # Replace 'myapp' with your app name
import random
from datetime import datetime, timedelta

fake = Faker()


class Command(BaseCommand):
    help = "Create fake data for testing"

    def handle(self, *args, **kwargs):
        # Create Positions
        positions = ["Manager", "Chef", "Waiter"]
        for position in positions:
            Position.objects.create(type=position)

        # Create Shifts
        shifts = [
            {
                "start_time": datetime.now(),
                "end_time": datetime.now() + timedelta(hours=8),
            },
            {
                "start_time": datetime.now() + timedelta(hours=8),
                "end_time": datetime.now() + timedelta(hours=16),
            },
            {
                "start_time": datetime.now() + timedelta(hours=16),
                "end_time": datetime.now() + timedelta(hours=24),
            },
        ]
        for shift in shifts:
            Shift.objects.create(
                start_time=shift["start_time"], end_time=shift["end_time"]
            )

        # Create Staff
        for _ in range(10):
            Staff.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.unique.email(),
                info=fake.text(),
                position=Position.objects.order_by("?").first(),
            )

        # Create StaffShifts

        for staff in Staff.objects.all():
            for _ in range(3):  # 3 shifts for each staff member
                shift = Shift.objects.order_by("?").first()

                # Check if a StaffShift with the same employee and shift already exists
                if not StaffShift.objects.filter(employee=staff, shift=shift).exists():
                    StaffShift.objects.create(
                        employee=staff,
                        shift=shift,
                        status=random.choice(["plannet", "inprogress", "done", "fail"]),
                    )

        # Create StaffAttendance
        for staff in Staff.objects.all():
            for _ in range(5):  # 5 attendance records for each staff member
                StaffAttandance.objects.create(
                    employee=staff,
                    date=fake.date_between(start_date="-30d", end_date="today"),
                    is_come=random.choice([True, False]),
                )

        self.stdout.write(self.style.SUCCESS("Fake data created successfully!"))
