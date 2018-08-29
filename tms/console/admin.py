from django.contrib import admin

from .models import Project, TestPlan, TestRun, Component, TestCase, Role, Tester, TestRunCase, Message, Release, \
    TesterRole, Device

# admin.site.register(Project)
# admin.site.register(TestPlan)
# admin.site.register(TestRun)
# admin.site.register(Component)
# admin.site.register(TestCase)
# admin.site.register(Role)
# admin.site.register(Tester)
# admin.site.register(TestRunCase)


class ComponentInline(admin.TabularInline):
    model = Component

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['name', 'description']
        else:
            return []

    def get_actions(self, request):
        actions = super(ComponentInline, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    extra = 0
    max_num = 0


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None, {'fields': ['description']}),
    ]
    list_display = ('name', 'description')
    inlines = [ComponentInline, TestCaseInline]
    # list_filter = ['name']
    search_fields = ['description']


admin.site.register(Project, ProjectAdmin)


class TestRunCaseInline(admin.TabularInline):
    model = TestRunCase
    extra = 0


class TestRunAdmin(admin.ModelAdmin):
    inlines = [TestRunCaseInline]


admin.site.register(TestRun, TestRunAdmin)

admin.site.register(TestPlan)

admin.site.register(Message)

admin.site.register(Release)

admin.site.register(Role)

admin.site.register(Tester)

admin.site.register(TesterRole)

admin.site.register(Device)

