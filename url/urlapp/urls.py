from django.urls import path
from urlapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home',views.homepage),
    path('<str:id>',views.originalpage)
]