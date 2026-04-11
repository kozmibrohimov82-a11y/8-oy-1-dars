# from rest_framework.request import Request
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound
from .models import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *


class CarPostGet(ListCreateAPIView):
    # queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return CarSerializer
        else:
            return CategorySerializer

class CarUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_url_kwarg = 'car_id'

    def get_object(self):
        car = self.queryset.get(pk=self.kwargs['car_id'])
        return car

################################################################3

class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class CategoryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




















# class CarView(APIView):
#     def get_car(self,pk):
#         car = Car.objects.filter(pk=pk).values().first()
#         if not car:
#                 raise NotFound(default="Car not found")
#         return car
#     def get(self,request:Request,pk=None):
#         if pk:
#             car=self.get_car(pk)
#             serializer=CarSerializer(car)
#             return Response(serializer.data)
#
#         cars = Car.objects.all()
#         serializer = CarSerializer(cars, many=True)
#         return Response(serializer.data)
#
#     def post(self,request:Request):
#         serializer=CarSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"message":"malumot saqlandi"})
#
#     def put(self,request:Request,pk):
#
#         car=self.get_car(pk)
#         serializer=CarSerializer(instance=car,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'message': 'Data update'})
#
#     def patch(self,request:Request,pk):
#         car = self.get_car(pk)
#         serializer = CarSerializer(instance=car, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'message': 'Data update'})
#
#
#     def delete(self,request:Request,pk):
#         car = self.get_car(pk)
#         car.delete()
#         return Response({"message":"Car delete seccesfull"})
#
#
# class CategoryView(APIView):
#     def get_category(self,pk):
#         category = Category.objects.filter(pk=pk).first()
#         if not category:
#                 raise NotFound(default="Category not found")
#         return category
#
#     def get(self, request: Request, pk=None):
#         if pk:
#             category = self.get_category(pk)
#             serializer = CategorySerializer(category)
#             return Response(serializer.data)
#
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#     def post(self, request: Request):
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"message": "Data save"})
#
#     def put(self, request: Request, pk):
#
#         category = self.get_category(pk)
#         serializer = CategorySerializer(instance=category, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'message': 'Data update'})
#
#     def patch(self, request: Request, pk):
#         category = self.get_category(pk)
#         serializer = CategorySerializer(instance=category, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'message': 'Data update'})
#
#     def delete(self, pk):
#         category = self.get_category(pk)
#         category.delete()
#         return Response({"message": "Category delete seccesfull"})
