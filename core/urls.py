from django.urls import path
from core.views.category.views import *
from django.conf import settings 
from django.conf.urls.static import static

app_name='erp'

urlpatterns = [
  path('category/list/',CategoryListView.as_view(),name='category_list'),
  path('category/add/',CategoryCreateView.as_view(),name='category_create'),
  path('category/edit/<int:pk>/',CategoryUpdateView.as_view(),name='category_update'),
  path('category/delete/<int:pk>/',CategoryDeleteView.as_view(),name='category_delete'),
  path('category/form/', CategoryFormView.as_view(), name='category_form'),
  
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)