from django.urls import path
from .views import proflie, studnetcreate, oders ,TechersView , TecherDetil , khtechers , batechers ,omtechers , shtechers , proflie

app_name = "accounts"

urlpatterns = [
    path('profile/' , proflie , name = 'proflie'),
    path('oders/' , oders , name = 'pr'),
    path("signup/", studnetcreate , name="regsiters"),
    path("techer/", TechersView.as_view() , name="techers"),
    path("techer/<int:pk>", TecherDetil.as_view() , name="techers_detil"),
    path('ka_techers', khtechers ,name='ka'),
    path('om_techers', omtechers ,name='om'),
    path('ba_techers', batechers ,name='ba'),
    path('sh_techers', shtechers ,name='sh'),
]
