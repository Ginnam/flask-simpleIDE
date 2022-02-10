# flask-onlineIDE
an online ide, base on flask and flask-codemirror

## How to use it？如何使用？
1. 下载完整项目文件

<img src=".\photo\1.PNG" alt="1" style="zoom: 80%;" />

2. 安装依赖

   > cd flask_cm
   >
   > pip install -r requirements.txt

   如果在pycharm添加依赖，出现Non-zero错误。这是因为pycharm 依赖于 --build-dir来安装包，但是这在最新版的pip中被移除了。将该项目的pip版本降至pip 21.2.4即可

   >cd venv/Scripts

   在powershell运行

   > .\python.exe -m pip install pip==21.2.4

3. 解压，运行app.py，默认运行在所有网络下，端口号5000

<img src=".\photo\2.PNG" alt="1" style="zoom: 80%;" />

## 运行时截图

<img src=".\photo\run.PNG" alt="1" style="zoom: 80%;" />

## 感谢

[flask-codemirror](https://github.com/j0ack/flask-codemirror)

[flask](https://flask.palletsprojects.com/)

