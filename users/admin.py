from django.contrib import admin
from .models import Staff, Shift, Position, StaffShift, StaffAttandance

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "position"]
    list_filter = ["first_name", "last_name", "position"]
    search_fields = ["first_name", "last_name", "phone"]


class ShiftAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time"]
    list_filter = ["start_time", "end_time"]
    search_fields = ["start_time", "end_time"]


class PositionAdmin(admin.ModelAdmin):
    list_display = ["type", "info"]
    list_filter = ["type", "info"]
    search_fields = ["type", "info"]


class StaffShiftAdmin(admin.ModelAdmin):
    list_display = ["employee", "shift", "status"]
    list_filter = ["employee", "shift", "status"]
    search_fields = ["employee", "shift"]


@admin.register(StaffAttandance)
class AttandanceAdmin(admin.ModelAdmin):
    list_display = ["date", "is_come", "employee__first_name", "employee__last_name"]
    list_filter = ["date", "is_come", "employee__first_name", "employee__last_name"]
    search_fields = ["employee__first_name", "employee__last_name"]
    readonly_fields = ["date", "is_come"]


admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffShift, StaffShiftAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Shift, ShiftAdmin)
