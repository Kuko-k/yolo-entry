import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO

# 页面配置
st.set_page_config(page_title="汽车零件AI质检系统", layout="wide", page_icon="🔍")

# 加载模型
@st.cache_resource
def load_model():
    return YOLO('weights/best.pt')

model = load_model()

# 主页面标题
st.markdown("""
<div style="background-color:#e3f2fd; padding:20px; border-radius:10px; margin-bottom:20px;">
    <h1 style="color:#0d47a1; margin:0;">🔍 汽车零件缺陷检测工作台</h1>
    <p style="color:#1565c0; margin:5px 0 0 0;">上传一张零件图片，AI自动识别并标注缺陷位置与置信度。</p >
</div>
""", unsafe_allow_html=True)

# 分左右两栏
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📤 上传图片")
    uploaded_file = st.file_uploader("选择一张汽车零件图片...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, channels="BGR", caption="待检测原图", use_column_width=True)

with col2:
    st.markdown("### 🎯 识别结果")
    if uploaded_file is not None:
        with st.spinner('AI正在推理中...'):
            results = model(img)
            result = results[0]
            
            annotated_img = result.plot()
            st.image(annotated_img, channels="BGR", caption="检测结果图", use_column_width=True)
            
            classes = result.boxes.cls.cpu().numpy()
            names = result.names
            count = {}
            for c in classes:
                name = names[int(c)]
                count[name] = count.get(name, 0) + 1
            
            st.markdown("### 📊 检测结果统计")
            if not count:
                st.success("未检测到明显缺陷。")
            else:
                for k, v in count.items():
                    st.error(f"发现缺陷 [{k}]：{v} 个")
    else:
        st.info("请在左侧上传图片开始检测...")