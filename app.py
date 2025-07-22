import streamlit as st
import cv2
import numpy as np
from PIL import Image
from ultralytics import YOLO

# Load YOLO model (replace with your trained model if needed)
model = YOLO("face.pt")

# Page configuration
st.set_page_config(page_title="🧑 Face Detection App", layout="wide")
st.markdown("""
    <h1 style='text-align: center;'>🧠 Face Detection App</h1>
    <p style='text-align: center; font-size:18px;'>Upload an image to detect faces using YOLOv12!</p>
    <hr>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("📤 Upload Image")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    detect_button = st.button("🧪 Detect Faces")

# Main content columns
col1, col2 = st.columns(2)

if uploaded_file:
    # Load image
    image = Image.open(uploaded_file).convert("RGB")
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # Show original image
    col1.image(image, caption="🖼️ Original Image", use_column_width=True)

    if detect_button:
        # Run detection
        results = model(img_bgr, conf=0.25)[0]
        annotated_img = img_bgr.copy()

        # Draw boxes with confidence & label
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            class_id = int(box.cls[0])
            label = model.names.get(class_id, "Face")

            cv2.rectangle(annotated_img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(annotated_img, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Convert to RGB for Streamlit
        annotated_rgb = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
        col2.image(annotated_rgb, caption="✅ Detected Faces", use_column_width=True)

        # Optional: show face count
        st.success(f"🎯 {len(results.boxes)} face(s) detected.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center;'>🔍 Powered by YOLOv12 · Built with ❤️ by JAGRITI</p>
""", unsafe_allow_html=True)