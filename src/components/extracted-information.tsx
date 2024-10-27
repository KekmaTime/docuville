import { cn } from "@/lib/utils"
import { FileText } from "lucide-react"

interface ExtractedInformationProps {
  className?: string
  isUploaded?: boolean
  extractedData?: {
    names?: string[];
    passport_number?: string;
    expiry_date?: string;
  } | null
}

export function ExtractedInformation({ 
  className,
  isUploaded = false,
  extractedData
}: ExtractedInformationProps) {
  return (
    <div className={cn(
      "rounded-lg border bg-card p-6 text-card-foreground shadow",
      className
    )}>
      <h3 className="mb-4 text-xl font-semibold">Extracted Information</h3>
      
      {!isUploaded ? (
        <div className="flex flex-col items-center justify-center py-12 text-muted-foreground">
          <FileText className="mb-4 h-12 w-12" />
          <p>Upload a document to see extracted information</p>
        </div>
      ) : (
        <div className="space-y-4">
          <div className="flex items-center gap-2 text-sm">
            <span className="font-medium">Upload Status:</span>
            <span className="rounded-full bg-green-500/10 px-2 py-1 text-xs text-green-500">
              Successfully uploaded
            </span>
          </div>
          
          {extractedData && (
            <div className="space-y-3">
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium">Name:</span>
                <span>{extractedData.names?.[1] || "Not found"}</span>
              </div>
              
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium">Document Number:</span>
                <span>{extractedData.passport_number || "Not found"}</span>
              </div>
              
              <div className="flex items-center gap-2 text-sm">
                <span className="font-medium">Expiration Date:</span>
                <span>{extractedData.expiry_date || "Not found"}</span>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
