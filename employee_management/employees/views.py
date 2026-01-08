from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model

from .models import Employee
from .serializers import EmployeeSerializer

User = get_user_model()

class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        email = data.get("email")
        username = data.get("username")
        password = data.get("password")

        if not password:
            return Response(
                {"detail": "Password is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not email and not username:
            return Response(
                {"detail": "Email or username is required."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
        if email and not username:
            user = User.objects.filter(email=email).first()
            if not user:
                return Response(
                    {"detail": "No active account found with the given credentials"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            data["username"] = user.username
            data.pop("email")  # VERY IMPORTANT

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
class EmployeeViewSet(viewsets.ModelViewSet):

    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Employee.objects.all()

    def destroy(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.status = Employee.Status.INACTIVE
        employee.save(update_fields=["status"])

        return Response(
            {"message": "Employee marked as inactive successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
