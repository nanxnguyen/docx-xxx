# 🌿 Topic 41: Git Workflow & Team Collaboration - Branching Strategy, Merge vs Rebase, Conflict Resolution

## 1. ⭐ Senior/Staff Summary

Git workflow tốt không phải là dùng nhiều lệnh Git phức tạp. Workflow tốt là workflow giúp team **review nhanh**, **ít conflict**, **history dễ hiểu**, **rollback được**, **CI/CD đáng tin**, và **production luôn recoverable**.

Các ý senior cần nắm:

- 🌳 **Branching strategy:** chọn Git Flow, GitHub Flow hoặc Trunk-Based theo release model, team size, CI maturity và feature flag maturity.
- 🔀 **Merge vs Rebase:** `merge` giữ context và an toàn cho public branches; `rebase` tạo linear history nhưng rewrite commit hash.
- 🚩 **Feature flags:** giúp merge/deploy code chưa bật cho user, giảm long-lived branches và conflict.
- ⚔️ **Conflict resolution:** conflict không chỉ là sửa marker `<<<<<<<`; phải hiểu intent của cả hai bên và test lại behavior.
- 🤝 **Team collaboration:** small PR, frequent sync, ownership rõ, CI bắt buộc, format tự động, communication sớm.
- 🧯 **Recovery:** biết dùng `reflog`, `revert`, `reset`, `stash`, `bisect`, `cherry-pick` đúng tình huống.

> 🔥 Golden rule: **Không rebase public/shared branches như `main`, `develop`**. Chỉ rebase branch cá nhân khi hiểu rõ và dùng `--force-with-lease` nếu cần push lại.

## 2. 🧠 Key Mental Model

- Git là **commit graph**, không phải chỉ là danh sách commit. Merge giữ graph; rebase viết lại một đoạn graph thành lịch sử tuyến tính.
- Branch là pointer nhẹ trỏ vào commit. Làm việc với branch nghĩa là di chuyển pointer một cách có kiểm soát.
- Public branch là contract của team. Đừng rewrite history mà người khác đã dựa vào.
- Conflict thường đến từ **long-lived branch**, **PR quá lớn**, **ownership mờ**, **format khác nhau**, hoặc **nhiều người sửa cùng vùng code**.
- CI/CD là safety net, nhưng không thay code review và communication.
- Git workflow phải phục vụ delivery model: release theo version khác continuous deployment.

## 3. 📚 Main Concepts

### 3.1. 🌳 Branching Models

#### Git Flow

Phù hợp khi release theo version rõ ràng, enterprise/mobile app, có nhiều môi trường và cần hotfix/versioning chặt.

```txt
main      ──●────────────●────────────●──  v1.0, v2.0
             \          / \          /
develop   ───●──●──●──●───●──●──●──●────
              \    \       \
feature/*      ●──● ●──●     ●──●
release/*               ●──●
hotfix/*                         ●──●
```

Branches chính:

- `main`: production, mỗi commit nên deployable/releasable.
- `develop`: integration branch cho work chưa release.
- `feature/*`: nhánh tính năng, branch từ `develop`.
- `release/*`: ổn định bản release, chỉ fix bug nhỏ/version/changelog.
- `hotfix/*`: fix production khẩn cấp, branch từ `main`, merge lại `main` và `develop`.

Ưu điểm:

- Rõ version và release lifecycle.
- Hợp team lớn cần stage release.
- Hotfix path rõ.

Nhược điểm:

- Nhiều nhánh, nhiều merge.
- Dễ tăng conflict nếu feature sống lâu.
- Không tối ưu cho continuous deployment.

#### GitHub Flow

Phù hợp SaaS/web app có CI/CD tốt và deploy thường xuyên.

```txt
main       ──●──●────●────●────●──
              \  \    \    \
feature/*      ●──●    ●──● ●──●
```

Flow:

1. Branch từ `main`.
2. Commit/push thường xuyên.
3. Mở Pull Request.
4. CI pass, review approve, staging/preview OK.
5. Merge vào `main`.
6. Auto deploy hoặc release pipeline chạy.

Ưu điểm:

- Đơn giản.
- Ít branch ceremony.
- Phù hợp CI/CD và review nhanh.

Nhược điểm:

- `main` phải luôn khỏe.
- Không hợp nếu cần maintain nhiều version song song.
- Cần test automation và rollback tốt.

