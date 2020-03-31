import os
import shutil
import json
from constants import DIGIT_MOBILE_PATH
from helpers import get_files_to_move

info = {"info": {"version" : 1, "author" : "xcode"}}

def generate_content_json(image_name):
  obj = {}
  obj["images"] = []
  scales = [1,2,3]
  for scale in scales:
    obj["images"].append({
      "idiom": "universal",
      "filename": "{}@{}x.png".format(image_name, scale),
      "scale": "{}x".format(scale)
    })
  obj["info"] = info["info"]
  return obj

def write_file(path, content):
  file = open(path, "w+")
  file.write(json.dumps(content, indent=2))

def make_directory(path):
  if not os.path.exists(path):
    os.mkdir(path)

def move_files(files_to_move, dest):
  for file in files_to_move:
    end_path = "{}/{}".format(dest, file)
    shutil.copyfile(file, end_path)

IOS_END_DIR = "{}/ios/digit/React/rn_assets.xcassets".format(DIGIT_MOBILE_PATH)

def create_ios_folder(image_name, folder):
  print("Adding iOS assets for {}".format(image_name))
  # Make image directory
  make_directory(folder)
  root_contents = "{}/Contents.json".format(folder)
  write_file(root_contents, info)

  # Make imageset folder
  imageset_folder = "{}/{}.imageset".format(folder, image_name, folder)
  make_directory(imageset_folder)

  imageset_contents = "{}/Contents.json".format(imageset_folder)
  content = generate_content_json(image_name)
  write_file(imageset_contents, content)

  # Copy over files
  files_to_move = get_files_to_move(image_name)
  move_files(files_to_move, imageset_folder)

  # Move folder the digit-mobile repo
  ios_dest = "{}/{}".format(IOS_END_DIR, folder)
  if not os.path.exists(ios_dest):
    shutil.move(folder, ios_dest)