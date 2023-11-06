from django.urls import path
from .views import CommentCreateAPIView, AdvertisingCreateAPIView, AdvertisingRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('comment', CommentCreateAPIView.as_view(), name='create_comment'),
    path('advertising', AdvertisingCreateAPIView.as_view(), name='create_advertising'),
    path('advertising/<pk>', AdvertisingRetrieveUpdateDestroyAPIView.as_view(),
         name='advertising_retrieve_update_destroy'),

]
