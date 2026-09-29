聚类结果 REST API 项目

【用途】
读取 output/MBSE_三张输出表.json，通过 REST API 给下游获取。

【VS Code 运行】
1. 用 VS Code 打开本文件夹
2. 打开 Terminal
3. 执行：
   python -m pip install -r requirements.txt
4. 启动：
   python -m uvicorn app:app --host 0.0.0.0 --port 8000

也可以安装依赖后双击 run.bat。

【Postman】
Method: GET
URL: http://127.0.0.1:8000/api/clustering/result
Params: 无
Body: none
Authorization: No Auth

点击 Send，正常返回 200 OK 和三张表 JSON。

【接入你的真实聚类结果】
将你的真实 MBSE_三张输出表.json 放入 output 文件夹并覆盖示例文件。
接口每次收到 GET 都会重新读取 JSON，所以算法更新文件后，下游再次 GET 即可得到最新数据。

【测试】
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs

注意：
127.0.0.1 仅用于同一台电脑测试。
如果以后另一台电脑调用，需要使用运行本服务电脑的 IP 或将服务部署到服务器。
