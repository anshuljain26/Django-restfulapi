from django.contrib.auth.models import User, Group

from rest_framework import serializers


from onlineprogram.models import project_category,Project,Upload,Enroll


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

        write_only_fields = ('password',)

        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(

            username=validated_data['username'],

            email=validated_data['email'],

            first_name=validated_data['first_name'],

            last_name=validated_data['last_name'],

            is_staff=True

        )

        user.set_password(validated_data['password'])
        user.save()

        return user



class UserSerializers(serializers.HyperlinkedModelSerializer):

	url = serializers.HyperlinkedIdentityField(view_name='api:detail')

	class Meta:

		model = User

		fields = ('url', 'username', 'email')





class UserDetailSerializer(serializers.ModelSerializer):

	url = serializers.HyperlinkedIdentityField(view_name='api:detail')

	class Meta:

		model = User

		fields = ['url','username','email','first_name','last_name','is_active','date_joined','is_staff']



class ProjectListSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='api:project_list',lookup_field='title')

    category_name = serializers.ReadOnlyField()

    class Meta:
        model = Project

        fields = ['url','category_name','title','image','timestamp']



class ProjecyDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:project_list',lookup_field='title')

    title_name    = serializers.ReadOnlyField()

    category_name  = serializers.ReadOnlyField()

    user_name     =  serializers.ReadOnlyField()

    Description   =  serializers.ReadOnlyField()

    Course_period =  serializers.ReadOnlyField()





    #publish =  serializers.ReadOnlyField()


   
    #video = serializers.HyperlinkedIdentityField(view_name='api:project_list',lookup_field='title')

    class Meta:

        model = Upload


        fields = ['user_name','title_name','category_name','Description','Course_period','Publish','url']


class ProjectCategorySerializer(serializers.ModelSerializer):

    class Meta:

        model = project_category

        fields = ['categories']



class ProjectVideoSerializers(serializers.ModelSerializer):
    title_name = serializers.ReadOnlyField()

    #url = serializers.HyperlinkedIdentityField(view_name='api:project_list',lookup_field='title')

    category_name = serializers.ReadOnlyField()

    class Meta:

        model = Upload

        fields = ['category_name','title_name','Content','Video','title_name','Publish']


class ProjectVideoUploadSerializers(serializers.ModelSerializer):

    class Meta:

        model = Upload

        fields = ['category_upload','title_upload','Content','Video','Publish']


class ProjectCategoryUploadSerializers(serializers.ModelSerializer):

    class Meta:

        model = Project

        fields = ['category','title','Description','Course_period','cost','Publish']


