# Hướng dẫn thành thạo Claude Code

## 0. Hiểu khái niệm cơ bản trước (đọc trước khi đi sâu)

Trước khi vào lệnh và tính năng, hiểu 5 khái niệm này thì mọi thứ khác sẽ dễ hiểu.

### 0.1 Claude Code hoạt động như thế nào? — Analogy nhà hàng

Hãy tưởng tượng Claude Code là **một đầu bếp giỏi nhưng có trí nhớ ngắn hạn**:

- Mỗi lần bạn order món (gửi prompt), đầu bếp phải **đọc lại toàn bộ thực đơn + sổ tay quán + lịch sử order từ đầu ca** rồi mới nấu.
- Quán có **bảng menu cố định** (system prompt) — đầu bếp thuộc lòng, không phải đọc lại.
- Mỗi món bạn order = thêm 1 dòng vào lịch sử → lần sau đầu bếp lại đọc cả lịch sử đó.
- Cuối ca, đầu bếp **quên sạch** (trừ khi bạn ghi vào sổ tay quán = CLAUDE.md).

→ Từ đó suy ra:
- Order càng nhiều → đầu bếp đọc càng lâu, tốn càng nhiều "công sức" (token).
- `/clear` = xé tờ giấy lịch sử order, bắt đầu lại.
- CLAUDE.md = sổ tay quán, đầu bếp đọc mỗi lần nấu món mới.

### 0.2 "Token" là gì? — Đơn vị đo "chữ"

- **Token** ≈ **âm tiết / mảnh chữ**. Tiếng Việt có dấu nên 1 chữ ≈ 2-3 token. Tiếng Anh 1 từ ≈ 1-2 token.
- Bạn **trả tiền theo token** (input + output).
- Mỗi request gửi đi: nhiều token vào (context) + ít token ra (Claude trả lời).
- → **Càng ít token vào, càng rẻ + càng nhanh.**

### 0.3 "Context" là gì? — Bộ nhớ ngắn hạn của Claude

Context = **toàn bộ thông tin Claude "nhìn thấy"** trong 1 lượt:
- System prompt (instructions + tools + CLAUDE.md)
- Lịch sử conversation (tất cả turn trước)
- File bạn vừa cho đọc
- Tag IDE (file đang mở, vùng chọn)

Context có **giới hạn** (Opus 4.7: ~200k token). Khi gần đầy → phải `/compact` hoặc `/clear`.

### 0.4 "Cache" là gì? — Tại sao quan trọng?

Anthropic có **prompt cache TTL 5 phút**: nếu phần đầu của prompt không đổi, lần sau dùng lại sẽ:
- Rẻ hơn ~10 lần
- Nhanh hơn ~2 lần

→ **System prompt + CLAUDE.md** nằm trong phần được cache. Nếu bạn **sửa CLAUDE.md giữa phiên** = phá cache = lượt sau đắt + chậm.

### 0.5 Sơ đồ tổng quan — Claude Code có gì?

```
┌─────────────────────────────────────────────────────────┐
│                    CLAUDE CODE                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   📝 MEMORY        ⚙️ SETTINGS       🔌 MCP            │
│   (CLAUDE.md)      (permissions,     (Playwright,       │
│                     hooks)            Figma, …)         │
│                                                         │
│   📂 COMMANDS      🤖 AGENTS         🛠️ SKILLS         │
│   (/deploy,        (Explore,         (vercel:deploy,    │
│    /review)         code-reviewer)    figma:use)        │
│                                                         │
│   🪝 HOOKS — code shell chạy tự động ở các thời điểm   │
│                                                         │
└─────────────────────────────────────────────────────────┘
                          ▼
                  Mọi thứ trên gộp thành
                  SYSTEM PROMPT gửi lên API
```

**Phân biệt nhanh:**

| Khái niệm | Là gì? | Khi nào load? |
|-----------|--------|---------------|
| **Memory (CLAUDE.md)** | Sổ tay convention dự án | Mỗi prompt — luôn vào context |
| **Settings** | Cấu hình hành vi (permissions, hooks) | Lúc start — không vào context |
| **MCP** | Tool ngoài (Figma, Playwright) | Lúc start — tool definitions vào context |
| **Commands** (`/xyz`) | Macro user gõ tay | Chỉ load khi user gõ |
| **Agents** | Claude phụ với context riêng | Chỉ load khi triệu hồi |
| **Skills** | Hướng dẫn "làm việc X như nào" | Claude tự load khi cần |
| **Hooks** | Script shell tự chạy ở event | Không load — chạy ngầm |

> 💡 **Phân biệt Skill vs Agent**: Skill như "đọc cuốn sách hướng dẫn" — Claude vẫn là Claude, học thêm cách làm. Agent như "nhờ đồng nghiệp khác làm hộ" — người khác làm, trả về kết quả tóm tắt.

---

## 1. Tất cả Slash Commands (lệnh trong phiên chat)

### Quản lý phiên & ngữ cảnh
| Lệnh | Công dụng |
|------|-----------|
| `/clear` | Xoá toàn bộ context — dùng khi chuyển sang task khác (tiết kiệm token nhiều nhất) |
| `/compact [hướng dẫn]` | Tóm tắt context cũ, giữ phần quan trọng. Có thể thêm hướng dẫn: `/compact tập trung phần API` |
| `/resume` hoặc `claude -r` | Mở lại session cũ |
| `/continue` hoặc `claude -c` | Tiếp tục session gần nhất |
| `/export` | Xuất conversation ra file |
| `/cost` | Xem token và chi phí đã dùng trong session |

### Cấu hình & môi trường
| Lệnh | Công dụng |
|------|-----------|
| `/config` | Mở UI cấu hình (theme, model, editor…) |
| `/model` | Đổi model (Opus/Sonnet/Haiku) — Haiku rẻ nhất |
| `/permissions` | Quản lý tool nào auto-allow, deny |
| `/hooks` | Cấu hình hooks (script tự động chạy khi có event) |
| `/add-dir` | Thêm thư mục làm việc (ngoài cwd) |
| `/ide` | Kết nối VSCode/JetBrains |
| `/terminal-setup` | Setup phím tắt terminal (Shift+Enter cho xuống dòng) |
| `/vim` | Bật/tắt vim mode |

