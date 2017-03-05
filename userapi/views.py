from django.shortcuts import render

from django.contrib.auth.models import User, Group


from userapi.serializers import(
	UserSerializers, 
	UserCreateSerializer, 
	UserDetailSerializer,
	ProjectListSerializer,
	ProjecyDetailSerializer,
	ProjectCategorySerializer,
	ProjectVideoSerializers,
	ProjectVideoUploadSerializers,
	ProjectCategoryUploadSerializers,
	)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from userapi.pagination import PostPageNumberPagination

from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)



from rest_framework import generics

from onlineprogram.models import project_category,Project,Upload,Enroll

# Create your views here.


class UserListAPIView(generics.ListAPIView):

	query = User.objects.all().order_by('-date_joined');

	permission_classes = [IsAuthenticated,IsAdminUser]

	serializer_class = UserSerializers


	def get_queryset(self, *args, **kwargs):

		return User.objects.all()





class UserCreateAPIView(generics.CreateAPIView):

	query = User.objects.all()

	serializer_class  = UserCreateSerializer


    


   

class UserDetailAPIvView (generics.RetrieveAPIView):

	queryset = User.objects.all()

	serializer_class = UserDetailSerializer

	permission_classes = [IsAuthenticated,IsAdminUser]

	def get_queryset(self, *args, **kwargs):

		return User.objects.all()


class ProjectlistAPIView(generics.ListAPIView):

	queryset = Project.objects.all()

	serializer_class = ProjectListSerializer

	pagination_class = PostPageNumberPagination

	filter_backends= [SearchFilter, OrderingFilter]

	search_fields = ['title','category__categories']


	def get_queryset(self, *args, **kwargs):

		return Project.objects.all()


class ProjectDetailAPIView(generics.RetrieveAPIView):

	queryset = Project.objects.all()

	serializer_class = ProjecyDetailSerializer

	lookup_field = 'title'

	def get_queryset(self, *args, **kwargs):

		return Project.objects.all()



class ProjectCategoryDetailView(generics.ListAPIView):

	queryset = project_category.objects.all()


	serializer_class = ProjectCategorySerializer

	lookup_field = 'categories'

	def get_queryset(self, *args, **kwargs):

		return project_category.objects.all()



class ProjectVideoView(generics.ListAPIView):

	queryset = Upload.objects.all()

	pagination_class = PostPageNumberPagination

	filter_backends= [SearchFilter, OrderingFilter]

	search_fields = ['title_upload__title','category_upload__categories']

	permission_classes = [IsAuthenticated,IsAdminUser]

	serializer_class = ProjectVideoSerializers


class VideoUploadView(generics.CreateAPIView):

	queryset = Upload.objects.all()

	pagination_class = PostPageNumberPagination

	filter_backends= [SearchFilter, OrderingFilter]

	search_fields = ['title_upload']


	permission_classes = [IsAdminUser]

	serializer_class = ProjectVideoUploadSerializers


class CategoryUploadView(generics.CreateAPIView):

	queryset = Project.objects.all()

	permission_classes = [IsAdminUser]

	serializer_class = ProjectCategoryUploadSerializers



