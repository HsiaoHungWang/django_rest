from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Categories, Member, Spotimagesspot

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class SpotimagesspotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Spotimagesspot
        fields = '__all__'

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        # fields = ['user_id','user_name','user_email']

    def validate_user_password(self, value):
        return make_password(value)
