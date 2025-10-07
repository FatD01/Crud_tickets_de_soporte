# tickets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # URLs de Usuario para CATEGORIAS
    path('categorias/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nuevo/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    
    # URLs de Usuario para TICKETS (Home)
    path('', views.TicketListView.as_view(), name='ticket_list'),
    path('tickets/nuevo/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('tickets/<int:pk>/editar/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('tickets/<int:pk>/eliminar/', views.TicketDeleteView.as_view(), name='ticket_delete'),
]