---
name: thumbnail-reverse
description: Reverse engineer thumbnail của 1 kênh YouTube (tải N thumbnail mới nhất, rút luật chung + khuôn bố cục + khối prompt), rồi tạo bộ thumbnail cùng gu cho kênh của user với mặt thật của user, logo thật, UI thật. Tạo ảnh bằng Codex CLI (tool image_gen của gói ChatGPT đang login, không cần API key). Test 3 mẫu cho user duyệt rồi mới làm số còn lại, cuối cùng ghép ảnh so cặp mẫu gốc với bản mới. Dùng khi user nói "reverse thumbnail kênh X", "làm thumbnail giống kênh này", "học style thumbnail", "thumbnail có mặt mình", "thumbnail kiểu Ben AI", hoặc dán link 1 kênh YouTube và muốn thumbnail theo gu đó.
---

# Thumbnail Reverse

Đưa link 1 kênh YouTube và ảnh mặt của bạn. Nhận lại luật thumbnail của kênh đó, bộ prompt dùng lại được, và bộ thumbnail mới cùng gu có mặt thật của bạn.

Ví dụ hoàn chỉnh: 15 thumbnail kiểu Ben AI (@BenAI92) cho kênh Contentta, xem `references/ben-ai-example.md`.

## Nguyên tắc

- **Test 3 trước, làm sau.** 3 mẫu đầu chưa được user duyệt thì không chạy số còn lại.
- **Chất liệu thật.** Logo tải từ nguồn chính chủ, UI crop từ frame video hoặc screenshot thật. Không để model tự vẽ logo hay UI.
- **Mặt giống thật.** Chỉ retouch nhẹ. Prompt phải tả đặc điểm mặt thật, không thì model biến thành người mẫu.
- **Chỉ tạo ảnh bằng Codex image_gen** (`codex exec` + ảnh tham chiếu qua `-i`, tối đa 5 ảnh). Không dùng API ảnh trả phí.
- **Tự xem từng ảnh** trước khi báo user: mặt, chữ, logo, góc phải dưới.
- Học bố cục và luật của kênh mẫu. Không copy chữ, không dùng lại ảnh của họ trong thumbnail mới.

Trong file này `S` = thư mục `scripts/` của skill (vd `~/.claude/skills/thumbnail-reverse/scripts`). Mọi lệnh chạy từ thư mục project.

## Bước 0. Chốt đầu vào

Đọc tin nhắn của user trước. Thiếu gì thì hỏi gom 1 lượt:

1. Link kênh mẫu. Số thumbnail cần học (mặc định 15).
2. Thư mục ảnh mặt. Tốt nhất là ảnh tách nền (PNG trong suốt), chụp studio, nhìn thẳng, 3 ảnh trở lên.
3. Màu: tự do theo logo và chủ đề từng video, hay ép bảng màu brand. Mặc định đề xuất màu tự do (xem `references/pitfalls.md`, mục Màu).
4. Danh sách video cần thumbnail: title + tool chính trong video. Chưa có thì lấy từ video thật của user (thư mục video, kênh YouTube của user) và nói rõ là mình tự chọn.
5. Nguồn UI thật: file video, frame render, screenshot app.

Kiểm công cụ: `yt-dlp`, Python có Pillow, `codex` đã login gói ChatGPT trả phí (gói Free không có tool tạo ảnh trong Codex CLI).

## Bước 1. Tải thumbnail và đọc

```bash
mkdir -p <project>/faces && cd <project>
python $S/fetch_channel_thumbs.py https://www.youtube.com/@<kênh> --n 15     # refs/01-<id>.jpg ..., refs/list.txt
python $S/sheet.py sheet-1.jpg "refs/0*.jpg" --cols 2
python $S/sheet.py sheet-2.jpg "refs/1*.jpg" --cols 2
```

Mở từng sheet ra xem. Ảnh nào khó đọc thì mở ảnh gốc trong `refs/`. Đọc thêm `refs/list.txt` để biết chữ trên thumbnail liên quan title ra sao.

Copy ảnh mặt vào `faces/` (hoặc đặt biến môi trường `THUMB_FACE_DIR`), rồi ghép sheet để chọn ảnh:

```bash
python $S/sheet.py faces-sheet.jpg "faces/*.png" --cols 4
```

## Bước 2. Rút luật và khuôn bố cục

