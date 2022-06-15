from django.contrib import admin
from django.urls import path, include
from quiz.views import RandomQuestion, UpdateScores, Leaderboard, IndexView

admin.site.site_header = 'Binance Quiz'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/random/', RandomQuestion.as_view(), name='random'),
    path('api/score/update/', UpdateScores.as_view(), name='score_update'),
    path('api/score/leaderboard/', Leaderboard.as_view(), name='leaderboard'),
    path('', IndexView.as_view(), name='index'),

]