#### Trunk-Based Development

Phù hợp team mature, CI mạnh, feature flags tốt, branch rất ngắn.

```txt
main/trunk ──●──●──●──●──●──●──
```

Key practices:

- Branch sống rất ngắn, thường dưới 1-2 ngày.
- Code chưa hoàn thiện nằm sau feature flag.
- Merge nhỏ, liên tục.
- CI bắt buộc nhanh và đáng tin.

Ví dụ feature flag:

```ts
if (featureFlags.isEnabled("new-checkout")) {
  renderNewCheckout();
} else {
  renderOldCheckout();
}
```

> 💡 Trunk-Based không có nghĩa là commit bừa vào `main`. Nó đòi hỏi test, review, flag, monitoring và rollback tốt hơn.

### 3.2. 🔀 Merge vs Rebase

#### `git merge`

Merge giữ nguyên graph và tạo merge commit nếu không fast-forward.

```txt
main:     A ── B ── C ── D
                  \       \
feature:           E ── F ─ M
```

Dùng khi:

- Merge PR vào `main`/`develop`.
- Cần giữ context branch.
- Branch public/shared.
- Team muốn audit timeline đầy đủ.

Ưu điểm:

- Không rewrite commit cũ.
- An toàn cho shared history.
- Conflict thường resolve một lần.

Nhược điểm:

- History có nhiều merge commit.
- Log có thể rối nếu PR nhỏ không được squash.

#### `git rebase`

Rebase “đặt lại” commits của branch lên base mới, tạo commit hash mới.

```txt
Trước:
main:     A ── B ── C ── D
              \
feature:       E ── F

Sau rebase main:
main:     A ── B ── C ── D
                        \
feature:                 E' ── F'
```

Dùng khi:

- Branch cá nhân cần cập nhật với `main`.
- Muốn PR history sạch trước review.
- Commits chưa public hoặc team thống nhất cho phép rebase feature branch.

Không dùng khi:

- Rebase `main`, `develop` hoặc branch nhiều người đang dùng.
- Bạn không hiểu impact của force push.

So sánh nhanh:

| Tiêu chí | Merge | Rebase |
|---|---|---|
| History | Giữ graph thật | Linear history |
| Commit hash | Không đổi | Đổi hash |
| Safety | An toàn cho public branch | Nguy hiểm nếu public/shared |
| Conflict | Thường một lần | Có thể lặp theo từng commit |
| Use case | Merge PR, release branch | Dọn branch cá nhân |

### 3.3. 🧹 Interactive Rebase và Squash

Interactive rebase giúp sửa commit history của branch cá nhân trước khi PR.

```bash
git rebase -i HEAD~3
```

Ví dụ:

```txt
pick f7f3f6d feat: add login form
squash 310154e fix: typo in login
squash a5f4a0d fix: add validation
```

Use cases:

- Squash `WIP` commits.
- Sửa commit message.
- Reorder commits.
- Drop commit sai.

> ⚠️ Chỉ làm với branch cá nhân. Nếu đã push branch và cần push lại, dùng `git push --force-with-lease`, không dùng force push mù.

### 3.4. 🚩 Feature Flags

Feature flag tách **deploy code** khỏi **release feature**.

Use cases:

- Merge code sớm nhưng chưa bật cho user.
- Gradual rollout: 1% → 10% → 50% → 100%.
- A/B testing.
- Kill switch khi feature lỗi.
- Giảm long-lived branch.

Tools:

- LaunchDarkly, Unleash, ConfigCat.
- Internal config service.
- Environment-based flags cho case đơn giản.

Rủi ro:

- Flag debt: flag cũ không xoá.
- Logic phân nhánh quá nhiều.
- Test matrix phức tạp.
- Security/permission không nên chỉ dựa vào client-side flag.

### 3.5. ⚔️ Conflict Prevention

Conflict prevention quan trọng hơn conflict resolution.

Thực hành tốt:

- Pull/rebase/merge từ base branch thường xuyên.
- PR nhỏ, scope rõ.
- Feature branch sống ngắn.
- Chia feature lớn bằng feature flag.
- Format tự động bằng Prettier/ESLint.
- Nói trước khi sửa file/module nóng.
- Code ownership rõ cho module nhạy cảm.
- Không trộn refactor lớn với feature behavior.
- Migration naming có timestamp hoặc tool quản lý.

