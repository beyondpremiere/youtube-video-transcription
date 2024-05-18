# YouTube Video Transcription

A Python script to download and transcribe YouTube videos using yt-dlp, pydub, and Whisper.

## Requirements

- Python 3.x
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [pydub](https://github.com/jiaaro/pydub)
- [whisper](https://github.com/openai/whisper)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/youtube-video-transcription.git
    cd youtube-video-transcription
    ```

2. Install the required libraries:
    ```bash
    pip install yt-dlp pydub whisper
    ```

## Usage

1. Open the `youtube_transcription.py` file and update the `channel_id` variable with the ID of the YouTube channel you want to process.

2. Run the script:
    ```bash
    python youtube_transcription.py
    ```

The script will download the last 239 videos from the specified YouTube channel, convert them to MP3, transcribe the audio using Whisper, and save the transcriptions as text files.

## Example

```python
if __name__ == "__main__":
    main()
