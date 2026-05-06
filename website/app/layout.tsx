import type { Metadata } from 'next';
import './globals.css';
import { getMarkdownTree } from '../lib/markdown';
import OSWrapper from '../components/OSWrapper';

export const metadata: Metadata = {
  title: 'Automation Research Kit OS',
  description: 'Ancient to Modern AI Era Automation Knowledge Base',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // Read the directory structure for the sidebar (Server side only)
  const tree = getMarkdownTree();

  return (
    <html lang="en">
      <body>
        <OSWrapper tree={tree}>
          {children}
        </OSWrapper>
      </body>
    </html>
  );
}