Ví dụ conflict dễ tránh:

```txt
❌ PR 1: refactor toàn bộ auth + thêm login + đổi format 50 files
✅ PR 1: format-only
✅ PR 2: refactor auth service
✅ PR 3: thêm login UI sau khi refactor merge
```

### 3.6. 🧩 Conflict Resolution

Khi conflict xảy ra:

```bash
git status
git diff
```

Conflict marker:

```ts
// <<<<<<< HEAD
export const timeout = 3000;
// =======
export const timeout = 5000;
// >>>>>>> feature/payment
```

Resolve đúng nghĩa là:

1. Hiểu intent của cả hai thay đổi.
2. Chọn hoặc kết hợp logic đúng.
3. Xoá conflict markers.
4. Chạy format/test.
5. Nếu không chắc, hỏi owner/người viết phần kia.

Sau khi resolve merge:

```bash
git add src/config.ts
git commit
```

Sau khi resolve rebase:

```bash
git add src/config.ts
git rebase --continue
```

Nếu sai:

```bash
git merge --abort
git rebase --abort
```

### 3.7. 🧰 Git Tools Cho Collaboration

| Tool | Dùng khi | Lệnh |
|---|---|---|
| `status` | Xem trạng thái working tree | `git status` |
| `diff` | Xem thay đổi trước commit | `git diff` |
| `log` | Hiểu lịch sử | `git log --oneline --graph --decorate` |
| `blame` | Tìm owner/context dòng code | `git blame path/file.ts` |
| `stash` | Cất work-in-progress tạm | `git stash push -m "wip"` |
| `reflog` | Khôi phục sau reset/rebase nhầm | `git reflog` |
| `bisect` | Tìm commit gây bug | `git bisect start` |
| `cherry-pick` | Lấy một commit sang branch khác | `git cherry-pick <sha>` |
| `worktree` | Làm nhiều branch cùng lúc | `git worktree add ../repo-hotfix main` |

> 💡 Senior habit: trước khi chạy lệnh rewrite history, kiểm tra `git status`, `git branch --show-current`, và hiểu branch có shared không.

### 3.8. 🚦 CI/CD Với Git Workflow

Một workflow team tốt nên có checks bắt buộc trước merge:

- Typecheck.
- Lint/format check.
- Unit tests.
- Integration/e2e tests nếu phù hợp.
- Build production.
- Security/dependency scan khi cần.
- Preview/staging deployment.

Ví dụ GitHub Actions tối giản:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build
```

### 3.9. 🪝 Git Hooks, `.gitignore`, Commit Convention

Git hooks giúp bắt lỗi sớm trên máy dev:

- `pre-commit`: format/lint staged files.
- `commit-msg`: validate Conventional Commits.
- `pre-push`: chạy test nhanh.

Tools phổ biến:

- Husky + lint-staged cho Node projects.
- pre-commit framework cho multi-language repos.

Conventional Commits:

```txt
feat: add checkout address form
fix: handle token refresh race condition
docs: update git workflow notes
chore: bump dependencies
```

`.gitignore` nên ignore:

```gitignore
node_modules/
dist/
build/
.env
.env.local
.DS_Store
coverage/
*.log
```

> ⚠️ Nếu secret đã commit, thêm vào `.gitignore` không xoá khỏi history. Cần rotate secret và xử lý history theo quy trình security.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Feature flag trong frontend

```ts
type FeatureFlags = {
  newCheckout: boolean;
  quickSearch: boolean;
};

function renderCheckout(flags: FeatureFlags) {
  if (flags.newCheckout) {
    return renderNewCheckout();
  }

  return renderLegacyCheckout();
}
```

Production note:

- Flag từ server/config service.
- Có default an toàn khi fetch config fail.
- Không dùng client-side flag làm security boundary.
- Có plan xoá flag sau rollout.

### 4.2. ✅ Small PR strategy cho frontend feature lớn

```txt
Feature: New checkout

