from django.shortcuts import render
from .models import User, salary
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialisers import UserSerializer, SalarySerializer


class Register(APIView):
    def post(self, request):
        print("1111")
        try:
            serialized = UserSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                res = {
                    "code": status.HTTP_200_OK,
                    "message": "user registration successfully"
                }
                return Response(res)
            else:
                res = {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": serialized.errors
                }
                return Response(res)
        except Exception as e:
            print("eeeeeeee", e)


class GetAllUsers(APIView):
    def get(self, request):
        try:

            data = User.objects.all()
            serialized_data = UserSerializer(data, many=True)
            res = {
                "code": status.HTTP_200_OK,
                "message": "data returned successfully",
                "data": serialized_data.data,
            }
            return Response(res)
        except Exception as e:
            print(e)


class Add_salary(APIView):
    def post(self, request):
        try:
            sal_serial = SalarySerializer(data=request.data)
            if sal_serial.is_valid():
                sal_serial.save()
                res = {
                    "code": status.HTTP_200_OK,
                    "message": "salary release successfully"
                }
                return Response(res)
            else:
                res = {
                    "code": status.HTTP_400_BAD_REQUEST,
                    "message": sal_serial.errors
                }
                return Response(res)
        except Exception as e:
            print(e)
