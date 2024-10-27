import easyocr
import logging
from typing import List

logger = logging.getLogger(__name__)

def initialize_reader(languages: List[str] = ['en']) -> easyocr.Reader:
    """Initialize the OCR reader with specified languages."""
    try:
        reader = easyocr.Reader(languages)
        logger.info(f"Initialized EasyOCR with languages: {languages}")
        return reader
    except Exception as e:
        logger.error(f"Failed to initialize EasyOCR: {str(e)}")
        raise

def extract_text(reader: easyocr.Reader, image_path: str) -> List[dict]:
    """Extract text from the given image."""
    from pathlib import Path
    path = Path(image_path)
    if not path.exists():
        logger.error(f"Image file not found: {image_path}")
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        results = reader.readtext(str(path))
        processed_results = [
            {
                "text": text,
                "confidence": confidence,
                "bbox": bbox
            }
            for bbox, text, confidence in results
        ]
        
        logger.info(f"Successfully extracted {len(processed_results)} text segments")
        return processed_results

    except Exception as e:
        logger.error(f"Error processing image {image_path}: {str(e)}")
        raise