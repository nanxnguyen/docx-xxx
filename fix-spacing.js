const fs = require('fs');

const filePath = './Frontend_Core_Fundamentals.md';
let content = fs.readFileSync(filePath, 'utf8');

// Remove --- between </details> and <details>
// Pattern: </details>\n\n---\n\n<details>
// Replace with: </details>\n\n<details>

content = content.replace(/<\/details>\s*\n\s*---\s*\n\s*<details>/g, '</details>\n\n<details>');

fs.writeFileSync(filePath, content, 'utf8');
console.log('✅ Fixed spacing - removed all --- between questions!');
