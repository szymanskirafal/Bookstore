from django.urls import path

from rest_framework import routers

from .views import BooksViewSet

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    path('import/', ImportAPIView.as_view()),
]

urlpatterns += router.urls
