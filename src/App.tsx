import { ThemeProvider } from "./components/theme-provider"
import { ModeToggle } from "./components/mode-toggle"
import { FileUpload } from "./components/file-upload"
import { Instructions } from "./components/instructions"
import { ExtractedInformation } from "./components/extracted-information"
import { useState } from "react"

function App() {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null)
  const [extractedData, setExtractedData] = useState(null)

  const handleFileSelect = (file: File) => {
    setUploadedFile(file)
    console.log("Selected file:", file)
  }

  return (
    <ThemeProvider defaultTheme="dark" storageKey="vite-ui-theme">
      <div className="min-h-screen bg-background text-foreground">
        <header className="border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
          <div className="container flex h-14 items-center">
            <div className="mr-4 flex">
              <ModeToggle />
            </div>
            <h1 className="text-4xl font-semibold">Docuville</h1>
          </div>
        </header>
        <main className="container mx-auto mt-8 px-4">
          <h2 className="mb-4 text-2xl font-bold">Document Extraction Tool</h2>
          <p className="mb-4 text-muted-foreground">
            Welcome to the Docuville document extraction tool. This application is currently a work in progress.
          </p>
          <div className="grid grid-cols-1 gap-6 md:grid-cols-2">
            <FileUpload 
              onFileSelect={handleFileSelect}
              className="h-full"
            />
            <ExtractedInformation 
              className="h-full"
              isUploaded={!!uploadedFile}
              extractedData={extractedData}
            />
          </div>
          <Instructions className="mt-8" />
        </main>
      </div>
    </ThemeProvider>
  )
}

export default App
