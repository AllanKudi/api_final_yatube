from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination

from django.shortcuts import get_object_or_404

from .permissions import AuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer
from .serializers import PostSerializer, FollowSerializer
from posts.models import Group, Post, Follow


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AuthorOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [AuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CreateListViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    pass


class FollowViewSet(CreateListViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
