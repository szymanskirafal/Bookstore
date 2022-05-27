from django.urls import path

from rest_framework import routers

from .views import BooksViewSet

router = routers.SimpleRouter()
router.register(r'books', BooksViewSet)

urlpatterns = [
    # path('forgot-password/', ForgotPasswordFormView.as_view()),
]

urlpatterns += router.urls
