'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

function TreeView({ data, level = 0, onNavClick }: { data: any[], level?: number, onNavClick: () => void }) {
  const pathname = usePathname();

  if (!data || data.length === 0) return null;

  return (
    <ul className="nav-list" style={{ marginLeft: level > 0 ? '0.5rem' : '0' }}>
      {data.map((item) => (
        <li key={item.path} className="nav-item">
          {item.type === 'directory' ? (
            <>
              <div className="nav-dir">{item.name.replace(/_/g, ' ')}</div>
              <TreeView data={item.children} level={level + 1} onNavClick={onNavClick} />
            </>
          ) : (
            <Link 
              href={`/${item.path}`} 
              className={`nav-link nav-link-file ${pathname === `/${item.path}` ? 'active' : ''}`}
              onClick={onNavClick}
            >
              {item.name.replace(/\.md$/, '').replace(/_/g, ' ')}
            </Link>
          )}
        </li>
      ))}
    </ul>
  );
}

export default function OSWrapper({ children, tree }: { children: React.ReactNode, tree: any[] }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const closeSidebar = () => setIsSidebarOpen(false);
  const toggleSidebar = () => setIsSidebarOpen(!isSidebarOpen);

  return (
    <div className="os-container">
      {/* Left Sidebar (Ancient Terminal Vibe) */}
      <aside className={`os-sidebar ${isSidebarOpen ? 'open' : ''}`}>
        <div className="os-sidebar-header">
          <span>SYS_NAV // ARK_OS</span>
          <button className="sidebar-close-btn" onClick={closeSidebar}>[X]</button>
        </div>
        <div className="os-sidebar-content">
          <TreeView data={tree} onNavClick={closeSidebar} />
        </div>
      </aside>

      {/* Main Workspace (Modern AI Vibe) */}
      <main className="os-main">
        <div className="os-topbar-glow"></div>
        <header className="os-topbar">
          <div style={{ display: 'flex', alignItems: 'center' }}>
            <button className="mobile-toggle" onClick={toggleSidebar}>
              ☰
            </button>
            <span className="os-topbar-title">AUTOMATION_RESEARCH_KIT</span>
          </div>
          <div className="os-topbar-status">STATUS: ONLINE // AI_ASSISTANT: ACTIVE</div>
        </header>
        <div className="os-content-scroll">
          {children}
        </div>
      </main>
    </div>
  );
}