### Memory & dự án
| Lệnh | Công dụng |
|------|-----------|
| `/init` | Tạo file `CLAUDE.md` từ codebase hiện tại |
| `/memory` | Mở editor sửa các file CLAUDE.md (project + global) |
| `#` (tiền tố) | Lưu nhanh một dòng vào memory: `# Luôn dùng yarn thay vì npm` |

### Subagents, MCP, Skills
| Lệnh | Công dụng |
|------|-----------|
| `/agents` | Quản lý subagents (tạo, sửa, xoá agent chuyên biệt) |
| `/mcp` | Quản lý MCP servers (Playwright, Figma, Serena…) |
| `/help` | Danh sách lệnh |

### Tài khoản & hệ thống
| Lệnh | Công dụng |
|------|-----------|
| `/login` `/logout` | Đăng nhập Anthropic |
| `/status` | Trạng thái auth, model, MCP |
| `/doctor` | Chẩn đoán cài đặt, kiểm tra môi trường |
| `/upgrade` | Nâng cấp gói (Pro/Max) |
| `/release-notes` | Xem changelog |
| `/bug` | Báo bug |
| `/install-github-app` | Cài app cho `@claude` trong PR |

### Git / PR
| Lệnh | Công dụng |
|------|-----------|
| `/review` | Review PR hiện tại |
| `/pr-comments` | Xem comment trong PR |
| `/security-review` | Quét bảo mật code đang sửa |

### Custom commands (của bạn / plugin)
Trong dự án này có sẵn rất nhiều skill, ví dụ: `/vercel:deploy`, `/vercel:env`, `/feature-dev:feature-dev`, `/code-review:code-review`, `/loop`, `/schedule`, `/simplify`, `/fewer-permission-prompts`…

Tạo custom command: đặt file Markdown trong `.claude/commands/` — tên file = tên lệnh.

---

## 2. CLI commands (chạy ngoài terminal)

```bash
claude                          # Mở phiên tương tác
claude -p "câu hỏi"             # Print mode: hỏi 1 lần, in kết quả, thoát (script-friendly)
claude -p "..." --output-format json
claude -c                       # Continue session gần nhất
claude -r                       # Resume — chọn từ list
claude --model sonnet           # Chỉ định model
claude --permission-mode plan   # Khởi động ở plan mode (read-only)
claude --dangerously-skip-permissions   # Bỏ confirm (nguy hiểm, chỉ dùng trong sandbox)
claude config                   # Cấu hình từ CLI
claude mcp add <name> <cmd>     # Thêm MCP server
claude update                   # Update Claude Code
claude doctor                   # Chẩn đoán
```

---

## 3. Cách dùng tiết kiệm token (quan trọng nhất)

### Hiểu đơn giản: Tại sao phải tiết kiệm token?

Tưởng tượng mỗi lượt nói chuyện với Claude = **gọi grab**. Càng đi xa = càng đắt. **Token = quãng đường.**

- Bạn vẫn cần đi → không tránh được.
- Nhưng đừng đi vòng vèo: gõ "ok" rồi đợi cũng tốn tiền như gõ 1 câu hỏi đầy đủ.
- Đi đúng địa chỉ (đường dẫn file cụ thể) → tài xế không phải hỏi đường.

### Quy tắc vàng
1. **`/clear` thường xuyên** — chuyển task khác → clear. Context dài = token vào prompt tăng tuyến tính mỗi lượt.
2. **`/compact` khi >50% context** — giữ phần cần, vứt phần thừa.
3. **Chọn model đúng việc**:
   - Haiku 4.5: việc đơn giản, rename, edit nhỏ (rẻ ~1/10 Opus)
   - Sonnet 4.6: mặc định, cân bằng
   - Opus 4.7: kiến trúc, debug khó, refactor lớn
4. **Đưa đường dẫn cụ thể** thay vì "tìm file xử lý order" → Claude phải grep/đọc nhiều file (tốn token). Ví dụ tốt: "sửa hàm `placeOrder` trong `apps/hsc-one/src/services/order.ts`"
5. **Dùng `@file` reference** — gõ `@` để chèn file path, Claude đọc đúng file, không đoán.
6. **Plan Mode (Shift+Tab 2 lần)** — Claude lên kế hoạch trước khi sửa code → tránh đi sai hướng rồi sửa lại.
7. **Subagent cho việc tìm kiếm rộng** — agent `Explore` tìm xong trả về tóm tắt ~500 token, thay vì 20k token đọc file đổ vào context chính.
8. **CLAUDE.md gọn** — đừng nhét cả tài liệu vào. Chỉ ghi convention, lệnh hay dùng, kiến trúc cốt lõi. File này load **mỗi prompt**.
9. **Tránh ping-pong vô nghĩa**: "ok", "tiếp tục", "đúng rồi" — mỗi lượt là 1 round trip qua toàn bộ context.
10. **`-p` mode cho task lẻ** — `claude -p "viết test cho file X"` không lưu session, không tích luỹ context.

### Anti-pattern (tốn token)
- Hỏi "kiểm tra lại đi" sau mỗi sửa đổi → Claude đọc lại file
- Để session chạy cả ngày, làm 5 task khác nhau không clear
- "Hãy thám hiểm codebase và cho tôi biết về dự án" — đốt 50k+ token. Thay vào đó: `/init` 1 lần, lưu vào CLAUDE.md.
- Copy paste đoạn lỗi siêu dài — paste phần liên quan thôi

### Mẹo nâng cao về cache
- Anthropic prompt cache có TTL **5 phút**. Nếu bạn rời máy >5 phút rồi quay lại, lượt đầu sẽ "cache miss" (chậm + đắt hơn).
- → Làm việc dồn dập trong khoảng cache, hơn là rải rác.
- CLAUDE.md, system prompt, MCP tool definitions đều nằm trong phần được cache → đừng sửa CLAUDE.md liên tục giữa các lượt (vỡ cache).

