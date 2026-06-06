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

from rest_framework import viewsets,permissions
from .models import Letter
from .serializers import LetterSerializer

class LetterViewSet(viewsets.ModelViewSet):
    serializer_class = LetterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Letter.objects.filter(user=self.request.user)
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

