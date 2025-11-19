const fs = require('fs');

const filePath = './Frontend_Core_Fundamentals.md';
let content = fs.readFileSync(filePath, 'utf8');

// Thêm CSS và JavaScript vào đầu file
const styleAndScript = `
<style>
.question-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.copy-question-btn {
  background: transparent;
  border: 1px solid #666;
  color: #666;
  padding: 4px 12px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 13px;
  margin-left: 10px;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  gap: 4px;
}
.copy-question-btn:hover {
  background: #f0f0f0;
  border-color: #333;
  color: #333;
}
.copy-question-btn.copied {
  background: #4CAF50;
  border-color: #4CAF50;
  color: white;
}
summary {
  list-style: none;
  cursor: pointer;
}
summary::-webkit-details-marker {
  display: none;
}
</style>

<script>
function copyQuestionContent(event, questionNumber) {
  event.preventDefault();
  event.stopPropagation();
  
  const btn = event.currentTarget;
  const details = btn.closest('details');
  if (!details) return;
  
  // Lấy nội dung text (loại bỏ HTML)
  let content = details.innerText || details.textContent;
  
  // Copy vào clipboard
  navigator.clipboard.writeText(content).then(() => {
    const icon = btn.querySelector('.copy-icon');
    const text = btn.querySelector('.copy-text');
    
    if (icon) icon.textContent = '✓';
    if (text) text.textContent = 'Copied!';
    btn.classList.add('copied');
    
    setTimeout(() => {
      if (icon) icon.textContent = '📋';
      if (text) text.textContent = 'Copy';
      btn.classList.remove('copied');
    }, 2000);
  }).catch(err => {
    console.error('Copy failed:', err);
  });
}
</script>
`;

// Tìm vị trí sau dòng "Phần sumary..."
const insertPosition = content.indexOf('> Phần sumary sẽ tóm tắt lại nội dung của câu hỏi');
if (insertPosition !== -1) {
  const endOfLine = content.indexOf('\n', insertPosition);
  content = content.slice(0, endOfLine + 1) + styleAndScript + content.slice(endOfLine + 1);
}

// Thêm nút copy cho từng câu hỏi
for (let i = 1; i <= 58; i++) {
  const pattern = new RegExp(
    `(<summary>\\s*<span style="font-size:1\\.25em;font-weight:bold;">(.*?Q${i}:.*?)</span>\\s*</summary>)`,
    'g'
  );
  
  content = content.replace(pattern, (match, fullMatch, questionTitle) => {
    return `<summary>
  <div class="question-header">
    <span style="font-size:1.25em;font-weight:bold;">${questionTitle}</span>
    <button class="copy-question-btn" onclick="copyQuestionContent(event, ${i})">
      <span class="copy-icon">📋</span>
      <span class="copy-text">Copy</span>
    </button>
  </div>
</summary>`;
  });
}

fs.writeFileSync(filePath, content, 'utf8');
console.log('✅ Added copy buttons to all 58 questions!');
