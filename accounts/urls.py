from django.conf.urls import url

from accounts.views import sign_in, sign_out

urlpatterns = [
    url(r'^login/$', sign_in, name="login"),
    url(r'^logout/$', sign_out, name="logout"),
#   url(r'^api/login/$', UserLoginView.as_view()),
]
