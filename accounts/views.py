from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *


# Create your views here.
class AccountView(APIView):
    def post(self, request):
        try:
            serializer = AccountSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({
                    "code": 0,
                    "message": serializer.data
                })
            return JsonResponse({
                "code": 0,
                "message": serializer.errors
            })

        except Exception as e:
            print(str(e))
            return JsonResponse({
                "code": 1,
                "message": ""
            })

    def get(self, request):
        data = request.GET
        if request.GET['action'] == "auth":
            try:
                isAuthenticated = AccountOtp.objects.filter(phoneNumber=data['phoneNumber'], otp=data['otp'])
                token = ""
                if isAuthenticated:
                    AccountModel.objects.filter(phoneNumber=data['phoneNumber']).update(token=token)
                    return JsonResponse({
                        "code": 0,
                        "token": token
                    })
                return JsonResponse({
                    "code": 1,
                    "message": "Not Authorized"
                })
            except Exception as e:
                return JsonResponse({
                    "code": 1,
                    "errors": "something went wrong"
                })
        if request.GET['action'] == "profile":
            try:
                account = AccountModel.objects.get(token=data['token'])
                return JsonResponse({
                    "profileImage": str(account.profileImage),
                    "fullName": str(account.fullName),
                    "phoneNumber": str(account.phoneNumber)
                })
            except Exception as e:
                return JsonResponse({
                    "code": 1,
                    "message": "Authorization Failed"
                })


"""
handles grups 
"""


class AccountGroupView(APIView):
    def post(self, request):
        try:
            serializers = AccountGroupSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({
                    "code": 0,
                    "message": "New Item Added"
                })

            return JsonResponse({
                "code": 1,
                "message": "Authoization Failed"
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "message": "Something went wrong"
            })

    def get(self, request):
        try:
            accounts = AccountModel.objects.filter(accounts__token=request.GET['token']).all().values()
            return JsonResponse({
                "code": 0,
                "accounts": list(accounts)
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "accounts": []
            })
