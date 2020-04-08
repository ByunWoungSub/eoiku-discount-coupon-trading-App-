from rest_framework.serializers import ModelSerializer
from .models import Post,User_info,Coupon   

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User_info
        fields = '__all__'

class CouponSerializer(ModelSerializer):
    class Meta:
        model = Coupon
        fields ='__all__'

        