import json
import jwt
import requests

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from my_settings import SECRET_KEY
from account.models import User


def login_decorator(func):
    def wrapper(self,request, *args,**kwargs):
        try:
            access_token = request.headers.get('Authorization',None)
            payload = jwt.decode(access_token,SECRET_KEY,algorithms='HS256')
            user = User.objects.get(id=payload['id'])
            request.user=user
        except jwt.exceptions.DecodeError:
            return JsonResponse({'message':'INVALID_TOKEN'},status=400)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'},status=400)

        return func(self,request,*args,**kwargs)

    return wrapper