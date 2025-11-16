
from rest_framework import serializers
from .models import Post, Category, Tag, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='author', write_only=True)

    post = serializers.PrimaryKeyRelatedField(read_only=True)
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), source='post', write_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content', 'author', 'author_id', 'post', 'post_id', 'created_at')



class PostSerializer(serializers.ModelSerializer):
    """ Posttin toliq magluwmatin korsetiw ushin """
    author = UserSerializer(read_only=True)
    # author_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='author', write_only=True)

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True, required=False, allow_null=True)

    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), source='tags', many=True, write_only=True, required=False)

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'author', 'category', 'category_id', 'tags', 'tag_ids', 'comments', 'created_at')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # if 'view' in self.context and self.context['view'].action == 'list':
        #     self.fields.pop('content')
        #     self.fields.pop('comment')

        if self.context['view'].action == 'list':
            self.fields.pop('content')
            self.fields.pop('comments')










