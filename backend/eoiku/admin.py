from django.contrib import admin

from .models import Post,User_info,Coupon
# Register your models here.


admin.site.register(Post)
admin.site.register(User_info)
admin.site.register(Coupon)