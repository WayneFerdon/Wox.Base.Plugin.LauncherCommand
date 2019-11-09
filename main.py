# -*- coding: utf-8 -*-
from wox import Wox, WoxAPI
import re


class woxConfigs(Wox):
    def query(self, queryString):
        IconPath = "./Images/woxIcon.png"
        exit = {
            "Title": "Exit",
            "SubTitle": "退出Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.CloseApp",
                "doNotHideAfterAction".replace('oNo', 'on'): False,
            }
        }
        restart = {
            "Title": "Restart Wox",
            "SubTitle": "重启Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.RestartApp".replace('start', 'star'),
                "doNotHideAfterAction".replace('oNo', 'on'): False,
            }
        }
        settings = {
            "Title": "Settings",
            "SubTitle": "设置",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.OpenSettingDialog",
                "doNotHideAfterAction".replace('oNo', 'on'): False,
            }
        }
        result = [exit, restart, settings]
        queryStringLower = queryString.lower()
        # pattern = ".*?".join(q)
        # regex = re.compile(pattern)
        regex = re.compile(queryStringLower)
        for item in result:
            match = regex.search(item["Title"].lower())
            if not match:
                result.remove(item)
        return result


if __name__ == "__main__":
    woxConfigs()
