# youtube-video-transcription
YouTube Channel Audio Transcriber
This project provides a comprehensive solution for downloading and transcribing audio from YouTube videos of a specific channel. It leverages yt-dlp for downloading and converting video audio to MP3 format, and whisper for transcribing the audio content.

Features
Download Videos: Download audio from up to 239 videos of a specified YouTube channel.
Convert to MP3: Convert the downloaded audio to MP3 format.
Transcribe Audio: Use Whisper to transcribe the audio content to text.
Save Transcriptions: Save the transcriptions as text files in the same directory as the MP3 files.
Requirements
Python 3.6 or higher
yt-dlp
pydub
whisper
Installation
Clone the Repository

sh
Copy code
git clone https://github.com/your-username/YouTube-Channel-Audio-Transcriber.git
cd YouTube-Channel-Audio-Transcriber
Install Dependencies

sh
Copy code
pip install yt-dlp pydub openai-whisper
Install FFmpeg

On macOS: brew install ffmpeg
On Ubuntu: sudo apt-get install ffmpeg
On Windows: Download FFmpeg and add it to your PATH.
Usage
Set the YouTube Channel ID
Replace UCSQ6ebJE6MTrEAN_P-L-fuA with the ID of the YouTube channel you want to process in the main() function.

Run the Script

sh
Copy code
python transcriber.py
Outputs

MP3 files are saved in the downloads directory.
Transcriptions are saved as .txt files in the same directory.
Code Overview
Download and Convert to MP3
python
Copy code
def download_and_convert_to_mp3(url, download_folder="downloads"):
    # Function to download YouTube video and convert to MP3
Transcribe Audio
python
Copy code
def transcribe_audio(mp3_file, model="base"):
    # Function to transcribe MP3 using Whisper
Fetch Video URLs
python
Copy code
def get_last_239_video_urls(channel_id):
    # Function to get the last 239 video URLs from a YouTube channel by channel ID
Main Function
python
Copy code
def main():
    # Main function to process videos from a YouTube channel
Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or new features.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
yt-dlp
Pydub
Whisper
