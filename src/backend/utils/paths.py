from pathlib import Path
from typing import List

def get_public_dir() -> Path:
    """Get the absolute path to the public directory."""
    current_file = Path(__file__).resolve()
    project_root = current_file.parent.parent.parent.parent
    public_dir = project_root / 'public'
    return public_dir

def get_valid_image_files(directory: Path) -> List[Path]:
    """Get all valid image files from the directory."""
    valid_extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    return [
        f for f in directory.iterdir()
        if f.is_file() and f.suffix.lower() in valid_extensions
    ]