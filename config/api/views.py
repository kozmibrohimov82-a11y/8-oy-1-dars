from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import *


class CarView(APIView):
    def get(self,request:Request,pk=None):
        if pk:
            car=Car.objects.filter(pk=pk).values().first()
            if not car:
                raise NotFound(default="Car not found")
            
            return Response(car)
        cars=Car.objects.values()
        return Response(cars)
    
    def post(self,request:Request):
        body=request.data
        Car.objects.create(**body)

        return Response({
            'message':'Car qoshildi'
        })    
    
    def put(self,request:Request,pk):
        car=Car.objects.filter(pk=pk).first()
        if not car:
            raise NotFound(default="Car not found")
        body=request.data
        car.model= body.get('model',car.model)
        car.year = body.get('year',car.year)
        car.color = body.get('color',car.color)
        car.category_id = body.get('category_id',car.category_id)
        car.save()

        return Response({'message':'Data update!'})
    
    def delete(self,request:Request,pk):
        car=Car.objects.filter(pk=pk).first()
        if not car:
            raise NotFound(default="Car not found")
        car.delete()

        return Response({'message':'Car delete seccesful!'})

class CategoryView(APIView):

    def get(self, request: Request,pk=None):
        if pk:
            category=Category.objects.filter(pk=pk).values().first()
            if not category:
                raise NotFound(default="Car not found")
            
            return Response(category)
        categories = Category.objects.values()
        return Response(categories)
    
    def post(self,request:Request):
        body=request.data
        Category.objects.create(**body)

        return Response({
            'message':'Categorya qoshildi'
        })
    
    def put(self,request:Request,pk):
        category=Category.objects.filter(pk=pk).first()
        if not category:
            raise NotFound(default="Car not found")
        body=request.data
        category.name= body.get('name',category.name)
        category.save()

        return Response({'message':'Data update!'})
    
    def delete(self,request:Request,pk):
        category=Category.objects.filter(pk=pk).first()
        if not category:
            raise NotFound(default="Car not found")
        category.delete()

        return Response({'message':'Car delete seccesful!'})
    