---

## 4. Tính năng quan trọng khác cần nắm

### 4.1 Memory hệ thống (3 cấp)
- `~/.claude/CLAUDE.md` — global, dùng mọi project
- `<project>/CLAUDE.md` — project, commit vào repo
- `<project>/CLAUDE.local.md` — local, không commit (gitignore)

Thứ tự ưu tiên: local > project > global. Cấp dưới ghi đè cấp trên.

### 4.2 Plan Mode
- Phím tắt: **Shift+Tab** để cycle qua các permission mode
- Plan mode: chỉ đọc, không sửa → an toàn để brainstorm
- Khi xong, Claude trình bày kế hoạch và xin phép mới thực thi
- Dùng khi: task lớn, không chắc cách làm, muốn review trước khi code

### 4.3 Hooks (`/hooks`)

**Hiểu đơn giản**: Hook = **đặt camera/báo động tự động** ở các thời điểm cố định. Bạn cài đặt 1 lần, nó chạy mãi mãi mà không cần nhờ Claude.

Ví dụ: "Mỗi lần Claude sửa file `.ts`, tự động chạy `prettier`" — Claude không thể quên vì đây là hook chạy ngầm.

Cấu hình trong `.claude/settings.json`:
- `PreToolUse` / `PostToolUse` — chạy script trước/sau khi gọi tool
- `SessionStart` — chạy khi mở session
- `UserPromptSubmit` — chặn/sửa prompt người dùng
- `Stop` — chạy khi Claude kết thúc lượt
- `Notification` — chạy khi có notification

Ví dụ hữu ích:
- Tự `npm run lint` sau khi edit file `.ts`
- Block commit nếu có `console.log`
- Inject context project mỗi khi mở session
- Beep/notify khi Claude hỏi permission

Ví dụ settings.json:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{ "type": "command", "command": "npm run lint --silent" }]
    }]
  }
}
```

### 4.4 Subagents (`/agents`)

**Hiểu đơn giản**: Subagent = **nhờ đồng nghiệp khác làm hộ rồi báo cáo lại**. Bạn (main Claude) không phải tự đọc 20 file — đồng nghiệp đọc rồi đưa tóm tắt 1 trang.

- Agent có **context riêng** — không "dính" vào main session. Đồng nghiệp ngồi phòng khác, không nghe được cuộc nói chuyện của bạn với sếp.
- Có sẵn: `Explore`, `Plan`, `feature-dev:code-architect`, `pr-review-toolkit:*`, `vercel:*`…
- Tạo agent custom: file `.md` trong `.claude/agents/` với frontmatter

**Khi nào dùng?**
| Tình huống | Lý do |
|-----------|-------|
| Tìm "hàm xử lý thanh toán ở đâu?" trong dự án 500 file | Explore agent đọc rộng, trả về tóm tắt — main context không nặng |
| Review code độc lập | Agent không biết bạn đã thử cách nào → góc nhìn fresh |
| Cần làm 3 việc song song | Spawn 3 agent cùng lúc → nhanh hơn làm tuần tự |

**Khi không nên?**
- Việc nhỏ, đã biết file cần sửa → tốn token "khởi động" agent
- Việc cần context của session chính (vd "sửa tiếp đoạn vừa rồi")

### 4.5 MCP servers

**Hiểu đơn giản**: Mặc định Claude Code biết Read/Edit/Bash file. MCP = **đeo thêm dụng cụ ngoài cho Claude** — như cài app cho điện thoại.

- Muốn Claude điều khiển browser? → Cài MCP Playwright.
- Muốn Claude đọc/sửa Figma? → Cài MCP Figma.
- Muốn Claude tra docs library? → Cài MCP Context7.

Mỗi MCP server = 1 process chạy riêng, expose 1 bộ tool qua giao thức chuẩn (JSON-RPC).

Cách thêm:
```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Hoặc cấu hình trong `.mcp.json` (commit vào repo để team dùng chung).

> ⚠️ Mỗi MCP server thêm vào = thêm tool definitions vào system prompt = tốn token mỗi prompt. Chỉ cài cái bạn dùng.

### 4.6 Skills

**Hiểu đơn giản**: Skill = **cuốn sách hướng dẫn "làm việc X như thế nào"**. Claude tự đọc khi cần, vẫn là Claude (cùng context), không phải nhờ ai khác.

So sánh với Subagent (rất dễ nhầm):

| | Skill | Subagent |
|---|-------|----------|
| **Là gì?** | Sách hướng dẫn | Đồng nghiệp khác |
| **Context** | Cùng với main Claude | Riêng, không thấy main |
| **Trigger** | Tự động khi liên quan | Phải gọi rõ qua `Agent` tool |
| **Output** | Claude làm việc luôn theo guide | Trả về 1 message tóm tắt |
| **Dùng khi** | Cần hướng dẫn quy trình | Cần ai đó làm 1 task riêng biệt |

- Đặt trong `.claude/skills/<tên>/SKILL.md`
- Có frontmatter `description` để Claude biết khi nào trigger
- Ví dụ trong dự án này: `vercel:deploy`, `figma:figma-use`, `code-review:code-review`

### 4.7 Permission modes
- **default**: hỏi trước khi chạy tool nguy hiểm
- **acceptEdits**: tự duyệt edit file (vẫn hỏi bash)
- **plan**: chỉ đọc, không sửa
- **bypassPermissions**: không hỏi gì (nguy hiểm, chỉ sandbox/CI)

Đổi nhanh: **Shift+Tab** trong session.

### 4.8 Background tasks
Lệnh dài (build, test, dev server) → chạy background, Claude nhận thông báo khi xong → không block input.

Cú pháp trong prompt: "chạy build trong background rồi tiếp tục viết test"

### 4.9 IDE integration
Trong VSCode/JetBrains extension:
- Claude thấy file đang mở, vùng đang chọn (`<ide_selection>`)
- Khi nói "fix đoạn này" mà có selection → Claude hiểu ngay
- Diff hiển thị trong IDE native, không phải terminal
- File references dạng `[file.ts:42](src/file.ts#L42)` click được

