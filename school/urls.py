from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('gallery/', views.gallery, name="gallery"),
    path('teacher_student_reg/', views.teacher_student_reg, name="teacher_student_reg"),
    path('tregister/', views.tregister, name="tregister"),
    path('log', views.log, name="log"),
    path('forget_pass/',views.forget_pass, name="forget_pass"),
    path('forget_pass_edit',views.forget_pass_edit, name="forget_pass_edit"),
    path('ad_home',views.ad_home, name="ad_home"),
    path('teacher_reg/',views.teacher_reg, name="teacher_reg"),
    path('^delete/(?P<id>\w+)', views.delete, name='delete'),
    path('logout/', views.logout, name="logout"),
    path('tlogin/', views.tlogin, name="tlogin"),
    path('teacher_home',views.teacher_home, name="teacher_home"),
    path('updation1',views.updation1,name='updation1'),
    path('note_upload', views.note_upload, name="note_upload"),
    path('assignment_upload', views.assignment_upload, name="assignment_upload"),
    path('attendance_upload', views.attendance_upload, name="attendance_upload"),
    path('timetable_upload', views.timetable_upload, name="timetable_upload"),
    path('^accept/(?P<idd>\w+)', views.accept, name='accept'),
    path('^reject/(?P<icc>\w+)', views.reject, name='reject'),
    path('student_reg/',views.student_reg, name="student_reg"),
    path('teacher_student_reg', views.teacher_student_reg, name="teacher_student_reg"),
    path('student_log/',views.student_log, name="student_log"),
    path('student_home',views.student_home, name="student_home"),
    path('updation',views.updation,name='updation'),
    path('works', views.works, name="works"),

]
