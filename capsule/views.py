# ============================================================
# DEVELOPER NOTE
# ------------------------------------------------------------
# get_queryset()
#   - Controls which Letter objects a user can READ.
#   - We filter by request.user so each user only sees
#     their own letters.
#   - Without this filter, every authenticated user could
#     see every letter in the database, which is a security
#     and privacy issue.
#
# perform_create()
#   - Controls what happens when a new Letter is CREATED.
#   - The serializer marks the 'user' field as read-only,
#     so clients cannot choose or fake an owner.
#   - We automatically assign request.user as the owner
#     when saving the object.
#
# Security Principle:
#   Never trust the client to tell you who they are.
#   Determine identity from the authenticated user on
#   the server side (request.user).
#
# Quick Reminder:
#   get_queryset()  -> Protects READ operations
#   perform_create() -> Protects WRITE operations
# ============================================================
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets,permissions
from .models import Letter
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import LetterSerializer

class LetterViewSet(viewsets.ModelViewSet):
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Letter.objects.filter(user=self.request.user)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
class RegistrationPoint(APIView):
    def post(self,request):
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.create_user(
            username = username,
            email = email,
            password = password
        )

        return Response({
            "id":user.id,
            "username":username,
            "email" : email,
            "message":"User created successfully!"
        }, status=status.HTTP_201_CREATED)


