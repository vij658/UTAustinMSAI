# Track C: The GenAI stack and enterprise architecture

Goal of this track: build the mental model of how a large company designs a generative-AI platform, from first principles up to bank-grade operations. Watch in order; each block assumes the previous one. Compiled 2026-11-09. Every video below was confirmed to exist with the oEmbed endpoint (title and channel are copied exactly as returned). AWS content here is GenAI-specific only (Bedrock, AgentCore, SageMaker AI for GenAI); no general AWS fundamentals.

How to read the tables:
- **Length**: exact when the video page gave it. A leading ">=" means a lower bound taken from the last chapter marker or the last transcript timestamp (the exact length could not be retrieved). "length ?" means no evidence was available.
- **Published**: the upload date from the video page. For AWS re:Invent 2025 sessions where the page did not give it, the text says "re:Invent 2025, upload date ?" (the conference ran 1-5 Dec 2025).
- **May be dated**: tools and services change fast. Anything published before 2025 is flagged. Even 2025 material on frameworks (LangChain, vLLM, Bedrock features) can be a release or two behind by Nov 2026.
- **Level**: Start (no prior knowledge), Deeper (assumes earlier blocks), Scholar (dense or advanced).
- **Mode**: BIKE (listen and glance at slides) or DESK (live coding or hands-on).

## Stack map

The layers of a generative-AI stack, bottom to top. Tag every video with the layer it teaches, and when you finish a video ask "which layer did that just move?"

| # | Layer | One-line job |
|---|-------|--------------|
| 1 | Data | Source documents, tables, events; quality, lineage, permissions travel with the data |
| 2 | Embeddings / vector | Turn content into vectors; store and index them (vector DB, search index) |
| 3 | Retrieval | Find the right context: chunking, hybrid search, reranking, query rewriting |
| 4 | Orchestration / agents | Prompts, tool calls, workflows, agent loops, memory, MCP connections |
| 5 | Model hosting | Which model, where it runs (API, managed, self-hosted), serving, gateway and routing |
| 6 | Evaluation | Offline evals, LLM-as-judge, regression suites, human review |
| 7 | Guardrails | Input/output filters, prompt-injection defence, PII handling, tool permissions |
| 8 | Observability | Tracing, logging, online evals, drift and quality monitoring |
| 9 | Cost | Token economics, caching, batching, model right-sizing, FinOps |
| 10 | Governance | Model risk management, compliance, audit, responsible-AI process, operating model |

Layer names used in the tables: Data, Embeddings/vector, Retrieval, Orchestration/agents, Model hosting, Evaluation, Guardrails, Observability, Cost, Governance. "Framing" means a video that spans all layers.

---

## Block 0: Big picture, what an enterprise GenAI platform looks like

**Why an architect needs this:** every later video is one layer of one system; without the whole picture you cannot decide where a new tool, risk or cost belongs.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 0.1 | Andrej Karpathy: Software Is Changing (Again) | Y Combinator | https://www.youtube.com/watch?v=LCEmiRjPEtQ | 39:31 | 2025-06-18 | Framing | Start | BIKE | The frame for the whole track: LLMs as a new kind of computer programmed in natural language, how to design partially autonomous apps with a human in the loop, and building software that agents as well as people can use. | verified |
| 0.2 | BUILDING A SELF SERVICE GENAI PLATFORM WITHIN A LARGE ENTERPRISE | European Chatbot and Conversational AI Summit | https://www.youtube.com/watch?v=c8KP7I7x6f8 | 15:28 | 2026-06-29 | Orchestration/agents, Governance | Deeper | BIKE | A practitioner case study (an energy company's "AI Hub"): a platform approach with reusable modules, stable reference architectures, a portal that gives users governed GenAI products and engineers shared components. Speakers are not named on the page; treat as one company's view. | verified |
| 0.3 | AWS re:Invent 2025 - AI agents in action: Architecting the future of applications (INV202) | AWS Events | https://www.youtube.com/watch?v=D0UkoghAVM0 | 1:00:04 | re:Invent 2025, upload date ? | Orchestration/agents | Start | BIKE | The cloud-provider view of where application architecture is heading with agents, with customer examples (Stedi, QAD, Pattern). More vision than blueprint, so use it to see the vendor's map of the territory. | verified |

Optional desk list: none for this block.

**Full circle:** the stack map is the old enterprise integration picture (gateway, orchestration, systems of record, authN/Z, audit) with a probabilistic component added in the middle; the same shape as a fraud or identity decisioning pipeline: signals in, model in the middle, rules and human review around it.

<details>
<summary>Recap questions (3)</summary>

1. Name the ten layers of the stack map from data to governance.
   - Data, embeddings/vector, retrieval, orchestration/agents, model hosting, evaluation, guardrails, observability, cost, governance.
2. Why do large companies build a self-service platform instead of letting each team wire up its own model and vector store?
   - Reuse of governed components, one place to apply security and cost controls, and stable reference architectures so teams ship faster and consistently (the point of the OMV talk).
3. What does "partial autonomy with a human in the loop" mean for system design?
   - The app should keep the AI's output easy to inspect and approve, with the amount of autonomy adjustable, so verification is fast and failures are caught; this shapes UI, evaluation and guardrail design.
</details>

---

## Block 1: How LLMs work, for architects

**Why an architect needs this:** tokens, context limits, sampling and hallucination are the physical constraints behind every cost, latency, quality and risk decision you will make later.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 1.1 | [1hr Talk] Intro to Large Language Models | Andrej Karpathy | https://www.youtube.com/watch?v=zjkBMFhNj_g | 59:48 | 2023-11-22 | Model hosting | Start | BIKE | The best one-hour mental model: an LLM as two files (weights plus run code), how it is trained and then tuned into an assistant, then tools, multimodality and the security issues of this new computing paradigm. Model names are dated (2023); the concepts are not. | verified |
| 1.2 | Transformers, the tech behind LLMs \| Deep Learning Chapter 5 | 3Blue1Brown | https://www.youtube.com/watch?v=wjZofJX0v4M | 27:14 | 2024-04-01 | Model hosting, Embeddings/vector | Start | BIKE | Visual walkthrough of next-token prediction, word embeddings, the transformer pipeline, and softmax with temperature. This is where "embeddings" and "temperature" become concrete. | verified |
| 1.3 | Attention in transformers, step-by-step \| Deep Learning Chapter 6 | 3Blue1Brown | https://www.youtube.com/watch?v=eMlx5fFNoYc | 26:09 | 2024-04-07 | Model hosting | Deeper | BIKE | Self-attention, multiple heads and cross-attention. Explains why cost grows with context length and why long prompts are not free. | verified |
| 1.4 | Deep Dive into LLMs like ChatGPT | Andrej Karpathy | https://www.youtube.com/watch?v=7xTGNNLPyMI | 3:31:23 | 2025-02-05 | Model hosting | Deeper | BIKE | The long version: pretraining data, tokenization, inference, how a base model becomes an assistant, why models hallucinate, and reinforcement learning / reasoning models. Split it across three or four rides; it builds on 1.1. | verified |
| 1.5 | AWS re:Invent 2025 - Mastering model choice: The 3-step Amazon Bedrock advantage (AIM391) | AWS Events | https://www.youtube.com/watch?v=Vu91YwZxskY | 56:43 | re:Invent 2025, upload date ? | Model hosting, Cost | Deeper | BIKE | The product angle on model families and trade-offs: how a team picks among many models (quality, latency, price) and switches between them, with a customer example. Vendor-framed, so keep the criteria and discount the sales parts. | verified |

