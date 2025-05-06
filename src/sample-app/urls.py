from django.conf import settings
from django.urls import re_path, include
from welcome.views import index, health, headers, basic_questions, folder

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^basic_questions/', basic_questions),
    re_path(r'^folder/', folder),
    re_path(r'^health/', health),
    re_path(r'^headers/', headers),
]
