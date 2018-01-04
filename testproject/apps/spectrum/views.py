# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import View

from django.db.models import Q
from django.shortcuts import render
from .models import InferComboReport
from pump.models import Pump
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