Optional desk list (hands-on, do at a desk later):

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 1.D1 | Let's build the GPT Tokenizer | Andrej Karpathy | https://www.youtube.com/watch?v=zduSFxRajkE | 2:13:34 | date ? | Model hosting | Scholar | DESK | Build a tokenizer from scratch; makes token counts, odd model failures and per-token pricing feel obvious. May be dated for tooling. | verified |
| 1.D2 | Let's build GPT: from scratch, in code, spelled out. | Andrej Karpathy | https://www.youtube.com/watch?v=kCc8FmEb1nY | 1:56:20 | date ? | Model hosting | Scholar | DESK | Code a small GPT end to end; the deepest way to internalise the architecture. Pre-2024 upload likely, so treat tools as dated (the concepts are stable). | verified |

**Full circle:** back to Block 0, the "model hosting" layer is just this: a very large function from tokens to a probability distribution over the next token, wrapped in sampling. Classically it descends from n-gram language models and softmax regression; the temperature knob is the Boltzmann temperature from statistical physics.

<details>
<summary>Recap questions (3)</summary>

1. What is a token, and why does it matter to an architect more than "words" or "characters"?
   - A token is a sub-word chunk produced by the tokenizer; pricing, context limits and latency are all counted in tokens, and different languages, code and numbers tokenize at very different efficiency.
2. What does temperature do, and when would you set it near zero for an enterprise use case?
   - It rescales the probabilities before sampling; low values make output more deterministic, which you want for extraction, classification and anything you need to regression-test. It does not remove hallucination.
3. Why do models hallucinate, and what architectural levers reduce it?
   - They are trained to produce plausible continuations, not to retrieve verified facts; levers are grounding with retrieval (Block 3), tools that fetch facts (Block 4), structured outputs, and evaluation (Block 5).
</details>

---

## Block 2: Prompting and structured outputs

**Why an architect needs this:** the prompt is the interface contract between your system and the model, and structured outputs and tool calls are how a probabilistic model plugs into deterministic enterprise code.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 2.1 | Prompting 101 \| Code w/ Claude | Anthropic | https://www.youtube.com/watch?v=ysPbXH0LpIE | 24:52 | 2025-07-31 (talk given 2025-05-22) | Orchestration/agents | Start | BIKE | Anthropic applied-AI staff (Hannah Moran, Christian Ryan) on how to structure a good prompt: role and task, context, examples, output format, iterating on failures. Concepts carry across vendors. | verified |
| 2.2 | Pydantic is STILL all you need: Jason Liu | AI Engineer | https://www.youtube.com/watch?v=pZ4DIH2BVqg | 15:21 | 2024-09-06 | Orchestration/agents | Deeper | BIKE | Why typed, validated outputs (schemas) are the bridge from LLM to application code, plus business use cases and where the field was heading. Provider-native structured-output modes have since matured, so treat the library specifics as possibly dated. | verified |

Optional desk list:

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 2.D1 | Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI | AI Engineer | https://www.youtube.com/watch?v=KUEmEb71vzQ | 1:42:54 | 2025-04-23 | Orchestration/agents | Deeper | DESK | Hands-on function calling: the history, building an agent loop, memory, delegation and agent-written tools. Do this at a desk after Block 4's concept videos. | verified |

**Full circle:** this is Block 1 turned into an API: the next-token distribution is steered by the prompt (conditioning) and then constrained (schema) so the result can be parsed. Classically it is design-by-contract: a typed interface with validation at the boundary, retried on failure.

<details>
<summary>Recap questions (3)</summary>

1. Why use a schema (structured output) instead of asking the model to "reply in JSON"?
   - A schema lets the platform validate and, with provider support, constrain the output, so downstream code gets guaranteed shapes and you can retry or fail cleanly on violations.
2. What goes in a system prompt versus the user message?
   - The system prompt holds stable role, rules, format and policy for every call; the user message holds the variable request and data. Treat the system prompt as configuration that is versioned and tested.
3. In function calling, who actually runs the function?
   - Your application code does; the model only emits a structured request naming the tool and arguments, and your code executes it (with permission checks) and returns the result to the model.
</details>

---

## Block 3: Embeddings, vector search and RAG

**Why an architect needs this:** retrieval-augmented generation is how most enterprise knowledge reaches a model, and most "the AI is wrong" tickets are really retrieval, chunking or permission problems.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 3.1 | RAG From Scratch: Part 1 (Overview) | LangChain | https://www.youtube.com/watch?v=wd7TZ4w1mSw | 5:13 | 2024-02-06 | Retrieval, Embeddings/vector | Start | BIKE | The idea of RAG (give the model private or fresh data at question time) and the plan for indexing, retrieval and generation. Only part 1 of the series is verified here; code in the series uses 2024 LangChain APIs (may be dated). | verified |
| 3.2 | Systematically improving RAG applications | Hamel Husain | https://www.youtube.com/watch?v=RrDBV6odPKo | 1:08:54 | 2024-07-11 | Retrieval, Evaluation | Deeper | BIKE | A practitioner method for improving RAG: collect feedback, analyse topics and failure clusters, build synthetic evaluation data, and fix chunking. Best "failure modes" video in the block. Tool names are 2024 (may be dated). | verified |
| 3.3 | AWS re:Invent 2025 - RAG is Dead: Long Live Intelligent Retrieval-Augmented Generation (AIM214) | AWS Events | https://www.youtube.com/watch?v=KQYe5T96hnM | 16:33 | 2025-12-03 | Retrieval, Embeddings/vector | Deeper | BIKE | Moving past naive vector lookup to agentic pipelines: reasoning, metadata-aware retrieval, hybrid search, reranking, query expansion and feedback loops. Presented by Pinecone, so a vector-DB vendor's view. | verified |
| 3.4 | AWS re:Invent 2025 - Advanced RAG Architectures: From Basic Retrieval to Agentic RAG (NTA403) | AWS Events | https://www.youtube.com/watch?v=ADrUp2cEdKg | 52:52 | re:Invent 2025, upload date ? | Retrieval | Scholar | BIKE | Architecture progression from basic retrieval to agentic RAG. Existence confirmed; page could not be read, so content is judged from the title only. | verified (existence); content per title only |
| 3.5 | AWS re:Invent 2024 - Build scalable RAG applications using Amazon Bedrock Knowledge Bases (AIM305) | AWS Events | https://www.youtube.com/watch?v=jSlNfr8Uuco | 56:51 | 2024 (re:Invent 2024, upload date ?) | Retrieval, Data | Deeper | BIKE | The AWS product angle on managed enterprise knowledge bases (ingestion, chunking, vector store, retrieval). Content judged from the title only. May be dated: Bedrock Knowledge Bases has changed a lot since Dec 2024. | verified (existence); content per title only |

