#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengj
    @   date    :       2019/11/25 22:25
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