### 4.10 Phím tắt input
| Phím | Tác dụng |
|------|----------|
| `Shift+Enter` | Xuống dòng (sau khi `/terminal-setup`) |
| `Ctrl+J` | Xuống dòng (luôn hoạt động) |
| `Ctrl+R` | Xem transcript dài |
| `Esc` | Ngắt Claude đang làm |
| `Esc Esc` | Rewind — quay lại lượt trước |
| `@` | Chèn file reference |
| `!` | Chạy bash inline (không qua Claude) |
| `#` | Lưu nhanh memory |
| `Shift+Tab` | Cycle permission mode |
| `Ctrl+C` | Thoát session |

### 4.11 Worktree
Cho phép Claude làm việc trên copy branch riêng, không ảnh hưởng working dir hiện tại. Dùng cho:
- Agent isolation (chạy agent thử nghiệm mà không sợ phá repo)
- Thử nhiều cách giải song song
- Code review độc lập

### 4.12 Headless mode (CI/automation)
```bash
# Trong CI script
claude -p "review PR diff và comment vào GitHub" --output-format json

# Loop với schedule
claude -p "check trạng thái deploy mỗi 5 phút"
```

### 4.13 Resume & session storage
- Session lưu trong `~/.claude/projects/<project-hash>/`
- Mỗi session = 1 file JSONL chứa toàn bộ lịch sử
- `claude -r` cho phép chọn session cụ thể để mở lại
- Có thể xoá session cũ để giải phóng disk

---

## 5. Lifecycle của Claude Code — Chuyện gì xảy ra khi bạn gõ `claude`?

### Hiểu đơn giản trước

Tưởng tượng bạn vào một **văn phòng ảo** — Claude Code là vòng đời của văn phòng đó:

1. **Mở cửa văn phòng** (`claude` start) — bật đèn, lấy sổ tay, gọi đối tác (MCP), dán note lên tường (CLAUDE.md), kiểm tra danh bạ liên lạc (commands/agents/skills).
2. **Bạn đến gặp Claude** (user prompt) — đặt câu hỏi.
3. **Claude làm việc** — đọc note, dùng tool, có thể nhờ đồng nghiệp (subagent), trả lời bạn.
4. **Bạn đi về hoặc hỏi tiếp** — lặp lại bước 2-3.
5. **Đóng cửa văn phòng** (exit/Ctrl+C) — lưu lịch sử, tắt đối tác.

**Hooks** = camera + báo động tự động ở văn phòng: bạn cài đặt sẵn, chạy không cần Claude can thiệp.
- Có camera trước cửa (`SessionStart`) chụp ảnh ai vào.
- Có cảm biến tay nắm (`PreToolUse`) cảnh báo trước khi mở két.
- Có chuông khi đóng cửa (`SessionEnd`).

Đó là tất cả. Phần dưới chỉ là chi tiết của analogy này.

---

### 5.1 Toàn cảnh vòng đời 1 session

