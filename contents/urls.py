from django.urls import path
from contents.views import home_page,about_us,projects,project,article,articles,contact_us

urlpatterns = [
    path('', home_page,name="home"),
    path('about-us', about_us,name="about_us"),
    path('contact-us', contact_us,name="contact_us"),
    path('projects', projects,name="projects"),
    path('project/<prid>', project,name="project"),
    path('articles/<ataype>', articles,name="articles"),
    path('article/<arid>', article,name="article"),

]

