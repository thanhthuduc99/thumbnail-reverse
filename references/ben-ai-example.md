# Ví dụ hoàn chỉnh: kênh Ben AI (@BenAI92)

Làm ngày 14/10/2026 cho kênh Contentta (Thành Vũ Đức). Đầu vào: 15 video mới nhất của https://www.youtube.com/@BenAI92, ảnh mặt tách nền của Thành, chủ đề lấy từ các video thật của Contentta. Kết quả: 15 thumbnail cùng gu, mặt thật, logo thật, UI thật, tạo bằng Codex image_gen. Mất khoảng 1 tiếng rưỡi, gồm 2 vòng test 3 mẫu.

Dùng file này để học cách viết, không copy nguyên. Luật và khuôn của kênh khác sẽ khác.

Tên mẫu: `bNN` = số thứ tự ảnh mẫu trong `refs/` đang mô phỏng. 3 mẫu test đầu đặt tên `v2-01` (mô phỏng ảnh 01), `v2-02` (ảnh 15), `v2-03` (ảnh 05). Các prompt gốc viết "the man"; template trong skill dùng "the person", đổi lại theo người thật.

## 1. Ben AI làm thumbnail thế nào

Quy tắc chung, đúng ở cả 15 cái:
- Tối đa 3 thành phần: mặt, chữ, 1 hình minh hoạ. Không có thứ thứ 4.
- Chữ 2-4 từ, IN HOA, font sans hình học rất đậm (kiểu Montserrat Black), dòng sát nhau. Chữ là cảm xúc/lời hứa, không lặp lại title ("INFINITE LEADS", "GAME CHANGER", "THIS FIXES EVERYTHING").
- 1 màu chủ đạo mỗi thumbnail, thường lấy từ logo của tool trong video (Claude ra cam, GPT Sites ra xanh navy). Nền xám than có lưới chấm mờ + vignette, hoặc nền gradient phát sáng sau đầu.
- Mặt: ảnh thật, chụp studio, cười nhẹ, nhìn thẳng camera, cắt ngang ngực, áo trơn tối màu, ánh sáng ấm, hạt film nhẹ.
- Mũi tên trắng vẽ tay, cong, nối chữ với hình minh hoạ.
- Logo là logo thật, đúng màu. UI là UI thật hoặc rất sát bản thật.

5 khuôn lặp lại:

| Khuôn | Bố cục | Ví dụ trong refs |
|---|---|---|
| A. Mặt + chữ + UI | Chữ trên-trái 2 dòng, UI dưới-trái, mặt phải 35-40%, mũi tên nối chữ với UI | 01, 07, 11, 13 |
| B. Mặt + nhãn dán | Chữ đen trên nhãn giấy trắng xé (2 nhãn lệch nhau), nền gradient phát sáng sau đầu, tên tool chữ serif nhỏ | 02, 15 |
| C. Phương trình logo | Chữ giữa-trên, 2 icon app bo góc to + dấu "+", mũi tên chỉ icon thứ 2, không mặt | 06, 12, 14 |
| D. Sản phẩm + thẻ | Tên sản phẩm cực to giữa-trên, hàng 5 thẻ UI có nhãn bên dưới, không mặt | 03, 04, 08 |
| E. Đối đầu | Cắt chéo 2 nửa nền khác nhau, logo + tên serif mỗi bên, huy hiệu "VS" ở giữa | 05 |

Ngoài lề: 09 (cảnh 3D đất sét), 10 (mặt + tường logo). Ít dùng, chưa đưa vào bộ test.

## 2. 15 prompt đã duyệt

### v2-01, khuôn A: Hệ thống AI edit videos Youtube

