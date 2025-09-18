import re
import json
import logging

logger = logging.getLogger(__name__)

def create_qa_pairs(cleaned_file, output_file="veri_setim.jsonl", min_pairs=100):
    """
    Generate question-answer pairs from a cleaned transcript file.
    
    Args:
        cleaned_file (str): Path to the cleaned transcript file.
        output_file (str): Path to save the QA pairs in JSONL format.
        min_pairs (int): Minimum number of QA pairs to generate.
        
    Returns:
        str: Path to the output file.
    """
    logger.info("Generating QA pairs...")
    
    with open(cleaned_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Split text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    qa_pairs = []
    
    # Generate QA pairs from sentences
    for i in range(len(sentences) - 1):
        current = sentences[i].strip()
        next_sentence = sentences[i + 1].strip()
        
        # Skip short sentences
        if len(current) < 10 or len(next_sentence) < 10:
            continue
        
        # Basic question generation strategies
        if "nedir" in current.lower() or "ne" in current.lower():
            question = current
            answer = next_sentence
        elif "nasıl" in current.lower() or "nasıl" in next_sentence.lower():
            question = next_sentence
            answer = current
        elif "hangi" in current.lower() or "hangi" in next_sentence.lower():
            question = next_sentence
            answer = current
        else:
            # Fallback question format
            question = f"{current.split()[0]} nedir?"
            answer = current
        
        # Add QA pair
        qa_pairs.append({
            "messages": [
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer}
            ]
        })
        
        # Stop when we have enough pairs
        if len(qa_pairs) >= min_pairs:
            break
    
    # Write to JSONL file
    with open(output_file, 'w', encoding='utf-8') as f:
        for pair in qa_pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + '\n')
    
    logger.info(f"Generated {len(qa_pairs)} QA pairs and saved to {output_file}")
    return output_file