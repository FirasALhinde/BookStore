from django.urls import path
from .import views

app_name ='book'
urlpatterns = [
    path('',views.book_list,name='book_list'),
    path('<int:id>/',views.book_detail,name='book_detail'),
    path('new/',views.new_book,name='new_book'),
    path('<int:id>/edit/',views.edit_book,name='edit_book'),
    path('<int:id>/delete/',views.delete_book,name='delete_book'),

]
