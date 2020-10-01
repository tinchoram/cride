"""Circles permission classes"""

#Django REST Framwork
from rest_framework.permissions import BasePermission

#Models
from cride.circles.models import Membership

class IsActiveCircleMember(BasePermission):
    """Allow access only to cricle members.

    Expect that the view implementing this permission
    have a 'circle' attribute assigned.
    """
    def has_permission(self, request, view):
        """Verify user is an active member of the circle"""
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True

class IsAdminOrMembershipOwner(BasePermission):
    """
    Allow accese only to (Circle's admin) or users
    that are owner of the membership (object).
    """

    def has_permission(self, request, view):
        membership = view.get_object()
        if membership.user == request.user:
            return True

        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True,
                is_admin=True
            )
        except Membership.DoesNotExist:
            return False
        return True
