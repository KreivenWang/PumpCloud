# _*_ encoding:utf-8 _*_

import xadmin

from .models import Company, Station, Pump


class CompanyAdmin(object):
    list_display = ['name','address']
    search_fields = ['name','address']
    list_filter = ['name','address']


class StationAdmin(object):
    list_display = ['name', 'company', 'address']
    search_fields = ['name', 'company', 'address']
    list_filter = ['name', 'company__name', 'address']


class PumpAdmin(object):
    list_display = ['name', 'pumpcode', 'station', 'status', 'running']
    search_fields = ['name', 'pumpcode', 'station', 'status', 'running']
    list_filter = ['name', 'pumpcode', 'station', 'status', 'running']


# class SpectrumAdmin(object):
#     list_display = ['num', 'pump', 'data', 'datetime', 'local']
#     search_fields = ['num', 'pump', 'data', 'local']
#     list_filter = ['num', 'pump__name', 'data', 'datetime', 'local']


xadmin.site.register(Company,CompanyAdmin)
xadmin.site.register(Station,StationAdmin)
xadmin.site.register(Pump,PumpAdmin)
# xadmin.site.register(Spectrum,SpectrumAdmin)