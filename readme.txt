【项目名称】汽车零件表面缺陷智能检测系统
【运行环境】Windows 10/11，Python 3.9+，建议使用Anaconda虚拟环境。

【环境配置】
1. 在Anaconda Prompt中创建环境：conda create -n yolo-env python=3.9
2. 激活环境：conda activate yolo-env
3. 安装依赖库：
   pip install ultralytics streamlit opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple

【运行方式】
网页版（推荐）：在当前目录下运行命令：streamlit run app_web.py
浏览器打开 http://localhost:8501 即可看到界面。