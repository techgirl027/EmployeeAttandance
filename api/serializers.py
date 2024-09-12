from rest_framework.serializers import ModelSerializer
from users.models import Staff, Shift, Position, StaffShift, StaffAttandance


class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class ShiftfSerializer(ModelSerializer):
    class Meta:
        model = Shift
        fields = "__all__"


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"


class StaffShiftSerializer(ModelSerializer):
    class Meta:
        model = StaffShift
        fields = "__all__"


class StaffAttandanceSerializer(ModelSerializer):
    class Meta:
        model = StaffAttandance
        fields = "__all__"