```
┌─────────────────────────────────────────────────────────────────┐
│                       SESSION START                              │
│  1. CLI parse args (--model, --permission-mode, -c, -r, …)      │
│  2. Load settings (global → project → local override)           │
│  3. Khởi động MCP servers (spawn process, handshake)            │
│  4. Load memory files (CLAUDE.md hierarchy)                     │
│  5. Quét registry: commands/, agents/, skills/                  │
│  6. Fire hook: SessionStart                                     │
│  7. Build system prompt (gộp tất cả trên + tool definitions)    │
│  8. Hiển thị prompt chờ user input                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       USER TURN                                  │
│  9. User gõ prompt + Enter                                      │
│  10. Fire hook: UserPromptSubmit (có thể chặn/sửa prompt)       │
│  11. Gửi request lên Anthropic API                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       ASSISTANT TURN (lặp lại)                   │
│  12. Claude sinh text + tool calls                              │
│  13. Với mỗi tool call:                                         │
│      a. Fire hook: PreToolUse (có thể block / sửa input)        │
│      b. Check permissions (allow/deny/ask)                      │
│      c. Thực thi tool                                           │
│      d. Fire hook: PostToolUse (có thể inject result)           │
│  14. Nếu Claude cần input → Fire hook: Notification              │
│  15. Khi Claude xong lượt → Fire hook: Stop                     │
│  16. Nếu là subagent → Fire hook: SubagentStop                  │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
                       (lặp về USER TURN)
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       CONTEXT MANAGEMENT                         │
│  • Khi context gần đầy → auto compact                           │
│  • Trước khi compact → Fire hook: PreCompact                    │
│  • User gõ /clear → reset hoàn toàn                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       SESSION END                                │
│  • User Ctrl+C / exit / kill MCP processes                      │
│  • Fire hook: SessionEnd                                        │
│  • Lưu transcript JSONL → ~/.claude/projects/<hash>/            │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Thứ tự load file khi `SessionStart`

Hiểu rõ thứ tự này giúp bạn debug "tại sao Claude không thấy convention X?" hoặc "tại sao tool Y bị block?".

#### Bước 1 — Settings (cấu hình)
Load theo thứ tự, file sau **ghi đè** file trước:
1. `~/.claude/settings.json` — user global
2. `<project>/.claude/settings.json` — project (commit vào repo)
3. `<project>/.claude/settings.local.json` — local override (gitignore)
4. Enterprise/managed policy (nếu công ty cấu hình)

→ Permission rules, hooks, env vars, model default, MCP allowlist…

#### Bước 2 — MCP servers
- Đọc `.mcp.json` (project) và `~/.claude/mcp.json` (global)
- Với mỗi server: spawn process, handshake JSON-RPC, fetch tool/resource list
- Tool MCP có dạng `mcp__<server>__<tool>` (như `mcp__plugin_playwright_playwright__browser_click`)
- Server nào fail → log warning, session vẫn tiếp tục

#### Bước 3 — Memory files (CLAUDE.md)
Load theo cây thư mục, **gộp lại** (không ghi đè):

```
~/.claude/CLAUDE.md                    ← global (mọi project)
↓
/Users/.../CLAUDE.md                   ← walk up từ cwd nếu có
↓
<project root>/CLAUDE.md               ← project chính (luôn load)
↓
<project root>/CLAUDE.local.md         ← local (gitignore)
↓
<subdir đang cwd>/CLAUDE.md            ← nếu cwd trong subdir
```

**Import syntax**: trong CLAUDE.md có thể ghi `@docs/architecture.md` → file đó được nhúng vào memory.

**Lazy loading**: CLAUDE.md ở subdir khác chỉ load khi Claude `cd` hoặc đọc file trong đó (Claude Code 2026+).

#### Bước 4 — Registry scan
Quét các thư mục để build registry (chưa load nội dung, chỉ index):

| Loại | Vị trí project | Vị trí global |
|------|----------------|---------------|
| Commands | `.claude/commands/*.md` | `~/.claude/commands/*.md` |
| Agents | `.claude/agents/*.md` | `~/.claude/agents/*.md` |
| Skills | `.claude/skills/*/SKILL.md` | `~/.claude/skills/*/SKILL.md` |
| Hooks | (từ settings.json) | (từ settings.json) |

Nội dung command/agent/skill **chỉ load khi được trigger** — không tốn context lúc start.

#### Bước 5 — Plugins & Extensions
Nếu cài plugin (như `vercel`, `figma`, `claude-code-guide`): plugin có thể inject thêm:
- Skills (xem dự án này có hàng loạt `vercel:*`, `figma:*`)
- Agents (như `pr-review-toolkit:*`)
- MCP servers
- SessionStart hooks (như dự án này tự load Vercel knowledge update)

#### Bước 6 — IDE integration (nếu có)
Khi chạy trong VSCode/JetBrains:
- Đọc file đang mở
- Đọc `<ide_selection>` nếu user đang chọn text
- Mở socket lắng nghe diff/edit events

#### Bước 7 — System prompt assembly
Tất cả gộp thành 1 system prompt khổng lồ gửi lên API (được prompt cache):
```
[base system prompt]
+ [tool definitions]
+ [MCP tool definitions]
+ [skills registry summary]
+ [agents registry summary]
+ [memory: CLAUDE.md merged]
+ [git status snapshot]
+ [environment info]
+ [SessionStart hook output]
```

→ Đây là lý do CLAUDE.md to = mỗi prompt đắt hơn.

### 5.3 Chi tiết các Hook events

#### Hiểu đơn giản: Hook là gì?

Hook = **đoạn script shell tự chạy** ở những thời điểm cố định, **không cần Claude can thiệp**.

So sánh dễ hiểu:
- **Claude** = nhân viên thông minh, hiểu ngữ cảnh, nhưng có thể quên hoặc làm sai.
- **Hook** = công tắc tự động, chạy CHÍNH XÁC quy tắc bạn đặt, không bao giờ quên.

Ví dụ tình huống dễ hình dung:
| Bạn muốn | Dùng hook nào |
|----------|---------------|
| Tự chạy `prettier` mỗi khi Claude sửa file `.ts` | `PostToolUse` matcher `Edit\|Write` |
| Cấm Claude chạy `rm -rf` | `PreToolUse` matcher `Bash`, exit 2 nếu phát hiện |
| Khi mở session, tự in version Node + branch hiện tại | `SessionStart` |
| Đẩy notification Slack khi Claude xong task | `Stop` |
| Backup transcript trước khi auto-compact | `PreCompact` |

#### 9 loại hook events

Hook hoạt động: bạn ghi script trong `.claude/settings.json`, Claude Code chạy script tại đúng thời điểm, đọc kết quả qua **stdin/stdout/exit code**.

#### `SessionStart`
- **Khi**: ngay sau khi load settings, trước khi assemble system prompt
- **Input**: JSON qua stdin (cwd, session ID, args…)
- **Output**: stdout được **inject vào system prompt** như context bổ sung
- **Use case**: load thông tin runtime (git branch hiện tại, version package, env hiện tại), inject team conventions
- **Ví dụ thực tế**: dự án này có hook load "Vercel Knowledge Updates" và cảnh báo Vercel CLI chưa cài

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "startup",
      "hooks": [{ "type": "command", "command": "echo Current branch: $(git branch --show-current)" }]
    }]
  }
}
```

#### `UserPromptSubmit`
- **Khi**: user gõ prompt + Enter, **trước khi** gửi API
- **Input**: prompt content
- **Output**: stdout append vào prompt; exit code ≠ 0 → **block** prompt
- **Use case**: thêm context tự động (date, branch), filter từ cấm, redact secret
- **Ví dụ**: block prompt chứa "rm -rf /"

```json
{
  "hooks": {
    "UserPromptSubmit": [{
      "hooks": [{ "type": "command", "command": "scripts/redact-secrets.sh" }]
    }]
  }
}
```

#### `PreToolUse`
- **Khi**: ngay trước khi thực thi 1 tool call
- **Input**: JSON gồm tool name + tool input
- **Output**: exit code 0 = allow; exit code 2 = **block** kèm message; output JSON `{"decision":"approve"}` = bypass permission check
- **Use case**: chặn tool nguy hiểm, audit log, force approve trong CI
- **Matcher**: filter theo tên tool (regex), ví dụ `"Bash|Edit"`

```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "scripts/block-dangerous-bash.sh"
      }]
    }]
  }
}
```

#### `PostToolUse`
- **Khi**: ngay sau khi tool chạy xong (kể cả lỗi)
- **Input**: JSON gồm tool name + input + result
- **Output**: stdout inject vào context như tool result bổ sung
- **Use case**: auto-format sau Edit, auto-lint, audit log, trigger test
- **Ví dụ kinh điển**: chạy `prettier` sau khi Edit file `.ts`

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "scripts/auto-format.sh \"$CLAUDE_TOOL_INPUT_FILE_PATH\""
      }]
    }]
  }
}
```

#### `Notification`
- **Khi**: Claude cần input từ user (xin permission, idle quá lâu)
- **Use case**: gửi notification desktop, beep, Slack DM
- **Ví dụ**: macOS `osascript -e 'display notification'`

#### `Stop`
- **Khi**: Claude kết thúc lượt (xong response)
- **Output**: exit code 2 + message = **bắt Claude tiếp tục**
- **Use case**: đảm bảo Claude không dừng giữa task ("phải chạy test xong mới được stop")

#### `SubagentStop`
- **Khi**: 1 subagent kết thúc (trước khi return về main)
- **Use case**: validate output của subagent, retry nếu cần

#### `PreCompact`
- **Khi**: trước khi auto-compact context
- **Use case**: backup transcript trước khi mất chi tiết, gửi log lên server

#### `SessionEnd`
- **Khi**: session đóng (Ctrl+C, exit)
- **Use case**: cleanup, gửi summary, lưu metric

### 5.4 Permission check flow (chi tiết)

Khi Claude gọi 1 tool:

```
Tool call → PreToolUse hook
              │
              ├─ exit 2 → BLOCKED (message về Claude)
              ├─ JSON {"decision":"approve"} → AUTO-ALLOW (bỏ qua bước dưới)
              └─ exit 0 → tiếp tục
                          ▼
                  Permission rules check
                  (settings.json: allow/deny/ask)
                          │
                  ├─ match allow → AUTO-ALLOW
                  ├─ match deny → DENIED
                  └─ match ask / no match → hỏi user
                          ▼
                  User chọn (Yes / Yes always / No)
                          ▼
                  Tool executes
                          ▼
                  PostToolUse hook
```

Ví dụ permission rule:
```json
{
  "permissions": {
    "allow": [
      "Bash(npm test:*)",
      "Bash(git status)",
      "Read(**)"
    ],
    "deny": [
      "Bash(rm -rf*)",
      "Bash(* --force*)"
    ]
  }
}
```

### 5.5 Context lifecycle trong 1 session — Chính xác file nào được load?

#### Hiểu đơn giản trước

Hãy nghĩ context của Claude như **balo đi học**: mỗi lần bạn hỏi Claude (= đến lớp), Claude phải vác **toàn bộ balo** đến (gửi lên API).

Trong balo có:
- **Sách giáo khoa** (system prompt) — luôn mang, không đổi → trường photo sẵn (cache).
- **Sổ tay convention** (CLAUDE.md) — luôn mang, bạn tự ghi.
- **Vở bài tập** (conversation history) — dày dần theo buổi học. Càng nhiều buổi → vở càng nặng.
- **Tài liệu MCP** (Figma, Playwright manual) — nếu đăng ký lớp đó thì mang theo.
- **Note IDE** (file đang mở, vùng chọn) — sticky note dán lên vở.

→ Tốn token = balo nặng. Cách giảm: bớt sổ tay (CLAUDE.md gọn), xé vở cũ (`/clear`), tóm tắt vở (`/compact`).

#### Inventory chi tiết — file nào vào balo?

Mỗi lượt user gửi đi, **toàn bộ context** được gửi lại lên API. Dưới đây là **inventory chi tiết** từng file/nguồn dữ liệu chui vào context.

#### A. Memory files — nội dung được **nhúng nguyên văn** vào system prompt

Đây là phần TỐN TOKEN NHẤT vì load trong mọi request.

| Thứ tự load | Đường dẫn | Khi nào tồn tại |
|-------------|-----------|-----------------|
| 1 | `~/.claude/CLAUDE.md` | User global memory, dùng mọi project |
| 2 | `/Users/<user>/CLAUDE.md` (parent dirs) | Nếu có file CLAUDE.md ở thư mục cha của cwd, Claude walk-up và load |
| 3 | `<project root>/CLAUDE.md` | Project memory, commit vào git — file chính |
| 4 | `<project root>/CLAUDE.local.md` | Local override, gitignored |
| 5 | `<cwd>/CLAUDE.md` | Nếu cwd là subdir và có CLAUDE.md riêng |
| 6 | Các file được `@import` bên trong CLAUDE.md | VD trong CLAUDE.md ghi `@docs/architecture.md` → file đó được nhúng |

Trong dự án này cụ thể (đoán dựa trên cấu trúc):
- `~/.claude/CLAUDE.md` (nếu bạn có)
- `/Users/nguyenanhnhut/Desktop/Projects/nx-build/CLAUDE.md` ← file dài, đang load mỗi prompt
- `/Users/nguyenanhnhut/Desktop/Projects/nx-build/CLAUDE.local.md` (nếu tạo)

> ⚠️ Tổng cộng các file này load vào **mỗi request**. CLAUDE.md của dự án bạn dài ~300 dòng → khoảng 3-5k token mỗi lượt.

#### B. Auto-memory system (memory động Claude tự tạo)

Hệ thống memory mà Claude tự ghi qua thời gian:

| File | Vị trí | Mục đích |
|------|--------|----------|
| `MEMORY.md` | `~/.claude/projects/<project-hash>/memory/MEMORY.md` | Index — luôn load |
| `<name>.md` | `~/.claude/projects/<project-hash>/memory/<name>.md` | Memory cụ thể — load lazy khi liên quan |

Trong dự án này: `/Users/nguyenanhnhut/.claude/projects/-Users-nguyenanhnhut-Desktop-Projects-nx-build/memory/`

`MEMORY.md` luôn được nhúng vào context (cap 200 dòng). Các file con chỉ load khi Claude thấy liên quan.

#### C. Settings files — KHÔNG nhúng vào prompt, dùng để config

Load theo thứ tự (file sau ghi đè file trước):

| Thứ tự | Đường dẫn | Vai trò |
|--------|-----------|---------|
| 1 | `~/.claude/settings.json` | User global config |
| 2 | `<project>/.claude/settings.json` | Project config (commit) |
| 3 | `<project>/.claude/settings.local.json` | Local override (gitignore) |
| 4 | Managed/enterprise policy file | Công ty cấu hình ép buộc (nếu có) |

Nội dung bên trong: permission rules, hooks, env vars, default model, MCP allowlist…
→ Settings **không vào prompt**, nhưng quyết định hành vi (vd hook nào fire, tool nào auto-allow).

#### D. MCP config — KHÔNG nhúng nguyên văn, nhưng **tool list** thì có

| File | Vị trí |
|------|--------|
| `.mcp.json` | `<project>/.mcp.json` (chuẩn mới) |
| `mcp.json` | `<project>/.claude/mcp.json` (vị trí cũ) |
| User MCP | `~/.claude/mcp.json` |

Claude Code đọc các file này → spawn process MCP server → fetch danh sách tool/resource → **nhúng tool definition vào system prompt**.

Ví dụ trong session hiện tại bạn thấy các tool như:
- `mcp__plugin_playwright_playwright__browser_click`
- `mcp__plugin_serena_serena__find_symbol`
- `mcp__plugin_figma_figma__authenticate`

→ Mỗi tool MCP = thêm một JSON schema vào prompt (vài trăm token).

#### E. Registry files — index ở start, **nội dung load lazy**

Claude scan các thư mục sau, build **danh sách tóm tắt** (chỉ tên + mô tả 1 dòng):

| Loại | Project | Global | Plugin |
|------|---------|--------|--------|
| Slash commands | `.claude/commands/*.md` | `~/.claude/commands/*.md` | `<plugin>/commands/*.md` |
| Subagents | `.claude/agents/*.md` | `~/.claude/agents/*.md` | `<plugin>/agents/*.md` |
| Skills | `.claude/skills/*/SKILL.md` | `~/.claude/skills/*/SKILL.md` | `<plugin>/skills/*/SKILL.md` |

→ Chỉ frontmatter `description` được nhúng vào prompt như "danh sách skill khả dụng". Nội dung đầy đủ chỉ load khi user gõ `/<name>` hoặc Claude trigger skill.

Trong dự án bạn cụ thể có:
- `.agent/skills/vercel-composition-patterns/` (đang ở git status)
- `.agent/skills/vercel-react-best-practices/`
- `.agent/skills/web-design-guidelines/`
- Plugin skills: `vercel:*`, `figma:*`, `pr-review-toolkit:*`, `feature-dev:*`…

#### F. Plugin-injected content

Plugin có thể chèn vào SessionStart hook để inject text bổ sung. Ví dụ trong session này:

```
SessionStart:startup hook success: # Vercel Plugin Session Context
SessionStart:startup hook success: IMPORTANT: The Vercel CLI is not installed.
```

→ Đó là plugin `vercel:knowledge-update` chạy SessionStart hook, output được nhúng vào system prompt.

#### G. Git state snapshot (chỉ chụp lúc start)

Tại thời điểm `SessionStart`, Claude Code chạy ngầm:
```bash
git status --porcelain      # untracked + modified files
git log -5 --oneline        # recent commits
git branch --show-current   # current branch
```

Kết quả nhúng vào system prompt một lần — **không refresh** suốt session (đó là lý do bạn thấy dòng "Note that this status is a snapshot in time" trong system prompt).

#### H. IDE context (nếu chạy trong VSCode/JetBrains)

| Loại | Nguồn |
|------|-------|
| File đang mở | Tab active của IDE → tag `<ide_opened_file>` |
| Vùng được chọn | Selection của user → tag `<ide_selection>` |
| Workspace folders | Folders đã mở trong IDE |

→ Mỗi lượt user, các tag này được tự động đính kèm (nếu thay đổi).

#### I. Environment info — hard-coded vào prompt

- Working directory (`/Users/nguyenanhnhut/Desktop/Projects/nx-build`)
- Additional working dirs (`/Users/nguyenanhnhut/.config`, `/Users/nguyenanhnhut/.claude`)
- Platform (darwin), shell (zsh), OS version
- Model ID đang dùng
- Date hiện tại
- Knowledge cutoff date
- Git repo status (true/false), branch, user

#### J. Conversation history — tăng dần mỗi lượt

```
Turn 1: user prompt + assistant response + tool calls + tool results
Turn 2: ...
Turn N-1: ...
Turn N: current user message
```

Đây là phần **tăng tuyến tính**. Sau 50 turn có tool call, dễ dàng vài chục nghìn token.

#### K. System reminders (tag `<system-reminder>`)

Claude Code chèn các nhắc nhở runtime trong từng turn:
- `<command-name>` khi user gõ slash command
- `<system-reminder>` cảnh báo về TodoWrite, file vừa edit, agents có sẵn…
- `<env>` info môi trường

#### Tổng kết — Mỗi request gửi lên API có gì?

```
═══════════════════════════════════════════════
SYSTEM PROMPT (cached 5 phút, đổi ít)
═══════════════════════════════════════════════
├─ [A] Base instructions Claude Code           ~5k tokens
├─ [D] Tool definitions (Read, Edit, Bash...)  ~3k tokens
├─ [D] MCP tool definitions (Playwright, …)    ~10k+ tokens
├─ [E] Skills registry summary                 ~2k tokens
├─ [E] Agents registry summary                 ~1k tokens
├─ [A] CLAUDE.md (global + project + local)   ~3-10k tokens
├─ [B] MEMORY.md index                         ~1k tokens
├─ [F] SessionStart hook outputs               ~2k tokens
├─ [G] Git status snapshot                     ~500 tokens
└─ [I] Environment info                        ~500 tokens

