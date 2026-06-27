[app]
title = TradingBot
package.name = tradingbot
package.domain = com.tradingbot
source.dir = .
# 改为入口 main.py
source.main = main.py
version = 1.0
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,env,md,xml
# 显式包含 src 目录和配置文件
source.include_patterns = src/*,config/*,groups_config.py

requirements = python3==3.11.2,kivy,kivymd,requests,urllib3,telethon,cryptg,python-dotenv,aiohttp,aiofiles,python-dateutil,plyer,pyjnius

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK,FOREGROUND_SERVICE
android.archs = arm64-v8a, armeabi-v7a
android.api = 33
android.minapi = 21
android.accept_sdk_license = True
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
p4a.branch = v2024.01.21