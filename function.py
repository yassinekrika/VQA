import numpy as np

def extract_spatial_features(frame):
    spatial_features = np.mean(frame)  
    return spatial_features

def extract_temporal_features(frame, prev_frame):
    temporal_features = np.abs(frame - prev_frame)  
    return temporal_features

def motion_based_feature_fusion(spatial_features, temporal_features, motion_map):
    fused_features = (1 - motion_map) * spatial_features + motion_map * temporal_features
    return fused_features

def spatial_temporal_feature_pooling(video_features):
    quality_score = np.mean(video_features) 
    return quality_score