import yt_dlp
import logging
import re

logger = logging.getLogger(__name__)

def get_transcripts(video_urls, output_file="tum_transkriptler.txt"):
    """
    Download transcripts for a list of YouTube videos.
    
    Args:
        video_urls (list): List of YouTube video URLs.
        output_file (str): Path to save the combined transcripts.
        
    Returns:
        str: Path to the output file.
    """
    logger.info("Downloading transcripts...")
    
    all_transcripts = []
    
    for url in video_urls:
        try:
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'subtitleslangs': ['tr', 'en'],
                'skip_download': True,
                'quiet': True
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Get transcript prioritizing Turkish > English
                transcript = None
                if 'subtitles' in info and 'tr' in info['subtitles']:
                    transcript = info['subtitles']['tr'][0]['data']
                elif 'subtitles' in info and 'en' in info['subtitles']:
                    transcript = info['subtitles']['en'][0]['data']
                elif 'automatic_captions' in info and 'tr' in info['automatic_captions']:
                    transcript = info['automatic_captions']['tr'][0]['data']
                elif 'automatic_captions' in info and 'en' in info['automatic_captions']:
                    transcript = info['automatic_captions']['en'][0]['data']
                
                if transcript:
                    all_transcripts.append(transcript)
                else:
                    logger.warning(f"No Turkish or English transcript found for {url}")
                    
        except Exception as e:
            logger.error(f"Failed to get transcript for {url}: {str(e)}")
    
    # Write all transcripts to file
    with open(output_file, 'w', encoding='utf-8') as f:
        for transcript in all_transcripts:
            f.write(transcript + "\n")
    
    logger.info(f"Saved all transcripts to {output_file}")
    return output_file

def clean_transcript(input_file, output_file="temiz_transkript.txt"):
    """
    Clean and process the transcript file.
    
    Args:
        input_file (str): Path to the input transcript file.
        output_file (str): Path to save the cleaned transcript.
        
    Returns:
        str: Path to the output file.
    """
    logger.info("Cleaning transcript...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Remove timestamps and other metadata
    # This is a simple cleaning, you might want to make it more sophisticated
    cleaned_text = re.sub(r'\d+:\d+:\d+\.\d+ --> \d+:\d+:\d+\.\d+', '', text)
    cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text)  # Remove HTML tags
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', cleaned_text)  # Remove extra newlines
    cleaned_text = re.sub(r'^\s+', '', cleaned_text, flags=re.MULTILINE)  # Remove leading whitespace
    
    # Write cleaned text to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)
    
    logger.info(f"Saved cleaned transcript to {output_file}")
    return output_file