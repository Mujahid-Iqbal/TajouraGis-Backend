from django.shortcuts import render
from rest_framework import generics, permissions,status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .models import CustomUser,School,AcademicLevel
from .serializers import UserSerializer, UserListSerializer,UserMeSerializer,SchoolSerializer,AcademicLevelSerializer,CreateSchoolWithLevelsSerializer


class UserSignupView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid login credentials'}, status=400)



class UserMeView(generics.RetrieveAPIView):
    serializer_class = UserMeSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]



class SchoolListView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]


class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated]

class LevelListView(generics.ListCreateAPIView):
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer
    permission_classes = [IsAuthenticated]
    
class LevelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AcademicLevel.objects.all()
    serializer_class = AcademicLevelSerializer
    permission_classes = [IsAuthenticated]


class BulkCreateSchoolsWithLevelsView(generics.CreateAPIView):
    serializer_class = CreateSchoolWithLevelsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Extract schools and academic levels data from the serializer
            schools_data = serializer.validated_data['schools']
            academic_levels_data = serializer.validated_data['academic_levels']

            # Create schools and academic levels
            created_schools = School.objects.bulk_create(schools_data)
            academic_levels = []

            # Link each academic level to its respective school
            for index, school in enumerate(created_schools):
                academic_level_data = academic_levels_data[index]
                academic_level_data['school'] = school
                academic_levels.append(AcademicLevel(**academic_level_data))

            AcademicLevel.objects.bulk_create(academic_levels)

            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)