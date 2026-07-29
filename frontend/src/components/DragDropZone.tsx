"use client";

import { useState } from "react";
import styles from "./DragDropZone.module.css";
import { Document } from "@/context/DocumentContext";

interface DragDropZoneProps {
  onUploadSuccess?: (document: Document) => void;
}

export default function DragDropZone({ onUploadSuccess }: DragDropZoneProps) {
  const [isDragActive, setIsDragActive] = useState(false);
  const [isUploading, setIsUploading] = useState(false);

  const handleDragEnter = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(true);
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(false);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const uploadFiles = async (files: FileList | File[]) => {
    setIsUploading(true);
    try {
      const formData = new FormData();
      const fileArray = Array.from(files);
      
      fileArray.forEach(file => {
        formData.append("files", file);
      });
      
      console.log("Uploading files to Documents API...", fileArray.map(f => f.name));
      
      const response = await fetch("/api/documents/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`Upload failed with status ${response.status}`);
      }

      const data = await response.json();
      
      if (data.success && onUploadSuccess) {
        fileArray.forEach(file => {
          if (data.uploaded_files.includes(file.name)) {
            const newDoc: Document = {
              id: Math.random().toString(36).substring(2, 11),
              name: file.name,
              size: file.size,
              type: file.type,
              uploadedAt: new Date().toISOString()
            };
            onUploadSuccess(newDoc);
          }
        });
      }
    } catch (error) {
      console.error("Upload failed", error);
    } finally {
      setIsUploading(false);
    }
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragActive(false);

    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      uploadFiles(e.dataTransfer.files);
    }
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      uploadFiles(e.target.files);
    }
  };

  return (
    <div
      className={`${styles.dropzone} ${isDragActive ? styles.active : ""} animate-fade-in`}
      onDragEnter={handleDragEnter}
      onDragLeave={handleDragLeave}
      onDragOver={handleDragOver}
      onDrop={handleDrop}
      onClick={() => document.getElementById("fileInput")?.click()}
    >
      <div className={styles.icon}>📁</div>
      <div className={styles.title}>
        {isUploading ? "Uploading..." : "Click or drag document to this area"}
      </div>
      <div className={styles.subtitle}>
        Supports PDF, PNG, JPG, and Word Documents
      </div>
      <input
        type="file"
        id="fileInput"
        style={{ display: "none" }}
        onChange={handleFileInput}
        accept=".pdf,.png,.jpg,.jpeg,.doc,.docx"
        multiple
      />
    </div>
  );
}
