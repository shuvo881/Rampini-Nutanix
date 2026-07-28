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

  const uploadFile = async (file: File) => {
    setIsUploading(true);
    // Mock API integration
    try {
      console.log("Uploading file to Documents API...", file.name);
      // Simulate network request
      await new Promise((resolve) => setTimeout(resolve, 1500));
      
      const newDoc: Document = {
        id: Math.random().toString(36).substr(2, 9),
        name: file.name,
        size: file.size,
        type: file.type,
        uploadedAt: new Date().toISOString()
      };
      
      if (onUploadSuccess) {
        onUploadSuccess(newDoc);
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
      const file = e.dataTransfer.files[0];
      uploadFile(file);
    }
  };

  const handleFileInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      uploadFile(e.target.files[0]);
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
      />
    </div>
  );
}
