#!/bin/bash

# =====================================
# MARKDOWN TO DOCX CONVERTER
# With Beautiful Formatting
# =====================================

INPUT_FILE="JavaScript_Core_Fundamentals.md"
OUTPUT_DIR="."

echo "🔄 Converting Markdown to DOCX..."

# 1. Basic version
pandoc "$INPUT_FILE" \
  -o "${OUTPUT_DIR}/JavaScript_Core_Fundamentals.docx" \
  --toc \
  --toc-depth=3 \
  --syntax-highlighting tango

echo "✅ Created: JavaScript_Core_Fundamentals.docx"

# 2. Formatted version (RECOMMENDED)
pandoc "$INPUT_FILE" \
  -o "${OUTPUT_DIR}/JavaScript_Core_Fundamentals_Formatted.docx" \
  --toc \
  --toc-depth=4 \
  --syntax-highlighting tango \
  --number-sections \
  --standalone

echo "✅ Created: JavaScript_Core_Fundamentals_Formatted.docx"

# 3. Professional version (with metadata)
pandoc "$INPUT_FILE" \
  -o "${OUTPUT_DIR}/JavaScript_Core_Fundamentals_Professional.docx" \
  --toc \
  --toc-depth=4 \
  --syntax-highlighting tango \
  --number-sections \
  --standalone \
  --metadata title="JavaScript Core Fundamentals - Comprehensive Guide" \
  --metadata author="Technical Documentation" \
  --metadata date="$(date '+%B %d, %Y')"

echo "✅ Created: JavaScript_Core_Fundamentals_Professional.docx"

# 4. PDF version (requires LaTeX)
if command -v pdflatex &> /dev/null; then
  pandoc "$INPUT_FILE" \
    -o "${OUTPUT_DIR}/JavaScript_Core_Fundamentals.pdf" \
    --toc \
    --toc-depth=4 \
    --syntax-highlighting tango \
    --number-sections \
    --pdf-engine=pdflatex
  
  echo "✅ Created: JavaScript_Core_Fundamentals.pdf"
else
  echo "⚠️  Skipped PDF (pdflatex not installed)"
fi

echo ""
echo "🎉 Conversion complete!"
echo ""
echo "📄 Files created:"
ls -lh "${OUTPUT_DIR}"/*.docx
