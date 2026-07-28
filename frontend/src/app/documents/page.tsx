"use client";

import DragDropZone from "@/components/DragDropZone";
import DocumentList from "@/components/DocumentList";
import { useDocuments } from "@/context/DocumentContext";

export default function DocumentsPage() {
  const { documents, addDocument } = useDocuments();

  return (
    <main style={{ padding: "32px", maxWidth: "800px", margin: "0 auto", height: "100%", overflowY: "auto" }}>
      <div style={{ marginBottom: "32px" }}>
        <h1 className="animate-fade-in" style={{ fontSize: "2.2rem", marginBottom: "8px" }}>
          Context Documents
        </h1>
        <p className="animate-fade-in" style={{ color: "var(--text-muted)", animationDelay: "0.1s" }}>
          Upload and manage documents for your RAG model.
        </p>
      </div>
      
      <div style={{ display: "flex", flexDirection: "column", gap: "32px" }}>
        <div style={{ animationDelay: "0.2s" }} className="animate-fade-in">
          <DragDropZone onUploadSuccess={addDocument} />
        </div>
        
        <div style={{ animationDelay: "0.3s" }} className="animate-fade-in">
          <DocumentList documents={documents} />
        </div>
      </div>
    </main>
  );
}