PR 1: Add types/API client behind unused code path
PR 2: Add UI components without route exposure
PR 3: Add feature flag and hidden route
PR 4: Enable for internal users
PR 5: Rollout 10% -> 50% -> 100%
PR 6: Remove old checkout + delete flag
```

### 4.3. ✅ Conflict resolution checklist trong PR

```txt
□ Đã pull/rebase base mới nhất chưa?
□ Conflict có nằm ở business logic hay chỉ format?
□ Có hiểu thay đổi của cả hai bên không?
□ Có hỏi owner nếu logic không rõ không?
□ Đã chạy test liên quan chưa?
□ Có manual test flow bị ảnh hưởng không?
□ Có update snapshot/golden file nếu cần không?
```

### 4.4. ✅ Recovery khi rebase sai

```bash
git reflog
git reset --hard HEAD@{1}
```

⚠️ `reset --hard` xoá changes chưa commit trong working tree. Chỉ dùng khi hiểu trạng thái hiện tại hoặc đã backup/stash.

An toàn hơn khi chưa chắc:

```bash
git branch backup-before-reset
git reflog
```

### 4.5. ✅ Dùng `git bisect` tìm commit gây bug

```bash
git bisect start
git bisect bad
git bisect good v1.8.0

# Git checkout commit ở giữa.
# Chạy test/manual check:
npm test -- checkout.test.ts

git bisect good # hoặc git bisect bad

