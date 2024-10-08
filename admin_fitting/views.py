from rest_framework.permissions import  IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from consumer.models import Fitting
from consumer.serializers import FittingSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import status

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            # Validate the user credentials and retrieve the token
            serializer.is_valid(raise_exception=True)
            user = serializer.user  # This will get the authenticated user
            token_data = serializer.validated_data
            
            # Create a custom response with the token and user details
            response_data = {
                "refresh": token_data["refresh"],
                "access": token_data["access"],
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "is_staff": user.is_staff
                }
            }

            return Response(response_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RegisterUserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data
        user = User.objects.create(
            username=data['username'],
            email=data.get('email', ''),
            password=make_password(data['password'])
        )
        return Response({"message": "User created successfully."}, status=201)
    
class AdminFittingViewSet(viewsets.ModelViewSet):
    queryset = Fitting.objects.all()
    serializer_class = FittingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Allow admins to view all fittings
        return self.queryset