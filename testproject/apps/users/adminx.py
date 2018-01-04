# _*_ encoding:utf-8 _*_

import xadmin

# from .models import EmailVerifyRecord
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = u"机泵云后台管理系统"
    site_footer = u"copyright 2017 上海航天动力科技工程有限公司"
    menu_style = "accordion"


# class EmailVerifyRecordAdmin(object):
#     list_display = ['code','email','send_time']
#     search_fields = ['code','email']
#     list_filter = ['code','email','send_time']


# xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)

