# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import re


class woxConfigs(Wox):
    @classmethod
    def query(cls, queryString):
        IconPath = "./Images/woxIcon.png"
        exit = {
            "Title": "Exit",
            "SubTitle": "退出Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.CloseApp",
                "dontHideAfterAction": False
            }
        }
        restart = {
            "Title": "Restart Wox",
            "SubTitle": "重启Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.RestarApp",
                "dontHideAfterAction": False
            }
        }
        settings = {
            "Title": "Settings",
            "SubTitle": "设置",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.OpenSettingDialog",
                "dontHideAfterAction": False
            }
        }
        reload = {
            "Title": "Reload Plugin Data",
            "SubTitle": "重新加载插件",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.ReloadAllPluginData",
                "dontHideAfterAction": False
            }
        }
        update = {
            "Title": "Check for Wox Update",
            "SubTitle": "检查更新",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.CheckForNewUpdate",
                "dontHideAfterAction": False
            }
        }
        result = [exit, restart, settings, reload, update]
        # pattern = ".*?".join(q)
        # regex = re.compile(pattern)
        regex = re.compile(queryString.lower())
        for item in result:
            match = regex.search(item["Title"].lower())
            if not match:
                result.remove(item)
        return result


if __name__ == "__main__":
    woxConfigs()
