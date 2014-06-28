from django.db import models

#################### BASE CONFIGURATION ITEM #####################

# Base class with common fields shared among all Configuration Items in the CMDB

class baseCI(models.Model):
    name = models.SlugField("Name", max_length=16) 
    displayname = models.CharField("Display Name", max_length=80)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.displayname

    class Meta:
        abstract = True

#################### KNOWLEDGE ITEMS #####################

# Procedures, file attachments, configuration data (TBD, this may become a seperate class)
# and similar data that we can attach to other classes for automatic, timely, contextual
# access

class KnowledgeItem(baseCI):
    types = (
        ('esclproc', 'Escalation Procedure'),
        ('tshtproc', 'Troubleshooting Procedure'),
        ('warmproc', 'Warmup Procedure'),
        ('othrproc', 'Other Procedure'),
        ('knwnissu', 'Known Issue'),
        ('attachmt', 'Attachment'),
        ('note', 'Note'),
    )
    type = models.CharField("Type", max_length=12, choices=types)

#################### ASSETS #####################

# Most hardware and logical components will be considered Assets

class Asset(baseCI):
    isvirtual = models.BooleanField("Virtual?")
    related_knowledgeitems = models.ManyToManyField(KnowledgeItem, verbose_name="Knowledge Items", blank=True, null=True)

    class Meta:
        abstract = True

# Logical Systems represent servers and other addressable/accessible
# 'devices' which usually run a single OS/Hypervisor and may be virtual, 
# cluster representations, or be hosted uniquely on a single HardwareDevice.

class LogicalSystem(Asset):  
    primaryip = models.IPAddressField("Primary IP", blank=True)
    managementip = models.IPAddressField("Management IP", blank=True)

    class Meta:
        abstract = True

class VirtualizationHost(LogicalSystem):
    hvfamilies = (
        ('vmware', 'VMware'),
        ('hyperv', 'HyperV'),
        ('zen', 'Zen'),
    )
    hvfamily = models.CharField("Hypervisor Family", max_length=15, choices=hvfamilies)
    hvversion = models.CharField("Hypervisor Version", max_length=80)

class Server(LogicalSystem):
    osfamilies = (
        ('windows', 'Windows'),
        ('linux', 'Linux'),
        ('other', 'Other'),
    )
    osfamily = models.CharField("OS Family", max_length=15, choices=osfamilies)
    osversion = models.CharField("OS Version", max_length=80)
    vhost = models.ForeignKey(VirtualizationHost, verbose_name="Virtualization Host", related_name="relatedservers", blank=True, null=True, on_delete=models.SET_NULL)


class LoadBalancer(LogicalSystem):
    pass


# Applications are autonomous services and groups of services providing
# a logical function in our environment.  These will eventually roll up
# into BusinessServices, Verticals, Products, or some similar higher
# level logical categorization representing their collective business function.

class Application(Asset):
    apptag = models.SlugField(max_length=12)
    #knowledgeitems = models.ManyToManyField(KnowledgeItem, verbose_name="Knowledge Items", related_name="related_applications", blank=True, null=True)


# Application Roles are individual functions performed by one or more systems.
# These are unique and systems involved should be interchangable either through
# load balancing, clustering, or manual active/passive changeover.

class ApplicationRole(Asset):
    roletag = models.SlugField(max_length=12)

# Components are the physical or logical devices contained within other Assets
# These may include physical or logical server components such as CPUs and Disk
# Volumes as well as logical constructs within a Load Balancer that tie 
# other assets and their resources together into a Pool.

class Component(Asset):
    class Meta:
        abstract = True

class LBComponent(Component):
    class Meta:
        abstract = True

class LBCService(LBComponent):
    pass

class LBCServer(LBComponent):
    pass

class LBCVirtualServer(LBComponent):
    pass





########################################
##### PLACEHOLDERS FOR FUTURE USE ######
########################################


#################### PLATFORMS #####################

# Platforms represent frameworks and development tools in which other applications are
# built.  This can include web server software such as IIS/Apache, middle tier systems
# such as SOLR and Memcache, and development frameworks such as NodeJS and Kitara.  These
# can include multiple versions and be associated with Applications to allow visibility
# into their use and management of patching, vulnerability analysis, and similar tasks.

class Platform(baseCI):
    class Meta:
        abstract = True

#################### PEOPLE #####################

# Persons will be used to associate technical and business ownership and escalation attributes
# either individually or as members of a Team

class Person(baseCI):
    class Meta:
        abstract = True


#################### TEAMS #####################

# Teams will be used to associate technical and business ownership and escalation attributes

class Team(baseCI):
    class Meta:
        abstract = True


#################### LOCATIONS  #####################

# Locations can be used to identify offices and other important company sites for identification
# of asset location and possibly other uses TBD

class Location(baseCI):
    class Meta:
        abstract = True
