import { getMarkdownContent, getMarkdownTree } from '../../lib/markdown';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  const tree = getMarkdownTree();
  const paths: { slug: string[] }[] = [];

  function extractPaths(nodes: any[]) {
    for (const node of nodes) {
      if (node.type === 'file') {
        paths.push({ slug: node.path.split('/') });
      } else if (node.type === 'directory' && node.children) {
        extractPaths(node.children);
      }
    }
  }

  extractPaths(tree);
  return paths;
}

export default async function MarkdownPage({ params }: { params: Promise<{ slug: string[] }> }) {
  const { slug } = await params;
  const data = getMarkdownContent(slug);

  if (!data) {
    notFound();
  }

  return (
    <div className="markdown-container">
      <ReactMarkdown remarkPlugins={[remarkGfm]}>
        {data.content}
      </ReactMarkdown>
    </div>
  );
}
