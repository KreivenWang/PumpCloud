# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View

from django.db.models import Q
from django.shortcuts import render
from .models import InferComboReport,GraphArchives,FaultItemReport
from pump.models import Pump,Company,Station
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import json
# Create your views here.


class FaultListView(View):
    def get(self,request):
        all_fault = InferComboReport.objects.using('PumpSystem').all()
        pump_id = request.GET.get('id', "")
        if pump_id:
            pump = Pump.objects.all().get(id=pump_id)
            code = pump.pumpcode
            code1 = 'Pump_' + code
            code2 = 'Motor_' + code
            all_fault = all_fault.filter(Q(CompCode=code1) | Q(CompCode=code2))
            # for infer in all_infer:
            #     dict = {"CompCode": infer.CompCode, "DisplayText": infer.DisplayText, "RtDatas": infer.RtDatas}
            #     list.append(dict)
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_fault, 10, request=request)
        faults = p.page(page)

        return render(request, "fault_list.html", {
            "all_fault":faults
        })


class FaultView(View):
    def get(self,request,id):
        all_fault = InferComboReport.objects.using('PumpSystem').all()
        if id:
            pump = Pump.objects.all().get(id=id)
            code = pump.pumpcode
            code1 = 'Pump_' + code
            code2 = 'Motor_' + code
            all_fault = all_fault.filter(Q(CompCode=code1) | Q(CompCode=code2))
        for fa in all_fault:
            str = fa.RtDatas
            result=str.split(',')
            list=str.split(',')
            for res in result:
                if res.find(":1") == -1:
                    list.remove(res)
            # list = list[:-1]
            # fa.RtDatas = list
            fa.new_field = list
            ss = fa.new_field
            print ss
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_fault, 15, request=request)
        faults = p.page(page)

        return render(request, "fault.html", {
            "all_fault":faults
        })


class SpectrumView(View):
    def get(self,request,id):
        if id:
            infer = InferComboReport.objects.using('PumpSystem').get(Id = id)
            result = infer.RtDatas.replace(' ','').split(',')
            for res in result:
                if res.find(":1") != -1:
                    RtData = res
                    break
            str = RtData[:-2]

            code = infer.CompCode

            item = FaultItemReport.objects.using('PumpSystem').filter(CriterionBuiltIds__contains=str,CompCode=code)
            if item:
                item = item.order_by("RRId").first()
                BuiltIds = item.CriterionBuiltIds
                GraphMap = item.GraphMap
                listBuiltIds = BuiltIds.replace(' ', '').split(',')
                listGraphMap = GraphMap.replace(' ', '').split(',')
                index = listBuiltIds.index(str)
                part = listGraphMap[index]
                GraphMapId = part[part.index(':') + 1:]
                map = GraphArchives.objects.using('PumpSystem').get(Id=GraphMapId)
            else:
                map = GraphArchives.objects.using('PumpSystem').first()
            datastr = map.DataStr
            featurestr = map.FeatureStr
        return render(request, "spectrum.html", {
            "dataStr":datastr,
            "featureStr":featurestr,
        })












