# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.views.generic import View

from .models import Company,Station,Pump
from spectrum.models import InferComboReport
from django.db.models import Q
import json

from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.


class CompanyView(View):
    def get(self,request):
        all_company = Company.objects.all()
        all_station = Station.objects.all()
        all_pump = Pump.objects.all()
        # inferComboReport = InferComboReport.objects.using("PumpSystem").none()
        return render(request, "index.html", {
            "all_company": all_company,
            "all_station":all_station,
            "all_pump":all_pump,
            # "all_inferComboReport":inferComboReport
        })


class loadFailureList(View):
    def get(self, request):
        id = request.GET.get('id', "")
        all_inferComboReport = InferComboReport.objects.using("PumpSystem").all()
        all_pump = Pump.objects.all()
        list = []
        if id:
            pump = all_pump.get(id = id)
            code = pump.pumpcode
            code1 = 'Pump_'+code
            code2 = 'Motor_'+code
            all_infer = all_inferComboReport.filter(Q(CompCode = code1)|Q(CompCode = code2))
            for infer in all_infer:
                dict = {}
                dict = {"CompCode":infer.CompCode,"DisplayText":infer.DisplayText,"RtDatas":infer.RtDatas}
                list.append(dict)
        return HttpResponse(json.dumps(list), content_type='application/json')


class PumpListView(View):
    def get(self, request):
        all_company = Company.objects.all()
        all_station = Station.objects.all()
        all_pump = Pump.objects.all().order_by("name")
        # inferComboReport = InferComboReport.objects.using("PumpSystem").none()
        sta_id = request.GET.get('sta', "")
        if sta_id:
            all_pump = all_pump.filter(station_id = int(sta_id))

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_pump, 10, request=request)
        pumps = p.page(page)

        return render(request, "pump_list.html", {
            "all_company": all_company,
            "all_station": all_station,
            "all_pump": pumps,
            # "all_inferComboReport": inferComboReport,
            "station_id":sta_id
        })


class PumpView(View):
    def get(self, request):
        all_station = Station.objects.all()
        all_pump = Pump.objects.all().order_by("station")
        inferComboReport = InferComboReport.objects.using("PumpSystem").none()
        sta_id = request.GET.get('sta', "")
        if sta_id:
            all_pump = all_pump.filter(station_id = int(sta_id))

        for pump in all_pump:
            code = pump.pumpcode
            fault = InferComboReport.objects.using('PumpSystem').filter(CompCode__contains = code).order_by("-RRId").first()
            RtData = ""
            DisplayText = ""
            Id = -1
            if fault:
                DisplayText = fault.DisplayText
                str = fault.RtDatas.replace(' ','')
                Id = fault.Id
                result = str.split(',')
                for res in result:
                    if res.find(":1") != -1:
                        RtData = res
                        break
            pump.RtData = RtData
            pump.DisplayText = DisplayText
            pump.InferId = Id
        return render(request, "pump.html", {
            "all_station": all_station,
            "all_pump": all_pump,
            "all_inferComboReport": inferComboReport,
            "station_id":sta_id
        })