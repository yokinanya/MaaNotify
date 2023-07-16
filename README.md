# MAA Notify
一个基于[onepush](https://github.com/y1ndan/onepush)的[MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights)通知推送脚本

# 使用方法
1. 使用`git clone`把脚本拉取到MAA的安装目录
    ```bash
    git clone https://github.com/yokinanya/MaaNotify
    ```
1. 安装依赖库
    ```bash
    cd MaaNotify
    pip install -r requirements.txt
    ```
1. 修改配置文件
    脚本使用 Onepush 推送信息，根据 [Alas文档](https://github.com/LmeSzinc/AzurLaneAutoScript/wiki/Onepush-configuration-%5BCN%5D) 完成`config.yaml`的配置
1. 在MAA中完成相关设置
    MAA `设置` - `连接设置` - `结束后脚本` 中填入 `MAAPush.bat` 的路径

# 注意事项
脚本暂时只考虑日常基建清体力结束后的日志推送，自动肉鸽结束后可能会出现日志过长无法推送的问题