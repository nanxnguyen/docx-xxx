#!/usr/bin/env python3
"""
Script để thêm/chỉnh sửa phần TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF
sang TIẾNG VIỆT HOÀN TOÀN cho tất cả các câu hỏi.
"""

import os
import re
from pathlib import Path

# Mapping các thuật ngữ tiếng Anh sang tiếng Việt
TRANSLATIONS = {
    # General
    "vs": "vs",
    "performance": "hiệu năng",
    "optimization": "tối ưu",
    "best practices": "thực hành tốt nhất",
    "use case": "trường hợp sử dụng",
    "trade-off": "đánh đổi",
    "senior": "senior",
    "staff": "staff",
    
    # Technical terms (giữ nguyên hoặc có giải thích tiếng Việt)
    "async": "bất đồng bộ",
    "sync": "đồng bộ",
    "callback": "callback",
    "promise": "Promise",
    "DOM": "DOM",
    "API": "API",
    "HTTP": "HTTP",
    "cache": "cache",
    "state": "state",
    "props": "props",
    "hook": "hook",
}

def get_files_to_process():
    """Lấy danh sách tất cả các file Q*.md"""
    questions_dir = Path(__file__).parent
    return sorted(questions_dir.glob("Q*.md"))

def check_has_summary(content):
    """Kiểm tra xem file đã có phần TÓM TẮT chưa"""
    return "⭐ TÓM TẮT CHO PHỎNG VẤN" in content

def has_english_in_summary(content):
    """Kiểm tra xem phần tóm tắt có chứa tiếng Anh không"""
    if not check_has_summary(content):
        return False
    
    # Các từ tiếng Anh thường gặp trong tóm tắt
    english_patterns = [
        r'\b(use|using|when|with|for|and|the|is|are|vs|best|good|bad)\b',
        r'\b(trigger|handle|optimize|compare|implement|feature)\b',
        r'\b(expensive|cheaper|faster|slower)\b',
    ]
    
    # Lấy phần tóm tắt
    summary_match = re.search(
        r'## \*\*⭐ TÓM TẮT.*?\n\n---',
        content,
        re.DOTALL
    )
    
    if summary_match:
        summary = summary_match.group(0)
        for pattern in english_patterns:
            if re.search(pattern, summary, re.IGNORECASE):
                return True
    
    return False

def main():
    """Main function"""
    files = get_files_to_process()
    
    print(f"Tìm thấy {len(files)} file câu hỏi")
    print()
    
    stats = {
        "has_summary": [],
        "has_english": [],
        "no_summary": [],
        "already_vietnamese": []
    }
    
    for file_path in files:
        file_name = file_path.name
        content = file_path.read_text(encoding='utf-8')
        
        if not check_has_summary(content):
            stats["no_summary"].append(file_name)
        elif has_english_in_summary(content):
            stats["has_english"].append(file_name)
            stats["has_summary"].append(file_name)
        else:
            stats["already_vietnamese"].append(file_name)
            stats["has_summary"].append(file_name)
    
    print("📊 THỐNG KÊ:")
    print(f"✅ Đã có tóm tắt: {len(stats['has_summary'])} file")
    print(f"🔄 Cần dịch sang tiếng Việt: {len(stats['has_english'])} file")
    print(f"✨ Đã là tiếng Việt: {len(stats['already_vietnamese'])} file")
    print(f"❌ Chưa có tóm tắt: {len(stats['no_summary'])} file")
    print()
    
    if stats["has_english"]:
        print("🔄 CÁC FILE CẦN DỊCH SANG TIẾNG VIỆT:")
        for f in stats["has_english"]:
            print(f"   - {f}")
        print()
    
    if stats["no_summary"]:
        print("❌ CÁC FILE CHƯA CÓ TÓM TẮT:")
        for f in stats["no_summary"]:
            print(f"   - {f}")
        print()
    
    if stats["already_vietnamese"]:
        print(f"✨ {len(stats['already_vietnamese'])} file đã hoàn thành:")
        for f in stats["already_vietnamese"][:10]:  # Chỉ hiển thị 10 file đầu
            print(f"   - {f}")
        if len(stats["already_vietnamese"]) > 10:
            print(f"   ... và {len(stats['already_vietnamese']) - 10} file khác")

if __name__ == "__main__":
    main()
