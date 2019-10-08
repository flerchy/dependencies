from django.conf.urls import include
from django.conf.urls import url

from .views import DispatchView
from .views import EmptyView
from .views import KwargsView
from .views import QuestionFormView
from .views import SelfView
from .views import UserView


urlpatterns = [
    url(r"^test_dispatch_request/(\d+)/(\w+)/$", DispatchView.as_view()),
    url(r"^test_empty_request/(\d+)/(\w+)/$", EmptyView.as_view()),
    url(r"^test_inject_user/(?P<pk>\d+)/(?P<slug>\w+)/$", UserView.as_view()),
    url(r"^test_inject_kwargs/(?P<pk>\d+)/(?P<slug>\w+)/$", KwargsView.as_view()),
    url(r"^test_inject_self/(?P<pk>\d+)/(?P<slug>\w+)/$", SelfView.as_view()),
    url(r"^test_form_view/(?P<pk>\d+)/$", QuestionFormView.as_view()),
    url(r"^api/", include("django_project.api.urls")),
]
