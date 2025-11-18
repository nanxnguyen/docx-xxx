const fs = require('fs');

const filePath = './Frontend_Core_Fundamentals.md';
let content = fs.readFileSync(filePath, 'utf8');

// Remove all standalone --- lines between details tags
content = content.replace(/<\/details>\s*\n+---\s*\n+<details>/g, '</details>\n\n<details>');

// Also remove --- that appears right after </details>
content = content.replace(/<\/details>\s*\n+---\s*\n+/g, '</details>\n\n');

fs.writeFileSync(filePath, content, 'utf8');
console.log('✅ Removed all --- separators between questions!');
