from rest_framework import permissions

class AdminOrReadonly(permissions.IsAdminUser):
    def has_permission(self, request, view): #this is a built in function
        if request.method in permissions.SAFE_METHODS: #SAFE_METHODS means get request
            return True
        else: #put,delete,post
            return bool(request.user and request.user.is_staff) #the user must be authenticated and must be a stuff
            
class ReviewerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view,obj):
        if request.method in permissions.SAFE_METHODS:
            #get request
            return True
        else:
            return obj.user==request.user