Optional desk list:

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 3.D1 | Learn RAG From Scratch – Python AI Tutorial from a LangChain Engineer | freeCodeCamp.org | https://www.youtube.com/watch?v=sVcwVQRHIc8 | 2:33:11 | date ? | Retrieval | Start | DESK | Follow-along coding of the full RAG pipeline; do it after 3.1-3.3 so the code has a mental model to land on. 2024-era LangChain (may be dated). | verified |
| 3.D2 | AWS re:Invent 2025 - Advanced agentic RAG Systems: Deep dive with Amazon Bedrock (AIM425) | AWS Events | https://www.youtube.com/watch?v=bu2cD1pCFTs | 58:17 | 2025-12-03 | Retrieval, Orchestration/agents | Scholar | DESK | Expert-level code talk: a production-grade agentic RAG system with Bedrock Knowledge Bases, Strands and AgentCore (agent with memory, authentication and deployment). Speakers not named on the page. | verified |

**Full circle:** to Block 1, an embedding is the same learned vector space you met in the 3Blue1Brown video, used here to measure similarity instead of predict the next token; classically it is information retrieval (TF-IDF/BM25 keyword search), which is why hybrid search wins: it keeps the old lexical signal and adds the semantic one.

<details>
<summary>Recap questions (3)</summary>

1. Why does hybrid search (keyword plus vector) often beat vector-only retrieval?
   - Vector search is good at meaning and paraphrase but weak on exact identifiers, names and rare terms; keyword search is the reverse. Combining them, then reranking, covers both.
2. A RAG answer is wrong. Name three places to look before blaming the model.
   - The chunking (answer split across chunks or lost), the retrieval (right document never returned, or wrong embedding/filters), and missing or stale source data; also permissions filtering out the document.
3. Why must access control be applied at retrieval time in an enterprise knowledge base?
   - Because the model will happily summarise whatever it is given; if retrieval returns documents the user may not see, the model leaks them. Filter by the caller's entitlements before anything reaches the prompt.
</details>

---

## Block 4: Agents and tools

**Why an architect needs this:** agents turn a model from an answer machine into a system that takes actions, which multiplies both value and blast radius; you need the patterns, the protocol (MCP) and the judgement for when a plain workflow is better.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 4.1 | How We Build Effective Agents: Barry Zhang, Anthropic | AI Engineer | https://www.youtube.com/watch?v=D7_ipDqhtwk | 15:09 | 2025-04-04 | Orchestration/agents | Start | BIKE | Anthropic's short, opinionated guide: what an agent loop is, when a simple workflow beats an agent, and how to design around the model's view of the world. Watch first; it is the "when NOT to use agents" video. (Summary of its principles taken from third-party write-ups seen in search; the page itself gave only title and length.) | verified |
| 4.2 | Why we built—and donated—the Model Context Protocol (MCP) | Anthropic | https://www.youtube.com/watch?v=PLyCki2K0Lg | 35:32 | 2025-12-11 | Orchestration/agents | Start | BIKE | Anthropic's Stuart Ritchie interviews MCP co-creator David Soria Parra on what MCP is (an open standard for connecting AI to tools and data) and why it was donated to the Linux Foundation. | verified |
| 4.3 | [Keynote] MCP201: The Protocol in Depth with David Soria Parra at Anthropic | Agentic AI Foundation | https://www.youtube.com/watch?v=C_nqAWHsldo | 25:41 | 2025-05-30 (keynote given 2025-05-23) | Orchestration/agents | Deeper | BIKE | The protocol internals from its co-creator: how clients, servers and capabilities fit together. MCP evolves quickly (auth, transports), so check the current spec after watching. | verified |
| 4.4 | The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory | AI Engineer | https://www.youtube.com/watch?v=ow1we5PzK-o | 18:30 | 2026-05-06 | Orchestration/agents | Deeper | BIKE | A taxonomy of five multi-agent strategies and a three-role design (orchestrator, workers, validators) with validation contracts and structured handoffs, drawn from one vendor's production data. | verified |
| 4.5 | Claude for Long-Horizon Tasks — Lance Martin, Anthropic | AI Engineer | https://www.youtube.com/watch?v=9QebvrrY3KY | 25:18 | date ? | Orchestration/agents | Deeper | BIKE | Memory and context management for agents that run for a long time. Page could not be read, so content is judged from the title only. | verified (existence); content per title only |
| 4.6 | Why Every AI Agent Needs Durable Execution \| Temporal, Samar Abbas | Lightspeed Venture Partners | https://www.youtube.com/watch?v=w4spcXq5uCw | 45:52 | 2026-02-20 | Orchestration/agents | Deeper | BIKE | Workflow orchestration for agents: why long-running, failure-prone agent runs need durable state, retries and resumption. An interview with the Temporal CEO, so a vendor's argument, but the underlying idea is sound. | verified |
| 4.7 | AWS re:Invent 2025 - Service-oriented builders guide to agentic AI: Insights from WEX (ARC313) | AWS Events | https://www.youtube.com/watch?v=DYbJG8T_Kk8 | 55:13 | re:Invent 2025, upload date ? | Orchestration/agents | Scholar | BIKE | An AWS architect (Andrew Baird) and a WEX engineer (Dan DeLauro) on building agentic systems the way you build services: boundaries, interfaces and operations. Content judged from the title and a third-party write-up. | verified |

