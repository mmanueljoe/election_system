# from django.contrib import admin
# from .models import Region, Constituency, Party, Candidate, PollingStation, Vote



# admin.site.register(Region)
# admin.site.register(Constituency)
# admin.site.register(Party)
# admin.site.register(Candidate)
# admin.site.register(PollingStation)
# admin.site.register(Vote)


# from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
# from .models import Region, Constituency, Party, Candidate, PollingStation, Vote

# @admin.register(Region)
# class RegionAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(Constituency)
# class ConstituencyAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(Party)
# class PartyAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(Candidate)
# class CandidateAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(PollingStation)
# class PollingStationAdmin(ImportExportModelAdmin):
#     pass

# @admin.register(Vote)
# class VoteAdmin(ImportExportModelAdmin):
#     pass


from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PollingStation, Region, Constituency, Party, Candidate, Vote
from .resources import PollingStationResource

# Admin for PollingStation with Import/Export functionality
@admin.register(PollingStation)
class PollingStationAdmin(ImportExportModelAdmin):
    resource_class = PollingStationResource  # Link to the resource class

# Register other models as normal
admin.site.register(Region)
admin.site.register(Constituency)
admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(Vote)
