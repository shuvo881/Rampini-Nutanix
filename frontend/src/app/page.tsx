"use client";

import ChatInterface from "@/components/ChatInterface";

export default function ChatPage() {
  return (
    <main style={{ height: "100%", padding: "32px", maxWidth: "1200px", margin: "0 auto" }}>
      <div style={{ height: "100%" }}>
        <ChatInterface />
      </div>
    </main>
  );
}
