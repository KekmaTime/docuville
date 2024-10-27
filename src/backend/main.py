from pathlib import Path
from typing import Dict, Any
import logging
import easyocr
from utils.logging import setup_logging
from utils.paths import get_public_dir, get_valid_image_files
from ocr.reader import initialize_reader, extract_text
from extractors.passport import extract_passport_number, extract_expiry_date
from extractors.names import extract_names, extract_names_from_mrz
from ioX.file_handler import save_results_to_file, save_extracted_names

logger = logging.getLogger(__name__)

def process_image(image_path: Path, reader: easyocr.Reader) -> Dict[str, Any]:
    """Process a single image and return extracted information."""
    try:
        results = extract_text(reader, str(image_path))
        
        names_mrz = extract_names_from_mrz(results)
        names_regular = extract_names(results) if not names_mrz else []
        extracted_names = names_mrz or names_regular
        
        return {
            'names': extracted_names,
            'passport_number': extract_passport_number(results),
            'expiry_date': extract_expiry_date(results),
            'raw_results': results
        }
        
    except Exception as e:
        logger.error(f"Error processing {image_path}: {str(e)}")
        raise

def main():
    try:
        # Initialize reader
        reader = initialize_reader()
        
        # Get the public directory
        public_dir = get_public_dir()
        
        # Get all valid image files
        image_files = get_valid_image_files(public_dir)
        
        if not image_files:
            logger.error(f"No valid image files found in {public_dir}")
            return
            
        # Process each image
        for image_path in image_files:
            print(f"\n=== Processing {image_path.name} ===")
            
            # Process the image
            extracted_data = process_image(image_path, reader)
            
            # Save results
            base_name = image_path.stem
            save_results_to_file(
                extracted_data['raw_results'],
                public_dir / f'{base_name}_ocr_results.txt'
            )
            save_extracted_names(
                extracted_data['names'],
                public_dir / f'{base_name}_extracted_names.txt'
            )
            
            # Print results
            print(f"\n=== Results for {image_path.name} ===")
            print("--------------------------------------------------")
            
            # Print Names
            print("\nNames:")
            if extracted_data['names']:
                for name_data in extracted_data['names']:
                    print(f"  • {name_data['name']}")
            else:
                print("  No valid names found")
                
            # Print Passport Number
            print("\nPassport Number:")
            if extracted_data['passport_number'] != "No passport number found":
                print(f"  • {extracted_data['passport_number']}")
            else:
                print("  No valid passport number found")
                
            # Print Expiry Date
            print("\nExpiry Date:")
            if extracted_data['expiry_date'] != "No expiry date found":
                print(f"  • {extracted_data['expiry_date']}")
            else:
                print("  No valid expiry date found")
                
            print("\n--------------------------------------------------")
                
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
