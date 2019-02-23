import tensorflow as tf
import numpy as np
import os
import tarfile
import cv2

cap = cv2.VideoCapture(0)

from utils import label_map_util

from utils import visualization_utils as vis_util

