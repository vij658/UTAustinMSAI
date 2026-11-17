# MSAI + GenAI Architect Roadmap: the bike-video plan

For Sankar. One hour a day on the stationary bike, watching, to build mental models before the UT Austin online MS in AI starts (Spring 2027) and while growing toward the goal of designing large-scale GenAI tech stacks for big companies (coding + architecture + AI).

Written 2026-11-09 to 2026-11-17. Status: **draft 3.** Eight tracks (A to H): seven to watch and learn from, and Track H to build with. Every video was checked to exist and its length was read from its YouTube page; none was watched. See "How much to trust this" before relying on any number.

## 1. What is in this folder

| File | What it is | Main-path videos | Optional |
|---|---|---|---|
| [tracks/A-ai-math.md](tracks/A-ai-math.md) | AI math: notation, calculus, linear algebra, multivariable calculus, probability, statistics, optimization, light discrete math | 47 (Blocks 0-7), plus 15 from gap-fill passes 1 and 2 (rows G1-G15) | 20 "optional extras" |
| [tracks/B-ai-ml-concepts.md](tracks/B-ai-ml-concepts.md) | AI/ML concepts in the order of the UT foundational courses: ML, deep learning, transformers, RL, planning, ethics, generative models | 48 (Blocks 1-8), plus 9 bike videos from gap-fill passes 1 and 2 (rows G1-G7, G9, G11; G8 and G10 are optional) | 30 (about 12 are desk-only) |
| [tracks/C-genai-stack.md](tracks/C-genai-stack.md) | The GenAI stack and enterprise architecture: stack map, LLMs for architects, prompting, RAG, agents/MCP, evals, security and governance, serving and cost, AWS GenAI, large-company patterns | about 50 (Blocks 0-9; the table has 51 rows), plus 8 from gap-fill pass 1 (rows G1-G8) | 8 desk videos |
| [tracks/D-tech-stack-bike.md](tracks/D-tech-stack-bike.md) | The general enterprise tech stack, bike path: stack map, distributed systems, data layer, APIs and messaging, cloud-native platform, security and identity (fast lane), reliability and observability, data and ML platform, architecture judgment and case studies | 53 (Blocks 0-8) | 32 (3 desk) |
| [tracks/E-tech-stack-desk.md](tracks/E-tech-stack-desk.md) | The same stack layers at the desk: hands-on and diagram-heavy videos, each block ending in a lab (draw it, run it, defend it). Cloud-neutral and open-source tools, Java/Spring where possible; not AWS service tutorials | 47 (Blocks 0-7, all DESK) | 24 |
| [tracks/F-ut-courses.md](tracks/F-ut-courses.md) | UT Austin MSAI course tracker: one block per course (all 15 in the handbook), each with the official description, free public materials, a short prep and companion video path, and recap questions; opens with an elective ranking for the GenAI-architect goal and questions for the program coordinator | 98 (Blocks 1-15; 48 are reused from Tracks A-C and G) | 50 |
| [tracks/G-genai-end-to-end.md](tracks/G-genai-end-to-end.md) | The end-to-end spine: 13 stages from how a model is made to how a governed GenAI system runs in production (build map, language-model basics, pretraining, post-training, adaptation, inference and serving, grounding and RAG, agents and tools, multimodal and diffusion, evaluation, safety and governance, LLMOps and platform, capstone designs). About 70% of its rows are reused from Tracks A to F; each block ends with a build step on one thread project | 76 (Blocks 0-12) | 48 |
| [tracks/H-genai-build-projects.md](tracks/H-genai-build-projects.md) | Build GenAI projects, one layer at a time: follow-along build videos (type along, run, get a working result) that start with one script calling a model and grow, block by block, into a full GenAI service on AWS (API, RAG, database, tools and agents, auth and gateway, ECS, domain and HTTPS, CloudFront and WAF, Bedrock, queues and cache, tracing and evals, guardrails, Terraform and CI/CD). Opens with a mental model of one request through the whole stack, a 23-block ladder with a progression check per block, and four milestone projects; one thread project, DocDesk, grows through every block | 87 (Blocks 0-22; 62 DESK) | 44 |