═══════════════════════════════════════════════
CONVERSATION HISTORY (tăng dần, KHÔNG cached tốt)
═══════════════════════════════════════════════
├─ Turn 1: messages + tool_use + tool_result
├─ Turn 2: ...
├─ ...
└─ Turn N: current user message + [H] IDE context

═══════════════════════════════════════════════
HỆ QUẢ TOKEN
═══════════════════════════════════════════════
• Session mới + CLAUDE.md dự án này:    ~30-40k tokens base
• Sau 20 turn có edit files:            +20-50k tokens history
• Sau /clear:                           reset history về 0, system prompt vẫn còn
• Sau /compact:                         history thay bằng summary (~2k tokens)
```

#### Cách kiểm tra chính xác file nào đang load

```bash
# Xem mọi file đang ảnh hưởng đến config
ls -la ~/.claude/CLAUDE.md
ls -la <project>/CLAUDE.md <project>/CLAUDE.local.md
ls -la <project>/.claude/settings*.json
ls -la <project>/.mcp.json

# Xem auto-memory
ls ~/.claude/projects/<project-hash>/memory/

# Xem registry
ls <project>/.claude/commands/ <project>/.claude/agents/ <project>/.claude/skills/

# Trong session: gõ /cost xem token đã dùng
# Trong session: gõ /status xem MCP servers active
# Trong session: gõ /memory xem các CLAUDE.md đang load
```

#### Hệ quả quan trọng để tiết kiệm

- **Càng nhiều turn, request càng đắt** — conversation history tăng tuyến tính, không cached tốt
- **`/clear`** = reset conversation history về 0 (system prompt giữ nguyên, vẫn cached)
- **`/compact`** = thay history bằng summary ngắn (~2k token)
- **Sửa CLAUDE.md giữa session** → **vỡ cache** system prompt → lượt sau cache miss, đắt + chậm
- **Thêm MCP server lúc đang làm việc** → vỡ cache (tool definitions thay đổi)
- **CLAUDE.md dự án nhỏ gọn** = mỗi request rẻ hơn vĩnh viễn
- **Disable plugin không dùng** = bớt skills/agents registry → bớt token system prompt

### 5.6 Sự khác biệt giữa subagent context và main context

Khi main Claude gọi subagent (qua tool `Agent`):
```
Main Claude
    │
    │  Agent(prompt="...", subagent_type="Explore")
    ▼
