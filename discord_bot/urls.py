from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from quiz.views import RandomQuestion
from scores.views import UpdateScores, Leaderboard

admin.site.site_header = 'Binance Quiz'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/random/', RandomQuestion.as_view(), name="random"),
    path('api/score/update/', UpdateScores.as_view(), name='score_update'),
    path('api/score/leaderboard/', Leaderboard.as_view(), name='leaderboard')

]
