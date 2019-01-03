# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:00:57 2019

@author: Dell
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]