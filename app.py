import tkinter as tk
from tkinter import filedialog
import numpy as np
import cv2

import test2

def get_frames(video_yuv_path, width=768, height=432):
    # YUV 4:2:0
    frame_size = width * height * 3 // 2

    with open(video_yuv_path, 'rb') as file:
        yuv_data = np.frombuffer(file.read(), dtype=np.uint8)

    yuv_data = yuv_data.reshape(-1, frame_size)

    # Extract Y component
    y_component = yuv_data[:, :width * height]
    y_frames = y_component.reshape(-1, height, width)
    return y_frames

def main():
    root = tk.Tk()
    root.withdraw()  

    file_path = filedialog.askopenfilename(title="Select Video file", filetypes=(("Video files", ".yuv"), ("All files", ".*")))

    if not file_path:
        print("No file selected. Exiting.")
        return

    frames = get_frames(file_path)

    total_features = []
    for i in range(len(frames)-1):
        # rgb_frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        # cv2.imshow('YUV Video frame', rgb_frame)
        # cv2.waitKey(0)

        spatial_features = test2.extract_spatial_features(frames[i])
        temporal_features = test2.extract_temporal_features(frames[i+1], frames[i])
        motion_map = np.random.rand(frames[i].shape[0], frames[i].shape[1])
        fused_features = test2.motion_based_feature_fusion(spatial_features, temporal_features, motion_map)
        total_features.append(fused_features)

    # cv2.destroyAllWindows()
    video_quality_score = test2.spatial_temporal_feature_pooling(np.array(total_features))
    print("Video Quality Score:", video_quality_score)


if __name__ == "__main__":
    main()
 
