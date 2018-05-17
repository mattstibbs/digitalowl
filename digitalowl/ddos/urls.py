from django.urls import path, include
from ddos import views

urlpatterns = [
    path(
        '',
        views.ServiceView.as_view(),
        name='service_list'
    ),
    path(
        '<str:identifier>',
        views.ServiceDetailView.as_view(),
        name='service_detail_view'
    )
]
