"""Download the N newest video thumbnails of a YouTube channel (Shorts excluded).

Usage (from the project folder):
  python fetch_channel_thumbs.py https://www.youtube.com/@BenAI92 --n 15

Output: refs/01-<videoId>.jpg ... (01 = newest) and refs/list.txt (number | id | title).
Needs yt-dlp on PATH. Tries maxresdefault.jpg (1280x720), falls back to hqdefault.jpg.
"""
import argparse
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path


def download(video_id):
    for size in ("maxresdefault", "hqdefault"):
        try:
            with urllib.request.urlopen(f"https://i.ytimg.com/vi/{video_id}/{size}.jpg", timeout=20) as r:
                return r.read(), size
        except urllib.error.HTTPError:
            continue
    return None, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("channel", help="channel URL, e.g. https://www.youtube.com/@BenAI92")
    ap.add_argument("--n", type=int, default=15, help="how many newest videos (default 15)")
    ap.add_argument("--out", default="refs", help="output folder (default refs)")
    args = ap.parse_args()

    ytdlp = shutil.which("yt-dlp")
    if not ytdlp:
        sys.exit("yt-dlp not found on PATH")
    url = args.channel.rstrip("/")
    if not url.endswith(("/videos", "/streams")):
        url += "/videos"
    r = subprocess.run([ytdlp, "--flat-playlist", "--playlist-end", str(args.n), "--print", "%(id)s|%(title)s", url],
                       capture_output=True, text=True, encoding="utf-8")
    rows = [line.split("|", 1) for line in r.stdout.splitlines() if "|" in line]
    if not rows:
        sys.exit(f"no videos found\n{r.stderr[-800:]}")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    listing = []
    for i, (vid, title) in enumerate(rows, 1):
        data, size = download(vid)
        if data:
            (out / f"{i:02d}-{vid}.jpg").write_bytes(data)
        listing.append(f"{i:02d} | {vid} | {title}")
        print(f"{i:02d} {vid} {size or 'MISSING'}")
    (out / "list.txt").write_text("\n".join(listing) + "\n", encoding="utf-8")
    print(f"{len(rows)} thumbnails in {out}")


if __name__ == "__main__":
    main()
