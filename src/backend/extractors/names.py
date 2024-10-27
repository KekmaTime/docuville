from typing import List, Dict, Any

def extract_names_from_mrz(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Extract names from MRZ line and regular text of passport."""
    exclusions = {
        'PASSPORT', 'PASSEPORT', 'PASAPORTE', 'TYPE', 'TIPO', 'CODE', 'CODIGO',
        'SURNAME', 'NOM', 'APELLIDOS', 'GIVEN', 'NAMES', 'PRENOMS', 'NOMBRES',
        'NATIONALITY', 'NATIONALITE', 'NACIONALIDAD', 'MATIONALITE', 'NATIONALILE',
        'DATE', 'FECHA', 'BIRTH', 'NAISSANCE', 'NACIMIENTO', 'PLACE', 'LIEU', 'LUGAR',
        'ISSUE', 'DELIVRANCE', 'EXPEDICION', 'EXPIRATION', 'EXPIRACION', 'CADUCIDAD',
        'SEX', 'SEXE', 'SEXO', 'AUTHORITY', 'AUTORITE', 'AUTORIDAD', 'CARD',
        'ENDORSEMENTS', 'MENTIONS', 'SPECIALES', 'ANOTACIONES', 'GERMANY', 'EXEMPLAR',
        'UNITED', 'STATES', 'AMERICA', 'USA', 'CANADA', 'ECUADOR', 'UK', 'PAGE', 'NEW',
        'NUMBER', 'NO', 'NUM', 'NUMERO', 'AUTHORIZED', 'SIGNATURE',
        'THE', 'OF', 'AND', 'FOR', 'TO', 'IN', 'ON', 'AT',
        'DE', 'LA', 'EL', 'LOS', 'LAS', 'DEL', 'DU', 'DES'
    }
    
    extracted_names = []
    
    def is_valid_name(text: str) -> bool:
        if (text in exclusions or len(text) < 2 or
            any(char.isdigit() for char in text) or
            not all(c.isalpha() or c.isspace() or c in "-'" for c in text)):
            return False
        return True
    
    # Extract from regular text with high confidence
    for result in results:
        text = result['text'].upper()
        confidence = result['confidence']
        if confidence > 0.9 and len(text) > 2 and text.isalpha() and is_valid_name(text):
            extracted_names.append({
                'name': text,
                'confidence': confidence,
                'bbox': result['bbox'],
                'word_count': 1
            })
    
    # Extract from MRZ line
    for result in results:
        text = result['text']
        if text.startswith('P<USA'):
            try:
                parts = text[5:].split('<<')
                if len(parts) >= 2:
                    name_part = parts[0]
                    remaining_names = parts[1]
                    
                    surname = name_part.replace('<', ' ').strip()
                    given_names = remaining_names.replace('<', ' ').strip()
                    
                    if surname and is_valid_name(surname) and surname not in [n['name'] for n in extracted_names]:
                        extracted_names.append({
                            'name': surname,
                            'confidence': result['confidence'],
                            'bbox': result['bbox'],
                            'word_count': 1
                        })
                    
                    if given_names and is_valid_name(given_names) and given_names not in [n['name'] for n in extracted_names]:
                        extracted_names.append({
                            'name': given_names,
                            'confidence': result['confidence'],
                            'bbox': result['bbox'],
                            'word_count': len(given_names.split())
                        })
            except Exception as e:
                logger.warning(f"Failed to parse MRZ line: {str(e)}")
                continue
            
    return extracted_names

def extract_names(results: List[Dict[str, Any]], min_confidence: float = 0.9) -> List[Dict[str, Any]]:
    """Extract names using regular text analysis with sophisticated filtering."""
    exclusions = {
        'PASSPORT', 'PASSEPORT', 'PASAPORTE', 'TYPE', 'TIPO', 'CODE', 'CODIGO',
        'SURNAME', 'NOM', 'APELLIDOS', 'GIVEN', 'NAMES', 'PRENOMS', 'NOMBRES',
        'NATIONALITY', 'NATIONALITE', 'NACIONALIDAD', 'MATIONALITE', 'NATIONALILE',
        'DATE', 'FECHA', 'BIRTH', 'NAISSANCE', 'NACIMIENTO', 'PLACE', 'LIEU', 'LUGAR',
        'ISSUE', 'DELIVRANCE', 'EXPEDICION', 'EXPIRATION', 'EXPIRACION', 'CADUCIDAD',
        'SEX', 'SEXE', 'SEXO', 'AUTHORITY', 'AUTORITE', 'AUTORIDAD', 'CARD',
        'ENDORSEMENTS', 'MENTIONS', 'SPECIALES', 'ANOTACIONES', 'GERMANY',
        'UNITED', 'STATES', 'AMERICA', 'USA', 'CANADA', 'ECUADOR', 'UK', 'PAGE', 'NEW',
        'NUMBER', 'NO', 'NUM', 'NUMERO', 'AUTHORIZED', 'SIGNATURE', 'EXEMPLAR',
        'THE', 'OF', 'AND', 'FOR', 'TO', 'IN', 'ON', 'AT',
        'DE', 'LA', 'EL', 'LOS', 'LAS', 'DEL', 'DU', 'DES'
    }

    def is_valid_name(text: str) -> bool:
        cleaned = ' '.join(text.strip().split())
        if (len(cleaned) < 2 or cleaned in exclusions or
            any(char.isdigit() for char in cleaned) or
            not all(c.isalpha() or c.isspace() or c in "-'" for c in cleaned)):
            return False
        return True

    extracted_names = []
    seen_names = set()

    for result in results:
        text = result['text'].upper()
        confidence = result['confidence']
        
        if confidence < min_confidence or not is_valid_name(text):
            continue
            
        name_parts = text.split()
        if len(name_parts) > 1 and not any(part in exclusions for part in name_parts):
            if text not in seen_names:
                seen_names.add(text)
                extracted_names.append({
                    'name': text,
                    'confidence': confidence,
                    'bbox': result['bbox'],
                    'word_count': len(name_parts)
                })

    return sorted(extracted_names, key=lambda x: (-x['confidence'], -x['word_count']))