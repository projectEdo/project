from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
	path('main', include('main.urls'), name='main'),
	path('job/', include('project.urls'), name='project'),
	path('', include('user.urls'), name='author'),
]