```
python $S/gen_thumb.py v2-01 --face face1.png face2.png face3.png --asset "real timeline UI screenshot=assets/ui/ai-cut-timeline.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: neutral dark charcoal grey #2A2A2A studio backdrop with a fine dot-grid texture and a soft dark vignette. A faint warm glow behind the man.
- Right 38% of the frame: the man from the reference photos, chest-up, head large (about 45% of frame height), body cut off by the bottom edge, facing the camera.
- Top-left: headline in two lines, pure white: "KHÔNG CẦN" on line 1, "EDITOR" on line 2. The headline fills about 55% of the frame width.
- Bottom-left, under the headline: the attached real timeline UI screenshot as a floating app window, tilted very slightly toward the viewer, with a soft drop shadow. Keep its dark panel, green audio waveform, red highlighted cut regions, clip thumbnails, subtitle chips and the Claude tile at its top-right corner exactly as in the screenshot. It can tuck slightly behind the man's shoulder.
- A white hand-drawn curved arrow from the end of "EDITOR" down to the timeline window.

[khối prompt chung, với:]
expression = warm confident smile with teeth, eyes looking straight into the lens
wardrobe = plain black crew-neck t-shirt
palette = neutral charcoal and white; the only colors come from the real UI screenshot (green waveform, red cut marks, Claude orange)
exact text = "KHÔNG CẦN" and "EDITOR"
```

### v2-02, khuôn B: Build website bằng AI miễn phí (đổi áo)

```
python $S/gen_thumb.py v2-02 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: radial gradient, warm bright orange #FF8A3D glow directly behind the man's head, fading to burnt orange #B4471A and then to near-black brown #1A0E08 at the edges. Smooth, slightly grainy.
- Left 42% of the frame: the man from the reference photos, chest-up, head large, body cut off by the bottom edge, shoulders turned slightly right, face toward the camera.
- Right side: two torn white paper label stickers, slightly rotated in opposite directions, stacked one above the other, each with black heavy all-caps text: top label "WEB XỊN", bottom label "0 ĐỒNG". The labels are big, about 50% of the frame width together. The "0" is clearly the digit zero, narrower than the letter O.
- Under the labels, small: the attached Claude app icon as a rounded-square app icon, followed by the words "Claude Code" in an elegant white serif font (like Lora).

[khối prompt chung, với:]
expression = relaxed half smile, slightly raised eyebrows, eyes looking straight into the lens
wardrobe = navy blue crew-neck sweatshirt (change from the black shirt in the references)
palette = warm orange glow and near-black brown, white paper labels, black text
exact text = "WEB XỊN", "0 ĐỒNG" and "Claude Code"
```

### v2-03, khuôn E: Fable 5.1 vs GPT 6 (không mặt)

```
python $S/gen_thumb.py v2-03 --asset "Claude app icon (Fable 5.1 is a Claude model)=assets/logos/claude.png" --asset "ChatGPT app icon=assets/logos/chatgpt.png"
```

```
Create a YouTube thumbnail, 16:9 landscape. No people.

LAYOUT:
- The frame is split by one diagonal line from bottom-left (at 40% width) to top-right (at 60% width), with a thin cream border along the line.
- Left half: warm sunset sky, deep navy-black at the top fading to a glowing burnt-orange horizon. Fine paper grain.
- Right half: bright clear blue daytime sky with soft white fluffy clouds. Fine paper grain.
- Left center: the attached Claude app icon as a large rounded-square app icon with a soft shadow. Under it the words "Fable 5.1" in a large elegant white serif font (like Lora).
- Right center: the attached ChatGPT app icon as a large rounded-square app icon with a soft shadow. Under it the words "GPT 6" in the same large white serif font, with a subtle shadow so it reads on the sky.
- Center, on the diagonal: a small round cream badge with a thin black border and the letters "VS" in black serif.

STYLE:
- Calm, premium, editorial. Only these elements. Large and readable at phone size.
- Real assets: both app icons come from the attached images. Keep their exact shapes and colors. Never redraw or recolor them.

TEXT RULES:
- The only text in the image is "Fable 5.1", "GPT 6" and "VS". Spell exactly.
- No other text, letters, numbers, logos or watermarks anywhere.
```



Tên mẫu `bXX` = số thứ tự thumbnail Ben đang mô phỏng. Chủ đề lấy từ video thật của kênh Contentta. Asset thật nằm trong `assets/logos/` và `assets/ui/`.

### b02, khuôn B: Gemini 4

