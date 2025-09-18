from setuptools import setup, find_packages

setup(
    name="youtube-qa-dataset-builder",
    version="1.0.0",
    author="Kodla AI Bot",
    author_email="example@example.com",
    description="A tool to build question-answer datasets from YouTube video transcripts",
    long_description="A tool to build question-answer datasets from YouTube video transcripts",
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/youtube-qa-dataset-builder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "yt-dlp",
        "beautifulsoup4",
        "tqdm",
    ],
    entry_points={
        "console_scripts": [
            "youtube-qa-builder=youtube_qa_builder:main",
        ],
    },
)