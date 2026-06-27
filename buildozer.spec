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

requirements = python3,
    kivy==2.1.0,
    kivymd==1.1.1,
    requests==2.31.0,
    urllib3==1.26.18,
    telethon==1.34.0,
    cryptg==0.4.0,
    python-dotenv==1.0.0,
    pydantic==2.5.2,
    aiofiles==23.2.1,
    python-dateutil==2.8.2,
    cryptography==41.0.8,
    pyopenssl==23.3.0,
    ujson==5.8.0,
    plyer==2.1.0,
    pyjnius==1.4.2

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