```
python $S/gen_thumb.py b02 --face face1.png face2.png face3.png
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: radial glow, bright electric blue #3B82F6 directly behind the man's head, fading to deep violet #4C1D95 and then near-black #0B0820 at the edges. Slightly grainy.
- Left 45% of the frame: the man from the reference photos, chest-up, head large, body cut off by the bottom edge, facing the camera.
- Right side: two white paper label stickers with slightly torn edges, each rotated a little in opposite directions, stacked: top label "GEMINI 4", bottom label "QUÁ GẮT", black heavy all-caps text. Together about 50% of the frame width.

[khối prompt chung, với:]
expression = confident closed-mouth smile, eyes looking straight into the lens
wardrobe = charcoal grey henley shirt (change from the black shirt in the references)
palette = electric blue to violet glow, white paper labels, black text
exact text = "GEMINI 4" and "QUÁ GẮT"
```

### b03, khuôn D: Claude Code edit video

```
python $S/gen_thumb.py b03 --asset "Claude app icon=assets/logos/claude.png" --asset "real screenshot: timeline=assets/ui/ai-cut-timeline.png" --asset "real screenshot: transcript=assets/ui/sys-transcript.png" --asset "real screenshot: components=assets/ui/sys-components.png" --asset "real screenshot: terminal=assets/ui/sys-terminal.png" --asset "real screenshot: render=assets/ui/sys-render.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: dark warm brown #1C120C with a strong orange stage-light glow behind the center.
- Top center: huge white headline "CLAUDE CODE", about 80% of the frame width.
- Center, under the headline: the attached Claude app icon, large, glowing, with soft orange light rays behind it.
- Bottom: a row of 5 white rounded cards fanned in a gentle arc, each slightly tilted, each holding one attached real screenshot with a bold black label under it: "Cắt video" (timeline), "Đọc transcript" (transcript), "Dựng 3D" (components), "Tự code" (terminal), "Render" (render). The row can be slightly cropped by the bottom edge.

[khối không người, với:]
palette = dark warm brown and orange glow, white cards, black labels
exact text = "CLAUDE CODE", "Cắt video", "Đọc transcript", "Dựng 3D", "Tự code" and "Render"
```

### b04, khuôn D: GPT 6 Astra

```
python $S/gen_thumb.py b04 --asset "ChatGPT app icon=assets/logos/chatgpt.png" --asset "real screenshot: Excel=assets/ui/astra-excel.png" --asset "real screenshot: document=assets/ui/astra-doc.png" --asset "real screenshot: website=assets/ui/astra-website.png" --asset "real screenshot: newspaper design=assets/ui/astra-newspaper.png" --asset "real screenshot: 3D app=assets/ui/astra-3d.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: deep navy gradient #0B1B3A to #13315C, soft light from the top, a faint grid.
- Top center: the attached ChatGPT app icon, then the white heavy text "GPT 6 Astra" next to it. Together about 70% of the frame width.
- Below: a row of 5 equal dark navy rounded cards with thin light borders and soft shadows. Each card shows one attached real screenshot on top and a white bold label below: "Excel", "Tài liệu", "Website", "Thiết kế", "3D".

[khối không người, với:]
palette = deep navy, white text, colors only from the real screenshots and the ChatGPT icon
exact text = "GPT 6 Astra", "Excel", "Tài liệu", "Website", "Thiết kế" and "3D"
```

### b06, khuôn C: Claude + Jev

```
python $S/gen_thumb.py b06 --asset "Claude app icon=assets/logos/claude.png" --asset "Jev app icon=assets/logos/jev.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: dark charcoal grey #2A2A2A with a fine dot-grid texture and a soft vignette.
- Top center: white heavy headline "ĐỔI CUỘC CHƠI", about 75% of the frame width.
- Center: two large rounded-square app icons side by side, same size, each about 35% of the frame height: left the attached Claude app icon, right the attached Jev icon (black tile, white isometric mark, the word "Jev"). A big white "+" between them.
- A white hand-drawn curved arrow from the end of the headline down to the Jev icon.

[khối không người, với:]
palette = charcoal grey and white; color only from the two icons
exact text = "ĐỔI CUỘC CHƠI" and the "+" sign
```

### b07, khuôn A: Showroom 3D

