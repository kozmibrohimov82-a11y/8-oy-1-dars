from rest_framework import serializers
from .models import Car, Category

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        
    def validate_model(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Model nomi bosh harfda bolishi kerak")
        if not value.isalpha():
            raise serializers.ValidationError("Model nomi faqat harflardan tashkil topkan bolishi kerak")

        return value
    def validate_color(self,value):
        if not value.isalpha():
            raise serializers.ValidationError("Ranglar nomi faqat harflardan tashkil topkan bolishi kerak")

        return value
    def validate_year(self,value):

        if not value>1950:
            raise serializers.ValidationError("Yili faqat 1950dan katta bolishi kerak")
        return value



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate_name(self,value):
        if not value.istitle():
            raise serializers.ValidationError("Model nomi bosh harfda bolishi kerak")
        if not value.isalpha():
            raise serializers.ValidationError("Model nomi faqat harflardan tashkil topkan bolishi kerak")
        return value