Copy `template/prompts.md` của skill vào project. Điền mục 1:

- **Luật chung**, đúng ở gần hết các ảnh: số thành phần, chữ (số từ, font, in hoa, chữ là cảm xúc hay lặp title), màu (1 màu chủ đạo lấy từ đâu, nền gì), mặt (biểu cảm, hướng nhìn, cắt khung, áo, ánh sáng), chi tiết lặp lại (mũi tên vẽ tay, nhãn dán...), logo và UI thật hay vẽ.
- **Khuôn bố cục**: gom các ảnh giống nhau về vị trí mặt, chữ, hình. Mỗi khuôn 1 dòng: tên, mô tả vị trí, **số thứ tự ảnh mẫu** (vd `01, 07, 11, 13`). Ảnh lẻ không vào khuôn nào thì ghi ở "Ngoài lề".

Ben AI ra 5 khuôn: mặt + chữ + UI, mặt + nhãn dán, phương trình logo, sản phẩm + thẻ, đối đầu. Xem bảng trong `references/ben-ai-example.md`.

## Bước 3. Khối prompt dùng chung

Mục "Khối dùng chung" trong `prompts.md` có 2 khối: có người và không người. Sửa theo luật vừa rút (font, số thành phần, phong cách ảnh).

Thay `[face features]` 1 lần: xem `faces-sheet.jpg`, tả bằng tiếng Anh các nét dễ bị model làm sai. Gồm dáng mặt, má, đường hàm, mắt và mí, lông mày, kiểu tóc, màu da, nét trẻ hay già. Ví dụ đã dùng:

```
round face with full cheeks, soft rounded jawline (not angular, not chiseled), youthful boyish look, eyes with low eyelid creases, short black hair with a side-swept fringe over the forehead
```

Đổi "the person" thành "the man" / "the woman" nếu muốn chắc hơn.

## Bước 4. Logo thật và UI thật

Logo, vào `assets/logos/`:

```bash
python $S/fetch_logo.py claude --term "Claude by Anthropic" --seller Anthropic   # App Store, phải khớp hãng
python $S/fetch_logo.py chatgpt --term ChatGPT --seller OpenAI
python $S/fetch_logo.py n8n --wiki "n8n logo" --domain n8n.io --icon            # wordmark, tách biểu tượng
python $S/sheet.py logos-check.jpg "assets/logos/*.png" --cols 6
```

Mở `logos-check.jpg` xem từng logo đúng chưa. Tool không có logo chính chủ thì crop từ ảnh có sẵn và báo user.

UI, vào `assets/ui/`: trích frame từ video thật, ghép sheet để chọn khung, rồi crop sạch theo mép UI.

```bash
mkdir -p frames assets/ui
ffmpeg -v error -ss 237.6 -i "<video>.mp4" -frames:v 1 frames/astra_237.6.png
python -c "from PIL import Image; Image.open('frames/astra_237.6.png').crop((540,220,1360,740)).save('assets/ui/astra-excel.png')"
```

Mở ảnh crop ra xem. Không để dính mẩu chữ bị cắt ở mép.

## Bước 5. Viết prompt từng ảnh

Mỗi thumbnail 1 mục trong phần "## Prompt" của `prompts.md`:

````
### b07, khuôn A: Showroom 3D

```
python $S/gen_thumb.py b07 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png" --asset "real screenshot: 3D showroom=assets/ui/showroom.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: ...
- Right 38% of the frame: the person from the reference photos, chest-up, head large, ...
- Top-left: ...

[khối prompt chung, với:]
expression = big friendly smile with teeth, eyes looking straight into the lens
wardrobe = plain black crew-neck t-shirt
palette = charcoal and warm light; color comes from the screenshot and the Claude icon
exact text = "SHOWROOM 3D"
```
````

- Tên `bNN`: `NN` = số thứ tự ảnh mẫu đang mô phỏng. Dễ ghép cặp so sánh về sau.
- LAYOUT tả theo khuôn: nền (màu hex, chất liệu), vị trí và tỉ lệ mặt, vị trí chữ, hình minh hoạ, mũi tên. Ghi % khung hình.
- Mỗi asset có vai trò rõ trong `--asset "vai trò=đường dẫn"`. Nhắc lại asset đó trong LAYOUT bằng chữ "the attached ...".
- Chữ 2-4 từ. Đổi áo thì ghi "(change from the black shirt in the references)".
- Mẫu không mặt dùng `[khối không người, với:]` và bỏ `--face`.

