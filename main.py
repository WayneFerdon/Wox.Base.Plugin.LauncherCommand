# ----------------------------------------------------------------
# Author: wayneferdon wayneferdon@hotmail.com
# Date: 2022-02-12 06:25:55
# LastEditors: WayneFerdon wayneferdon@hotmail.com
# LastEditTime: 2023-04-09 10:45:36
# FilePath: \FlowLauncher\Plugins\Wox.Base.Plugin.LauncherCommand\main.py
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
        LauncherAPI.OpenSettingDialog,
        LauncherAPI.ReloadAllPluginData,
        LauncherAPI.CheckForNewUpdate,
        LauncherAPI.RestartApp,
        LauncherAPI.CloseApp
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
    def getAPIResult(api:LauncherAPI):
        return QueryResult(
            api.getDescription(),
            api.getDescription(Launcher.language),
            Plugin.defaultIcon,
            None,
            api.API_name,
            True
        ).toDict()

if __name__ == "__main__":
    Command()
