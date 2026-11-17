# Resume here (updated 2026-11-17)

What this is: video learning roadmap for Sankar (UT Austin online MSAI, Spring 2027; goal: design large-scale GenAI tech stacks). Tracks are markdown in `tracks/`; `python3 tools/build_html.py` builds `html/` (index plus one page per track). `tools/checkpoint.sh "message"` rebuilds, commits and pushes.

## Rebuild from the Project copy
Create a folder with `tracks/*.md`, `ROADMAP.md`, `tools/build_html.py`, run `python3 tools/build_html.py` (needs `pip install markdown`). Tracks: A math, B AI/ML concepts, C GenAI stack, D tech stack (bike), E tech stack (desk), F UT course tracker, G end-to-end GenAI (13 stages, Blocks 0-12). The builder skips missing files.

## Rules that carry over
- Nothing was watched. "Verified" means YouTube oEmbed returned the same ID, title and channel. A length means it was read from that video's YouTube watch page (no cookies, nothing played).
- Keep roadmap videos out of his YouTube watch history (standing preference). Do not open or play videos in his signed-in browser. For lengths use cookie-less fetches of watch-page HTML from a youtube.com tab (`credentials:'omit'`), paced about 30 seconds apart, only with his history paused, and stop on 429 or 403. Never delete history without asking.
- One research agent at a time, and tell him before each starts (three at once hit the rate limit).
- GitHub: repo is vij658/UTAustinMSAI (public, created by the user on 2026-11-16). The shell's `gh` login is invalid, but attaching the repo to the session (add_repo tool, push access) lets plain `git push origin main` work through the session proxy. Commit authors are only Claude <noreply@anthropic.com>; keep personal email out of commits. No employer or sensitive details belong in this public repo.
- Do not edit his Project doc `UT_MSAI_Todo.md` without his approval; proposed edits only (see the end of this file).

## State (2026-11-17)
- Tracks A-E: 62, 57, 58, 53, 47 main-path videos; every length measured; stale "length ?" wording replaced; main-path hours A 22 h 41 m, B 39 h 55 m, C 41 h 53 m, D 33 h 35 m, E 31 h 08 m.
- Track F (UT courses): 15 courses (Block 15 = Agentic Software Engineering, added from the handbook), 98 main rows. The 2027-2028 MSAI Student Handbook (he supplied it) has been merged: course numbers, only Ethics in AI required, prerequisites, coordinator questions. The Spring 2027 offering list is NOT in the handbook; it comes from his program email of 2026-11-16 (recorded in his to-do).
- Track G (end-to-end GenAI): complete, 13 stages, 76 main rows, 124 rows, 121 distinct videos.
- HTML builder has `fix_lists()` so lists under bold labels render as lists.
- ROADMAP.md is regenerated from measured numbers by the scratchpad script `build_roadmap.py`; MORNING.md lists pages I could not open.

## Length lookup status
- 377 lengths (all A-E ids) merged on 2026-11-16/17. The remaining 123 ids (Tracks F and G only) were being looked up 30-35 s apart in a Chrome tab on 2026-11-17; see the final commit message for whether it finished. Results go into the tracks with `merge_lengths.py` (replaces the Length cell with `H:MM:SS`), then `patch_fg.py` rewrites the F and G counts and wording.

## Proposed edits to his to-do (not applied)
- Section 9a: refund wording (a Q-drop from day 13 has no refund) and the coordinator-drop wording, to match the handbook; add or drop the refund sentence as he prefers.
- Replace "Foundational" with the handbook's wording: only Ethics in AI is required; the other nine courses are free electives.
- Ask whether AI in Astrophysics is offered (the handbook lists it, the program email does not).
