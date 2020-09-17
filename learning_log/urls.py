"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls), #书本上的写法，会报错，将include（）取消就可以了
    url(r'^admin/', admin.site.urls),
    url(r'', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
    url(r'^users/', include(('users.urls', 'users'), namespace='users')),
]
