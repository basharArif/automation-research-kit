import fs from 'fs';
import path from 'path';
import { getMarkdownContent } from '../lib/markdown';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import Link from 'next/link';

export default function HomePage() {
  // Try to load README.md for the home page if it exists
  const readmeData = getMarkdownContent(['README']);
  
  if (readmeData) {
    return (
      <div className="markdown-container">
        <ReactMarkdown remarkPlugins={[remarkGfm]}>
          {readmeData.content}
        </ReactMarkdown>
      </div>
    );
  }

  // Fallback Welcome Screen
  return (
    <div className="welcome-screen">
      <div className="welcome-logo">⚛</div>
      <h1 className="welcome-title">ARK_OS // INITIALIZED</h1>
      <p className="welcome-desc">
        Welcome to the Automation Research Kit Knowledge Base.
        <br/><br/>
        Navigate the core memory banks via the terminal sidebar.
        <br/>
        System status: OPTIMAL.
      </p>
    </div>
  );
}
