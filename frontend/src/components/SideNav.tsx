"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function SideNav() {
  const pathname = usePathname();

  return (
    <nav className="side-nav">
      <div>
        <div className="nav-brand">Nutanix RAG</div>
        <div className="nav-links" style={{ marginTop: "32px" }}>
          <Link 
            href="/" 
            className={`nav-link ${pathname === "/" ? "active" : ""}`}
          >
            Chat
          </Link>
          <Link 
            href="/documents" 
            className={`nav-link ${pathname === "/documents" ? "active" : ""}`}
          >
            Documents
          </Link>
        </div>
      </div>
    </nav>
  );
}
