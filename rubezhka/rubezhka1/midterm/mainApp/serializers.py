from rest_framework import serializers
from .models import *

class BlogsSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 100, min_length = 5, allow_null = False)

        
    

    def create(self, validated_data):
        blogs = blogs(**validated_data)
        blogs.save()
        return blogs

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class BlogListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 200, allow_null = False)
    bloglist = BlogsSerializers(required = False, read_only = True)
    blog_list_id = serializers.IntegerField(write_only = True)

    def create(self, validated_data):
        blog = blog(**validated_data)
        blog.save()
        return blog
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.blogs_id = validated_data.get('blogs_id', instance.blogs_id)
        instance.save()
        return instance