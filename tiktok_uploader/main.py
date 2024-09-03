# uploads given Video to playful user
import argparse
import tiktok
from basics import eprint
from youtube_downloader import youtube_downloader
import sys, os

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TikTokAutoUpload CLI, scheduled and immediate uploads")
    subparsers = parser.add_subparsers(dest="subcommand")

    # video and title...add link here
    video, title = youtube_downloader(link="https://youtube.com/shorts/ELmQPE9K4eE?si=23es8APgjjEUkAb-")

    # Upload subcommand.
    upload_parser = subparsers.add_parser("upload", help="Upload video on TikTok")
    upload_parser.add_argument("-p", "--proxy", default="")

    # Parse the command-line arguments
    args = parser.parse_args()
    if args.subcommand == "upload":
        if video is not False:
            tiktok.upload_video("playful", video, title, allow_comment=1, allow_duet=0, allow_stitch=0, visibility_type=0, brand_organic_type=0, branded_content_type=0, ai_label=0)

    