Every block in every track has: why it matters, an ordered table (title, channel, link, length, level, mode, what you will get, status), a "full circle" line, and three recap questions with hidden answers. Each track ends with **Gaps** (topics where no good video was found) and **Not checked**.

Tags: **Level** = Start / Deeper / Scholar. **Mode** = BIKE (you can mostly listen) or DESK (needs code, paper or pausing, so it never uses up a ride).

## 2. How much to trust this

- **Verified means "exists".** For each video the YouTube oEmbed lookup returned the same video ID, and titles and channels are copied exactly as returned. Nobody watched the videos. "What you will get" comes from titles, chapter lists and the channel's usual format.
- **Lengths are measured.** Between 2026-11-16 and 2026-11-17 I read each video's length from its public YouTube page, without cookies, with your watch history paused and nothing played, and, after the first 190 requests went out back to back, I spaced the rest about 30 seconds apart at your request. No request was blocked. 484 of the 484 distinct videos in the tracks have a length this way; none are missing. The tables show the measured length; the older notes in the track files about lengths taken from chapter markers or conference pages were replaced.
- **Hours of the main path, by track** (different videos counted per track, so a video shared with another track is counted in both; a video used twice inside one track counts once, which is why F has 98 main rows but 96 videos and G 76 rows but 74 videos; the optional column is the optional videos not already on the main path):

| Track | Main-path videos | Main-path hours | Optional hours |
|---|---|---|---|
| A math | 62 | 22 h 41 m | 12 h 32 m |
| B AI/ML concepts | 57 | 39 h 55 m | 32 h 27 m |
| C GenAI stack | 58 | 41 h 53 m | 14 h 08 m |
| D tech stack (bike) | 53 | 33 h 35 m | 22 h 35 m |
| E tech stack (desk) | 47 | 31 h 08 m | 15 h 23 m |
| F UT courses | 96 | 77 h 58 m | 38 h 31 m |
| G end-to-end GenAI | 74 | 46 h 16 m | 39 h 12 m |
| H build projects (desk) | 87 | 41 h 37 m of video | 20 h 39 m |

  Counting each video once, the main paths of Tracks A to G together are 350 videos and 233 h 54 m (174 h 02 m of BIKE rows and 59 h 51 m of DESK rows, by the mode of the first track that lists each video). Track H adds 71 main-path videos not on any other main path (32 h 44 m of video); its hours are video time only, and building along takes two to four times as long.
- **What to plan with.** At one hour of riding a day, Track A's main path is about 22 h 41 m of listening, Track G's about 46 h 16 m. Tracks A and G together (the shortest route to both the math and the end-to-end stack) are 136 distinct videos and about 68 h 58 m; adding Track B makes 179 videos and about 99 h 49 m. Real riding is slower than listening time: pauses, rewinds and recap questions add time, and lectures such as Karpathy's *Deep Dive into LLMs* (3 h 31 m) take several rides on their own. Re-plan after the first week.
- **Level and Mode tags** are judgement calls, not lookups.
- **Tools change fast.** In Track C, anything published before 2025 is flagged "may be dated" in its table, and even 2025 material on frameworks and services can be a release or two behind by now.

## 3. The routine (bike mode)

1. **Ride:** about an hour of videos, in table order, from the block you are on. Lengths are measured now: Track A videos average 22 minutes (two or three per ride), Tracks B and C about 42 minutes (one or two per ride). Watch the intuition video before the lecture; the tables are already ordered that way.
2. **Right after:** answer that block's recap questions out loud, then open the hidden answers. Missed one? Re-watch only that video. Do not push on.
3. **One line of notes:** "what hurt, and what fixed it" for each video. If you keep this habit, the Atlas style of thinking carries over directly.
4. **Desk items are optional.** Never let a DESK video eat a ride. Save them for a weekend session, if at all. Track E is the desk path: one block per weekend session, after the Track D block it pairs with.
5. **If you fall behind, cut in this order:** optional lists first, then Track A Block 7 (discrete math), then Track B Blocks 7-8, then Track E labs you have not reached, then the later Track C blocks. Never cut the first three blocks of Track C, or Track A Blocks 1-6: the rest builds on them.
6. **Keep the roadmap out of your main YouTube history.** Watch on a separate Chrome profile or a second Google or brand account signed in on the bike monitor. Playlists for the Atlas step should be created on that account too. Adding to a playlist does not touch watch history; playing does.

