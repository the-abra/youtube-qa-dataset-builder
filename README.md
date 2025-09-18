# YouTube QA Dataset Builder

This project extracts YouTube video transcripts from a specified channel and generates a question-answer dataset suitable for training AI models.

## Features
- Fetches video URLs from a YouTube channel
- Downloads and cleans transcripts (prioritizing Turkish)
- Generates basic question-answer pairs from the text
- Outputs data in JSONL format

## Requirements
- Python 3.6+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd youtube-qa-dataset-builder
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python youtube_qa_builder.py --channel_url <YOUTUBE_CHANNEL_URL> --max_videos <NUMBER> --output_dir <DIRECTORY>
```

### Example:
```bash
python youtube_qa_builder.py --channel_url https://www.youtube.com/@kodla_dev --max_videos 50 --output_dir ./data
```

### Command Line Arguments:
- `--channel_url` (required): YouTube channel URL
- `--max_videos` (optional, default: 50): Maximum number of videos to process
- `--min_pairs` (optional, default: 100): Minimum number of QA pairs to generate
- `--output_dir` (optional, default: "./data"): Directory to save output files

## Project Structure
- `youtube_qa_builder.py`: Main script
- `youtube_fetcher.py`: Handles YouTube video fetching
- `transcript_processor.py`: Processes and cleans transcripts
- `qa_generator.py`: Creates QA pairs from text
- `requirements.txt`: Python dependencies
- `data/`: Default output directory (created automatically)

## How It Works
1. **Fetch Videos**: Extracts video URLs from the specified YouTube channel
2. **Download Transcripts**: Downloads transcripts prioritizing Turkish, then English
3. **Clean Transcripts**: Processes and cleans the downloaded transcripts
4. **Generate QA Pairs**: Creates question-answer pairs from the cleaned text
5. **Output**: Saves all data in structured formats in the output directory

## Contributing
Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.