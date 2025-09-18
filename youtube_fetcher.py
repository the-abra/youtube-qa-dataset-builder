import yt_dlp
import logging

logger = logging.getLogger(__name__)

def get_youtube_video_urls(channel_url, max_videos=50):
    """
    Extract video URLs from a YouTube channel.
    
    Args:
        channel_url (str): The URL of the YouTube channel.
        max_videos (int): Maximum number of videos to fetch.
        
    Returns:
        list: List of video URLs.
    """
    logger.info(f"Fetching video URLs from channel: {channel_url}")
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'discard_in_playlist',
        'playlistend': max_videos
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(channel_url, download=False)
            video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in info_dict['entries']]
        
        logger.info(f"Found {len(video_urls)} videos.")
        return video_urls
    
    except Exception as e:
        logger.error(f"Failed to fetch video URLs: {str(e)}")
        raise