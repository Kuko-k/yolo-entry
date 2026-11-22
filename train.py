from ultralytics import YOLO

if __name__ == '__main__':
    # 加载轻量模型
    model = YOLO('yolov8n.pt')
    
    # 开始训练
    results = model.train(
        data='/root/metal_project/neu/data.yaml',  # 云端Linux路径
        epochs=100,        # 训练100轮
        imgsz=1024,        # 提高分辨率，看清微小缺陷
        batch=4,           # 防止显存爆炸
        hsv_v=0.5,         # 解决金属反光问题
        device=0           # 使用GPU
    )