import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';

const rootDirectory = path.join(process.cwd(), '..');

// Get a list of all markdown files recursively, returning a tree structure for the sidebar
export function getMarkdownTree(dir = rootDirectory) {
  const items = fs.readdirSync(dir, { withFileTypes: true });
  
  const tree = [];
  
  for (const item of items) {
    // Ignore internal folders and non-markdown files (unless directory)
    if (['.git', 'node_modules', '.next', 'public', 'app', 'lib', 'website'].includes(item.name) || item.name.startsWith('.')) continue;

    const fullPath = path.join(dir, item.name);
    
    if (item.isDirectory()) {
      const children = getMarkdownTree(fullPath);
      if (children.length > 0) {
        tree.push({
          type: 'directory',
          name: item.name,
          path: path.relative(rootDirectory, fullPath),
          children,
        });
      }
    } else if (item.name.endsWith('.md')) {
      tree.push({
        type: 'file',
        name: item.name,
        path: path.relative(rootDirectory, fullPath).replace(/\.md$/, ''),
      });
    }
  }

  // Sort: directories first, then files, alphabetically
  return tree.sort((a, b) => {
    if (a.type !== b.type) return a.type === 'directory' ? -1 : 1;
    return a.name.localeCompare(b.name);
  });
}

// Get the content of a specific markdown file by its slug
export function getMarkdownContent(slugParts: string[]) {
  const relPath = path.join(...slugParts) + '.md';
  const fullPath = path.join(rootDirectory, relPath);

  if (!fs.existsSync(fullPath)) {
    return null;
  }

  const fileContents = fs.readFileSync(fullPath, 'utf8');
  // Use gray-matter in case there is frontmatter, though standard markdown will just have content
  const { data, content } = matter(fileContents);
  
  // Extract title from first heading if not in frontmatter
  let title = data.title;
  if (!title) {
    const headingMatch = content.match(/^#\s+(.+)$/m);
    title = headingMatch ? headingMatch[1] : path.basename(relPath, '.md');
  }

  return { content, title };
}