Build ra file prompt:

```bash
python $S/build_prompts.py      # prompts/<tên>.txt, báo lỗi nếu còn [placeholder] chưa điền
```

## Bước 6. Test 3 mẫu, dừng cho user duyệt

Chọn 3 mẫu thuộc 3 khuôn khác nhau, có ít nhất 1 mẫu có mặt và 1 mẫu không mặt. Chạy song song (Bash `run_in_background`), mỗi lệnh 1 job:

```bash
python $S/gen_thumb.py b01 --face face1.png face2.png face3.png --asset "..."
```

Xong thì kiểm `out/<tên>.png` có tồn tại (Codex trả exit 0 cả khi không ra ảnh, lỗi nằm trong `out/<tên>.log`). Mở từng ảnh, soát:

- Mặt: crop mặt ở ảnh mẫu và ở thumbnail, ghép cạnh nhau. Không giống thì thêm nét vào `[face features]`, chạy lại.
- Chữ đúng từng dấu. Số 0 không thành chữ O.
- Logo và UI giữ đúng hình, đúng màu.
- Góc phải dưới trống. Không có thứ thừa ngoài LAYOUT.

Ghép ảnh so cặp, ảnh mẫu bên trái, bản mới bên phải:

```bash
python $S/sheet.py review-3.jpg refs/01-<id>.jpg out/b01.png refs/05-<id>.jpg out/b05.png refs/15-<id>.jpg out/b15.png --cols 2 --width 800
```

**Dừng.** Gửi user `review-3.jpg` + bảng: mẫu, khuôn, chất liệu thật đã đưa vào, lỗi còn lại, token đã tốn. Hỏi user muốn sửa gì. Sửa luật hoặc khối chung thì cập nhật `prompts.md` rồi test lại 3 mẫu.

## Bước 7. Làm số còn lại

Viết prompt cho các mẫu còn lại, build lại, rồi chạy 4 job một lượt:

```bash
python $S/build_prompts.py
grep -E "^python .*gen_thumb.py b[0-9]+" prompts.md > out/batch.txt
tr '\n' '\0' < out/batch.txt | xargs -0 -P 4 -I{} bash -c '{}'
```

Lệnh trong `prompts.md` ghi `$S` thì export biến `S` trước khi chạy. Mẫu nào `NO IMAGE` thì đọc log, sửa, chạy lại riêng mẫu đó.

## Bước 8. Ghép review và báo cáo

```bash
python $S/sheet.py review-all.jpg "out/b*.png" --cols 3 --no-labels
python $S/sheet.py review-vs-ref.jpg refs/01-<id>.jpg out/b01.png refs/02-<id>.jpg out/b02.png ... --cols 2
```

Báo user: link 2 ảnh review, bảng mẫu (chủ đề, khuôn, chất liệu thật), lỗi còn lại cần user xem, tổng token đã tốn.

Muốn dùng ChatGPT web thay Codex: dán `prompts/<tên>.txt` vào ChatGPT, đính kèm đúng các ảnh mặt và asset như lệnh `gen_thumb.py`.

## Cấu trúc project

```
<project>/
  refs/            thumbnail kênh mẫu + list.txt (không đưa lên repo public)
  faces/           ảnh mặt của user
  assets/logos/    logo thật đã tải
  assets/ui/       UI thật đã crop
  prompts.md       luật, khuôn, khối chung, prompt từng ảnh (nguồn duy nhất để sửa)
  prompts/         <tên>.txt build từ prompts.md
  out/             <tên>.png, <tên>.log, <tên>-sheet.png
  sheet-*.jpg, review-*.jpg
```

## Bẫy hay gặp

Đầy đủ trong `references/pitfalls.md`. 5 cái hay gặp nhất:

1. Mặt ra như người mẫu: tả đặc điểm mặt thật trong `[face features]`.
2. Logo tự vẽ bị giả: luôn tải logo thật, `--seller` phải khớp hãng.
3. UI vẽ kiểu 3D hoạt hình: crop UI thật từ video hoặc screenshot.
4. Gửi quá 5 ảnh tham chiếu bị Codex từ chối: `gen_thumb.py` tự gộp ảnh dư thành 1 sheet.
5. Chữ lấn góc phải dưới, số 0 thành chữ O: soát từng ảnh.
