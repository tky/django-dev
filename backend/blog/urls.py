from rest_framework import routers
from .views import UserViewSet, EntryViewSet

app_name = 'blog'
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'entries', EntryViewSet, 'entries')
