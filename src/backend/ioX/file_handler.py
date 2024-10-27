from pathlib import Path
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

def save_results_to_file(results: List[Dict[str, Any]], output_path: Path) -> None:
    """Save OCR results to a text file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("Extracted Text Results\n")
            f.write("-" * 50 + "\n")
            for idx, result in enumerate(results, 1):
                f.write(f"Result {idx}:\n")
                f.write(f"Text: {result['text']}\n")
                f.write(f"Confidence: {result['confidence']:.2f}\n")
                f.write(f"Bounding Box: {result['bbox']}\n")
                f.write("-" * 50 + "\n")
        logger.info(f"Results saved to {output_path}")
    except Exception as e:
        logger.error(f"Error saving results to file: {str(e)}")
        raise

def save_extracted_names(names: List[Dict[str, Any]], output_path: Path) -> None:
    """Save extracted names to a file."""
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("Extracted Names\n")
            f.write("-" * 50 + "\n")
            
            if not names:
                f.write("No valid names found with sufficient confidence\n")
                return
                
            for idx, name_data in enumerate(names, 1):
                f.write(f"Name {idx}:\n")
                f.write(f"Text: {name_data['name']}\n")
                f.write(f"Confidence: {name_data['confidence']:.2f}\n")
                f.write(f"Bounding Box: {name_data['bbox']}\n")
                f.write(f"Word Count: {name_data['word_count']}\n")
                f.write("-" * 50 + "\n")
                
        logger.info(f"Names saved to {output_path}")
    except Exception as e:
        logger.error(f"Error saving names to file: {str(e)}")
        raise