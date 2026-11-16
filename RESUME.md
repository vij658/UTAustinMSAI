# Resume here (written 2026-11-16)

What this is: video learning roadmap for Sankar (UT Austin online MSAI, Spring 2027; goal: design large-scale GenAI tech stacks). Tracks are markdown in `tracks/`; `python3 tools/build_html.py` builds `html/` (index plus one page per track). `tools/checkpoint.sh "message"` rebuilds and commits.

## Rebuild from the Project copy
Create a folder with `tracks/*.md`, `ROADMAP.md`, `tools/build_html.py`, run `python3 tools/build_html.py` (needs `pip install markdown`). Tracks: A math, B AI/ML concepts, C GenAI stack, D tech stack (bike), E tech stack (desk), F UT course tracker, G end-to-end GenAI (F and G are being built; the builder skips missing files).

## Rules that carry over
- Nothing was watched. "Verified" means YouTube oEmbed returned the same ID, title and channel. Lengths are filled only where seen.
- Keep roadmap videos out of his YouTube watch history (standing preference). Do not open or play videos in his signed-in browser. For lengths use cookie-less fetches of watch-page HTML from a youtube.com tab, paced about 30 seconds apart, and only with his history paused.
- One research agent at a time, and tell him before each starts (three at once hit the rate limit).
- GitHub push is blocked (invalid token). Needs an empty `MSAIAtlas` repo and a working token.

## State at this checkpoint
- A 62, B 57, C 58, D 53, E 47 main-path videos; gap-fill passes 1 and 2 done for A, B, C.
- In progress: Track F (one UT course per block, 14 courses; part 1 = courses 1-6 by an agent, part 2 = courses 7-14 still to do, then elective ranking), then Track G (end-to-end GenAI, stages 0-12: build map, language-model basics, pretraining, post-training, adaptation, inference and serving, grounding and RAG, agents and tools, multimodal and diffusion, evaluation, safety and governance, LLMOps and platform, capstone designs; reuse verified rows from A-E and add new videos only for gaps).
- In progress: a paced length lookup (about 187 videos) held in a Chrome tab; results are written into the tracks when it finishes.
