
from .models import Post, Category, Tag, Comment, User
from .serializers import PostSerializer, CategorySerializer, TagSerializer, CommentSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly   # hamme postlardi kore aladi, put, post, patch, delete ushin sistemaga kiriw kerek.
from .permissions import IsAuthorOrReadOnly, IsAdminOrReadOnly, IsAdminOrCreateOnlyOrReadOnly
from rest_framework import permissions



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]    # permission claasin qosamiz

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)   # Jana posttin avtorin avtomatliq belgilew



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None
    permission_classes = [IsAdminOrReadOnly]



class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminOrCreateOnlyOrReadOnly]



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Paydalanıwshılardıń dizimin hám detal maǵlıwmatın kórsetiw ushın.
    Biz paydalanıwshılardı API arqalı ózgertiwdi qálemeymiz, sonlıqtan tek oqıwǵa ruqsat beremiz.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