```
python $S/gen_thumb.py b07 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png" --asset "real screenshot: 3D showroom=assets/ui/showroom-gclass.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: dark charcoal #232323 with a fine dot-grid texture, a soft warm glow and a vignette.
- Top-left: the attached Claude app icon as a small rounded square, followed by the white headline "SHOWROOM 3D" on one line, about 60% of the frame width.
- Bottom-left: a real silver laptop, screen facing the viewer, showing the attached real 3D showroom screenshot full screen. The laptop takes about 55% of the frame width and is slightly cropped by the bottom edge.
- Right 38% of the frame: the man from the reference photos, chest-up, head large, body cut off by the bottom edge.

[khối prompt chung, với:]
expression = big friendly smile with teeth, eyes looking straight into the lens
wardrobe = plain black crew-neck t-shirt
palette = charcoal and warm light; color comes from the showroom screenshot and the Claude icon
exact text = "SHOWROOM 3D"
```

### b08, khuôn D: Sản xuất YouTube tự động

```
python $S/gen_thumb.py b08 --asset "Claude app icon=assets/logos/claude.png" --asset "real screenshot: transcript=assets/ui/sys-transcript.png" --asset "real screenshot: component library=assets/ui/sys-library.png" --asset "real screenshot: review page=assets/ui/sys-review.png" --asset "real screenshot: YouTube page=assets/ui/sys-youtube.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: vivid royal blue #1E5BFF with a soft radial light in the center and darker edges.
- Top: white heavy headline "TỰ ĐỘNG HẾT" with a dark shadow, about 85% of the frame width.
- Center: a real silver open laptop, screen dark grey, showing only the attached Claude app icon large in the middle of the screen.
- Around the laptop, 4 attached real screenshots as floating windows with thin white borders and soft shadows, overlapping the laptop edges: top-left transcript, bottom-left component library, top-right review page, right-middle YouTube page.

[khối không người, với:]
palette = vivid royal blue, white headline, colors from the real screenshots
exact text = "TỰ ĐỘNG HẾT"
```

### b09, cảnh thu nhỏ: Skill mới

```
python $S/gen_thumb.py b09 --asset "Claude Code mascot (orange blocky creature)=assets/ui/cc-mascot.png" --asset "Claude app icon=assets/logos/claude.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Left 40%: huge condensed heavy headline in two lines: "SKILL" in white, "MỚI." in Claude orange #D97757.
- Right 60%: a macro photo of real tabletop miniatures: an army of small orange blocky figures with the exact shape and color of the attached Claude Code mascot (two black rectangular eyes, short legs), marching toward the viewer on a dusty warm surface. Two figures in front carry tall cloth flags, each flag printed with the attached Claude app icon.
- Background: very dark brown to black, warm golden backlight, floating dust, shallow depth of field.
- The figures look like real painted clay or plastic miniatures photographed with a macro lens. Not a cartoon, not a game render.

[khối không người, với:]
palette = near-black brown, warm golden light, Claude orange
exact text = "SKILL" and "MỚI."
```

### b10, mặt + tường logo: Bộ AI cho agency

```
python $S/gen_thumb.py b10 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png" --asset "ChatGPT app icon=assets/logos/chatgpt.png" --asset "Gemini app icon=assets/logos/gemini.png" --asset "Notion app icon=assets/logos/notion.png" --asset "n8n logo mark=assets/logos/n8n-icon.png" --asset "Cursor logo mark=assets/logos/cursor-icon.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: warm orange-brown studio gradient, #C2581F in the center fading to #2A130A at the edges.
- Center: the man from the reference photos, chest-up, head large, body cut off by the bottom edge.
- Behind him at head height: a horizontal row of 6 large rounded-square app icons with soft shadows, partly hidden behind his head: Claude, ChatGPT, Gemini, Notion, n8n, Cursor, using the attached logos exactly. The n8n and Cursor marks sit centered on white rounded tiles.
- Bottom: white heavy caption "COPY BỘ AI NÀY" with a dark shadow, centered slightly left, not touching the bottom-right corner.

[khối prompt chung, với:]
expression = big genuine laughing smile, looking slightly off-camera to the right
wardrobe = olive green overshirt over a white t-shirt (change from the black shirt in the references)
palette = warm orange-brown studio light; logo colors stay original
exact text = "COPY BỘ AI NÀY"
```

