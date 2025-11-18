const fs = require('fs');

const filePath = './Frontend_Core_Fundamentals.md';
let content = fs.readFileSync(filePath, 'utf8');

const lines = content.split('\n');
const result = [];
let openDetails = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  const nextLine = lines[i + 1] || '';
  
  // Track opening details
  if (line.includes('<details open>')) {
    openDetails++;
    result.push(line);
  }
  // Don't duplicate closing
  else if (line.includes('</details>')) {
    if (openDetails > 0) {
      result.push(line);
      openDetails--;
    }
  }
  // Before new question or section, close previous if needed
  else if (line.includes('### 📚 Q') && openDetails > 1) {
    result.push('</details>');
    result.push('');
    openDetails--;
    result.push(line);
  }
  // Before --- close if needed
  else if (line === '---' && openDetails > 0 && !nextLine.includes('<details')) {
    result.push('</details>');
    result.push('');
    openDetails--;
    result.push(line);
  }
  else {
    result.push(line);
  }
}

// Close any remaining
while (openDetails > 0) {
  result.push('</details>');
  openDetails--;
}

fs.writeFileSync(filePath, result.join('\n'), 'utf8');
console.log('✅ Fixed all closing tags!');