┌────────────────────────────┐
│  Subagent — context RIÊNG  │
│  ├─ Hệ system prompt khác  │
│  ├─ Tool subset            │
│  ├─ Memory CLAUDE.md vẫn   │
│  │   load (cùng project)   │
│  ├─ Không thấy turn của    │
│  │   main Claude           │
│  └─ Kết thúc → trả về 1    │
│      message duy nhất      │
└─────────────┬──────────────┘
              │ (message)
              ▼
Main Claude nhận message → tiếp tục
```

→ Đây là lý do subagent **tiết kiệm token main context**: nó đọc 20 file rồi trả về tóm tắt 500 token. Main không thấy 20 file đó.

---

## 6. Cấu trúc thư mục `.claude/` của một dự án

```
.claude/
├── settings.json          # Cấu hình project (commit)
├── settings.local.json    # Cấu hình cá nhân (gitignore)
├── commands/              # Custom slash commands
│   └── deploy.md
├── agents/                # Custom subagents
│   └── my-reviewer.md
├── skills/                # Custom skills
│   └── my-skill/SKILL.md
├── hooks/                 # Hook scripts
└── mcp.json              # MCP server config
```

Global tương đương ở `~/.claude/`.

---

## 7. Lộ trình đề xuất để thành thạo

### Tuần 1 — Cơ bản
- Quen `/clear`, `/compact`, `/cost`
- Dùng `@file` reference
- Thử `Shift+Tab` plan mode
- Đọc CLAUDE.md của dự án

### Tuần 2 — Memory & context
- Viết/sửa CLAUDE.md chuẩn cho dự án
- Thử `/init` ở project khác
- Lưu memory bằng `#`
- Hiểu 3 cấp memory

