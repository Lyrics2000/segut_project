

from django.urls import path
from .views import index,signup,logout_user,profile_image,activate_account


app_name = "account"

urlpatterns = [
    path('', index,name="sign_in"),
    path('signup/', signup,name="sign_up"),
    path('logout',logout_user,name="logout"),
    path('profile_image/',profile_image,name="upload_image"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_account, name='activate')
]



