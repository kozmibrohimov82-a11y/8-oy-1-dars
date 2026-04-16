from rest_framework import serializers
from .models import Car, Category
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

    def validate(self, attrs):
        password1=attrs.get('password1')
        password2 = attrs.get('password2')

        if password1!=password2:
            raise serializers.ValidationError({
                'password':"Parollar bir xil bolishi kerak"
            })

        return attrs
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password1')

        return User.objects.create_user(password=password,**validated_data)
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





