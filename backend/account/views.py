import json
import bcrypt
import jwt

from backend.settings import SECRET_KEY
from .models import User
from django.shortcuts import render

from django.views import View
from django.http import JsonResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class SignUpView(View):
    def post(self,request):
        data =json.loads(request.body)
        try:
            if User.objects.filter(id=data['id']).exists():
                return JsonResponse({'message':'User is already exists'},status=401)
            
            pw=data['pw'].encode('utf-8')
            pw_crypt = bcrypt.hashpw(pw,bcrypt.gensalt())
            pw_crypt = pw_crypt.decode('utf-8')

            
            User(
                id = data['id'],
                nickname = data['nickname'],
                pw = pw_crypt,
                email = data['email'],
                phonenum = data['phonenum']

            ).save()

            return JsonResponse({'message':'Success'},status=200)
        except KeyError:
            return JsonResponse({'message':'FAIL'},status=404)



class SignInView(View):
    def post(self,request):
        data = json.loads(request.body)
        
        try:
            if User.objects.filter(id=data['id']).exists():
                user = User.objects.get(id=data['id'])

                if bcrypt.checkpw(data['pw'].encode('utf-8'),user.pw.encode('utf-8')):
                    token = jwt.encode({'id':data['id']},SECRET_KEY,algorithm="HS256")
                    token = token.decode('utf-8')
                    return JsonResponse({'token':token},status=200)
                else :
                    return JsonResponse({'message':'FAIL'},status=401)

            return JsonResponse({'message':'FAIL'},status=400)

        except KeyError:
            return JsonResponse({'message':'FAIL'},status=404)



class TokenCheckview(View):
    def post(self,request):
        data = json.loads(request.body)

        user_token_info = jwt.decode(data['token'],SECRET_KEY,algorithms='HS256')

        if User.objects.filter(id=user_token_info['id']).exists():
            return JsonResponse({'message':'Success'},status=200)

        return JsonResponse({'message':'FAIL'},status=403)