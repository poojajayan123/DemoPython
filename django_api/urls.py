from django.contrib import admin
from django.urls import path, include
import Question,Exam,User,Category
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('question/', include('Question.urls')),
    path('user/', include('User.urls')),
    #path('exam/', include('Exam.urls')),

]
