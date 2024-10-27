import re
from typing import List, Dict, Any

def extract_passport_number(results: List[Dict[str, Any]]) -> str:
    """Extract passport number from OCR results."""
    old_pattern = r'^\d{9}$'  # Nine digits
    new_pattern = r'^[A-Z]\d{8}$'  # One uppercase letter followed by 8 digits
    
    for result in results:
        text = result['text'].strip()
        confidence = result['confidence']
        
        if confidence < 0.6:
            continue
            
        if re.match(new_pattern, text):
            return text
            
        if re.match(old_pattern, text):
            return text
            
        new_matches = re.findall(r'[A-Z]\d{8}', text)
        if new_matches:
            return new_matches[0]
            
        old_matches = re.findall(r'\d{9}', text)
        if old_matches:
            return old_matches[0]
    
    return "No passport number found"

def extract_expiry_date(results: List[Dict[str, Any]]) -> str:
    """Extract expiry date from OCR results."""
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
              'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    dates = []
    
    for result in results:
        text = result['text'].lower()
        if (any(month in text for month in months) and 
            any(char.isdigit() for char in text)):
            dates.append(result['text'])
    
    return dates[-1] if dates else "No expiry date found"