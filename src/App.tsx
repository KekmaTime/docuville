import { ThemeProvider } from "./components/theme-provider"
import { ModeToggle } from "./components/mode-toggle"

function App() {
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
          <div className="rounded-lg border border-border bg-card p-6 shadow-sm">
            <h3 className="mb-2 text-xl font-semibold">Key Information Extracted:</h3>
            <ul className="list-inside list-disc space-y-2">
              <li>Name</li>
              <li>Document Number</li>
              <li>Expiration Date</li>
            </ul>
          </div>
        </main>
      </div>
    </ThemeProvider>
  )
}

export default App