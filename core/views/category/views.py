from django.http.response import JsonResponse
from  django.views.generic import ListView ,CreateView , UpdateView ,DeleteView
from core.models import Category ,Product
from django.shortcuts import render ,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from core.forms import CategoryForm
from django.urls import reverse_lazy


class CategoryListView(ListView):
    model=Category
    template_name='category/list.html'      
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs): 
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): 
        data={}
        try:
            data=Category.objects.get(pk=request.POST['id']).toJSON()     
        except Exception as e:
                data['error']=str(e)              
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Listado de Categorias'
        context['create_url']=reverse_lazy('erp:category_create')
        context['list_url']=reverse_lazy('erp:category_list')
        context['entity']='Categorias'
        return context
    
    
class CategoryCreateView(CreateView):    
    model=Category
    form_class=CategoryForm
    template_name='category/create.html'
    success_url=reverse_lazy('erp:category_list')
    
    def post(self, request, *args, **kwargs): 
        data={}
        try:
            action=request.POST['action']
            if action == 'add':
                form=self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors    
            else:
                data['error']='no ingreso a ninguna opcion'                
        except Exception as e:
                data['error']=str(e)              
        return JsonResponse(data)  
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Creacion de una Categorias'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        context['action']='add'
        return context
    
    
class CategoryUpdateView(UpdateView):
    model=Category
    form_class=CategoryForm
    template_name='category/create.html'
    success_url=reverse_lazy('erp:category_list')     
    
    def dispatch(self, request, *args, **kwargs): 
        self.object=self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs): 
        data={}
        try:
            action=request.POST['action']
            if action == 'edit':
                form=self.get_form()
                if form.is_valid():
                    form.save()
                else:
                    data['error']=form.errors    
            else:
                data['error']='no ingreso a ninguna opcion'                
        except Exception as e:
                data['error']=str(e)              
        return JsonResponse(data)  
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Edicion de una Categorias'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        context['action']='edit'
        return context
    
class CategoryDeleteView(DeleteView):    
    model=Category
    form_class=CategoryForm
    template_name='category/delete.html'
    success_url=reverse_lazy('erp:category_list') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Eliminacion de una Categorias'
        context['entity']='Categorias'
        context['list_url']=reverse_lazy('erp:category_list')
        return context
    
    
    
    
    
    
    
    
    