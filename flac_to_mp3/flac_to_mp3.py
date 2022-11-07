#!/usr/bin/env python3

"""
Converts flac to mp3 (320 kb) using ffmpeg
Put flac files/folders into 'flac_folder' and run script.
Requirements:
	ffmpeg: sudo apt install ffmpeg
	lame: sudo apt install lame
	flac: sudo apt install flac
	magic: pip3 install python-magic
"""

import os
import sys
import threading
import subprocess
import magic


def worker(flac_song_path, mp3_song_path):
    flac_song = os.path.basename(flac_song_path)
    print("Processing:\t{}".format(flac_song))
    mp3_song_folder = os.path.dirname(mp3_song_path)
    if not os.path.isdir(mp3_song_folder):
        os.makedirs(mp3_song_folder)
    subprocess.check_output(
        ["ffmpeg", "-y", "-i", flac_song_path, "-b:a", "320k", mp3_song_path]
    )
    print("Complete:\t{}".format(flac_song))


def get_flag_song_list():
    flac_song_list = []
    for root, dirs, file_name in os.walk(flac_dir):
        for i in file_name:
            file_path = os.path.join(root, i)
            mime_type = magic.from_file(file_path, mime=True)
            # print(f"{mime_type} - {file_path}")
            if mime_type.split("/")[0] == "audio" and mime_type.split("/")[-1].endswith(
                "flac"
            ):
                flac_song_list.append(file_path)
    return flac_song_list


def get_mp3_song_path(flac_song_path):
    flac_song = os.path.basename(flac_song_path)
    flac_song_folder = os.path.dirname(flac_song_path)
    mp3_song_folder = mp3_dir.join(flac_song_folder.split(flac_dir))
    mp3_song = flac_song.replace(".flac", ".mp3")
    mp3_song_path = os.path.join(mp3_song_folder, mp3_song)
    return mp3_song_path


def check_dependencies():
    dependency_list = ["flac", "lame", "ffmpeg"]
    dependencies_installed = True
    for dependency in dependency_list:
        not_installed_message = "{} not installed. sudo apt install {}".format(
            dependency, dependency
        )
        try:
            output = subprocess.check_output(["which", dependency]).strip()
            expected_output = "/usr/bin/{}".format(dependency).encode()
            if output == expected_output:
                print("{} installed: {}".format(dependency, str(output)))
            else:
                print(not_installed_message)
                dependencies_installed = False
        except subprocess.CalledProcessError as e:
            print(not_installed_message)
            dependencies_installed = False
    if dependencies_installed is False:
        sys.exit(0)


def dependencies_installed():
    dependency_list = ["flac", "lame", "ffmpeg"]
    dependency_check_passed = True
    for dependency in dependency_list:
        try:
            output = subprocess.check_output(["which", dependency]).strip().decode()
            if os.path.isfile(output):
                pass
            else:
                print(f"{dependency} does not exist")
                dependency_check_passed = False
        except subprocess.CalledProcessError as e:
            print(f"{dependency} not installed")
            dependency_check_passed = False
    return dependency_check_passed


if not dependencies_installed():
    print("Not all dependncies installed. Exiting.")
    sys.exit(0)

root_dir = os.path.dirname(os.path.abspath(__file__))
flac_dir = os.path.join(root_dir, "flac")
mp3_dir = os.path.join(root_dir, "mp3")

if __name__ == "__main__":
    threads = []
    flac_song_list = get_flag_song_list()
    for flac_song_path in flac_song_list:
        print(flac_song_path)
        mp3_song_path = get_mp3_song_path(flac_song_path)
        print(mp3_song_path)
        # t = threading.Thread(target=worker, args=(flac_song_path, mp3_song_path))
        # threads.append(t)
        # t.start()
