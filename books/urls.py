from django.urls import path

from rest_framework import routers

from .views import BooksViewSet, ImportCreateAPIView

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('import/', ImportCreateAPIView.as_view()),
]

urlpatterns += router.urls
