"""
Split data into training and testing sets (80/20).
Assumes images and labels are in 'data/images/' and 'data/labels/' directories.
YOLO format: images/*.jpg, labels/*.txt (same filename).
"""

import os
import shutil
import random

IMG_DIR = 'data/images'
LBL_DIR = 'data/labels'

TRAIN_IMG = 'data/train/images'
TRAIN_LBL = 'data/train/labels'
TEST_IMG = 'data/test/images'
TEST_LBL = 'data/test/labels'

SPLIT_RATIO = 0.8

def make_dirs():
    for d in [TRAIN_IMG, TRAIN_LBL, TEST_IMG, TEST_LBL]:
        os.makedirs(d, exist_ok=True)

def split_data():
    images = [f for f in os.listdir(IMG_DIR) if f.endswith('.jpg') or f.endswith('.png')]
    random.shuffle(images)
    split = int(SPLIT_RATIO * len(images))
    train_imgs = images[:split]
    test_imgs = images[split:]
    
    for img_list, img_dest, lbl_dest in [
        (train_imgs, TRAIN_IMG, TRAIN_LBL),
        (test_imgs, TEST_IMG, TEST_LBL)
    ]:
        for img in img_list:
            img_src = os.path.join(IMG_DIR, img)
            lbl_src = os.path.join(LBL_DIR, os.path.splitext(img)[0] + '.txt')
            shutil.copy(img_src, img_dest)
            if os.path.exists(lbl_src):
                shutil.copy(lbl_src, lbl_dest)

if __name__ == "__main__":
    make_dirs()
    split_data()
    print(f"Data split complete. Train: {TRAIN_IMG}, Test: {TEST_IMG}")
