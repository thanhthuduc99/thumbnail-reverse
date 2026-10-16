# Thumbnail kiểu <tên kênh>

Nguồn: <N> thumbnail mới nhất của <link kênh>, ảnh gốc trong `refs/`, danh sách trong `refs/list.txt`.

## 1. Kênh này làm thumbnail thế nào

Luật chung (đúng ở gần hết các ảnh):
- Số thành phần:
- Chữ (số từ, font, in hoa hay không, nội dung):
- Màu:
- Mặt (biểu cảm, hướng nhìn, cắt khung, áo, ánh sáng):
- Chi tiết lặp lại (mũi tên, nhãn dán, viền...):
- Logo và UI (thật hay vẽ):

Khuôn bố cục:

| Khuôn | Bố cục | Ảnh mẫu trong refs |
|---|---|---|
| A. | | |

Ngoài lề (ít dùng):

## 2. Màu và chất liệu

- Màu: <tự do theo logo/chủ đề, hoặc bảng màu brand>.
- Logo: tải bằng `fetch_logo.py` vào `assets/logos/`, mở ra xem rồi mới dùng.
- UI: crop từ frame video hoặc screenshot thật vào `assets/ui/`.

## Khối dùng chung

Dán khối này vào cuối mọi prompt có mặt người. Thay `[face features]` 1 lần ngay trong khối này. Các chỗ `[...]` còn lại điền theo từng thumbnail.

```
PERSON (identity is the top priority):
- The attached reference photos show the real person. Use them as the only source for their identity. Keep their exact face shape, eyes, eyelids, eyebrows, nose, lips, jawline, ears, skin tone and hairstyle. They must be instantly recognizable as the same person.
- Their real features, keep them: [face features]. Do not make them look like a model, and do not make them look older than in the photos.
- Light professional retouch only: even skin tone, less shine, softer under-eye shadows, tidy hair. Keep real skin texture and pores. No beauty filter, no face slimming, no bigger eyes, no plastic or airbrushed look.
- Expression: [expression].
- Wardrobe: [wardrobe].
- Photo style: real studio portrait, soft key light from front-left, subtle warm rim light on hair and shoulders, 85mm lens, slight film grain. The person is cut out cleanly and blended into the background with matching light.

STYLE:
- Premium tech-creator YouTube thumbnail. Maximum 3 elements: the person, the headline, one graphic.
- Headline font: very heavy geometric sans-serif (like Montserrat Black), all caps, tight line spacing, soft dark drop shadow.
- Colors: [palette].
- Real assets: every logo and UI in the image comes from the attached asset images. Show them as real crisp app icons and real screenshots, with their original colors, shapes and layout. Never invent a logo. Never redraw UI as a flat illustration or a 3D cartoon.
- Large and readable at phone size. Keep the bottom-right corner free of text and key graphics.
- Do not add any graphic, card, icon or UI that is not described in LAYOUT.

TEXT RULES:
- The only new text in the image is [exact text]. Spell it exactly, with correct diacritics.
- Text that already exists inside an attached UI screenshot stays as it is. No other text, letters, numbers, logos or watermarks anywhere.
```

Khối cho mẫu không có người (đánh dấu `[khối không người, với:]`):

```
STYLE:
- Premium tech-creator YouTube thumbnail. No people.
- Headline font: very heavy geometric sans-serif (like Montserrat Black), all caps, tight line spacing, soft dark drop shadow.
- Colors: [palette].
- Real assets: every logo and UI in the image comes from the attached asset images. Show them as real crisp app icons and real screenshots, with their original colors, shapes and layout. Never invent a logo. Never redraw UI as a flat illustration or a 3D cartoon.
- Large and readable at phone size. Keep the bottom-right corner free of text and key graphics.
- Do not add any graphic, card, icon or UI that is not described in LAYOUT.

TEXT RULES:
- The only new text in the image is [exact text]. Spell it exactly, with correct diacritics.
- Text that already exists inside an attached UI screenshot or logo stays as it is. No other text, letters, numbers, logos or watermarks anywhere.
```

## Prompt

Mỗi mẫu 1 mục `### bNN, khuôn X: <chủ đề>`, `NN` = số thứ tự ảnh mẫu trong `refs/` đang mô phỏng. Mỗi mục có 2 khối code: lệnh `gen_thumb.py`, rồi prompt (LAYOUT + `[khối ..., với:]` + các dòng `key = value`).

### b01, khuôn A: <chủ đề>

```
python $S/gen_thumb.py b01 --face face1.png face2.png face3.png --asset "real screenshot: <mô tả>=assets/ui/<file>.png"
```

```
Create a photorealistic YouTube thumbnail, 16:9 landscape.

LAYOUT:
- Background: <màu, chất liệu, vignette>.
- Right 38% of the frame: the person from the reference photos, chest-up, head large (about 45% of frame height), body cut off by the bottom edge, facing the camera.
- Top-left: headline in two lines, pure white: "<DÒNG 1>" on line 1, "<DÒNG 2>" on line 2.
- Bottom-left: the attached real screenshot as a floating app window, tilted very slightly, with a soft drop shadow. Keep its layout exactly as in the screenshot.
- A white hand-drawn curved arrow from the end of the headline down to the window.

[khối prompt chung, với:]
expression = warm confident smile with teeth, eyes looking straight into the lens
wardrobe = plain black crew-neck t-shirt
palette = <màu chủ đạo + nền>
exact text = "<DÒNG 1>" and "<DÒNG 2>"
```
