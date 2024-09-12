from .views import (
    StaffListCreateView,
    StaffUpdateDestroy,
    PositionListCreateView,
    PositionUpdateDestroy,
    ShiftListCreateView,
    ShiftUpdateDestroy,
    StaffShiftListCreateView,
    StaffShiftUpdateDestroy,
    StaffAttandanceListCreateView,
    StaffAttandanceUpdateDestroy,
)
from django.urls import path

urlpatterns = [
    path("staffs/", StaffListCreateView.as_view()),
    path("staffs/<int:pk>/", StaffUpdateDestroy.as_view()),
    path("position/", PositionListCreateView.as_view()),
    path("position/<int:pk>/", PositionUpdateDestroy.as_view()),
    path("shift/", ShiftListCreateView.as_view()),
    path("shift/<int:pk>/", ShiftUpdateDestroy.as_view()),
    path("staffshift/", StaffShiftListCreateView.as_view()),
    path("staffshift/<int:pk>/", StaffShiftUpdateDestroy.as_view()),
    path("staffattandance/", StaffAttandanceListCreateView.as_view()),
    path("staffattandance/<int:pk>/", StaffAttandanceUpdateDestroy.as_view()),
]
