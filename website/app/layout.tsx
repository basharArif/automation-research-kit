import type { Metadata } from 'next';
import './globals.css';
import { getMarkdownTree } from '../lib/markdown';
import Link from 'next/link';

export const metadata: Metadata = {
  title: 'Automation Research Kit OS',
  description: 'Ancient to Modern AI Era Automation Knowledge Base',
};

// Recursive component to render the file tree
function TreeView({ data, level = 0 }: { data: any[], level?: number }) {
  if (!data || data.length === 0) return null;

  return (
    <ul className="nav-list" style={{ marginLeft: level > 0 ? '1rem' : '0' }}>
      {data.map((item) => (
        <li key={item.path} className="nav-item">
          {item.type === 'directory' ? (
            <>
              <div className="nav-dir">{item.name.replace(/_/g, ' ')}</div>
              <TreeView data={item.children} level={level + 1} />
            </>
          ) : (
            <Link href={`/${item.path}`} className="nav-link nav-link-file">
              {item.name.replace(/\.md$/, '').replace(/_/g, ' ')}
            </Link>
          )}
        </li>
      ))}
    </ul>
  );
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // Read the directory structure for the sidebar
  const tree = getMarkdownTree();

  return (
    <html lang="en">
      <body>
        <div className="os-container">
          {/* Left Sidebar (Ancient Terminal Vibe) */}
          <aside className="os-sidebar">
            <div className="os-sidebar-header">
              SYS_NAV // ARK_OS
            </div>
            <div className="os-sidebar-content">
              <TreeView data={tree} />
            </div>
          </aside>

          {/* Main Workspace (Modern AI Vibe) */}
          <main className="os-main">
            <div className="os-topbar-glow"></div>
            <header className="os-topbar">
              <div>AUTOMATION_RESEARCH_KIT // KNOWLEDGE_BASE</div>
              <div>STATUS: ONLINE // AI_ASSISTANT: ACTIVE</div>
            </header>
            <div className="os-content-scroll">
              {children}
            </div>
          </main>
        </div>
      </body>
    </html>
  );
}
