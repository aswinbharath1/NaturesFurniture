from django.conf.global_settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Home.urls')),
    path('login/',include('accounts.urls')),
    path('adminhome/',include('dashboard.urls')),
    path('store/',include('store.urls')),
    path('user-profile/',include('user_profile.urls')),
    path('cart/',include('cart.urls')),
    path('wishlist/',include('wishlist.urls')),


]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,documents_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)