import os
from yt_dlp import YoutubeDL

def download_youtube_mp3(url, output_path="downloads"):
    """
    Downloads the audio from a YouTube video as an MP3 file using yt-dlp.

    Parameters:
    - url (str): The YouTube video URL.
    - output_path (str): The directory where the MP3 file will be saved.

    Returns:
    - str: The file path of the downloaded MP3.
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

        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_youtube_mp3(video_url)
