from django.conf.urls import url, include

from rest_framework import routers

from .views import (
	UserListAPIView, 
	UserCreateAPIView, 
	UserDetailAPIvView,
	ProjectlistAPIView,
	ProjectDetailAPIView,
	ProjectCategoryDetailView,
	ProjectVideoView,
	VideoUploadView,
	CategoryUploadView,
	)


urlpatterns = [

# Users Related Url
url(r'^users/$',UserListAPIView.as_view(),name="User"),

url(r'^users/create/$',UserCreateAPIView.as_view(),name="create"),

url(r'^users/(?P<pk>[\w-]+)/$', UserDetailAPIvView.as_view(), name='detail'),


#project Related Url

url(r'project/$',ProjectlistAPIView.as_view(),name="Project"),

url(r'^project/(?P<title>[\w-]+)/$', ProjectDetailAPIView.as_view(), name='project_list'),

url(r'^categories/$', ProjectCategoryDetailView.as_view(), name='categories'),

url(r'^videos/',ProjectVideoView.as_view(),name="video"),

url(r'^video/upload',VideoUploadView.as_view(),name="Upload"),

url(r'category/upload',CategoryUploadView.as_view(),name="category-upload"),
]

