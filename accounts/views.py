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
            groups = AccountGroup.objects.filter(account__token=request.GET['token']).all().values()
            return JsonResponse({
                "code": 0,
                "data": list(groups)
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "accounts": []
            })


class AccountGroupItemView(APIView):
    def post(self, request):
        data = request.data
        try:
            if request.POST['action'] == "create":
                serializer = AccountGroupItemSerializer(data=data)
                if serializer.is_valid():
                    return JsonResponse({
                        "code": 0,
                        "message": "New Account Item"
                    })
                return JsonResponse({
                    "code": 1,
                    "message": "Something went wrong"
                })

            elif request.POST['action'] == "update":
                product = ProductModel.objects.get(product_id=data['product'])
                AccountGroupItem.objects.filter(group__account__token=data['token'], group__groupId=data['groupId'], name=data['name']).update(product=product)
                return JsonResponse({
                    "code": 0,
                    "message": "account group item updated"
                })
        except Exception as e:
            return JsonResponse({
                "code": 1,
                "message": "Something went wrong"
            })

    def get(self, request):
        try:
            items = AccountGroupItem.objects.filter(account__token=request.GET['token']).all().values('name', 'details', 'product__image', 'product__name')
            return JsonResponse({
                "code": 0,
                "data": list(items)
            })
        except Exception as e:
            return JsonResponse({
                "code": 0,
                "errors": "Something went wrong"
            })

