import type { Metadata } from "next";
import "./globals.css";
import { DocumentProvider } from "@/context/DocumentContext";
import SideNav from "@/components/SideNav";
import { ThemeProvider } from "@/components/ThemeProvider";
import ThemeToggle from "@/components/ThemeToggle";

export const metadata: Metadata = {
  title: "Nutanix RAG Project",
  description: "Upload documents and chat with your AI assistant",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider>
          <DocumentProvider>
            <div className="app-container">
              <SideNav />
              <div className="page-container">
                <ThemeToggle />
                {children}
              </div>
            </div>
          </DocumentProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}

