"use client";

import styles from "./DocumentList.module.css";

interface Document {
  id: string;
  name: string;
  size: number;
  type: string;
  uploadedAt: string;
}

interface DocumentListProps {
  documents: Document[];
}

export default function DocumentList({ documents }: DocumentListProps) {
  const formatSize = (bytes: number) => {
    if (bytes === 0) return "0 B";
    const k = 1024;
    const sizes = ["B", "KB", "MB", "GB"];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + " " + sizes[i];
  };

  const getIcon = (type: string) => {
    if (type.includes("pdf")) return "📄";
    if (type.includes("image")) return "🖼️";
    if (type.includes("word") || type.includes("doc")) return "📝";
    return "📁";
  };

  return (
    <div className={`${styles.listContainer} animate-fade-in`}>
      <div className={styles.title}>
        Uploaded Documents
        <span className={styles.badge}>{documents.length}</span>
      </div>
      
      {documents.length === 0 ? (
        <div className={styles.emptyState}>
          No documents uploaded yet.
        </div>
      ) : (
        documents.map((doc) => (
          <div key={doc.id} className={styles.documentItem}>
            <div className={styles.docIcon}>{getIcon(doc.type)}</div>
            <div className={styles.docInfo}>
              <div className={styles.docName}>{doc.name}</div>
              <div className={styles.docMeta}>
                <span>{formatSize(doc.size)}</span>
                <span>•</span>
                <span>{new Date(doc.uploadedAt).toLocaleDateString()}</span>
              </div>
            </div>
            <button className="btn-secondary" style={{ padding: "6px 12px", fontSize: "0.85rem" }}>
              View
            </button>
          </div>
        ))
      )}
    </div>
  );
}
