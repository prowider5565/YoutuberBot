
from pytubefix import YouTube
import os

def download_youtube_video(video_url, save_path):
    try:
        # Create YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Check if the save path exists, create it if it doesn't
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        # Download the video to the given path
        stream.download(output_path=save_path)
        
        print(f'Video downloaded successfully and saved to {save_path}')
    
    except Exception as e:
        print(f"An error occurred: {e}")

