"use client";

import React, { createContext, useContext, useState, ReactNode } from "react";

export interface Document {
  id: string;
  name: string;
  size: number;
  type: string;
  uploadedAt: string;
}

interface DocumentContextType {
  documents: Document[];
  addDocument: (doc: Document) => void;
}

const DocumentContext = createContext<DocumentContextType | undefined>(undefined);

export function DocumentProvider({ children }: { children: ReactNode }) {
  const [documents, setDocuments] = useState<Document[]>([]);

  const addDocument = (doc: Document) => {
    setDocuments((prev) => [doc, ...prev]);
  };

  return (
    <DocumentContext.Provider value={{ documents, addDocument }}>
      {children}
    </DocumentContext.Provider>
  );
}

export function useDocuments() {
  const context = useContext(DocumentContext);
  if (context === undefined) {
    throw new Error("useDocuments must be used within a DocumentProvider");
  }
  return context;
}
