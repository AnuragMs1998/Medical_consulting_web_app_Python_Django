from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND,HTTP_200_OK)
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth.forms import UserCreationForm
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicineSerializer, MedicineSearchSerializer
from .serializers import UserRegister, UserDataSerializer, MedicineDataSerializer, MedicineRegister
from med_site.models import Medicine


from django.contrib.auth.decorators import login_required

#  Medicine availability
@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def available_med(request):
    med = Medicine.objects.all()
    serializer = MedicineSerializer(med, many=True)
    return Response(serializer.data,status=HTTP_200_OK)

#  search medicine
@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def search_med(request):
    search = request.data.get("search")
    search_data = Medicine.objects.filter(med_name__contains=search)
    
    serializer = MedicineSearchSerializer(search_data, many=True)
    return Response(serializer.data,status=HTTP_200_OK)



# medicines details
@permission_classes((IsAuthenticated,))    
class medicine_details(APIView):
    def get_med(self,pk):
        try:
            return Medicine.objects.get(pk=pk)
        except:
            raise Http404
    def get(self,request,pk):
        meddata = self.get_med(pk)
        serializer = MedicineDataSerializer(meddata)
        return Response(serializer.data)
    def put(self,request,pk):
        meddata = self.get_med(pk)
        serializer = MedicineDataSerializer(meddata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'messege':'error found','error':serializer.errors})
    def delete(self,request,pk):
        meddata = self.get_med(pk)
        meddata.delete()
        return Response({'messege':'Medicine deleted'})
#  add Medicine
@permission_classes((IsAuthenticated,))
class add_medicine(APIView):
       
    def post(self,request):
        serializer = MedicineRegister(data=request.data)
      
        dic={}
        if serializer.is_valid():
            med_data = serializer.save()
            dic['response']= 'The following medicine added'
            dic['med_name']= med_data.med_name
            dic['purpose']= med_data.purpose
            dic['unit']= med_data.unit
            dic['dosage']= med_data.dosage
            dic['stock']= med_data.stock
            
        else:
           serializer.errors
        return Response(dic)



# sign up


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):
    form = UserCreationForm(data=request.data)
    if form.is_valid():
        user = form.save()
        return Response("account created successfully", status=status.HTTP_201_CREATED)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)

#  login
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)


