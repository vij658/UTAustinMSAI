# MSAI + GenAI Architect Roadmap: the bike-video plan

For Sankar. One hour a day on the stationary bike, watching, to build mental models before the UT Austin online MS in AI starts (Spring 2027) and while growing toward the goal of designing large-scale GenAI tech stacks for big companies (coding + architecture + AI).

Written 2026-11-09/10. Status: **draft 1.** The video lists exist and every video was checked to exist; none was watched. See "How much to trust this" before relying on any number.

## 1. What is in this folder

| File | What it is | Main-path videos | Optional |
|---|---|---|---|
| [tracks/A-ai-math.md](tracks/A-ai-math.md) | AI math: notation, calculus, linear algebra, multivariable calculus, probability, statistics, optimization, light discrete math | 47 (Blocks 0-7) | 20 "optional extras" |
| [tracks/B-ai-ml-concepts.md](tracks/B-ai-ml-concepts.md) | AI/ML concepts in the order of the UT foundational courses: ML, deep learning, transformers, RL, planning, ethics, generative models | 48 (Blocks 1-8) | 30 (about 12 are desk-only) |
| [tracks/C-genai-stack.md](tracks/C-genai-stack.md) | The GenAI stack and enterprise architecture: stack map, LLMs for architects, prompting, RAG, agents/MCP, evals, security and governance, serving and cost, AWS GenAI, large-company patterns | about 50 (Blocks 0-9; the table has 51 rows), plus 8 from gap-fill pass 1 (rows G1-G8) | 8 desk videos |

Every block in every track has: why it matters, an ordered table (title, channel, link, length, level, mode, what you will get, status), a "full circle" line, and three recap questions with hidden answers. Each track ends with **Gaps** (topics where no good video was found) and **Not checked**.

Tags: **Level** = Start / Deeper / Scholar. **Mode** = BIKE (you can mostly listen) or DESK (needs code, paper or pausing, so it never uses up a ride).

## 2. How much to trust this

