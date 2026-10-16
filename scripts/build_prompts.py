"""Build prompts/<name>.txt from prompts.md (run from the project folder).

Each "### <name>, ..." section under "## Prompt" holds 2 code blocks: the gen_thumb command, then the prompt.
A marker line "[khối prompt chung, với:]" or "[khối không người, với:]" pulls in the matching shared block from
"## Khối dùng chung" and fills it with the "key = value" lines below the marker.

Usage: python build_prompts.py
"""
import re
import sys
from pathlib import Path

ROOT = Path.cwd()
PLACEHOLDERS = r"\[(?:expression|wardrobe|palette|exact text|face features)\]|<[^<>\n]+>"

md = (ROOT / "prompts.md").read_text(encoding="utf-8")
if "## Khối dùng chung" not in md or "## Prompt" not in md:
    sys.exit("prompts.md needs the sections '## Khối dùng chung' and '## Prompt' (copy template/prompts.md)")
shared = md.split("## Khối dùng chung")[1].split("\n## ")[0]
face_block, noface_block = re.findall(r"```\n(.*?)```", shared, re.S)[:2]
SHARED = {"[khối prompt chung, với:]": face_block, "[khối không người, với:]": noface_block}
(ROOT / "prompts").mkdir(exist_ok=True)

for section in re.split(r"^### ", md.split("## Prompt")[1], flags=re.M)[1:]:
    name = section.split(",")[0].strip()
    blocks = re.findall(r"```\n(.*?)```", section, re.S)
    if not blocks:
        continue
    prompt = blocks[-1]
    for mark, block in SHARED.items():
        if mark in prompt:
            layout, params = prompt.split(mark)
            for line in params.strip().splitlines():
                key, value = line.split(" = ", 1)
                block = block.replace(f"[{key.strip()}]", value.strip())
            prompt = layout.rstrip() + "\n\n" + block
    leftover = re.findall(PLACEHOLDERS, prompt)
    if leftover:
        sys.exit(f"{name}: unfilled {leftover}")
    (ROOT / "prompts" / f"{name}.txt").write_text(prompt.strip() + "\n", encoding="utf-8")
    print(f"prompts/{name}.txt")
