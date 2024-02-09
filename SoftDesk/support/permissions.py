from rest_framework.permissions import BasePermission, SAFE_METHODS
 
class IsAdminAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
    
class IsContributorAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)
    
class IsAuthorOrReadOnly(BasePermission):

    #s'applique sur le point de terminaison, 
    #def has_permission(self, request, view):
    #    pass

    #s'applique sur l'objet, les SAFE_METHODS sont les actions que peuvent faire ceux en read only, 
    #par exemple si méthode get sur l'objet si tu n'es pas auteur tu peux voir quand même.
    #Le premier True veut dire qu'on autorise la première action, dans le else si c'est vrai ça retournera True donc ça fonctionnera, sinon ce sera False
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user

