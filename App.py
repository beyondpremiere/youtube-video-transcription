import os
import yt_dlp as youtube_dl
from pydub import AudioSegment
import whisper

# Function to download YouTube video and convert to MP3
def download_and_convert_to_mp3(url, download_folder="downloads"):
    # Ensure download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            mp3_file = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            return mp3_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to transcribe MP3 using Whisper
def transcribe_audio(mp3_file, model="base"):
    # Load the Whisper model
    whisper_model = whisper.load_model(model)

    # Transcribe the audio file
    transcription = whisper_model.transcribe(mp3_file)

    return transcription['text']

# Function to get the last 239 video URLs from a YouTube channel by channel ID
def get_last_239_video_urls(channel_id):
    channel_url = f"https://www.youtube.com/channel/{channel_id}/videos"
    ydl_opts = {
        'ignoreerrors': True,
        'quiet': True,
        'extract_flat': True,
        'skip_download': True,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        if 'entries' in result:
            return [f"https://www.youtube.com/watch?v={entry['id']}" for entry in result['entries'][:239] if entry]
        return []

def main():
    channel_id = "INSERT ID HERE"

    print("Fetching the last 239 video URLs from the channel...")
    video_urls = get_last_239_video_urls(channel_id)

    for video_url in video_urls:
        print(f"Processing video: {video_url}")
        mp3_file = download_and_convert_to_mp3(video_url)
        if mp3_file:
            print(f"MP3 file saved at: {mp3_file}")

            print("Transcribing audio using Whisper...")
            transcription = transcribe_audio(mp3_file)

            # Save transcription to a text file
            transcription_file = mp3_file.replace(".mp3", ".txt")
            with open(transcription_file, "w") as f:
                f.write(transcription)

            print(f"Transcription saved at: {transcription_file}")
        else:
            print(f"Skipping video: {video_url}")

if __name__ == "__main__":
    main()
