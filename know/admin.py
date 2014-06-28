from django.contrib import admin
from know.models import VirtualizationHost, Server, LoadBalancer, KnowledgeItem, Application, ApplicationRole, LBCService, LBCServer, LBCVirtualServer

class KIInline(admin.StackedInline):
    model = KnowledgeItem
    extra = 0

class ApplicationAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_knowledgeitems',)

class ApplicationRoleAdmin(admin.ModelAdmin):
    filter_horizontal = ('related_knowledgeitems',)

admin.site.register(VirtualizationHost)
admin.site.register(Server)
admin.site.register(LoadBalancer)
admin.site.register(KnowledgeItem)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(ApplicationRole, ApplicationRoleAdmin)
admin.site.register(LBCService)
admin.site.register(LBCServer)
admin.site.register(LBCVirtualServer)
