from django.utils.translation import gettext_lazy as _
from rest_framework.permissions import BasePermission

from common.messages import ACCESS_DENIED


#
class OwnerPermission(BasePermission):
    message = _(ACCESS_DENIED)

    def has_permission(self, request, view):
        print('check perm')
        obj = view.model.objects.get_object(pk=view.kwargs['pk'])
        return request.user.id == obj.user.id
