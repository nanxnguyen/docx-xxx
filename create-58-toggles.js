const fs = require('fs');

const filePath = './Frontend_Core_Fundamentals.md';
let content = fs.readFileSync(filePath, 'utf8');

// First, find all 58 questions with their line positions
const lines = content.split('\n');
const questions = [];

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  // Match: ### **Q[number]: [title]**
  const match = line.match(/^###\s+\*\*(Q\d+):\s*(.+?)\*\*\s*$/);
  if (match) {
    const qNum = parseInt(match[1].substring(1));
    const title = match[2].trim();
    questions.push({
      num: qNum,
      fullTitle: `${match[1]}: ${title}`,
      lineIndex: i
    });
  }
}

console.log(`Found ${questions.length} questions`);

// Sort by question number
questions.sort((a, b) => a.num - b.num);

// Verify we have Q1-Q58
const missing = [];
for (let i = 1; i <= 58; i++) {
  if (!questions.find(q => q.num === i)) {
    missing.push(i);
  }
}

if (missing.length > 0) {
  console.log('❌ Missing questions:', missing.join(', '));
} else {
  console.log('✅ All 58 questions found!');
}

// Now convert: for each question, find its end (next ### **Q or ## ** or end of file)
const result = [];
let currentQuestionIndex = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  
  // Check if this line is a question start
  const isQuestionStart = questions.find(q => q.lineIndex === i);
  
  if (isQuestionStart) {
    // Close previous question if exists
    if (currentQuestionIndex > 0) {
      result.push('</details>');
      result.push('');
    }
    
    // Open new question
    result.push('<details open>');
    result.push('<summary>');
    result.push('');
    result.push(`### 📚 ${isQuestionStart.fullTitle}`);
    result.push('');
    result.push('</summary>');
    result.push('');
    
    currentQuestionIndex++;
  } else {
    result.push(line);
  }
}

// Close last question
if (currentQuestionIndex > 0) {
  result.push('');
  result.push('</details>');
}

fs.writeFileSync(filePath, result.join('\n'), 'utf8');
console.log(`✅ Created ${currentQuestionIndex} toggles!`);
console.log('Question numbers:', questions.map(q => `Q${q.num}`).join(', '));
