# Bẫy đã gặp

Gặp thật trong lần làm 15 thumbnail kiểu Ben AI (14/10/2026). Mỗi dòng: hiện tượng, nguyên nhân, cách sửa.

## Mặt

- **Mặt ra như người mẫu.** Lần test đầu, mặt dài hơn, hàm vuông, nhìn già và "đẹp trai chung chung" hơn người thật. Chỉ đưa ảnh tham chiếu là chưa đủ. Sửa: tả đặc điểm thật vào `[face features]` (dáng mặt, má, đường hàm, mí mắt, kiểu tóc, nét trẻ hay già), thêm câu cấm "do not make them look like a model". Chạy lại thì giống.
- **Kiểm mặt bằng ảnh so cạnh nhau.** Crop mặt ở ảnh tham chiếu và ở thumbnail, ghép cạnh nhau rồi mới kết luận giống hay không. Nhìn cả thumbnail dễ bị lừa.
- **Ảnh mặt nên là ảnh tách nền, chụp studio.** Ảnh webcam có nền phòng, chất lượng thấp cho mặt kém hơn. Mỗi lần đưa 2-3 ảnh, khác góc, cùng 1 người.
- **Đổi áo** ghi trong `wardrobe` kèm câu "(change from the black shirt in the references)". Không ghi thì model giữ áo trong ảnh mặt.

## Logo

- **Model tự vẽ logo là ra logo giả.** Mẫu "Fable 5.1 vs GPT 6" lần đầu ra ngôi sao 4 cánh thay cho logo Claude. Sửa: luôn tải logo thật và đưa vào làm ảnh tham chiếu, ghi vai trò "REAL asset, reproduce exactly".
- **App Store khớp nhầm app bên thứ ba.** Tìm "n8n" ra app "N8N Automations" của một hãng khác. `fetch_logo.py` giờ bắt buộc `--seller` khớp hãng phát hành. Tool không có app chính chủ thì dùng `--wiki` (Wikimedia Commons).
- **Favicon quá nhỏ.** Favicon n8n.io chỉ 48x48, đưa vào là mờ. `--domain` để làm đường cuối.
- **Logo dạng chữ dài** (n8n, Cursor) cần tách phần biểu tượng ra để đặt lên ô vuông app. Dùng `--icon`.
- **Tool không có logo chính thức** (vd model mới chưa có app): crop từ ảnh có sẵn, ghi rõ nguồn trong báo cáo cho user biết.
- Tải xong luôn mở ảnh ra xem, ghép 1 sheet các logo để kiểm 1 lượt.

## UI

- **UI vẽ kiểu 3D hoạt hình nhìn giả.** User chê "vẽ lên nhìn giả". Sửa: crop UI thật từ frame video của chính video đó (ffmpeg trích frame), từ ảnh render, hoặc screenshot app, rồi đưa vào làm ảnh tham chiếu.
- **Crop dính mẩu chữ bị cắt.** Thumbnail showroom 3D còn dính chữ "no G-" ở mép màn hình laptop vì khung crop cắt ngang 1 dòng chữ. Crop sạch theo mép khung UI, mở ảnh crop ra xem trước khi dùng.
- **Nhân vật/mascot**: viết "macro photo of real painted clay or plastic miniatures, not a cartoon, not a game render" để ra như đồ thật chụp macro.

## Màu

- **Ép màu brand cho mọi ảnh làm thumbnail lệch gu.** Lần test đầu ép 1 màu brand cho cả 3 mẫu, user đổi ý: màu tự do, lấy từ logo tool chính của video (Claude ra cam, ChatGPT ra navy). Hỏi user ở bước 0, đừng mặc định màu brand.

## Bố cục và chữ

- **Model tự thêm thứ không có trong prompt.** 1 mẫu tự vẽ thêm card website ở góc phải dưới. Sửa: câu "Do not add any graphic, card, icon or UI that is not described in LAYOUT" nằm sẵn trong khối chung.
- **Góc phải dưới phải trống** vì YouTube đè thời lượng video lên đó. Chữ dài vẫn có thể lấn vào (mẫu "COPY BỘ AI NÀY" bị chữ "NÀY" lấn). Kiểm từng ảnh.
- **Số 0 ra giống chữ O.** "0 ĐỒNG" ra 2 lần đều trông như "O ĐỒNG", dù prompt đã dặn. Tránh số 0 đứng riêng trong chữ lớn, hoặc đổi chữ (vd "MIỄN PHÍ").
- Chữ tiếng Việt có dấu ra đúng ở cả 15 mẫu khi prompt ghi rõ "Spell it exactly, with correct diacritics".

## Codex

- **image_gen nhận tối đa 5 ảnh tham chiếu.** Lần đầu 3 mẫu gửi 6-9 ảnh bị từ chối, mất khoảng 75k token vô ích. `gen_thumb.py` giờ tự gộp ảnh dư vào 1 tấm sheet có nhãn A), B), C).
- **Chi phí:** mỗi ảnh khoảng 23-46k token quota Codex. 12 mẫu tốn khoảng 488k token. Chạy song song tối đa 4 job.
- **Thời gian:** 1 ảnh khoảng 1,5-3 phút. 12 ảnh chạy 4 job/lượt mất khoảng 6 phút.
- **Gói ChatGPT Free không có tool tạo ảnh trong Codex CLI** (đã thử). Cần gói trả phí.
- Codex trả exit 0 cả khi không ra ảnh. Luôn kiểm file `out/<tên>.png` có tồn tại, không có thì đọc `out/<tên>.log`.

## Windows

- Python in tiếng Việt ra console lỗi `UnicodeEncodeError: 'charmap'`. Đặt `PYTHONIOENCODING=utf-8` hoặc ghi ra file với `encoding="utf-8"`.
- Không pipe ghi đè `prompts.md` bằng script đọc chính nó. Lần làm gốc đã lỡ làm trống file này. Sửa `prompts.md` bằng Edit.