### Tuần 3 — Tự động hoá
- Tạo 1 custom command trong `.claude/commands/`
- Dùng `Explore` agent cho search lớn
- Thử Plan mode cho task phức tạp

### Tuần 4 — Nâng cao
- Setup hook (auto-lint sau edit)
- Thử headless mode `claude -p` trong script
- Tạo custom subagent
- Thêm MCP server (Playwright cho test E2E)

### Tuần 5+ — Master
- Multi-agent parallel workflow
- CI integration
- Custom skills cho team
- Tối ưu CLAUDE.md để giảm token

---

## 8. Quick reference — Best practices tóm tắt

**DO:**
- `/clear` giữa các task khác nhau
- Cung cấp đường dẫn file cụ thể
- Dùng plan mode cho task lớn
- Commit CLAUDE.md vào repo
- Dùng subagent cho việc tìm kiếm rộng
- Chọn model phù hợp độ khó

**DON'T:**
- Để session chạy cả ngày không clear
- Hỏi "explore codebase" mỗi lần mở session
- Sửa CLAUDE.md liên tục giữa các lượt (vỡ cache)
- Dùng Opus cho việc rename biến
- Bỏ qua plan mode khi không chắc
- `--dangerously-skip-permissions` trên repo thật

---

## 9. Tài nguyên thêm

- Tài liệu chính thức: https://docs.claude.com/en/docs/claude-code
- GitHub issues (bug report): https://github.com/anthropics/claude-code/issues
- Lệnh `/release-notes` để xem update mới
- Lệnh `/help` luôn có sẵn

---

> **Ghi chú**: Tài liệu này dành cho Claude Code version 2026, model mặc định Opus 4.7 / Sonnet 4.6 / Haiku 4.5. Một số tính năng có thể đổi khi update — luôn check `/release-notes`.

---

## 10. TL;DR — Nếu bạn chỉ nhớ 3 thứ

1. **Context = balo, token = nặng nhẹ của balo.** `/clear` giữa các task để xé bớt vở cũ. CLAUDE.md = sổ tay luôn mang theo → giữ gọn.

2. **Có 3 thứ Claude "biết" khi mở session**: CLAUDE.md (convention), settings.json (permissions + hooks), MCP/skills/agents (tool ngoài). Hiểu cái nào load vào prompt, cái nào không → biết tại sao tốn token, tại sao Claude "không thấy" convention.

3. **Hooks > nhắc Claude bằng lời.** Convention quan trọng (lint, format, secret check) → cài hook trong `settings.json`. Claude có thể quên, hook thì không.

Còn lại — slash commands, plan mode, model selection — đều là công cụ. Hiểu 3 cái trên rồi học công cụ sau dễ.
