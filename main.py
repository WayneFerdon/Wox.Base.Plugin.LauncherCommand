# -*- coding: utf-8 -*-
# require pypiwin32, can be install by pip
from wox import Wox, WoxAPI
import os
import re


class woxConfigs(Wox):
    def query(self, query):
        IconPath = "Images/app.png"
        exit = {
            "Title": "Exit",
            "SubTitle": "退出Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.CloseApp",
                "dontHideAfterAction": False,
            }
        }
        restart = {
            "Title": "Restart Wox",
            "SubTitle": "重启Wox",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.RestarApp",
                "dontHideAfterAction": False,
            }
        }
        settings = {
            "Title": "Settings",
            "SubTitle": "设置",
            "IcoPath": IconPath,
            "JsonRPCAction": {
                "method": "Wox.OpenSettingDialog",
                "dontHideAfterAction": False,
            }
        }
        result = [exit, restart, settings]
        query = query.replace(" ", "")
        q = query.lower()
        # pattern = ".*?".join(q)
        # regex = re.compile(pattern)
        regex = re.compile(q)
        for item in result:
            match = regex.search(item["Title"].lower())
            if not match:
                result.remove(item)
        return result


if __name__ == "__main__":
    woxConfigs()
