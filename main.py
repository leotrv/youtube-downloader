import os
from yt_dlp import YoutubeDL

def download_youtube_mp3(url, output_path="downloads"):
    """
    Downloads the audio from a YouTube video as an MP3 file using yt-dlp.
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("MP3 download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def download_youtube_mp4(url, output_path="downloads"):
    """
    Downloads the video from a YouTube link as an MP4 file using yt-dlp.
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "merge_output_format": "mp4",
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("MP4 download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

# General usage
if __name__ == "__main__":
    print("Welcome to the YouTube Downloader!")
    filetype = input("Type 'mp3' to download audio or 'mp4' to download video: ").strip().lower()
    if filetype not in ("mp3", "mp4"):
        print("Invalid option. Please type 'mp3' or 'mp4'.")
    else:
        video_url = input("Enter the YouTube video URL: ").strip()
        if filetype == "mp3":
            download_youtube_mp3(video_url)
        else:
            download_youtube_mp4(video_url)
