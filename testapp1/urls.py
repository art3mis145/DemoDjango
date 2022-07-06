
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('student/<int:student_id>', views.student_by_id, name='DanhSachHocSinh')
]
