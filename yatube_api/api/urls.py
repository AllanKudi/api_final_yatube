from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comment')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
