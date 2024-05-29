from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
    path('home/', views.Home.as_view(), name='Home'),
    path('thesis/', views.thesis.as_view(), name='Thesis'),
    path('thesis/add', views.add_thesis, name='thesisAdd'),
    path('thesis/delete_thesis/<int:id>', views.delete_thesis, name='ThesisDelete'),
    path('thesis/thesis-edit/<pk>', views.ThesisUpdateView.as_view(), name='ThesisUpdate'),
    path('thesis/comment/<int:theses_id>', views.thesis_comments, name='Thesisapp_comments'),
]

