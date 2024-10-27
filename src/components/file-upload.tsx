import { useCallback, useState } from "react"
import { Button } from "./ui/button"
import { Upload } from "lucide-react"
import { cn } from "@/lib/utils"

interface FileUploadProps {
  onFileSelect: (file: File, data: ProcessedData) => void
  className?: string
}

interface ProcessedData {
  names: string[];
  passport_number: string;
  expiry_date: string;
}

export function FileUpload({ onFileSelect, className }: FileUploadProps) {
  const [isDragging, setIsDragging] = useState(false)
  const [isProcessing, setIsProcessing] = useState(false)
  const [processedData, setProcessedData] = useState<ProcessedData | null>(null)
  const [error, setError] = useState<string | null>(null)

  const processFile = async (file: File) => {
    setIsProcessing(true)
    setError(null)
    
    const formData = new FormData()
    formData.append('file', file)
    
    try {
      const response = await fetch('http://localhost:8000/api/process-document', {
        method: 'POST',
        body: formData,
      })
      
      const result = await response.json()
      
      if (result.success) {
        setProcessedData(result.data)
        onFileSelect(file, result.data) // Pass both file and data to parent
      } else {
        setError(result.error || 'Failed to process document')
      }
    } catch (err) {
      setError('Failed to connect to server')
    } finally {
      setIsProcessing(false)
    }
  }

  const handleDragOver = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(true)
  }, [])

  const handleDragLeave = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(false)
  }, [])

  const handleDrop = useCallback(
    async (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault()
      setIsDragging(false)
      
      const files = Array.from(e.dataTransfer.files)
      if (files.length > 0) {
        await processFile(files[0])
      }
    },
    [onFileSelect]
  )

  const handleFileInput = useCallback(
    async (e: React.ChangeEvent<HTMLInputElement>) => {
      const files = e.target.files
      if (files && files.length > 0) {
        await processFile(files[0])
      }
    },
    [onFileSelect]
  )

  return (
    <div className="space-y-4">
      <div
        className={cn(
          "relative rounded-lg border-2 border-dashed border-border p-12 text-center",
          isDragging && "border-primary bg-accent/50",
          className
        )}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          className="hidden"
          id="file-upload"
          onChange={handleFileInput}
          accept="image/*"
        />
        <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-muted">
          <Upload className="h-6 w-6 text-muted-foreground" />
        </div>
        <p className="mb-2 text-sm text-muted-foreground">
          {isProcessing ? 'Processing...' : 'Drag and drop your document here or'}
        </p>
        <label htmlFor="file-upload">
          <Button 
            variant="secondary" 
            className="mt-2" 
            onClick={() => document.getElementById('file-upload')?.click()}
            disabled={isProcessing}
          >
            Browse Files
          </Button>
        </label>
      </div>

      {error && (
        <div className="text-red-500 text-sm mt-2">
          {error}
        </div>
      )}
    </div>
  )
}
