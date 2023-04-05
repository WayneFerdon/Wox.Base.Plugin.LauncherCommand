# ----------------------------------------------------------------
# Author: wayneferdon wayneferdon@hotmail.com
# Date: 2022-02-12 06:25:55
# LastEditors: WayneFerdon wayneferdon@hotmail.com
# LastEditTime: 2023-04-05 05:22:58
# FilePath: \Plugins\Wox.Base.Plugin.LauncherCommand\main.py
# ----------------------------------------------------------------
# Copyright (c) 2022 by Wayne Ferdon Studio. All rights reserved.
# Licensed to the .NET Foundation under one or more agreements.
# The .NET Foundation licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.
# ----------------------------------------------------------------

# -*- coding: utf-8 -*-s
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from WoxPluginBase_Query import *

class Command(QueryPlugin):
    Plugin.setPlatformAsPluginIcon()
    SupportedAPIs = [
        Launcher.API.OpenSettingDialog,
        Launcher.API.ReloadAllPluginData,
        Launcher.API.CheckForNewUpdate,
        Launcher.API.RestartApp,
        Launcher.API.CloseApp # API.CloseApp might not working sometimes while the launcher is run as Administrator, in which the launcher might just hide launcher instead
    ]
    
    def query(self, queryString):
        resultList = list()
        for api in Command.SupportedAPIs:
            resultList.append(Command.getAPIResult(api))
        results = list()
        regex = RegexList(queryString)
        for result in resultList:
            if not regex.match(result["Title"]):
                continue
            results.append(result)
        return results
    
    @staticmethod
    def getAPIResult(api:Launcher.API):
        return QueryResult(
            api.getDescription(),
            api.getDescription(Launcher.language),
            Plugin.defaultIcon,
            None,
            api.name,
            True
        ).toDict()

if __name__ == "__main__":
    Command()
