from django.urls import path
from . import views

urlpatterns = [
    path('updateStat', views.update_stat_all),
    path('newYoutuber/<str:url>', views.make_new_youtuber),
    path('updateYoutuber/<int:yno>', views.update_youtuber),
]
