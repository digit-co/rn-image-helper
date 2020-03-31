import os
import shutil
from constants import DIGIT_MOBILE_PATH
from helpers import get_files_to_move
ANDROID_BASE_DIR = "{}/js/android/app/src/main/res".format(DIGIT_MOBILE_PATH)

scale_to_android_folder = {
  "1": "drawable-mdpi",
  "2": "drawable-xhdpi",
  "3": "drawable-xxhdpi",
}

def get_file_scale(file_name):
  return file_name.split("@")[1][0]

def move_android_assets(image_name):
  print("Adding Android assets for {}".format(image_name))
  raw_name = "{}.png".format(image_name)

  files = get_files_to_move(image_name)
  for file in files:
    scale = get_file_scale(file)
    folder = scale_to_android_folder[scale]

    android_dest = "{}/{}/{}".format(ANDROID_BASE_DIR, folder, raw_name)
    shutil.copy(file, android_dest)