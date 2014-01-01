from django.conf.urls import patterns, url
from .views import create_menu, dishes, setup, preview


urlpatterns = patterns(
    '',

    url(
        r'^setup/$',
        setup,
        name='menu_setup'
    ),

    url(
        r'^dishes/$',
        dishes,
        name='menu_dishes'
    ),

    url(
        r'^preview/$',
        preview,
        name='menu_preview'
    ),

    url(
        r'^(?:(?P<day>[a-z]+))?$',
        create_menu,
        name='menu_create'
    ),
)