## 4. Order of play

Two lanes run in parallel so the math and the goal both move every week.

- **Lane M (math and ML), 4 rides a week:** Track A in block order, then Track B Blocks 1-3.
- **Lane G (GenAI stack), 2 rides a week:** Track C in block order.
- Week layout: Monday-Thursday Lane M, Friday-Saturday Lane G, Sunday rest or catch-up. Your AWS reading at the desk (see section 6) is separate from the bike.

### Before January (about 8 weeks)

Rides are about an hour, six a week (Monday to Saturday). The hours below are the measured main-path lengths of each block; optional rows and gap-fill rows are extra. Re-plan after week one: pauses and rewinds make real pace slower than the measured lengths.

| Weeks | Lane M | Lane G |
|---|---|---|
| 1-2 | A0 notation and warm-up; A1 calculus | C0 the big picture; C1 LLMs for architects (watch 1.1 to 1.3 now; treat the 3 h 31 m deep dive 1.4 as its own run of rides later) |
| 3-4 | A2 vectors and linear algebra (10 videos, the biggest block); A3 multivariable calculus | C1 finish; C2 prompting and structured outputs (add G1, G2 and G3 from the gap-fill section; the track file says where each one goes) |
| 5 | A4 probability | C3 embeddings and RAG (start) |
| 6 | A5 statistics; A6 optimization (start) | C3 finish |
| 7 | A6 finish; B1 what AI/ML is | C4 agents and tools (start) |
| 8 | B2 classical ML (start) | C4 finish |

