from django.conf.urls import url
from .views import PredictApi

app_name = 'api'

urlpatterns = [
    url(r'^$', PredictApi.as_view()),
]
