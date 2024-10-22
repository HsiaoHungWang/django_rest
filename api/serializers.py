from rest_framework import serializers
from .models import Categories, Member

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        # fields = ['user_id','user_name','user_email']
