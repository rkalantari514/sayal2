from django.contrib import admin
from contents.models import About, Team, Projects, ProjectPicture, Services, Articles, ArticlesFile, Customer, Grades, \
    Test
from django.utils.html import format_html


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'active']
    # # list_filter = ['active']
    # list_editable = ['name','family','active','owner']
    # search_fields = ['name','family']
    # list_per_page = 20
    # sortable_by = ['name','family','active']
    class Meta:
        model = About

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'active','super']
    class Meta:
        model = Team
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'active','subject']
    class Meta:
        model = Projects
class ProjectPictureAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.pimage.url))
    list_display = ['__str__', 'image_tag', 'active', 'project','pimage']
    class Meta:
        model = ProjectPicture







class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['__str__','name', 'active']
    class Meta:
        model = Articles


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    class Meta:
        model = Services
class ArticlesFileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    class Meta:
        model = ArticlesFile
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    class Meta:
        model = Customer
class GradesAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
    class Meta:
        model = Grades
class TestAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'active']
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
admin.site.register(Test, TestAdmin)
