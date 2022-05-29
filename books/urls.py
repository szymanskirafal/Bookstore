from django.urls import path

from rest_framework import routers

from .views import ApiSpecAPIView, BooksViewSet, ImportCreateAPIView

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('api_spec/', ApiSpecAPIView.as_view(), name='api-spec'),
    path('import/', ImportCreateAPIView.as_view(), name='import'),
]

urlpatterns += router.urls
