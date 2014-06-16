from django.contrib import admin
from know.models import VirtualizationHost, Server, LoadBalancer, KnowledgeItem

admin.site.register(VirtualizationHost)
admin.site.register(Server)
admin.site.register(LoadBalancer)
admin.site.register(KnowledgeItem)
