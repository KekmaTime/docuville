# Docuville Document Extraction Tool

A powerful document extraction tool that uses OCR (Optical Character Recognition) to automatically extract key information from identity documents like passports and driving licenses.

## Features

- **Document Processing**: Upload and process images of identity documents
- **OCR Extraction**: Uses EasyOCR for accurate text extraction
- **Key Information Detection**: Automatically identifies and extracts:
  - Full Names
  - Document/Passport Numbers  
  - Expiration Dates
- **Modern UI**: Clean, responsive interface with dark/light mode support
- **Real-time Processing**: View extracted information immediately after upload
- **Cross-platform**: Works on any modern browser

## Technology Stack

### Frontend

- React 18 with TypeScript
- TailwindCSS for styling
- Lucide React for icons
- Shadcn/ui components

### Backend  

- FastAPI for the REST API
- EasyOCR for text extraction
- Python 3.8+
- Uvicorn ASGI server

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 16+ or Bun
- pip package manager

### Installation & Setup

1. **Frontend Setup**

   ```bash
   # Install dependencies
   bun install
   
   # Start development server
   bun run dev
   ```

   The frontend will be available at <http://localhost:5173>

2. **Backend Setup**

   ```bash
   # Install Python dependencies
   pip install -r src/backend/requirements.txt
   
   # Start the server
   python src/backend/server.py
   ```

   The API will be available at <http://localhost:8000>

## Usage

1. Open the application in your browser
2. Upload a document by either:
   - Dragging and dropping an image file
   - Clicking "Browse Files" to select an image
3. Wait for the processing to complete
4. View the extracted information in the right panel

## API Endpoints

- `POST /api/process-document`: Process an uploaded document image
  - Accepts: multipart/form-data with image file
  - Returns: JSON with extracted information
