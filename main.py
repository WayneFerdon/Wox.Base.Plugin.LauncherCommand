# ----------------------------------------------------------------
# Author: wayneferdon wayneferdon@hotmail.com
# Date: 2022-02-12 06:25:55
# LastEditors: WayneFerdon wayneferdon@hotmail.com
# LastEditTime: 2023-03-04 14:16:53
# FilePath: \Flow.Launcher.Plugin.LauncherCommand\main.py
# ----------------------------------------------------------------
# Copyright (c) 2022 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

# -*- coding: utf-8 -*-s
from RegexList import *
from Query import *

class Command(Query):
    def query(cls, queryString):
        IconPath = "./Images/Icon.png"
        exit = QueryResult('Exit ' + Launcher.Name, '退出' + Launcher.Name, IconPath, None, Launcher.GetAPIName(Launcher.API.CloseApp), True).toDict()
        restart = QueryResult('Restart ' + Launcher.Name, '重启' + Launcher.Name, IconPath, None, Launcher.GetAPIName(Launcher.API.RestartApp), True).toDict()
        settings = QueryResult('Settings', '设置', IconPath, None, Launcher.GetAPIName(Launcher.API.OpenSettingDialog), True).toDict()
        reload = QueryResult('Reload Plugin Data', '重载插件数据', IconPath, None,Launcher.GetAPIName(Launcher.API.ReloadAllPluginData), True).toDict()
        update = QueryResult('Check for {} Update'.format(Launcher.Name), '检查更新', IconPath, None, Launcher.GetAPIName(Launcher.API.CheckForNewUpdate), True).toDict()

        resultList = [exit, restart, settings, reload, update]
        results = list()
        regex = RegexList(queryString)
        for result in resultList:
            if regex.match(result["Title"]):
                results.append(result)
        return results

if __name__ == "__main__":
    Command()
