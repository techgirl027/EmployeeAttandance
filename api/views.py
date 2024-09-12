from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from users.models import Position, Shift, Staff, StaffAttandance, StaffShift
from .serializers import (
    PositionSerializer,
    ShiftfSerializer,
    StaffAttandanceSerializer,
    StaffShiftSerializer,
    StaffSerializer,
)


# for listing and creating staffs
class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


# for update and delete staffs
class StaffUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftfSerializer


class ShiftUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftfSerializer


class StaffShiftListCreateView(generics.ListCreateAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer


class StaffShiftUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffShift.objects.all()
    serializer_class = StaffShiftSerializer


class StaffAttandanceListCreateView(generics.ListCreateAPIView):
    queryset = StaffAttandance.objects.all()
    serializer_class = StaffAttandanceSerializer


class StaffAttandanceUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffAttandance.objects.all()
    serializer_class = StaffAttandanceSerializer
