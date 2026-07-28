"use client";

import { useState, useRef, useEffect } from "react";
import styles from "./ChatInterface.module.css";

interface Message {
  id: string;
  text: string;
  isUser: boolean;
}

export default function ChatInterface() {
  const [messages, setMessages] = useState<Message[]>([
    { id: "1", text: "Hello! I am your AI assistant. How can I help you with your documents today?", isUser: false }
  ]);
  const [inputValue, setInputValue] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSendMessage = async () => {
    if (!inputValue.trim()) return;

    const userMessage = {
      id: Date.now().toString(),
      text: inputValue,
      isUser: true,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInputValue("");
    setIsTyping(true);

    // Mock Chat API Call
    try {
      await new Promise((resolve) => setTimeout(resolve, 1200));
      const botResponse = {
        id: (Date.now() + 1).toString(),
        text: "I received your message. I'm currently a mockup, but soon I'll connect to the real Nutanix Chat API!",
        isUser: false,
      };
      setMessages((prev) => [...prev, botResponse]);
    } catch (error) {
      console.error("Chat error:", error);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className={`${styles.chatContainer} animate-fade-in`}>
      <div className={styles.chatHeader}>
        <div className={styles.statusIndicator}></div>
        AI Assistant
      </div>
      
      <div className={styles.messagesArea}>
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`${styles.message} ${msg.isUser ? styles.userMessage : styles.botMessage}`}
          >
            {msg.text}
          </div>
        ))}
        {isTyping && (
          <div className={`${styles.message} ${styles.botMessage}`}>
            <span className="typing-dots">Typing...</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className={styles.inputArea}>
        <input
          type="text"
          className={styles.input}
          placeholder="Ask something about your documents..."
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSendMessage()}
        />
        <button 
          className={styles.sendButton} 
          onClick={handleSendMessage}
          disabled={!inputValue.trim() || isTyping}
        >
          ➤
        </button>
      </div>
    </div>
  );
}
