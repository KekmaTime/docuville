import { useCallback, useState } from "react"
import { Button } from "./ui/button"
import { Upload } from "lucide-react"
import { cn } from "@/lib/utils"

interface FileUploadProps {
  onFileSelect: (file: File) => void
  className?: string
}

export function FileUpload({ onFileSelect, className }: FileUploadProps) {
  const [isDragging, setIsDragging] = useState(false)

  const handleDragOver = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(true)
  }, [])

  const handleDragLeave = useCallback((e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault()
    setIsDragging(false)
  }, [])

  const handleDrop = useCallback(
    (e: React.DragEvent<HTMLDivElement>) => {
      e.preventDefault()
      setIsDragging(false)
      
      const files = Array.from(e.dataTransfer.files)
      if (files.length > 0) {
        onFileSelect(files[0])
      }
    },
    [onFileSelect]
  )

  const handleFileInput = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const files = e.target.files
      if (files && files.length > 0) {
        onFileSelect(files[0])
      }
    },
    [onFileSelect]
  )

  return (
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
      />
      <div className="mx-auto mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-muted">
        <Upload className="h-6 w-6 text-muted-foreground" />
      </div>
      <p className="mb-2 text-sm text-muted-foreground">
        Drag and drop your document here or
      </p>
      <label htmlFor="file-upload">
        <Button variant="secondary" className="mt-2" onClick={() => document.getElementById('file-upload')?.click()}>
          Browse Files
        </Button>
      </label>
    </div>
  )
}