git bisect reset
```

## 5. 🏭 Production Notes / React Implications

- ⚛️ **Frontend PRs:** UI changes nên có screenshot/preview link khi ảnh hưởng layout, responsive, accessibility hoặc visual regression.
- 🧪 **Testing:** PR lớn cần chia nhỏ theo risk: API contract, state logic, UI, e2e flow.
- 🚩 **Feature flags:** Với React app, flag nên được đọc ở boundary rõ ràng; tránh flag lồng sâu khắp component tree gây khó xoá.
- 📦 **Bundle:** Branch strategy không giải quyết bundle bloat. CI nên có build/bundle check nếu app nhạy performance.
- 🔐 **Security:** Hotfix security nên branch từ production baseline, review nhanh nhưng không bỏ qua test tối thiểu và secret rotation nếu cần.
- 🚀 **Deploy:** GitHub Flow/Trunk-Based cần rollback, observability và feature flag kill switch.
- 🧱 **Maintainability:** Không trộn format-only/refactor-only với behavior change trong cùng PR.
- ♿ **Accessibility:** UI PR nên có checklist keyboard/focus/screen reader khi đổi component tương tác.

## 6. ⚠️ Common Pitfalls

- ❌ Rebase `main`/`develop` hoặc branch đang được nhiều người dùng.
- ❌ `git push --force` thay vì `--force-with-lease`.
- ❌ Commit trực tiếp vào protected branch.
- ❌ PR quá lớn, nhiều mục tiêu, khó review và dễ conflict.
- ❌ Long-lived feature branch nhiều tuần.
- ❌ Merge code chưa test vì “chỉ conflict nhỏ”.
- ❌ Resolve conflict bằng cách chọn một bên mà không hiểu logic bên kia.
- ❌ Dùng feature flag nhưng không xoá sau rollout.
- ❌ Không sync hotfix từ `main` về `develop`.
- ❌ Revert merge commit sai cách.
- ❌ Dùng `reset --hard` khi còn uncommitted work.
- ❌ Commit `.env`, token, build output, dependency folder.
- ❌ CI chỉ chạy sau merge, không chạy trên PR.

## 7. ✅ Decision Guide / Checklist

### Chọn workflow nào?

| Tình huống | Chọn | Lý do |
|---|---|---|
| SaaS/web app deploy liên tục | GitHub Flow | Đơn giản, PR vào `main`, CI/CD nhanh |
| Enterprise/mobile release theo version | Git Flow | Có `release/*`, `hotfix/*`, version lifecycle rõ |
| Team rất mature, CI mạnh, flag tốt | Trunk-Based | Integration liên tục, ít branch conflict |
| Feature lớn chưa sẵn sàng release | Feature flag | Merge sớm, bật dần sau |
| Branch cá nhân muốn cập nhật base | Rebase | Linear history, PR sạch |
| Merge vào public branch | Merge hoặc squash merge | Không rewrite shared history |
| Production bug khẩn cấp | Hotfix branch từ `main` | Fix đúng production baseline |
| Cần tìm commit gây bug | `git bisect` | Binary search commit history |
| Lỡ rebase/reset sai | `git reflog` | Tìm lại trạng thái cũ |

### Checklist trước khi merge PR

| Câu hỏi | Trả lời ngắn |
|---|---|
| PR có nhỏ và một mục tiêu không? | Nên nhỏ, review được trong một lượt. |
| Base branch đã mới chưa? | Nên sync trước khi merge để giảm conflict bất ngờ. |
| CI đã pass chưa? | Không merge nếu test/build/lint fail. |
| Có conflict không? | Resolve bằng hiểu logic hai bên, không chọn bừa. |
| Có feature flag nếu feature lớn chưa xong không? | Cần để merge sớm mà không expose user. |
| Có migration/config/env change không? | Cần note rõ trong PR và release checklist. |
| Có UI thay đổi không? | Nên có screenshot/preview và test responsive/accessibility. |
| Có secret hoặc file build bị commit nhầm không? | Kiểm tra diff trước khi merge. |
| Có rollback plan không? | Cần revert strategy, flag kill switch hoặc hotfix path. |
| Commit history có cần squash không? | Squash WIP commits nếu team muốn main sạch. |

## 8. 🗣️ Short Interview Answer

Theo em, Git workflow tốt là workflow giúp team ship nhanh nhưng vẫn review được, rollback được và ít conflict. Nếu sản phẩm deploy liên tục như SaaS web app, em thường chọn GitHub Flow: branch ngắn từ `main`, mở PR, CI pass, review xong thì merge và deploy. Nếu dự án release theo version hoặc mobile/enterprise cần staging release rõ, Git Flow hợp hơn vì có `develop`, `release/*`, `hotfix/*`. Với team rất mature, CI mạnh và feature flags tốt thì Trunk-Based giúp integration liên tục và giảm long-lived branches.

Về `merge` và `rebase`, em dùng merge cho public/shared branches vì nó không rewrite history và giữ context. Rebase em dùng cho branch cá nhân để cập nhật base hoặc dọn commit trước PR. Rule quan trọng là không rebase `main`/`develop` hoặc branch người khác đang dùng. Khi có conflict, em không chỉ xoá marker mà phải hiểu intent của cả hai bên, hỏi owner nếu cần, rồi chạy test/manual flow liên quan.

Điểm senior là giảm conflict từ đầu: PR nhỏ, pull thường xuyên, format tự động, code ownership rõ, feature flags cho work lớn, CI bắt buộc và communication sớm. Khi sự cố xảy ra, biết dùng `reflog`, `revert`, `bisect`, `cherry-pick` đúng tình huống giúp team recover nhanh mà không phá history chung.

## 9. 📖 Giải thích các thuật ngữ trong topic

- `Branch`: Con trỏ tới commit, dùng để phát triển song song.
- `main/master`: Branch chính, thường đại diện production hoặc deployable state.
- `develop`: Branch integration trong Git Flow.
- `feature branch`: Branch cho một tính năng hoặc task.
- `release branch`: Branch chuẩn bị release version mới.
- `hotfix branch`: Branch fix lỗi production khẩn cấp.
- `merge`: Gộp lịch sử hai branch, thường tạo merge commit.
- `rebase`: Viết lại commits của branch lên base mới, đổi commit hash.
- `merge commit`: Commit có nhiều parent, ghi nhận việc merge branch.
- `fast-forward`: Di chuyển branch pointer khi không cần merge commit.
- `squash`: Gộp nhiều commits thành một commit.
- `interactive rebase`: Rebase tương tác để sửa/squash/reorder/drop commits.
- `public branch`: Branch đã share cho người khác hoặc CI/CD dựa vào.
- `force push`: Push ghi đè history remote.
- `--force-with-lease`: Force push an toàn hơn, chỉ push nếu remote chưa thay đổi ngoài dự kiến.
- `Pull Request`: Quy trình đề xuất merge code, review và chạy CI.
- `CI/CD`: Tự động test/build/deploy.
- `feature flag`: Cờ bật/tắt behavior để deploy code độc lập với release.
- `conflict`: Khi Git không tự gộp được thay đổi.
- `reflog`: Log local ghi lại các vị trí HEAD/branch từng trỏ tới, hữu ích để recover.
- `stash`: Cất tạm thay đổi chưa commit.
- `bisect`: Tìm commit gây bug bằng binary search.
- `cherry-pick`: Áp dụng một commit cụ thể sang branch hiện tại.
- `worktree`: Tạo working directory khác cho branch khác trong cùng repo.
- `gitignore`: File khai báo pattern không track.
- `git hook`: Script chạy tự động ở các thời điểm như commit/push.
