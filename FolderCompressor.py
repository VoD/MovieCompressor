import os
import os.path
import subprocess
import uuid
import shutil
import glob


def compress_movie(src_path: str, is_high_quality: bool):

    if is_high_quality:
        quality = "65"
    else:
        quality = "40"

    dirname = os.path.dirname(src_path)
    dst_path = os.path.join(dirname, str(uuid.uuid4()) + ".mp4")

    try:
        subprocess.run(["ffmpeg", "-hide_banner", "-i", src_path, "-c:v", "hevc_videotoolbox", "-q:v", quality, "-tag:v","hvc1", "-vf", "scale=1280:720", "-an", dst_path], check=True)
    except subprocess.CalledProcessError as e:
        print("Failed to compress movie.")
        print(e)
    else:
        os.remove(src_path)
        os.rename(dst_path, os.path.splitext(src_path)[0] + ".mp4")


def compress_folder(dir_path: str, high_quality: bool):
    file_paths = glob.glob(os.path.join(dir_path, "*.mp4"))
    for path in file_paths:
        compress_movie(path, high_quality)



if __name__ == "__main__": 
    compress_folder('/tmp/test_folder', True)
