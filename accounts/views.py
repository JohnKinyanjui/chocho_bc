from django.http import JsonResponse
from rest_framework.views import APIView
from .serializers import *
import uuid



class OtpView(APIView):
    """
    handles creation of otp and confirmation
    """
    def post(self, request):
        data = request.data
        #sends otp to the user
        
        try:
            phoneNumber = "254"+data["phoneNumber"][1:]
            
            phoneExists = AccountOtp.objects.filter(phoneNumber=phoneNumber).exists()
            otp = "000000"
            print(phoneExists)
            if phoneExists:
                AccountOtp.objects.filter(phoneNumber=phoneNumber).update(otp=otp)
                return JsonResponse({
                    "code": 0,
                    "message": "Otp send successfully"
                })
                
            otp = AccountOtp(
                phoneNumber = phoneNumber,
                otp = otp
            )
            otp.save()
            return JsonResponse({
                "code": 0,
                "message": "Otp send successfully"
            })
        except Exception as e:
            print(e);
            return JsonResponse({
                "code": 1,
                "message": "Something went wrong",
                "error": str(e)
            })                    
            

class AccountView(APIView):
    """
    Account View the creation of accounts and sign up page
    """
    def post(self, request):
        # creates new accounts
        try:
            token = "djskhjskhfjshfskjhkh"
            data = request.data
            print(data)
            serializer = AccountSerializer(data=data)
            print(request.data)
            if serializer.is_valid():
                serializer.save()
                AccountModel.objects.filter(phoneNumber=data['phoneNumber']).update(token=token)
                return JsonResponse({
                    "code": 0,
                    "token": token
                })
            return JsonResponse({
                "code": 1,
                "message": serializer.errors
            })

        except Exception as e:
            print(str(e))
            return JsonResponse({
                "code": 1,
                "error": str(e)
            })

    def get(self, request):
        data = request.GET
        if request.GET['action'] == "auth":
            try:
                isAuthenticated = AccountOtp.objects.filter(phoneNumber=data['phoneNumber'], otp=data['otp']).exists()
                token = "dfjfkdjhaklhjdjalhfau"
                if isAuthenticated:
                    print(isAuthenticated)
                    accountExists = AccountModel.objects.filter(phoneNumber=data['phoneNumber']).exists()
                    print(accountExists)
                    if accountExists:
                        AccountModel.objects.filter(phoneNumber=data['phoneNumber']).update(token=token)
                        return JsonResponse({
                            "code": 0,
                            "token": token
                        })
                    return JsonResponse({
                        "code": 0,
                        "message": "Ready to Sign Up"
                    })
                return JsonResponse({
                    "code":1,
                    "message": "No Such Otp"
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


class AccountGroupView(APIView):
    """
    handles groups that belong to a certain user 
    """
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
            if data['action'] == "create":
                serializer = AccountGroupItemSerializer(data=data["data"])
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        "code": 0,
                        "message": "New Account Item"
                    })
                return JsonResponse({
                    "code": 1,
                    "message": serializer.errors
                })

            elif data['action'] == "update":
                product = ProductModel.objects.get(product_id=data['product'])
                AccountGroupItem.objects.filter(group__account__token=data['token'], group__groupId=data['groupId'],
                                                name=data['name']).update(product=product)
                return JsonResponse({
                    "code": 0,
                    "message": "account group item updated"
                })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 1,
                "message": "Something went wrong"
            })

    def get(self, request):
        try:
            items = AccountGroupItem.objects.filter(group__account__token=request.GET['token']).all().values('name', 
                                                                                                             'details',
                                                                                                      'phoneNumber',
                                                                                                      'product_id',
                                                                                                      'product__image',
                                                                                                      'product__name',
                                                                                                      'product__cost'
                                                                                                      )
            return JsonResponse({
                "code": 0,
                "data": list(items)
            })
        except Exception as e:
            print(e)
            return JsonResponse({
                "code": 0,
                "errors": "Something went wrong"
            })