That targets A0-A6 (43 videos, 13 h 46 m), B1-B2 (18 videos, 7 h 04 m) and C0-C4 (22 videos, 15 h 57 m, plus the gap-fill rows G1-G3, 1 h 58 m). Lane M has about 32 rides in eight weeks and needs about 21 for A0-A6 and B1-B2 (Track A's two gap-fill passes add 3 h 55 m if you want them); Lane G has about 16 rides and needs about 18 for C0-C4 with G1-G3, so Lane G is the tight one: if it slips, move C4 into January and keep C0-C3. If Lane M has room, take B2 slowly; if not, B2 and B3 slip into the semester. That is fine: B2 and B3 are the preview of the UT Machine Learning and Deep Learning courses.

### The tech-stack paths (Track D bike, Track E desk)

Track D is the general enterprise stack that sits under the GenAI stack (Track C). Track E is the same layers done at the desk, each block ending in a lab. The rule is: watch a D block on the bike, then do its E block at the desk, and watch the C block it feeds. This is the dependency map:

| Track D block (bike) | Track E block (desk) | Feeds Track C block |
|---|---|---|
| D0 stack map | E0 drawing and designing systems | C0 big picture |
| D1 distributed systems | (covered inside E1 and E2 labs) | C7 serving and cost (latency, caching) |
| D2 data layer | E1 data layer lab | C3 embeddings, vector search and RAG |
| D3 APIs and messaging | E2 APIs and messaging lab | C4 agents and tools |
| D4 cloud-native platform | E3 cloud-native lab | C7 customization and serving |
| D5 security and identity (your fast lane) | E4 security and observability lab | C6 safety, security and governance |
| D6 reliability and observability | E4 security and observability lab | C5 evaluation and observability |
| D7 data and ML platform | E5 data and ML platform lab | C7 serving, C6 governance |
| D8 architecture judgment | E6 system-design walkthroughs, E7 GenAI-era designs | C9 enterprise architecture at scale |

**Time reality.** The four bike tracks (A to D) hold 230 main-path videos and 138 h 04 m of measured listening (A 22 h 41 m, B 39 h 55 m, C 41 h 53 m, D 33 h 35 m). At an hour a ride that is about 138 rides, roughly four and a half months of daily riding, so everything cannot fit before January. Suggested order: finish A0-A4 and C0-C2 first as planned, then make Lane G alternate: a D block, then the C block it feeds (D2 before C3, D3 before C4, D6 before C5, D5 before C6, D4 and D7 before C7). Do the E blocks on weekends, one per weekend, and alternate them with your AWS desk study rather than adding to it. Re-plan after week one: your real pace, with pauses and rewinds, will be slower than the measured lengths.

### Track G: the end-to-end spine

Track G puts the whole life of a GenAI system in the order you would build and run one: how a model is made (Blocks 1-3), how you adapt and serve it (4-5), how you ground it in your documents (6), how it acts (7), what else it can handle (8), how you know it works (9), how you keep it safe and governed (10), how you operate it (11) and how you draw and defend the whole design (12). It reuses about 70% of its rows from Tracks A to F and adds new videos only where a stage had a gap, so a video you have watched anywhere is ticked everywhere on the HTML pages (progress is kept by video ID). Each block names what to have watched first (for example A4 probability and B4 transformers before Block 1) and ends with a 1 to 3 hour build step on one thread project: an enterprise knowledge assistant for a fictional bank, using public data only and nothing from work.

| Block | Stage | Build step (first sentence; Block 8 has an optional try-it instead) |
|---|---|---|
| 0 | The build map | Set up the folder and the charter for the thread project, an enterprise knowledge assistant for a fictional bank, using only public data. |
| 1 | Language-model basics | Train a tiny GPT from scratch on a small public text, and learn what "it works" means for a language model. |
| 2 | Pretraining | Run a miniature pretraining pipeline on your Block 1 corpus and compare tokenizers fairly. |
| 3 | Post-training and alignment | Write instruction and preference data for the assistant and run a small supervised pass, so that post-training is something you have done, not only read. |
| 4 | Adaptation | Compare four ways of adapting the assistant on the same questions, then shrink the winner. |
| 5 | Inference and serving | Serve the quantized model from Block 4 behind an OpenAI-compatible endpoint and measure how it behaves under load. |
| 6 | Grounding and RAG | Ground the assistant on your public-document corpus and measure retrieval, not just answers. |
| 7 | Agents and tools | Turn the grounded assistant from Block 6 into an agent with three tools, and expose the same tools through an MCP server. |
| 8 | Multimodal and diffusion | See how a vision-language model reads a scanned form, and how it fails. |
| 9 | Evaluation | Score the assistant on one golden set with rules and an LLM judge, check the judge against your own labels, and compare two variants. |
| 10 | Safety and governance | Add authorization, input and output guardrails and an audit trail to the assistant, then attack it with a red-team list and write its model card. |
| 11 | LLMOps and platform | Put the assistant behind an open-source gateway, with a trace for every question, a per-request cost log and a prompt that is versioned and gated. |
| 12 | Capstone designs | Draw and defend the whole-stack design of the thread project, and write it up in two pages. |

My suggestion, not a rule: do Track A Blocks 0-4 and Track C Blocks 0-2 first, as planned above, then let Lane G follow Track G in order and keep Tracks B to F as the library behind it (Track F for the courses you are about to take, Tracks D and E for the enterprise layers under the stack). Block 8 (multimodal and diffusion) has no build step and can wait. Track G's main path is 76 videos and about 46 h 16 m.
### Track H: build it yourself (desk)

Tracks A to G are for watching; Track H is for building. It starts with the mental model of one request through a real GenAI system (internet, DNS, CDN and firewall, gateway, auth, API, orchestration, model, data, and the production layers around them), then climbs a 23-block ladder where each block adds one layer to a project you keep: DocDesk, an assistant over public bank-style PDFs. The 22 build blocks form four milestone projects, each a complete system:

| Milestone | Blocks | What runs at the end | Video time |
|---|---|---|---|
| 1. A chat app with its own API | 1-6 | web chat, FastAPI, structured output, hosted or local model | 5 h 26 m |
| 2. A document assistant with tools | 7-13 | RAG with citations, Postgres + pgvector, tools, an agent, an MCP server, login and an Nginx front door, all in Docker Compose | 11 h 56 m |
| 3. The same system on AWS | 14-17 | ECS Fargate, RDS, S3, secrets, your domain over HTTPS through CloudFront, WAF and a load balancer, Bedrock | 7 h 31 m |
| 4. A production-grade service | 18-22 | queues, cache and streaming; traces, cost and evals; guardrails; Terraform and a pipeline with an eval gate; Cognito; a design document | 15 h 59 m |

How it fits: Track H is desk work, so it never uses up a ride. A natural pairing is to ride the Track C or G block on a topic, then build the matching Track H block at the desk the same week (for example C3 or G6 on RAG, then H7-H8). Milestone 1 fits before January alongside the plan above if you have desk evenings; Milestone 3 onward costs money on AWS, so Block 14 sets a budget alarm before anything is created, and every cloud block ends with what to delete.

### During the semester

| Track block | Why now |
|---|---|
| B2, B3 | Ahead of the UT Machine Learning and Deep Learning courses |
| B5 (RL), B6 (planning), B7 (ethics), B8 (generative models) | Ahead of the matching UT courses |
| C5 evals and observability, C6 safety and governance (add G4-G6 on prompt injection), C7 serving and cost (add G8), C8 AWS GenAI, C9 enterprise architecture | Keep Lane G moving toward the goal; these are the most architect-heavy blocks |
| G7 (HNSW indexes in pgvector, a university seminar) | Optional, Scholar level; after C3 once RAG feels familiar |
| A7 | Only if a course needs it |

## 5. How this maps to the UT courses

Sources: the program page (https://cdso.utexas.edu/msai, opened 2026-11-09 and 2026-11-16) and the MSAI Online Handbook, published for 2027-2028, which you supplied (read in full on 2026-11-16). The block mapping is my reading of the course descriptions, not UT's. Track F has one block per course with the official description, free public materials and a prep path; it opens with a ranking of the courses by fit to the GenAI-architect goal (a judgement, not salary data).

**What the handbook settles.** The degree is 30 credit hours: 1 required course (Ethics in AI, grade B- or better) and 9 electives (grade C or better), letter grades only, a 3.0 GPA to graduate. The four courses the program page calls foundational (Machine Learning, Deep Learning, Reinforcement Learning, Planning) are listed as electives, so they are not mandatory; the page still recommends taking them first. Six years to finish (1.5 to 3 expected); at most 6 transfer credit hours; thesis option needs a UT AI faculty sponsor. The handbook lists 15 courses; Agentic Software Engineering is one the program page did not list, and it has a title only.

| UT course (handbook number) | Track F block | Prepare with (Tracks A and B) | Spring 2027 per the program's 2026-11-16 email |
|---|---|---|---|
| Machine Learning (AI 391L) | 1 | A2 (SVD/PCA), A4-A6, B1, B2 | runs |
| Deep Learning (AI 394D) | 2 | A1, A3, A6, B3, B4 | runs |
| Reinforcement Learning (AI 394R) | 3 | A4, B5 | does not run |
| Planning, Search, and Reasoning Under Uncertainty (AI 388U) | 4 | A4, B6 | does not run |
| Ethics in AI (AI 380E, required) | 5 | B7 | runs |
| Natural Language Processing (AI 388) | 6 | B4, then C1 | does not run |
| Advances in Deep Learning (AI 395T) | 7 | B3-B4 | runs |
| Advances in Generative Models (AI 395T; the program page says "Deep Generative Models") | 8 | B8 | runs |
| Case Studies in Machine Learning (AI 391M) | 9 | B1, B2 | runs |
| Optimization (AI 388J) | 10 | A6 | runs |
| Online Learning and Optimization (AI 388K) | 11 | A6 | runs |
| Automated Logical Reasoning (AI 389L) | 12 | A7 | runs |
| AI in Healthcare (AI 380H) | 13 | B1 | runs |
| AI in Astrophysics (AI 395T; needs a B or better in Machine Learning and Deep Learning passed or concurrent) | 14 | B1, B3 | not on that email's course list |
| Agentic Software Engineering (AI 395T) | 15 | Track G Block 7 | runs |

Courses that fit the GenAI-architect goal most closely, by my reading of their descriptions: Deep Learning, Advances in Deep Learning, Natural Language Processing and Advances in Generative Models; Agentic Software Engineering is unrated because the handbook gives only its title. I am not a career advisor, so treat that as input. Questions for the program coordinator are at the top of Track F.

## 6. How this fits the material you already have

You already have the desk side. The bike videos give the mental model; these are where to read and practise.

- **SAA-C03 course companion** (the 54-page set): the AWS Associate track. Not part of the bike plan.
- **AWS system design visual guide** (25 pages plus the three-part production architecture set): its AI pages line up with Track C.

| Track C block | Matching guide page |
|---|---|
| C7 customization and serving | Page 15 customization strategies; Page 21 model deployment and monitoring |
| C6 safety, security and governance | Page 16 guardrails and responsible AI; Page 25 AI security and governance |
| C8 AWS GenAI | Page 19 AI service landscape |
| C3 RAG | Page 15 customization strategies (likely covers RAG against fine-tuning; check) |
| C4 agents | Page 22 agentic systems |
| C7 cost | Page 23 AI cost and security |
| C1, B1 fundamentals | Page 24 AI/ML fundamentals; Page 20 ML lifecycle |

The Page 15-25 titles are from the output list of that chat; I did not open the pages themselves, so check that each really covers the block before relying on the pairing.

## 7. Known gaps (from all eight tracks)

Gaps are listed, never filled with weak videos. These are the open ones for Tracks A to C; every track file also ends with its own Gaps and Not checked sections.

- **Track A:** sets (no main-path video); learning-rate schedules, momentum and Adam; Hessian and second-order convexity; Bayesian inference beyond the basics; dedicated continuous random variables and densities.
- **Track B:** training, tuning and debugging neural networks; a short animated overview of supervised/unsupervised/RL; a short visual VC-dimension video; graphical models beyond one lecture; scaling laws and fine-tuning as standalone videos; a short POMDP intro; a university lecture on ethics guidelines.
- **Track C, after gap-fill pass 1:** eight videos were added (prompting, structured outputs, tool calling, prompt injection, HNSW, token cost). Still open: bank model-risk management for LLMs (the one candidate is a registration page, not a video); how to choose a vector store; prompt caching and batching from an AI-lab or cloud-provider channel; case studies from banks' own engineers (the one candidate is a podcast episode with no YouTube ID); Simon Willison's own lethal-trifecta talk was never recorded; open versus closed models at architect level; non-AWS reference architectures. Block 2 is still only five BIKE items. Not searched at all: OpenAI, Google DeepMind and Microsoft official channels, Stanford CS224N and similar courses, Databricks and Snowflake talks, NIST AI RMF and EU AI Act walkthroughs.
- **Tracks D and E:** see the Gaps sections at the end of each file.
- **Track F:** most of the online courses have no public site or lectures of their own, so the prep paths use public materials of the same topics; Advances in Deep Learning rests on the UT Deep Learning Group's site, whose match with the online course is unconfirmed; Agentic Software Engineering has no description.
- **Track G:** no dedicated video on preparing fine-tuning data or on the hosted-API-versus-self-hosted decision; chunking is covered only by a desk video; only the first Stanford CS336 lecture could be verified; several rows are title-based (the Status column says which).
- **Track H:** no single "anatomy of an LLM app" video; LangGraph only optional; the Python Docker videos are from 2020 and 2022; no verified CloudFront follow-along; no ALB-versus-API-Gateway concept video; no Python Redis-caching video from a credible channel; many AWS console rows come from small channels (each row says so). Its Gaps section lists the rest.

## 8. What is pending

1. **Lengths:** done for 484 of 484 videos (read from YouTube pages, 2026-11-16 and 17).
2. **Playlists:** turn each block into an ordered YouTube playlist, on the account you keep for riding (adding to a playlist does not touch watch history; playing does).
3. **Handbook questions for the coordinator:** which instructor teaches Advances in Deep Learning; what Agentic Software Engineering covers; whether AI in Astrophysics runs; whether the program recommends Machine Learning and Deep Learning first; whether the 2027-2028 handbook governs a Spring 2027 start. Track F lists them.
4. **Pages I could not open** are in MORNING.md.
5. **Repo:** done. https://github.com/vij658/UTAustinMSAI holds the tracks, this file and the generator for the HTML pages. It is public, so it holds only your first name, the program and the study plan.
6. **Optional:** a hosted private copy of the HTML pages, if you want to open them from the bike monitor without copying files.

## Appendix: videos that appear in more than one track

Watch each once, the first time you reach it in the plan. Row labels are the track and the row number in that track's table. This table shows only the overlaps among Tracks A to C; Tracks F and G reuse many more rows from earlier tracks, and the HTML pages tick a video in every track once you mark it watched.

| Video | Channel | Where it appears |
|---|---|---|
| [StatQuest: Principal Component Analysis (PCA), Step-by-Step](https://www.youtube.com/watch?v=FgakZw6K1QQ) | StatQuest with Josh Starmer | A 19, B 2.7 |
| [Maximum Likelihood, clearly explained!!!](https://www.youtube.com/watch?v=XepXtl9YKwc) | StatQuest with Josh Starmer | A 34, B 2.11 |
| [Gradient descent, how neural networks learn / Deep Learning Chapter 2](https://www.youtube.com/watch?v=IHZwWFHWa-w) | 3Blue1Brown | A 38, B 3.2 |
| [Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8) | StatQuest with Josh Starmer | A 39, B 2.1 |
| [Backpropagation, intuitively / Deep Learning Chapter 3](https://www.youtube.com/watch?v=Ilg3gGewQ5U) | 3Blue1Brown | A 42, B 3.3 |
| [Backpropagation calculus / Deep Learning Chapter 4](https://www.youtube.com/watch?v=tIeHLnjs5U8) | 3Blue1Brown | A 43, B 3.O4 |
| [Singular Value Decomposition (SVD): Mathematical Overview](https://www.youtube.com/watch?v=nbBvuuNVfco) | Steve Brunton | A 2, B 2.8 |
| [Machine Learning Fundamentals: Bias and Variance](https://www.youtube.com/watch?v=EuBBz3bI-aA) | StatQuest with Josh Starmer | A 5, B 1.2 |
| [But what is a neural network? / Deep learning chapter 1](https://www.youtube.com/watch?v=aircAruvnKk) | 3Blue1Brown | A 6, B 3.1 |
| [Transformers, the tech behind LLMs / Deep Learning Chapter 5](https://www.youtube.com/watch?v=wjZofJX0v4M) | 3Blue1Brown | B 4.1, C 1.2 |
| [Attention in transformers, step-by-step / Deep Learning Chapter 6](https://www.youtube.com/watch?v=eMlx5fFNoYc) | 3Blue1Brown | B 4.2, C 1.3 |
| [[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) | Andrej Karpathy | B 4.3, C 1.1 |
| [Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI) | Andrej Karpathy | B 4.4, C 1.4 |
| [Let's build GPT: from scratch, in code, spelled out.](https://www.youtube.com/watch?v=kCc8FmEb1nY) | Andrej Karpathy | B 4.O3, C 1.D2 |
| [Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) | Andrej Karpathy | B 4.O4, C 1.D1 |

<!-- 15 shared videos -->
