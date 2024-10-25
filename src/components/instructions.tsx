import { cn } from "@/lib/utils"

interface InstructionsProps {
  className?: string
}

export function Instructions({ className }: InstructionsProps) {
  return (
    <div className={cn("rounded-lg border border-border bg-card p-6 shadow-sm", className)}>
      <h3 className="mb-4 text-lg font-semibold">Instructions</h3>
      <ul className="space-y-2 text-sm text-muted-foreground">
        <li className="flex items-center">
          <span className="mr-2">•</span>
          Upload either a passport or driver's license image
        </li>
        <li className="flex items-center">
          <span className="mr-2">•</span>
          Supported file types: JPG, PNG
        </li>
        <li className="flex items-center">
          <span className="mr-2">•</span>
          Ensure the document is clearly visible and all text is readable
        </li>
        <li className="flex items-center">
          <span className="mr-2">•</span>
          The system will automatically extract the required information
        </li>
        <li className="flex items-center">
          <span className="mr-2">•</span>
          Verify the extracted information matches your document
        </li>
      </ul>
    </div>
  )
}