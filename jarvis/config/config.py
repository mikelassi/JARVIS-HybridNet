import os,sys,inspect
from yacs.config import CfgNode as CN

#General Configurations
_C = CN()
_C.PROJECTS_ROOT_PATH = 'projects'
_C.PROJECT_NAME = None
_C.DATALOADER_NUM_WORKERS = 4
_C.USE_MIXED_PRECISION = False


#Dataset Configurations
_C.DATASET = CN()
_C.DATASET.DATASET_ROOT_DIR = 'datasets'
_C.DATASET.DATASET_2D = None
_C.DATASET.DATASET_3D = None
_C.DATASET.TRAIN_SET = 'train'
_C.DATASET.VAL_SET = 'val'
_C.DATASET.MEAN = [0.485, 0.456, 0.406]
_C.DATASET.STD = [0.229, 0.224, 0.225]
_C.DATASET.IMG_SIZE = None


#EfficientTrack 2D Center Detector Configuration
_C.CENTERDETECT = CN()
_C.CENTERDETECT.IMAGE_SIZE = 320
_C.CENTERDETECT.COMPOUND_COEF = 0
_C.CENTERDETECT.NUM_JOINTS = 1
_C.CENTERDETECT.BATCH_SIZE = 4
_C.CENTERDETECT.OPTIMIZER = 'adamw'
_C.CENTERDETECT.USE_ONECYLCLE = True
_C.CENTERDETECT.MAX_LEARNING_RATE = 0.02
_C.CENTERDETECT.CHECKPOINT_SAVE_INTERVAL = 10
_C.CENTERDETECT.ONLY_SAVE_ON_IMPROVEMENT = False    #TODO: actually implement
_C.CENTERDETECT.VAL_INTERVAL = 1
_C.CENTERDETECT.USE_EARLY_STOPPING = False
_C.CENTERDETECT.EARLY_STOPPING_MIN_DELTA = 0.002
_C.CENTERDETECT.EARLY_STOPPING_PATIENCE = 5

#EfficientTrack 2D Keypoint Tracking Network Configuration
_C.KEYPOINTDETECT = CN()
_C.KEYPOINTDETECT.COMPOUND_COEF = 0
_C.KEYPOINTDETECT.NUM_JOINTS = 0
_C.KEYPOINTDETECT.BOUNDING_BOX_SIZE = 320
_C.KEYPOINTDETECT.BATCH_SIZE = 4
_C.KEYPOINTDETECT.OPTIMIZER = 'adamw'
_C.KEYPOINTDETECT.USE_ONECYLCLE = True
_C.KEYPOINTDETECT.MAX_LEARNING_RATE = 0.02
_C.KEYPOINTDETECT.CHECKPOINT_SAVE_INTERVAL = 10
_C.KEYPOINTDETECT.ONLY_SAVE_ON_IMPROVEMENT = False    #TODO: actually implement
_C.KEYPOINTDETECT.VAL_INTERVAL = 1
_C.KEYPOINTDETECT.USE_EARLY_STOPPING = False
_C.KEYPOINTDETECT.EARLY_STOPPING_MIN_DELTA = 0.002
_C.KEYPOINTDETECT.EARLY_STOPPING_PATIENCE = 5

_C.AUGMENTATION = CN()
_C.AUGMENTATION.COLOR_MANIPULATION = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.ENABLED = True
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_BLUR = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_BLUR.PROBABILITY = 0.5
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_BLUR.SIGMA = [0,0.5]
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_NOISE = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_NOISE.PER_CHANNEL_PROBABILITY = 0.6
_C.AUGMENTATION.COLOR_MANIPULATION.GAUSSIAN_NOISE.SCALE = [0.0, 0.02]
_C.AUGMENTATION.COLOR_MANIPULATION.LINEAR_CONTRAST = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.LINEAR_CONTRAST.PROBABILITY = 1.0
_C.AUGMENTATION.COLOR_MANIPULATION.LINEAR_CONTRAST.SCALE = [0.7,1.0]
_C.AUGMENTATION.COLOR_MANIPULATION.MULTIPLY = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.MULTIPLY.PROBABILITY = 0.3
_C.AUGMENTATION.COLOR_MANIPULATION.MULTIPLY.SCALE = [0.7,1.5]
_C.AUGMENTATION.COLOR_MANIPULATION.PER_CHANNEL_MULTIPLY = CN()
_C.AUGMENTATION.COLOR_MANIPULATION.PER_CHANNEL_MULTIPLY.PROBABILITY = 0.3
_C.AUGMENTATION.COLOR_MANIPULATION.PER_CHANNEL_MULTIPLY.PER_CHANNEL_PROBABILITY = 0.3
_C.AUGMENTATION.COLOR_MANIPULATION.PER_CHANNEL_MULTIPLY.SCALE = [0.8,1.2]
_C.AUGMENTATION.MIRROR = CN()
_C.AUGMENTATION.MIRROR.PROBABILITY = 0.5
_C.AUGMENTATION.AFFINE_TRANSFORM = CN()
_C.AUGMENTATION.AFFINE_TRANSFORM.PROBABILITY = 0.5
_C.AUGMENTATION.AFFINE_TRANSFORM.ROTATION_RANGE = [-60,60]
_C.AUGMENTATION.AFFINE_TRANSFORM.SCALE_RANGE = [0.8, 1.25]


#HybridNet 3D Tracking Network Configuration
_C.HYBRIDNET = CN()
_C.HYBRIDNET.NUM_CAMERAS = 0
_C.HYBRIDNET.ROI_CUBE_SIZE = None
_C.HYBRIDNET.GRID_SPACING = None

_C.HYBRIDNET.BATCH_SIZE = 1
_C.HYBRIDNET.OPTIMIZER = 'adamw'
_C.HYBRIDNET.LEARNING_RATE = 0.0005
_C.HYBRIDNET.CHECKPOINT_SAVE_INTERVAL = 5
_C.HYBRIDNET.VAL_INTERVAL = 1
_C.HYBRIDNET.USE_EARLY_STOPPING = False
_C.HYBRIDNET.EARLY_STOPPING_MIN_DELTA = 0.002
_C.HYBRIDNET.EARLY_STOPPING_PATIENCE = 5