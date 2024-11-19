from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, viewsets, status
from .models import FGFPost
from .serializers import FGFPostSerializer, FGFPostInfoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly

# Basic view and creation in one. In prod this would not need a create since it should be handled elsewhere
class FGFPostViewSet(viewsets.ModelViewSet): # Maybe should be a generics.ListAPIView
  """
  API endpoint that allows FGF posts to be viewed or edited
  """
  queryset = FGFPost.objects.all().order_by('-date_posted') # using FGFPost.objects.filter() or FGFPost.objects.exclude(post_flair="Expired") might be good. Unless there's a better way to do it
  serializer_class = FGFPostSerializer
  # lookup_url_kwarg = "reddit_id"
  # authentication_classes = [SessionAuthentication, BasicAuthentication]
  # permission_classes = [permissions.IsAuthenticated]

  def get_permissions(self):
      if self.action in ['create', 'update', 'partial_update', 'destroy']:
          permission_classes = [IsAdminUser]
      else:
          permission_classes = [IsAuthenticatedOrReadOnly]
      return [permission() for permission in permission_classes]


# Function based stuff \/

# def create(self, request, *args, **kwargs):
#   serializer = self.get_serializer(data=request.data)
#   if serializer.is_valid():
#       self.perform_create(serializer)
#       headers = self.get_success_headers(serializer.data)
#       return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # Should conver this to an APIView instead if I were to use it for something
# @api_view(["GET"])
# def fgfpost_info(request):
#   fgfposts = FGFPost.objects.all()
#   serializer = FGFPostInfoSerializer({
#     "fgfposts": fgfposts,
#     "count": len(fgfposts),
#   })

# Optimizing DB searches
# reference related name on model
#orders = Orders.objects.prefetch_related(
#   #'items',
#   'items__product'
# )