import argparse
import os
import logging
from youtube_fetcher import get_youtube_video_urls
from transcript_processor import get_transcripts, clean_transcript
from qa_generator import create_qa_pairs
from version import __version__

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description="Build a QA dataset from YouTube video transcripts.")
    parser.add_argument("--channel_url", required=True, help="YouTube channel URL")
    parser.add_argument("--max_videos", type=int, default=50, help="Maximum number of videos to process")
    parser.add_argument("--min_pairs", type=int, default=100, help="Minimum number of QA pairs to generate")
    parser.add_argument("--output_dir", default="./data", help="Directory to save output files")
    parser.add_argument("--version", action="version", version=f"Youtube QA Builder v{__version__}")
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Define file paths
    transcript_file = os.path.join(args.output_dir, "tum_transkriptler.txt")
    cleaned_file = os.path.join(args.output_dir, "temiz_transkript.txt")
    qa_file = os.path.join(args.output_dir, "veri_setim.jsonl")
    
    try:
        logger.info("Starting YouTube QA dataset building process...")
        
        # Step 1: Get video URLs
        video_urls = get_youtube_video_urls(args.channel_url, args.max_videos)
        
        # Step 2: Download transcripts
        transcript_file = get_transcripts(video_urls, transcript_file)
        
        # Step 3: Clean transcripts
        cleaned_file = clean_transcript(transcript_file, cleaned_file)
        
        # Step 4: Generate QA pairs
        qa_file = create_qa_pairs(cleaned_file, qa_file, args.min_pairs)
        
        logger.info("Process completed successfully!")
        logger.info(f"Generated files:")
        logger.info(f"- All transcripts: {transcript_file}")
        logger.info(f"- Cleaned transcripts: {cleaned_file}")
        logger.info(f"- QA dataset: {qa_file}")
        
    except Exception as e:
        logger.error(f"An error occurred during processing: {str(e)}")
        raise

if __name__ == "__main__":
    main()