- **Verified means "exists".** For each video the YouTube oEmbed lookup returned the same video ID, and titles and channels are copied exactly as returned. Nobody watched the videos. "What you will get" comes from titles, chapter lists and the channel's usual format.
- **Lengths are mostly unknown.** YouTube returned a bot-protection page for most watch pages and the agents did not work around it. Per the track files: A has a confirmed length for 8 of 47 main videos (2 h 58 m), B for 11 of 48 (about 4 h 13 m, plus lower bounds for two Karpathy talks), C for 28 of about 50 (at least 25.6 h combined). No total can be stated yet. Opening each link once fills the "length ?" cells.
- **The planning below uses a guess.** I assumed about 30 minutes per video, so two videos per ride. Lectures run longer (Karpathy's *Deep Dive into LLMs* is at least 3 h 21 m on its own), so expect to get through fewer videos than the plan says. Re-plan after week one.
- **Level and Mode tags** are judgement calls, not lookups.
- **Tools change fast.** In Track C, anything published before 2025 is flagged "may be dated" in its table, and even 2025 material on frameworks and services can be a release or two behind by now.

## 3. The routine (bike mode)

1. **Ride:** two videos, in table order, from the block you are on. Watch the intuition video before the lecture; the tables are already ordered that way.
2. **Right after:** answer that block's recap questions out loud, then open the hidden answers. Missed one? Re-watch only that video. Do not push on.
3. **One line of notes:** "what hurt, and what fixed it" for each video. If you keep this habit, the Atlas style of thinking carries over directly.
4. **Desk items are optional.** Never let a DESK video eat a ride. Save them for a weekend session, if at all.
5. **If you fall behind, cut in this order:** optional lists first, then Track A Block 7 (discrete math), then Track B Blocks 7-8, then the later Track C blocks. Never cut the first three blocks of Track C, or Track A Blocks 1-6: the rest builds on them.

## 4. Order of play

Two lanes run in parallel so the math and the goal both move every week.

- **Lane M (math and ML), 4 rides a week:** Track A in block order, then Track B Blocks 1-3.
- **Lane G (GenAI stack), 2 rides a week:** Track C in block order.
- Week layout: Monday-Thursday Lane M, Friday-Saturday Lane G, Sunday rest or catch-up. Your AWS reading at the desk (see section 6) is separate from the bike.

### Before January (about 8 weeks)

Approximate; re-plan after week one when you know real lengths.

| Weeks | Lane M | Lane G |
|---|---|---|
| 1-2 | A0 notation and warm-up; A1 calculus | C0 the big picture; C1 LLMs for architects (watch 1.1 to 1.3 now; treat the 3 h 21 m deep dive 1.4 as its own run of rides later) |
| 3-4 | A2 vectors and linear algebra (10 videos, the biggest block); A3 multivariable calculus | C1 finish; C2 prompting and structured outputs (add G1, G2 and G3 from the gap-fill section; the track file says where each one goes) |
| 5 | A4 probability | C3 embeddings and RAG (start) |
| 6 | A5 statistics; A6 optimization (start) | C3 finish |
| 7 | A6 finish; B1 what AI/ML is | C4 agents and tools (start) |
| 8 | B2 classical ML (start) | C4 finish |

That targets A0-A6 (43 videos), B1-B2 (18 videos) and C0-C4 (22 videos, plus G1-G3). If the 30-minute guess is optimistic, B2 slips into the semester. That is fine: B2 and B3 are the preview of the UT Machine Learning and Deep Learning courses.

### During the semester

| Track block | Why now |
|---|---|
| B2, B3 | Ahead of the UT Machine Learning and Deep Learning courses |
| B5 (RL), B6 (planning), B7 (ethics), B8 (generative models) | Ahead of the matching UT courses |
| C5 evals and observability, C6 safety and governance (add G4-G6 on prompt injection), C7 serving and cost (add G8), C8 AWS GenAI, C9 enterprise architecture | Keep Lane G moving toward the goal; these are the most architect-heavy blocks |
| G7 (HNSW indexes in pgvector, a university seminar) | Optional, Scholar level; after C3 once RAG feels familiar |
| A7 | Only if a course needs it |

## 5. How this maps to the UT courses

Course topics are from the official program page (https://cdso.utexas.edu/msai), which I opened on 2026-11-09. The block mapping is my reading of the syllabi, not UT's. The page lists no prerequisites, and I did not find the Spring 2027 start date or the reading lists.

| UT foundational course | Syllabus topics (from the page) | Prepare with |
|---|---|---|
| Machine Learning | PAC learning, VC dimension, perceptron, linear regression and gradient descent, boosting, PCA/SVD, maximum likelihood, Bayesian inference, EM, graphical models, neural networks | A2 (SVD/PCA), A4-A6, B1, B2 |
| Deep Learning | Deep and convolutional networks, sequence modelling, reinforcement learning, PyTorch | A1, A3, A6, B3, B4 |
| Planning, Search, and Reasoning Under Uncertainty | Heuristic search, adversarial planning, Bayesian state estimation, MDPs, POMDPs | A4, B6 |
| Reinforcement Learning | Bandits, MDPs, dynamic programming, Monte Carlo, temporal-difference learning, policy gradients | A4, B5 |
| Ethics in AI (the only course the page labels required) | History, ethical theories, fairness, accountability, transparency | B7 |

Electives that fit the GenAI-architect goal and what to watch first: Natural Language Processing (B4, then C1), Advances in Deep Learning (B3-B4), Advances in Deep Generative Models (B8). I am not a career advisor, so treat that as input.

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

## 7. Known gaps (from the three tracks)

Gaps are listed, never filled with weak videos. These are the open ones.

- **Track A:** sets (no main-path video); learning-rate schedules, momentum and Adam; Hessian and second-order convexity; Bayesian inference beyond the basics; dedicated continuous random variables and densities.
- **Track B:** training, tuning and debugging neural networks; a short animated overview of supervised/unsupervised/RL; a short visual VC-dimension video; graphical models beyond one lecture; scaling laws and fine-tuning as standalone videos; a short POMDP intro; a university lecture on ethics guidelines.
- **Track C, after gap-fill pass 1:** eight videos were added (prompting, structured outputs, tool calling, prompt injection, HNSW, token cost). Still open: bank model-risk management for LLMs (the one candidate is a registration page, not a video); how to choose a vector store; prompt caching and batching from an AI-lab or cloud-provider channel; case studies from banks' own engineers (the one candidate is a podcast episode with no YouTube ID); Simon Willison's own lethal-trifecta talk was never recorded; open versus closed models at architect level; non-AWS reference architectures. Block 2 is still only five BIKE items. Not searched at all: OpenAI, Google DeepMind and Microsoft official channels, Stanford CS224N and similar courses, Databricks and Snowflake talks, NIST AI RMF and EU AI Act walkthroughs.

## 8. What is pending

1. **Gap-filling, one agent at a time.** Pass 1 (Track C) is done. Next are Track A (Adam and momentum, Bayesian inference beyond the basics, densities, sets), then Track B. Each run is capped and reports back before the next starts, and I tell you before each one.
2. **Lengths:** open each link once to fill the "length ?" cells, or ask for a pass when YouTube access allows it.
3. **Playlists:** turn each block into an ordered YouTube playlist (the Atlas script can do this once the lists settle).
4. **Repo:** this folder is committed locally, but pushing to GitHub is blocked until a repository named `MSAIAtlas` exists and the session has push access (the session's GitHub login is currently invalid).

## Appendix: videos that appear in more than one track

Watch each once, the first time you reach it in the plan. Row labels are the track and the row number in that track's table.

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
