from typing import Type
from django.db import models
from datetime import datetime
from django.forms import model_to_dict

class Type(models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre')
    
    def __str__(self):
        return 'nro:{} / nombre:{}'.format(self.id,self.name)
    
    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        ordering=['id']
           
    
class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre',unique=True)
    desc=models.CharField(max_length=500,null=True,blank=True,verbose_name='Description')
    
    def __str__(self):
        return 'nro:{} / nombre:{}'.format(self.id,self.name)  
    
    def toJSON(self):
        item=model_to_dict(self)
        return item    
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['id']
        
class Product(models.Model):
    name=models.CharField(max_length=150,verbose_name='Nombre',unique=True)        
    cate=models.ForeignKey(Category,on_delete=models.CASCADE)      
    image=models.ImageField(upload_to='product/%Y/%m/%d',null=True,blank=True)
    pvp=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Produtos'
        ordering=['id']  
        
class Client(models.Model):
    names=models.CharField(max_length=150,verbose_name='Nombres')
    surnames=models.CharField(max_length=150,verbose_name='Apellidos')
    dni=models.CharField(max_length=10,unique=True,verbose_name='Dni')
    birthday=models.DateField(default= datetime.now,verbose_name='fecha de nacimiento')
    address=models.CharField(max_length=150,null=True,blank=True,verbose_name='Direccion')
    sexo=models.CharField(max_length=10,default='Male',verbose_name='Sexo')  
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['id']  
        
class Sale(models.Model):
    cli=models.ForeignKey(Client,on_delete=models.CASCADE)
    date_joined=models.DateField(default= datetime.now)
    subtotal=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    iva=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    total=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    
    def __str__(self):
        return self.cli.names
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering=['id']       
        
class DetSale(models.Model):
    sale=models.ForeignKey(Sale,on_delete=models.CASCADE)
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    cant=models.IntegerField(default=0)
    subtotal=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    
    def __str__(self):
        return self.prod.name
    
    class Meta:
        verbose_name='Detalle de Venta'
        verbose_name_plural='Detalle de Ventas'
        ordering=['id']                
  

class Employee(models.Model):
    categ=models.ManyToManyField(Category)
    type=models.ForeignKey(Type,on_delete=models.CASCADE) #on_delete en casacada(elimina todo si se elimina type) o SET_NULL(se pone nulo y NULL=True)
    names=models.CharField(max_length=150,verbose_name='nombres')
    dni=models.CharField(max_length=10,unique=True,verbose_name='Dni')
    date_joined=models.DateField(default=datetime.now,verbose_name='fecha registro')
    date_creation=models.DateTimeField(auto_now=True)
    date_updated=models.DateTimeField(auto_now_add=True)
    age=models.PositiveIntegerField(default=0)
    salary=models.DecimalField(default=0.0,max_digits=9,decimal_places=2)
    state=models.BooleanField(default=True)
    #gender=models.CharField(max_length=50,null=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d',null=True,blank=True)
    cvitae=models.FileField(upload_to='cvitae/%Y/%m/%d',null=True,blank=True)
    
    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name='Empleado'
        verbose_name_plural='Empleados'
        db_table='empleado'
        ordering=['id'] #se ordena de forma descendente si ponemos -id sera ascendente
        
    