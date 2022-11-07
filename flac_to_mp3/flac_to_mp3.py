#!/usr/bin/env python3

import os
import pathlib
import sys
import threading
import subprocess
import magic
from dependency_checker import DependencyCheck
import logging

def worker(flac_song_path, mp3_song_path):
    flac_song = os.path.basename(flac_song_path)
    logger.info("Processing:\t{}".format(flac_song))
    mp3_song_folder = os.path.dirname(mp3_song_path)
    if not os.path.isdir(mp3_song_folder):
        os.makedirs(mp3_song_folder)
    subprocess.check_output(
        ["ffmpeg", "-y", "-i", flac_song_path, "-b:a", "320k", mp3_song_path]
    )
    logger.info("Complete:\t{}".format(flac_song))


def get_flag_song_list():
    flac_song_list = []
    for root, dirs, file_name in os.walk(flac_dir):
        for i in file_name:
            file_path = os.path.join(root, i)
            mime_type = magic.from_file(file_path, mime=True)
            logger.debug(f"{mime_type} - {file_path}")
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


def dependency_check():
    """dependency_check checks if the operating system is supported and all
    dependencies are installed. If not, the script exits.
    """    
    d = DependencyCheck()
    if d.supported_system() is False:
        # print(f"{d.operating_system} is not currently supported.")
        logger.info(f"{d.operating_system} is not currently supported.")
        sys.exit(0)
    else:
        pass

    if not d.all_dependencies_installed():
        logger.info(f"Ffmpeg installed: {d.ffmpeg_installed()}")
        logger.info(f"Lame installed: {d.lame_installed()}")
        logger.info(f"Flac installed: {d.flac_installed()}")
        logger.info("Not all dependencies installed. Exiting.")
        sys.exit(0)
    else:
        pass
    

def convert_flac():
    threads = []
    flac_song_list = get_flag_song_list()
    for flac_song_path in flac_song_list:
        logger.debug(flac_song_path)
        mp3_song_path = get_mp3_song_path(flac_song_path)
        logger.debug(mp3_song_path)
        t = threading.Thread(target=worker, args=(flac_song_path, mp3_song_path))
        threads.append(t)
        t.start()

# os.path directory setup. Script uses os.walk which is not available in pathlib
root_dir = os.path.dirname(os.path.abspath(__file__))
flac_dir = os.path.join(root_dir, "flac")
mp3_dir = os.path.join(root_dir, "mp3")

# Logging setup
logger = logging.getLogger(__name__)
log_file_dir = pathlib.Path(__file__).parent.joinpath("logs")
log_file_dir.mkdir(parents=True, exist_ok=True)
log_file_name = f"{pathlib.Path(__file__).stem}.log"
log_file_path = log_file_dir.joinpath(log_file_name)
FORMAT = "%(asctime)s | %(name)s | %(levelname)s | [%(module)s.%(funcName)s():line %(lineno)s] ==> %(message)s"
logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler(log_file_path), logging.StreamHandler(sys.stdout)],
)

if __name__ == "__main__":
    dependency_check()
    convert_flac()
    
