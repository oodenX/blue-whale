# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from .serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    """
    用户信息API
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class HealthzViewSet(ViewSet):
    """
    健康探测API
    """

    @action(detail=False, methods=["get"], url_path="healthz")
    def healthz(self, request, *args, **kwargs):
        """
        获取应用健康状态
        """
        return Response({"healthy": True})

    @action(detail=False, methods=["get"], url_path="ping")
    def ping(self, request, *args, **kwargs):
        """
        应用ping 接口
        """
        return Response("pong")