### b11, khuôn A nền sáng: Sửa CLAUDE.md

```
python $S/gen_thumb.py b11 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: clean off-white #F4F4F2 studio wall, soft shadow behind the man.
- Right 38% of the frame: the man from the reference photos, chest-up, head large, body cut off by the bottom edge.
- Top-left: headline in near-black #1E1E1E, two lines: "SỬA 1 FILE" on line 1, "ỔN HẾT" on line 2.
- Under the headline on the left: two horizontal usage bars. Bar 1: small grey label "TRƯỚC" above a long coral-red #F06B5B pill bar filled to 100%, with the attached Claude app icon at its right end. Bar 2: small grey label "SAU" above a light grey track with a short green #22C55E fill at about 15%.
- A black hand-drawn curved arrow from the end of bar 1 down to bar 2.

[khối prompt chung, với:]
expression = calm confident closed-mouth smile, eyes looking straight into the lens
wardrobe = plain black crew-neck t-shirt
palette = off-white background, near-black text, coral red and green bars
exact text = "SỬA 1 FILE", "ỔN HẾT", "TRƯỚC" and "SAU"
```

### b12, khuôn C: Edit bằng skill

```
python $S/gen_thumb.py b12 --asset "Claude app icon=assets/logos/claude.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: dark charcoal grey #2A2A2A with a fine dot-grid texture and a soft vignette.
- Top center: white heavy headline "EDIT BẰNG SKILL", about 75% of the frame width.
- Center: left the attached Claude app icon, large; a big white "+" in the middle; right a large realistic macOS-style folder icon in the same terracotta orange as the Claude icon, with the label "/edit-long" in bold black on the folder front. Both items about 35% of the frame height.
- A white hand-drawn curved arrow from the end of the headline down to the folder.

[khối không người, với:]
palette = charcoal grey and white, terracotta orange from the Claude icon
exact text = "EDIT BẰNG SKILL", "/edit-long" and the "+" sign
```

### b13, khuôn A: Claude nhớ mọi thứ

```
python $S/gen_thumb.py b13 --face face1.png face2.png face3.png --asset "Claude app icon=assets/logos/claude.png" --asset "real screenshot: Claude docs page=assets/ui/claude-memory-docs.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: dark warm charcoal #262220 with a soft vignette.
- Top-left: the attached Claude app icon as a small rounded square, then the white headline "NHỚ MỌI THỨ" on one line, with a white hand-drawn underline under "MỌI THỨ".
- Bottom-left: a real laptop with a thin dark bezel, screen facing the viewer, showing the attached real Claude docs screenshot. It takes about 55% of the frame width and is slightly cropped by the bottom edge.
- Right 36% of the frame: the man from the reference photos, chest-up, head large, body cut off by the bottom edge.

[khối prompt chung, với:]
expression = warm smile with teeth, eyes looking straight into the lens
wardrobe = dark navy polo shirt (change from the black shirt in the references)
palette = warm charcoal, white text, colors from the docs screenshot and the Claude icon
exact text = "NHỚ MỌI THỨ"
```

### b14, khuôn C: Claude Code + n8n

```
python $S/gen_thumb.py b14 --asset "Claude app icon=assets/logos/claude.png" --asset "n8n logo mark=assets/logos/n8n-icon.png"
```

```
Create a YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: deep navy-slate #1E2433 with a fine dot-grid texture and a soft vignette.
- Top center: white heavy headline "N8N HẾT KHÓ", about 70% of the frame width.
- Center: left the attached Claude app icon, large; a big white "+" in the middle; right a rounded-square app tile in dark #16161F holding the attached n8n mark centered, in its original pink-red. Both tiles the same size, about 35% of the frame height.
- A white hand-drawn curved arrow from the end of the headline down to the n8n tile.

[khối không người, với:]
palette = deep navy-slate and white, color only from the two logos
exact text = "N8N HẾT KHÓ" and the "+" sign
```
