from django.contrib import admin
from contents.models import About, Team, Projects, ProjectPicture, Services, Articles, ArticlesFile, Customer, Grades, \
    Test, ArticlesPicture
from django.utils.html import format_html


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    list_filter =['title', 'active']
    list_editable =['active']
    search_fields =['title', 'active']

    # # list_filter = ['active']
    # list_editable = ['name','family','active','owner']
    # search_fields = ['name','family']
    # list_per_page = 20
    # sortable_by = ['name','family','active']
    class Meta:
        model = About

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'active','super']
    list_filter =  ['name', 'active','super']
    list_editable = [ 'active','super']
    search_fields =  ['name', 'active','super']



    class Meta:
        model = Team
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'active','subject']
    list_filter =['name', 'active','subject']
    list_editable =[ 'active','subject']
    search_fields =['name', 'active','subject']

class Meta:
        model = Projects
class ProjectPictureAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.pimage.url))
    list_display = ['__str__', 'image_tag', 'active', 'project','pimage']
    list_filter =['active', 'project','pimage']
    list_editable =['active', 'project','pimage']
    search_fields =['active', 'project','pimage']

class Meta:
        model = ProjectPicture
class ArticlesPictureAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.aimage.url))
    list_display = ['__str__', 'image_tag', 'active', 'article']
    list_filter =['active', 'article']
    list_editable =['active', 'article']
    search_fields =['active', 'article']

class Meta:
        model = ArticlesPicture







class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['__str__','name', 'active']
    list_filter = ['name', 'active']
    list_editable =['name', 'active']
    search_fields =['name', 'active']

class Meta:
        model = Articles


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter =['active']
    list_editable =['active']
    search_fields =['active']

class Meta:
        model = Services
class ArticlesFileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter =['active']
    list_editable =['active']
    search_fields =['active']

class Meta:
        model = ArticlesFile
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter =['active']
    list_editable =['active']
    search_fields =['active']

class Meta:
        model = Customer
class GradesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter =['active']
    list_editable =['active']
    search_fields =['active']

class Meta:
        model = Grades
class TestAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    list_filter =['active']
    list_editable =['active']
    search_fields =['active']

class Meta:
        model = Test


admin.site.register(About, AboutAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectPicture, ProjectPictureAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Articles, ArticlesAdmin)
admin.site.register(ArticlesFile, ArticlesFileAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Grades, GradesAdmin)
admin.site.register(ArticlesPicture, ArticlesPictureAdmin)
admin.site.register(Test, TestAdmin)
