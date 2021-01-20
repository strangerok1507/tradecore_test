from rest_framework.routers import DefaultRouter

from apps.post.views import PostViewSet, LikeViewSet


app_name = 'post'
router = DefaultRouter()

router.register(r'like', LikeViewSet)
router.register(r'', PostViewSet)

urlpatterns = router.urls
