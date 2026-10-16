"""Contact sheet: put many images in one labeled 16:9 grid, so a single image read shows them all.

  python sheet.py sheet-1.jpg "refs/0*.jpg" --cols 2                 # read the reference thumbnails
  python sheet.py faces.jpg "faces/*.png" --cols 4                   # pick face photos (transparent PNG goes on grey)
  python sheet.py review.jpg refs/01-x.jpg out/b01.png refs/05-y.jpg out/b05.png --cols 2   # pairs: reference | new
  python sheet.py review-all.jpg "out/b*.png" --cols 3 --no-labels   # final grid

Each cell is 16:9 and the whole image is fitted inside (nothing is cropped). Labels are the file names.
Quoted globs are expanded here, so it works the same in bash and PowerShell.
"""
import argparse
import glob

from PIL import Image, ImageDraw, ImageFont


def font(size):
    for name in ("arial.ttf", "Arial.ttf", "DejaVuSans.ttf", "Helvetica.ttc"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def fit(im, w, h):
    """Scale the whole image into a w x h cell, letterboxed on the sheet background."""
    im = im.copy()
    im.thumbnail((w, h), Image.LANCZOS)
    cell = Image.new("RGB", (w, h), (20, 20, 20))
    cell.paste(im, ((w - im.width) // 2, (h - im.height) // 2))
    return cell


def load(path):
    im = Image.open(path)
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGBA", im.size, (128, 128, 128, 255))
        bg.alpha_composite(im)
        im = bg
    return im.convert("RGB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("images", nargs="+")
    ap.add_argument("--cols", type=int, default=3)
    ap.add_argument("--width", type=int, default=640, help="cell width in px (default 640)")
    ap.add_argument("--no-labels", action="store_true")
    args = ap.parse_args()

    files = []
    for pattern in args.images:
        files += sorted(glob.glob(pattern)) if any(c in pattern for c in "*?[") else [pattern]
    if not files:
        raise SystemExit("no images matched")

    w, h, gap = args.width, args.width * 9 // 16, 10
    rows = (len(files) + args.cols - 1) // args.cols
    sheet = Image.new("RGB", (args.cols * (w + gap) - gap, rows * (h + gap) - gap), (20, 20, 20))
    draw, f = ImageDraw.Draw(sheet), font(max(14, w // 28))
    for i, path in enumerate(files):
        x, y = (i % args.cols) * (w + gap), (i // args.cols) * (h + gap)
        sheet.paste(fit(load(path), w, h), (x, y))
        if not args.no_labels:
            label = path.replace("\\", "/").split("/")[-1]
            draw.text((x + 8, y + 6), label, fill=(255, 230, 0), font=f, stroke_width=2, stroke_fill=(0, 0, 0))
    sheet.save(args.out, quality=85)
    print(f"{args.out} | {len(files)} images | {sheet.width}x{sheet.height}")


if __name__ == "__main__":
    main()
