# Resume here (written 2026-11-16)

What this is: video learning roadmap for Sankar (UT Austin online MSAI, Spring 2027; goal: design large-scale GenAI tech stacks). Tracks are markdown in `tracks/`; `python3 tools/build_html.py` builds `html/` (index plus one page per track). `tools/checkpoint.sh "message"` rebuilds and commits.

## Rebuild from the Project copy
Create a folder with `tracks/*.md`, `ROADMAP.md`, `tools/build_html.py`, run `python3 tools/build_html.py` (needs `pip install markdown`). Tracks: A math, B AI/ML concepts, C GenAI stack, D tech stack (bike), E tech stack (desk), F UT course tracker, G end-to-end GenAI (G is being built; the builder skips missing files).

## Rules that carry over
- Nothing was watched. "Verified" means YouTube oEmbed returned the same ID, title and channel. Lengths are filled only where seen.
- Keep roadmap videos out of his YouTube watch history (standing preference). Do not open or play videos in his signed-in browser. For lengths use cookie-less fetches of watch-page HTML from a youtube.com tab, paced about 30 seconds apart, and only with his history paused.
- One research agent at a time, and tell him before each starts (three at once hit the rate limit).
- GitHub: repo is vij658/UTAustinMSAI (public, created by the user on 2026-11-16). The shell's `gh` login is invalid, but attaching the repo to the session (add_repo tool, push access) lets plain `git push origin main` work through the session proxy. Commit authors are only Claude <noreply@anthropic.com>; keep personal email out of commits. No employer or sensitive details belong in this public repo.

## State at this checkpoint
- A 62, B 57, C 58, D 53, E 47 main-path videos; gap-fill passes 1 and 2 done for A, B, C.
- Done: Track F (UT course tracker: 14 courses, 93 main videos, elective ranking at the top of the file). Track G part 1 (Blocks 0-6: build map, language-model basics, pretraining, post-training, adaptation, inference and serving, grounding and RAG; 40 main videos) is written and committed. In progress: Track G part 2 (Blocks 7-12 plus Gaps, Not checked, morning list, intro counts); the file ends with `<!-- STAGES 7-12 GO HERE -->` until it lands. Then: update ROADMAP.md for Track G, fill lengths, send files.
- In progress: a paced length lookup (187 videos, paced 30-35 s) held in a Chrome tab; results (video id -> seconds) go into the tracks with scratchpad `merge_lengths.py` (replaces the Length cell with the measured time plus '(per YouTube page, 2026-11-16)'). After it finishes, run the same lookup for Track F and G IDs that are not in A-E, recompute total hours, replace the 30-minute-per-video guess in ROADMAP.md.