Optional desk list:

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 4.D1 | Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic | AI Engineer | https://www.youtube.com/watch?v=kQmXtrmQ5Zg | 1:44:11 | date ? (early 2025 per a third-party note; unverified) | Orchestration/agents | Deeper | DESK | Hands-on MCP workshop: build servers and an agent that uses them. Do it after 4.2-4.3. Workshop code predates later MCP spec changes (may be dated). | verified |

**Full circle:** to Block 2, an agent is a prompt plus tool calls in a loop (the model proposes, your code executes, the result goes back in); to Block 3, retrieval is just one more tool. Classically this is a control loop or a workflow engine with a fuzzy decision step, which is why durable execution and idempotent tools matter exactly as they do in payment systems.

<details>
<summary>Recap questions (3)</summary>

1. When should you NOT use an agent?
   - When the steps are known and stable: a fixed workflow is cheaper, faster, easier to test and safer. Use agents only where the path genuinely cannot be specified in advance and the value justifies the cost and risk.
2. What problem does MCP solve, and what does it not solve?
   - It standardises how an application connects models to tools and data (one protocol instead of N custom integrations). It does not solve authorisation, trust in third-party servers or tool quality; those remain your design work.
3. Why does a long-running agent need durable execution?
   - Runs take minutes to hours, call flaky services and can crash; durable execution persists state so the run resumes without repeating side effects, which also gives you an audit trail.
</details>

---

## Block 5: Evaluation and observability

**Why an architect needs this:** a GenAI system has no unit-test oracle, so evals and traces are your only evidence that it works, that a model upgrade did not break it, and that a regulator or risk team can be shown how it behaves.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 5.1 | Evals, error analysis, and better prompts: A systematic approach to improving your AI products | How I AI | https://www.youtube.com/watch?v=PgzOBNse2EA | 54:49 | 2025-10-13 | Evaluation | Start | BIKE | Hamel Husain on error analysis first, binary pass/fail evals, validating an LLM-as-a-judge against human labels, and refining prompts, with client examples. The clearest practical route into evals. | verified |
| 5.2 | Why AI evals are the hottest new skill for product builders \| Hamel Husain & Shreya Shankar | Lenny's Podcast | https://www.youtube.com/watch?v=BsWxPI9UM4c | 1:46:33 | 2025-09-25 | Evaluation | Deeper | BIKE | A long conversation with two eval practitioners: building a review process, common mistakes, and how evals fit the product loop. Long; split across two rides. Content judged from the title plus chapters. | verified |
| 5.3 | LLM observability in production: tracing and online evals | Evidently AI | https://www.youtube.com/watch?v=r-CYvjJ-W3k | 5:08 | date ? | Observability | Deeper | BIKE | Tracing LLM calls and running evals on live traffic. Vendor channel; content judged from the title only. | verified (existence); content per title only |
| 5.4 | AWS re:Invent 2025 - Improve agent quality in production with Bedrock AgentCore Evaluations(AIM3348) | AWS Events | https://www.youtube.com/watch?v=Gcje6pRGr1g | 58:00 | re:Invent 2025, upload date ? | Evaluation, Observability | Deeper | BIKE | The AWS product angle: managed evaluation of agents in production (Amanda Lester, Vivek Singh, Ishan Singh). | verified |

Optional desk list:

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 5.D1 | Traceability and Observability in Multi-Step LLM Systems \| Langfuse \| LLMOps | LLMOps Space | https://www.youtube.com/watch?v=vRFSVGaNaG4 | 48:29 | date ? | Observability | Deeper | DESK (assumed from title) | Tracing a multi-step LLM pipeline with Langfuse. Content and mode judged from the title only. | verified (existence); content per title only |

**Full circle:** to Block 3, the RAG-improvement loop in 3.2 is this block applied to retrieval; classically it is test-driven development and production monitoring, except the "assertions" are graded by humans or by another model, which must itself be validated.

<details>
<summary>Recap questions (3)</summary>

1. Why start with error analysis rather than picking metrics up front?
   - Looking at real failures tells you which failure modes actually occur; generic metrics (helpfulness, tone) often miss the problems that matter, and your eval set should be built from observed failures.
2. How do you trust an LLM-as-judge?
   - Calibrate it against human labels on a sample, keep the rubric narrow and binary, and re-check it when the judge model or prompt changes; otherwise you are measuring the judge.
3. Which three things should a regression suite protect when you swap models or prompts?
   - Core task accuracy on a fixed gold set, known past failures (so they do not return), and safety/policy behaviours, with cost and latency tracked alongside.
</details>

---

## Block 6: Safety, security and governance

**Why an architect needs this:** in a bank the model is the easy part; the approval to run it depends on prompt-injection defence, data protection, access control and a model-risk story that an auditor will accept.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 6.1 | Prompt Injection and the Lethal Trifecta - minimising risks of agents | CharlieCowanAI | https://www.youtube.com/watch?v=js6rgedzjGs | 50:39 | date ? | Guardrails | Start | BIKE | Explains prompt injection and the "lethal trifecta" (an agent with private data, untrusted content and a way to send data out). This is a secondary explainer by an individual creator, judged from the title only; swap in Simon Willison's own talk when you find it (see Gaps). | verified (existence); content per title only |
| 6.2 | AWS re:Invent 2025 - Advanced AI Security: Architecting Defense-in-Depth for AI Workloads (SEC410) | AWS Events | https://www.youtube.com/watch?v=2sWNBNLxBlc | 1:00:57 | re:Invent 2025, upload date ? | Guardrails | Deeper | BIKE | Defence-in-depth for AI workloads from two AWS AI-security principals (Riggs Goodman, Jason Garman): threats, layered controls and where each sits in the architecture. | verified |
| 6.3 | AWS re:Invent 2025 - Keep Your Agents Out of Trouble with Amazon Bedrock AgentCore (AIM3330) | AWS Events | https://www.youtube.com/watch?v=ymwpOYMg1ng | 36:06 | re:Invent 2025, upload date ? | Guardrails | Deeper | BIKE | Controls for agents (policy, permissions, guardrails) in AgentCore. Content judged from the title only. | verified (existence); content per title only |
| 6.4 | AWS re:Invent 2025-Privacy-preserving AI primitives: Building blocks for regulated industries-ARC328 | AWS Events | https://www.youtube.com/watch?v=vfkKJhllnx4 | 56:48 | re:Invent 2025, upload date ? | Guardrails, Governance | Scholar | BIKE | Building blocks for keeping data private when using AI in regulated industries (Ruben Merz, J.D. Bean, AWS). Dense; expect infrastructure-level detail. | verified |
| 6.5 | AWS re:Invent 2025 - From principles to practice: Scaling AI responsibly with Indeed (AIM3323) | AWS Events | https://www.youtube.com/watch?v=7nY-BifCorI | 39:31 | re:Invent 2025, upload date ? | Governance | Deeper | BIKE | How a responsible-AI programme is turned into process and tooling: AWS's Mike Diamond with Indeed's head of responsible AI, Lewis Baker. | verified |
| 6.6 | AWS re:Invent 2025 - BCC: Hybrid architecture for generative AI to meet regulatory needs (HMC324) | AWS Events | https://www.youtube.com/watch?v=dqHjRlZSVNM | 19:49 | re:Invent 2025, upload date ? | Governance, Model hosting | Deeper | BIKE | A bank (Bank CenterCredit) explains a hybrid architecture so GenAI can run under regulatory constraints (data residency and control), with an AWS architect. Short and directly relevant to banking. | verified |
| 6.7 | Navigating AI and Model Risk Management in Banking | QuantUniversity Channel | https://www.youtube.com/watch?v=821nn3DrYqs | 57:42 | date ? | Governance | Deeper | BIKE | Model risk management for AI in banks. Content judged from the title only; check the date and speaker before relying on it. | verified (existence); content per title only |

