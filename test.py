import numpy as np
import cv2

# Step 1: Feature Extraction
def extract_spatial_features(frame):
    spatial_features = np.mean(frame)  
    return spatial_features

def extract_temporal_features(frame, prev_frame):
    temporal_features = np.abs(frame - prev_frame) 
    return temporal_features

# Step 2: Motion-Based Feature Fusion
def motion_based_feature_fusion(spatial_features, temporal_features, motion_map):
    fused_features = (1 - motion_map) * spatial_features + motion_map * temporal_features
    return fused_features

# Step 3: Spatial-Temporal Feature Pooling
def spatial_temporal_feature_pooling(video_features):
    quality_score = np.mean(video_features)  
    return quality_score

frame1 = cv2.imread('frame1.jpg')
frame2 = cv2.imread('frame2.jpg')

# Extract features from frames
spatial_features = extract_spatial_features(frame1)
temporal_features = extract_temporal_features(frame2, frame1)

# Generate motion map (example: random values for demonstration)
motion_map = np.random.rand(frame1.shape[0], frame1.shape[1])

# Fuse features based on motion
fused_features = motion_based_feature_fusion(spatial_features, temporal_features, motion_map)

# Pool spatial-temporal features to derive quality score
quality_score = spatial_temporal_feature_pooling(fused_features)

print("Quality Score:", quality_score)
