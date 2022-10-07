# ----------------------------------------------------------------
# Author: wayneferdon wayneferdon@hotmail.com
# Date: 2022-02-12 06:25:55
# LastEditors: wayneferdon wayneferdon@hotmail.com
# LastEditTime: 2022-10-07 19:37:33
# FilePath: \Wox.Plugin.ChromeBookmarksc:\Users\WayneFerdon\AppData\Local\Wox\app-1.4.1196\Plugins\Wox.Plugin.WoxCommand\main.py
# ----------------------------------------------------------------
# Copyright (c) 2022 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

# -*- coding: utf-8 -*-
from RegexList import *
from WoxQuery import *

class WoxCommand(WoxQuery):
    def query(cls, queryString):
        IconPath = "./Images/woxIcon.png"
        exit = WoxResult('Exit', '退出Wox', IconPath, None, "Wox.CloseApp", True).toDict()
        restart = WoxResult('Restart Wox', '重启Wox', IconPath, None, "Wox.RestarApp", True).toDict()
        settings = WoxResult('Settings', '设置', IconPath, None, "Wox.OpenSettingDialog", True).toDict()
        reload = WoxResult('Reload Plugin Data', '重载插件数据', IconPath, None, "Wox.ReloadAllPluginData", True).toDict()
        update = WoxResult('Check for Wox Update', '检查更新', IconPath, None, "Wox.CheckForNewUpdate", True).toDict()

        resultList = [exit, restart, settings, reload, update]
        results = list()
        regex = RegexList(queryString)
        for result in resultList:
            if regex.match(result["Title"]):
                results.append(result)
        return results

if __name__ == "__main__":
    WoxCommand()