Optional desk list: none for this block.

**Full circle:** to Block 1 (hallucination and Karpathy's security segment in 1.1) and to Block 4 (every tool you add enlarges the attack surface). Classically this is the confused-deputy problem plus model risk management: validate, document, monitor and challenge a model before and after it goes live.

<details>
<summary>Recap questions (3)</summary>

1. What makes prompt injection different from SQL injection?
   - There is no reliable boundary between instructions and data inside a prompt, so you cannot sanitise it away; you limit damage by controlling what the agent can access and do (least privilege, no unmonitored exfiltration path) and by adding layered checks.
2. What is the "lethal trifecta" and how do you break it?
   - Private data access, exposure to untrusted content, and an external communication channel in the same agent. Remove at least one leg (for example, no outbound network or no raw untrusted input).
3. What does a bank need beyond guardrails to put an LLM system in production?
   - A governance trail: model inventory and risk tiering, documented purpose and limits, independent validation, ongoing monitoring, change control and human oversight, mapped to the applicable model-risk and compliance requirements.
</details>

---

## Block 7: Customization and serving

**Why an architect needs this:** the choice between prompting, RAG, fine-tuning and a smaller model, and how you serve it, sets your cost, latency and control for years.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 7.1 | RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models | IBM Technology | https://www.youtube.com/watch?v=zYGDpG-pTho | 13:10 | date ? | Model hosting | Start | BIKE | A short decision frame for the three customization options. Content judged from the title only. | verified (existence); content per title only |
| 7.2 | LoRA & QLoRA Fine-tuning Explained In-Depth | Mark Hennings | https://www.youtube.com/watch?v=t1caDsMzWBk | 14:39 | date ? | Model hosting | Deeper | BIKE | The idea behind low-rank adapters and quantised LoRA (why you can tune a big model cheaply). Content judged from the title only; likely 2023-24, so tooling may be dated. | verified (existence); content per title only |
| 7.3 | AWS re:Invent 2025 - Customize models for agentic AI at scale with SageMaker AI and Bedrock (AIM381) | AWS Events | https://www.youtube.com/watch?v=OwcwLZPJ43s | 46:12 | re:Invent 2025, upload date ? | Model hosting | Deeper | BIKE | The AWS view of when and how to customise models (fine-tuning, distillation-style approaches) for agent workloads on SageMaker AI and Bedrock. | verified |
| 7.4 | Efficient LLM Serving with vLLM (Ray x AI21 Meetup) | AI21 Labs | https://www.youtube.com/watch?v=oObhZfVdcpI | 23:29 | date ? | Model hosting, Cost | Scholar | BIKE | How an open-source inference engine gets throughput (batching, memory management). Content judged from the title only; vLLM moves fast, so verify features against current docs. | verified (existence); content per title only |
| 7.5 | AWS re:Invent 2025 - vLLM on AWS: testing to production and everything in between (OPN414) | AWS Events | https://www.youtube.com/watch?v=sx-DLGXv49g | 51:27 | re:Invent 2025, upload date ? | Model hosting | Deeper | BIKE | Phi Nguyen and Omri Shiv on a four-level path from experimenting with an open model to running vLLM in production on AWS (including AI on EKS). | verified |
| 7.6 | AWS re:Invent 2025 - Scaling foundation model inference on Amazon SageMaker AI (AIM424) | AWS Events | https://www.youtube.com/watch?v=nHaLbyLPK7s | 53:24 | re:Invent 2025, upload date ? | Model hosting, Cost | Deeper | BIKE | Inference scaling on SageMaker AI with a Salesforce customer example (AWS's Vivek Gangasani and Kareem Syed-Mohammed, Salesforce's Richard Chang). | verified |
| 7.7 | AWS re:Invent 2025 - Sustainable and cost-efficient generative AI with agentic workflows (AIM333) | AWS Events | https://www.youtube.com/watch?v=tFiDkSG2ess | 54:05 | re:Invent 2025, upload date ? | Cost | Deeper | BIKE | Ways to cut cost and energy in GenAI workloads (model right-sizing, caching and workflow design), by AWS solutions architects Isha Dua and Parth Patel. | verified |

Optional desk list: none for this block (hands-on LoRA and vLLM labs were not verified).

**Full circle:** to Block 3 (RAG is the cheap way to add knowledge; fine-tuning changes behaviour and style) and to Block 1 (serving cost is the transformer's attention and memory cost from 1.3, paid per token). Classically this is the old build-versus-tune-versus-configure choice plus capacity planning.

<details>
<summary>Recap questions (3)</summary>

1. When do you choose RAG, fine-tuning or prompting?
   - Prompting first for behaviour you can describe; RAG when the model lacks current or private facts; fine-tuning when you need consistent style, format or a cheaper smaller model on a narrow task, and you have good data.
2. What does LoRA change, and why is it cheap?
   - It trains small low-rank adapter matrices instead of all weights, so memory and training cost drop sharply and adapters can be swapped per use case on one base model.
3. Name three levers that reduce serving cost and latency.
   - Batching requests, caching (including prompt/prefix caching), quantisation or a smaller model for easy tasks, and routing hard requests to larger models.
</details>

---

## Block 8: AWS GenAI specifically

**Why an architect needs this:** if your company is on AWS, Bedrock, AgentCore and SageMaker AI are the concrete services behind the stack map; knowing which layer each covers keeps you from buying or building the wrong thing. GenAI-specific only: no general AWS fundamentals here (you cover those at the desk). AWS services in this block changed monthly through 2025-26, so re-check feature names against current docs.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 8.1 | AWS re:Invent 2025 - Bridging from POC to production: An intro to Amazon Bedrock AgentCore (AIM2204) | AWS Events | https://www.youtube.com/watch?v=oDjESsByBmM | 59:01 | 2025-12-03 | Orchestration/agents | Start | BIKE | The map of AgentCore (runtime, identity, gateway, memory and related pieces) from its product lead, an AWS tech lead and an Ericsson customer (Vivek Singh, Mark Roy, Sarbashish Das). Start here for the AWS agent platform. | verified |
| 8.2 | AWS re:Invent 2025 - Agents in the enterprise: Best practices with Amazon Bedrock AgentCore(AIM3310) | AWS Events | https://www.youtube.com/watch?v=w5XJxCpUADY | 59:55 | re:Invent 2025, upload date ? | Orchestration/agents, Governance | Deeper | BIKE | Enterprise best practices for running agents on AgentCore. Content judged from the title only. | verified (existence); content per title only |
| 8.3 | AWS re:Invent 2025 - Scale agent tools with Amazon Bedrock AgentCore Gateway (AIM3313) | AWS Events | https://www.youtube.com/watch?v=DlIHB8i6uyE | 56:52 | re:Invent 2025, upload date ? | Orchestration/agents | Deeper | BIKE | How agent tools are exposed and governed centrally through a gateway (the enterprise answer to "many agents, many tools"). Content judged from the title only. | verified (existence); content per title only |
| 8.4 | AWS re:Invent 2025 - Customize & scale foundation models using Amazon SageMaker AI (AIM363) | AWS Events | https://www.youtube.com/watch?v=_38nkfU9obE | 54:49 | re:Invent 2025, upload date ? | Model hosting | Deeper | BIKE | SageMaker AI for GenAI: customising and scaling foundation models, with live demos (Sumedha Swamy, Giuseppe). | verified |

Cross-references already in earlier blocks (AWS angle): Bedrock Knowledge Bases in 3.5 and 3.D2, Bedrock/AgentCore evaluation in 5.4, AgentCore guardrails in 6.3, model choice in 1.5, customization and inference in 7.3-7.6.

Optional desk list:

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 8.D1 | Amazon Bedrock Knowledge Bases - how to build RAG on AWS in 2025 | AWS Polska | https://www.youtube.com/watch?v=It769ydwS-k | 1:01:15 | date ? | Retrieval | Start | DESK (assumed from title) | A build-along for RAG on Bedrock Knowledge Bases. Regional AWS channel; content and mode judged from the title only. | verified (existence); content per title only |

**Full circle:** back to the Stack map in this file: Bedrock is model hosting, Knowledge Bases is retrieval, Guardrails is the guardrails layer, AgentCore is orchestration and runtime for agents, SageMaker AI is customization and serving. If you can place every service on a layer, you can compare it with a non-AWS alternative.

<details>
<summary>Recap questions (3)</summary>

1. Which stack-map layers does AgentCore cover, and which does it not?
   - It covers agent runtime, tool access (gateway), identity, memory and (with evaluations) quality and observability; it does not replace your data layer, your source systems or your governance process.
2. When would you pick SageMaker AI over Bedrock for a model?
   - When you need to customise or host models you control (fine-tuning, custom weights, specific serving settings); Bedrock suits managed access to many models with less operational burden.
3. Why put a gateway in front of agent tools?
   - One place to authenticate, authorise, log and rate-limit tool calls, instead of every agent integrating and securing each tool separately.
</details>

---

## Block 9: Enterprise architecture and operating at scale

**Why an architect needs this:** the hard part of GenAI at a big company is not a demo; it is gateways, resilience, cost control, platform ownership and a build-versus-buy stance that survives audit.

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| 9.1 | AWS re:Invent 2025 - The next frontier: Building the agentic future of Financial Services (INV209) | AWS Events | https://www.youtube.com/watch?v=_Wi_4I40bqQ | 54:45 | 2025-12-03 | Framing | Start | BIKE | Financial-services view from AWS's FS lead (Scott Mullins) with Allianz Technology's CTO (Axel Schell) and Coinbase's developer-platform engineering head (Erik Reppel). | verified |
| 9.2 | AWS re:Invent 2025 - Moody's: Architecting a multi-agent system on AWS (IND3303) | AWS Events | https://www.youtube.com/watch?v=HC8jSzNmNpU | 58:04 | re:Invent 2025, upload date ? | Orchestration/agents | Deeper | BIKE | A financial-data company's multi-agent architecture on AWS (Samuel Baruffi, AWS; Dennis Clement, Moody's Analytics). A real case study in a regulated, data-heavy domain. | verified |
| 9.3 | AWS re:Invent 2025 - Powering Enterprise AI: Architecting and Governing Agents at Iberdrola on AWS | AWS Events | https://www.youtube.com/watch?v=hKlX4xwNoKY | 36:10 | re:Invent 2025, upload date ? | Governance, Orchestration/agents | Deeper | BIKE | How a large utility architects and governs agents at enterprise scale (Global CIO Sergio Merchan, Unai Bermejo, AWS's Joseph Santamaria). Not a bank, but a good governance operating-model example. | verified |
| 9.4 | AWS re:Invent 2025 - Build and scale AI: from reliable agents to transformative systems (INV204) | AWS Events | https://www.youtube.com/watch?v=tqHCjUSRKxc | 1:02:25 | re:Invent 2025, upload date ? | Orchestration/agents | Deeper | BIKE | Reliability and scale lessons with AWS's Marc Brooker, Lyft's EVP of AI transformation (Jason Vogrinec) and Sendbird's CEO. Useful for platform-team and operating-model thinking. | verified |
| 9.5 | Multi-LLM Routing Strategies for Gen AI - Ethan Ferdosi | Optimized AI Conference | https://www.youtube.com/watch?v=2ld7cR9y0Po | 19:38 | date ? | Model hosting, Cost | Deeper | BIKE | Routing between models for cost, quality and availability (the gateway pattern). Content judged from the title only. | verified (existence); content per title only |
| 9.6 | FinOps X 2026 Keynote Day 1: The Wild West of AI, Token Economics and the New Job of FinOps | FinOps Foundation | https://www.youtube.com/watch?v=W4g8xvduIbs | 1:37:52 | 2026 (per title; upload date ?) | Cost | Deeper | BIKE | Token economics and what FinOps becomes with AI, from the FinOps Foundation's own conference. Content judged from the title only. | verified (existence); content per title only |
| 9.7 | AI Agents That Banks Can Trust | YC Root Access | https://www.youtube.com/watch?v=UKwpr_Trvns | 11:47 | date ? | Governance | Scholar | BIKE | Trust and control for agents in banking. Content judged from the title only; check the speaker and date. | verified (existence); content per title only |

Optional desk list: none for this block.

**Full circle:** the whole track in one frame. Each production concern here (routing, resilience, cost, ownership) maps to a layer from the stack map and to a block you have already watched; classically it is the enterprise platform-team pattern (shared gateway, paved road, chargeback) applied to a model instead of a database.

<details>
<summary>Recap questions (3)</summary>

1. Why put an LLM gateway between applications and models?
   - It centralises authentication, routing and fallback across models and regions, logging, guardrails, caching and cost attribution, so applications do not each rebuild these and you can swap models without code changes.
2. What belongs in a GenAI FinOps practice?
   - Cost per request and per business outcome (not just total spend), token budgets and quotas per team, model right-sizing and caching, and visibility of agent loops that multiply calls.
3. For a bank, how do you decide build versus buy for a GenAI capability?
   - Build where it is a differentiator or needs deep control of data and risk; buy where it is commodity and the vendor can meet your security, residency, audit and exit requirements. Keep the gateway, evaluation and governance layers under your own control either way.
</details>

---

## Gaps

- **Prompt-injection concept from a primary source.** Simon Willison's own talk on prompt injection and the lethal trifecta was not verified; 6.1 is a secondary explainer judged from its title. (The video "Open Questions for AI Engineering: Simon Willison" on the AI Engineer channel exists, but its content was not checked.)
- **Bank model-risk management for LLMs (SR 11-7 applied to GenAI)** from a regulator, large bank or Big-4 firm: only a training-channel video (6.7) was found, judged by title.
- **Vector database internals** (HNSW and other ANN indexes, vector DB selection): no credible video verified; Block 1.2 and Block 3.3 cover embeddings and retrieval but not index internals.
- **Tool/function-calling concept in BIKE form:** only a hands-on workshop (2.D1) was verified. Block 4 covers the agent loop at concept level.
- **Prompt caching, batching and token-cost mechanics from a primary source:** covered only indirectly by 7.4, 7.7 and 9.6.
- **Open versus closed models, small versus large, cost per token** as a dedicated architect-level video: not found; 1.5 is the nearest (vendor-framed).
- **JPMorgan, Capital One, Morgan Stanley and Citi-class case studies** from the banks' own engineers: search found mostly commentary channels, which were not used. 9.1-9.3 give financial-services and enterprise examples from AWS-hosted sessions instead.
- **Block 2 is thin** (two BIKE videos plus one desk workshop) because the search budget ran out before more candidates could be verified.
- **Non-AWS reference architectures** (Google Cloud, Microsoft/Azure) from the cloud providers' own channels: one candidate (an Egen partner interview from Google Cloud Next 2026) was read and rejected as marketing.

## Not checked

- **Exact lengths** are missing for many videos (marked "length ?"); the page's duration was blocked. For re:Invent sessions, ">=" values come from the last timestamp in a third-party write-up (dev.to, Kazuya) of the transcript, not from YouTube.
- **Upload dates** for many re:Invent sessions (marked "upload date ?").
- **Content of "per title only" videos** (about 20 of the 50): oEmbed confirmed that they exist with that title and channel, but the video page or a summary could not be read. Treat their "What you will get" as expectation, not verified content.
- **Seven pages that failed or were rate-limited when fetched** and were therefore not used or used by title only: Akka's "A Blueprint for Agentic AI Services | QCon London 2025" (EpPrZ1-OMe8, dropped), Nordic APIs "Design an Implementation of a Self-Service GenAI Platform in a Large Enterprise" (ktVuR4IdpzQ, dropped), AWS Cloud Bytes "Architecting Enterprise-Grade GenAI Systems on AWS" (J9QyD88LYvo, channel not confirmed as official, dropped), Matt Williams "How does function calling with tools really work?" (IdPdwQdM9lA, dropped), AIM3310, AIM3313 and NTA403 (kept by title).
- **Dropped after checking:** Jason Liu "Systematically Improving RAG applications" (e668bTot45w) was a course promotion; a Stanford CS229 lecture ID from memory returned an error and the re-upload found was by an unrelated channel; several lookalike channels (e.g. summary or relaxation channels re-using talk titles) were rejected.
- **Not searched at all:** OpenAI, Google DeepMind and Microsoft official channels; university courses (Stanford CS224N, CS329S, Berkeley LLM Agents); Databricks and Snowflake summit talks; NIST AI RMF and EU AI Act walkthroughs; the Google "Gemini Enterprise Agent Platform" videos.
- **Totals:** 28 of the 50 main videos have a known length or lower bound (sum >= 25.6 h); the other 22 are unknown, so the whole main path is an estimate of roughly 38-42 h. Optional desk videos are extra.

---

## Gap-fill pass 1 (2026-11-10)

One capped pass over the Gaps list. Every row below was confirmed with the YouTube oEmbed endpoint (title and channel copied exactly as returned, ID matched in the thumbnail URL). Lengths marked "(per podwise)" come from the third-party podwise.ai listing, not the YouTube page; lengths marked "(per ai.engineer)" come from the AI Engineer site's talk page. Dates: "upload date ?" means the YouTube upload date was not seen; the event year is given instead where a page stated it.

### Prompting and structured outputs (Block 2 gap)

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| G1 | AI prompt engineering: A deep dive | Anthropic | https://www.youtube.com/watch?v=T9aRN5JkmL8 | 1:16:42 | 2024-09-05 (per podwise) | Orchestration/agents | Start | BIKE | A roundtable of Anthropic staff on what makes a good prompt engineer and how to write and iterate on prompts; the philosophy behind prompting rather than a template list. A conversation, so it works with no screen. Pre-2025, so model names are dated; the habits are not. | verified; content per podwise summary |
| G2 | No more bad outputs with structured generation: Remi Louf | AI Engineer | https://www.youtube.com/watch?v=aNmfvN6S_n4 | 15:31 | AI Engineer World's Fair 2024, upload date ? | Orchestration/agents | Deeper | BIKE | How constrained decoding (the Outlines library, by its creator) forces a model to emit output that matches a schema, as opposed to asking nicely and retrying. This is the mechanism behind provider "structured output" modes. Content judged from the title and the conference page. | verified |

Belongs after Block 2 (2.1 and 2.2). Suggested order: G1, then 2.1, then 2.2, then G2.

### Tool and function calling as a concept (listen-only)

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| G3 | Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks | AI Engineer | https://www.youtube.com/watch?v=zuMw0pkPXpU | 25:17 | AI Engineer Summit 2025, upload date ? | Orchestration/agents | Deeper | BIKE | Per the talk page: a tool definition (name, description, input and output schema) is a behavioural contract; who owns the model-tool loop (your app or the agent framework); hosting tools behind MCP or a tool platform so you can swap frameworks; the risk of letting the model generate queries instead of using fixed tools. Architect-level, no live coding. | verified |

Belongs after Block 2 as the listen-only counterpart to desk video 2.D1, and again alongside Block 4 (4.1).

### Prompt injection, the lethal trifecta and tool-call risk

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| G4 | Prompt Injection, explained | Simon Willison | https://www.youtube.com/watch?v=FgxwCaL6UTA | 12:16 | 2023-05-02 (date of the blog post that embeds it) | Guardrails | Start | BIKE | Prompt injection from the person who named it: the attack, why it is not solved like SQL injection, and why it matters once a model has tools. 2023, so it predates the "lethal trifecta" framing but gives the foundations. | verified |
| G5 | Open Questions for AI Engineering: Simon Willison | AI Engineer | https://www.youtube.com/watch?v=AjLVoAu-u-Q | 24:33 | AI Engineer Summit 2023 (his companion post is dated 2023-10-17); upload date ? | Guardrails | Deeper | BIKE | A broad keynote; the prompt-injection section ("When content becomes an instruction", from 15:35 per the talk page) covers the attack and an email-assistant example. Listen to the relevant segment rather than treating the whole talk as on-topic. May be dated (2023). | verified |
| G6 | "I've never seen anything scarier than an LLM with tool calls." — Erik Meijer aka @HeadinTheBox | AI Engineer | https://www.youtube.com/watch?v=-CnA2lGfymY | 21:13 | AI Engineer World's Fair 2026, upload date ? | Guardrails | Deeper | BIKE | Per the talk page: prompt injection compared with SQL injection, the lethal trifecta (private data, untrusted content, external communication), and a proposal to have a checker inspect an agent's plan before an interpreter runs it. The most current of the three, but a single speaker's argument. | verified |

Belongs after Block 6 (6.1). Suggested order: G4, G6, G5 segment; then 6.1 is now optional. Simon Willison's own lethal-trifecta talk (Bay Area AI Security Meetup, Aug 2025) was not recorded per his blog, so it cannot be watched; his annotated slides are on his site.

### Vector database internals

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| G7 | pgvector: Stylish Hierarchical Navigable Small World Indexes (Jonathan Katz) | CMU Database Group | https://www.youtube.com/watch?v=YU66YlZW6dA | 1:10:37 | 2023-11-21 (per podwise; talk given 2023-11-20) | Embeddings/vector | Scholar | BIKE | A university database seminar on how HNSW indexes work and how pgvector implements them: design decisions, performance work, trade-offs. Dense and database-oriented, so best after Block 3. Fits a bank that already runs Postgres. 2023, so pgvector features have moved on; the index ideas have not. | verified; content per CMU page description |

Belongs after Block 3 (3.3). This is a single-index deep dive, not a "how to choose a vector store" survey; that survey remains a gap.

### Token-cost mechanics

| # | Title | Channel | Link | Length | Published | Layer | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-----------|-------|-------|------|-------------------|--------|
| G8 | Your Agent Is Wasting Tokens and You Don't Know It - Erik Hanchett, AWS | AI Engineer | https://www.youtube.com/watch?v=uiP88SpCi1Q | 5:55 | AI Engineer World's Fair 2026, upload date ? | Cost | Start | BIKE | Per the talk page, five controls: cache repeated prompt content (system prompt, tool definitions), route tasks by difficulty to cheaper models, offload large tool results, cap loops, trim history with a summary. Short and from an AWS developer advocate using the Strands SDK for demos, so the SDK parts are vendor-specific; the five levers are general. | verified |

Belongs after Block 7 (7.7) and alongside Block 9 (9.5, 9.6).

### Still gaps after this pass

- **Bank model-risk management for LLMs (SR 11-7 style):** one candidate was found (GARP webcast "Managing the Risks of GenAI Models", 2024-11-06, with H2O.ai and MathWorks speakers covering SR 11-7 validation of LLMs) but it is a registration page, not a YouTube video, so it was not added. 6.7 remains the only video in the file.
- **How to choose a vector store** (survey of options and trade-offs): nothing credible found; G7 covers one index type only.
- **Prompt caching, batching and routing from an AI-lab or cloud-provider channel itself:** G8 is the only item; no Anthropic, OpenAI or AWS-channel video on caching or batch pricing was verified.
- **Case studies from large banks' own engineers:** one candidate found (Capital One's Rashmi Shetty on the TWIML AI Podcast, episode 765, 2026-04-16, about 50 min by chapter list) but no YouTube ID could be found, so it could not be oEmbed-checked. It is an audio-first episode that can be listened to from twimlai.com/go/765 (not verified in this pass as a video).
- **Block 2** is still only five BIKE items (2.1, 2.2, G1, G2, G3) and no OpenAI or Google structured-outputs talk.
- **Simon Willison's lethal-trifecta talk** has no recording; G6 is the best verified substitute.

### Rejected or unverified in this pass

- hkhDdcM5V94, "Building with Anthropic Claude: Prompt Workshop with Zack Witten" (AI Engineer): oEmbed confirmed it exists, but length, date and whether it is listen-only or a live-prompting workshop could not be checked. Not added; try it at a desk if wanted.
- yj-wSRJwrrc, "Pydantic is all you need" (Jason Liu, AI Engineer Summit 2023): listed on ai.engineer but not oEmbed-checked, and it overlaps 2.2. Not added.
- Capital One / Rashmi Shetty (TWIML #765): no YouTube ID found, see above.
- GARP "Managing the Risks of GenAI Models": not a YouTube video, registration required.
- Simon Willison, "My Lethal Trifecta talk at the Bay Area AI Security Meetup": his post says the talk was not recorded.
- recapio.com, podwise.ai, lilys.ai and pulse.bot pages: third-party summary sites, used only to find IDs or lengths; the lilys.ai page redirected to another host and was not followed.
- Search results for HNSW and prompt caching returned only blogs, vendor docs and course-note sites (KodeKloud notes, Zilliz, DigitalOcean, AWS blog posts); no verifiable video IDs came out of them.

