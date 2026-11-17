# Track H: Build GenAI projects, one layer at a time

**What this track is.** A desk track of follow-along build videos: you type the code the video types, run it, and end each block with something that works. It starts with a single script that calls a language model and grows, one layer at a time, into a complete GenAI system on AWS: a domain name, HTTPS, an edge firewall, a gateway, authentication, an API service, retrieval, tools and agents, a database, a queue, a cache, tracing, evaluations, guardrails, infrastructure as code and a delivery pipeline. Tracks C, D, E and G explain these layers; this track has you build them.

**The one rule: progression.** Each block adds one new layer (at most two small ones) on top of what already works. Nothing appears that an earlier block did not introduce. Every block ends with a **Progression check** (what is new, what is reused, whether the step is too big), and the ladder below was split wherever a step looked too big.

**Two kinds of building in each block.**
1. **Follow the video.** Build exactly what the main video builds, in its own code. This is the safe, guided part: if you get stuck, the video and its repository are there.
2. **Carry it into DocDesk.** Then add the same layer to your own running project, DocDesk (below), with a short checklist. This is where the layers pile up into one system instead of twenty unrelated demos.

**The thread project: DocDesk.** A question-answering assistant over a small library of public documents of the kind a bank publishes or reads (for example consumer guides from the CFPB or FDIC, downloaded as PDFs). It starts as a terminal chatbot (Block 2) and ends as a multi-user service on AWS with its own domain (Block 22). Public data only: nothing from work, no employer data, no real customer data.

**Defaults.** Python 3.11 or later; VS Code; Git and GitHub; Docker from Block 9; AWS from Block 14, kept inside a monthly budget alarm (Block 14 sets one up). A hosted model API (OpenAI or Anthropic) for the first blocks, a local model with Ollama from Block 6, Amazon Bedrock from Block 17. Every cloud block ends with **Cost and teardown**.

---

## The mental model: one request through a real GenAI system

Read this before Block 1, and come back to it at the start of every block. The ladder lights up one box at a time.

```
 You (browser or app)
   |
   |  1. DNS: the name docdesk.example.com becomes an address        [Block 16]
   v
 CDN + WAF: cache static files close to the user, block bad traffic  [Block 16]
   |
   |  2. HTTPS: an encrypted connection (TLS certificate)            [Block 16]
   v
 Load balancer / API gateway: one front door; routes, throttles,     [Blocks 13, 16]
 checks API keys
   |
   v
 Auth: who is this user, and what may they see? (login, tokens)      [Blocks 13, 22]
   |
   v
 Web UI  --->  API service (FastAPI): the contract of your app       [Blocks 4, 5]
                  |
                  v
          GenAI orchestration: the "brain" of the request
            - prompt templates and structured output                  [Block 3]
            - conversation memory                                     [Block 2]
            - retrieval (RAG): find the right passages first          [Blocks 7, 8]
            - tools and agents: call functions, loop until done       [Blocks 11, 12]
            - guardrails: check what goes in and comes out            [Block 20]
                  |
                  v
          Model: hosted API, local model or Amazon Bedrock           [Blocks 1, 6, 17]
                  |
   Data layer:  SQL database (users, chats)                           [Block 10]
                vector store (embeddings)                             [Blocks 7, 10]
                object storage (the PDFs)                             [Block 14]
                cache (repeat questions)                              [Block 18]
                queue + workers (slow jobs such as ingesting files)   [Block 18]

 Around everything:
   containers and a runtime (where the code runs)                    [Blocks 9, 15]
   cloud account, identities and secrets                             [Blocks 14, 15]
   logs, traces, cost per request, evaluations                       [Block 19]
   infrastructure as code and a delivery pipeline                    [Block 21]
```

**The walk, in words.** A user types a question. DNS turns the name into an address; the request reaches the edge, where a CDN serves static files and a web application firewall drops obvious attacks; HTTPS keeps it private. A load balancer or API gateway is the single front door: it routes the request, throttles abusive clients and checks keys. The auth layer decides who the user is and which documents they may see. The API service receives a typed request. The orchestration code builds the prompt, looks up relevant passages (retrieval), maybe calls tools, and sends everything to a model. The answer comes back through guardrails and is streamed to the user, while the system writes the conversation to the database, logs a trace with the cost of the call, and keeps slow work (reading new PDFs) on a queue for background workers. Infrastructure as code describes all of it, and a pipeline tests and ships each change.

**Why this order.** You build from the inside out: first the part that is new to you and unique to GenAI (talking to a model, prompts, retrieval, tools), then wrap it in the parts every enterprise system has (API, containers, database, auth), then move it to the cloud and add the internet edge, and last the parts that keep it reliable, safe and cheap in production (queues, caches, tracing, evaluations, guardrails, automation). Each wrapper is introduced only when there is something worth wrapping.

---

## The ladder

| Block | You build | New layer(s) | Reuses | Progression check |
|---|---|---|---|---|
| 0 | Nothing yet: the map above, plus a few short "how it works" videos | the mental model | nothing | Starting point. |
| 1 | One Python script that sends a question to a model and prints the answer | model API, API keys in environment variables | Block 0 map | Smallest possible step: one file, one call. |
| 2 | A terminal chatbot that remembers the conversation, streams its answer and prints token use and cost | conversation memory, streaming, tokens and cost | Block 1 call | One idea added: a list of messages. Cost appears early on purpose. |
| 3 | Prompt templates and structured output: the model returns JSON your code validates | prompt layer, output contract (Pydantic) | Block 2 chatbot | Still one file; adds the "contract" idea the API needs later. |
| 4 | A chat web page (Streamlit or Gradio) over the Block 2-3 code | user interface | Blocks 2-3 as functions | Only the screen is new; the logic is unchanged. |
| 5 | Your own HTTP API (FastAPI); the web page now calls it | API service, HTTP and JSON, OpenAPI docs | Blocks 3-4 | Splits one program into client and server: the first real architecture step. |
| 6 | A local model with Ollama, switchable with the hosted one by a setting | model abstraction (provider switch) | Block 5 API | Same API, different engine behind it; prepares for Bedrock in Block 17. |
| 7 | Embeddings and semantic search over a few documents (vector store such as Chroma) | embeddings, vector store | Block 5-6 API | Retrieval without generation first, so RAG is not two new ideas at once. |
| 8 | RAG: ask questions of your PDFs with cited answers, behind your API | chunking, retrieval pipeline, citations | Blocks 6-7 | Joins two things you already have: search (7) and generation (1-6). |
| 9 | Put the API and UI in containers and run them together with Docker Compose | containers, multi-service runtime | Block 8 app | Packaging only; the code does not change. |
| 10 | Add Postgres with pgvector: users, chat history and vectors in one database | SQL database, persistence, migrations | Blocks 8-9 | Swaps the vector store and adds history; runs in the Compose stack from Block 9. |
| 11 | Tool calling: the model calls your functions (a calculator, a database query) | tool layer | Blocks 5, 10 | One tool loop, no agent framework yet. |
| 12 | A small agent (LangGraph or similar) and your own MCP server exposing a DocDesk tool | agent loop, MCP | Block 11 tools | Tools first, then the loop that chooses them. |
| 13 | Login and API keys, rate limiting, and a reverse proxy / gateway in front, all locally | authentication, authorization, gateway | Blocks 5, 9, 10 | Security edge built locally before any cloud, so only one thing is new. |
| 14 | AWS foundations: account safety, IAM users and roles, the CLI, a budget alarm, S3 for the PDFs | cloud account, identity, object storage | DocDesk PDFs | No deployment yet; just a safe place to deploy into. |
| 15 | Deploy the DocDesk containers to AWS (ECR plus App Runner or ECS Fargate), database on RDS, secrets in Secrets Manager | cloud runtime, managed database, secrets | Blocks 9, 10, 14 | The same containers from Block 9 move to the cloud; nothing else changes. |
| 16 | The internet edge: your domain (Route 53), HTTPS (ACM), a load balancer or API Gateway, CloudFront and WAF | DNS, TLS, edge, cloud gateway | Block 15 service | Puts a proper front door on a service that already runs. |
| 17 | Amazon Bedrock as a third model provider, then Bedrock Knowledge Bases compared with your own RAG | managed GenAI services | Blocks 6, 8 | Uses the provider switch from Block 6; build-versus-buy is the lesson. |
| 18 | A queue and workers for ingesting PDFs, a cache for repeat questions, streaming responses | async processing, caching | Blocks 8, 15 | Slow work moves off the request path. |
| 19 | Tracing, logs and cost per request; a small evaluation set scored automatically | observability, evaluation | Blocks 8, 17 | You measure before you tune or add guardrails. |
| 20 | Guardrails: prompt-injection tests, PII redaction, input/output checks, permission-aware retrieval | safety layer | Blocks 13, 19 | Uses the eval set from Block 19 to show the guardrails work. |
| 21 | Infrastructure as code (Terraform or AWS CDK) and a GitHub Actions pipeline with tests and evals | IaC, CI/CD | Blocks 14-20 | Writes down what you built by hand, so it can be rebuilt and changed safely. |
| 22 | Capstone: DocDesk end to end, with multi-user sign-in (Cognito), per-user data, cost dashboard and a two-page design document | the whole stack, design review | everything | No new technology; joins and defends the whole system. |

---

## Block 0: The map

**What you build:** Nothing yet. You watch five short "how it works" videos and then draw the request walk from the mental model above from memory, so every later block has a box to land in.
**New layer:** the mental model (names for the boxes and arrows). **Reuses:** nothing.
**Needs:** nothing. Paper and a pen, or any diagram tool.
**Architecture so far:**
```
 * browser --DNS/TLS/HTTP--> * load balancer / API gateway --> * API service
                                                                  |
                                              * prompt + (RAG, tools, guardrails)
                                                                  |
                                                               * model
 (all boxes are ideas only; nothing is built yet)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 0.1 | What happens when you type a URL into your browser? | ByteByteGo | https://www.youtube.com/watch?v=AlkDbnbv7dk | length ? | Start | BIKE | The first two arrows of the map: the name becomes an address (DNS), a connection is opened and secured (TCP, TLS), and an HTTP request goes out and a response comes back. From 2022, but these steps have not changed. | verified; description |
| 0.2 | What is a REST API? | IBM Technology | https://www.youtube.com/watch?v=lsMQRaeKNDk | 9:12 | Start | BIKE | Fast lane: a short REST refresher, probably familiar to you; included so the REST, gRPC and GraphQL comparison has its third corner. | verified; title-based; also in Track D 3.O4; watch once |
| 0.3 | What is an API Gateway? | NGINX | https://www.youtube.com/watch?v=hYgP0cBORVg | length ? | Start | BIKE | Per its chapters, a short vendor explainer of the gateway as the single entry point that secures, scales and speeds up API traffic, from monoliths to microservices; keep the idea and skip the product part at the end (2019). | verified; description |
| 0.4 | What is LOAD BALANCING? ⚖️ | Gaurav Sen | https://www.youtube.com/watch?v=K0Ta65OqQkY | length ? | Start | BIKE | Client and server terms, why one server is not enough, and how a load balancer spreads requests across several, including request stickiness; a 2018 whiteboard talk whose ideas are unchanged. | verified; description |
| 0.5 | RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models | IBM Technology | https://www.youtube.com/watch?v=zYGDpG-pTho | 13:10 | Start | BIKE | A comparison of the three ways to adapt a model to a task: what each costs, what each can and cannot add, and how they are combined. | verified; content per sozai transcript page; also in Track B G6; watch once |

**Code:** none; this block is concepts only.
**Optional (extra):** none for this block.
**Do it (30 minutes):**
1. Close the page. On one sheet, draw the request walk from the mental model from memory: browser, DNS, CDN and firewall, HTTPS, load balancer or API gateway, auth, web UI, API service, orchestration (prompt, memory, retrieval, tools, guardrails), model, and the data layer underneath.
2. Draw the arrows for one question: "What fees can my bank charge on a checking account?" Number them in the order the request travels, and draw the answer coming back.
3. Next to each box, write in a few words what it does, in your own words (for example "load balancer: spreads requests across copies of the API").
4. Mark with a star the six boxes that Blocks 1 to 6 build (model call, memory, prompt and structured output, web UI, API service, provider switch); everything else stays grey for now.
5. Compare with the diagram in this file and fix what you missed in a different colour. Keep the sheet; you will update it at the end of every block.

**Carry it into DocDesk:**
- Create an empty folder `docdesk/` (a Git repository) with a `README.md` that holds a photo or ASCII copy of your diagram.
- Download three to five public consumer-banking guides as PDFs (for example from the CFPB or FDIC) into `docdesk/docs/`. Nothing from work.
- In the README, write one sentence on what DocDesk will do and one on who would use it.

**Done when:** you can draw the whole walk from memory in under ten minutes, and you can say in one sentence what each of DNS, TLS, API gateway, load balancer and RAG does.
**Stretch:** open your browser's developer tools (Network tab), load any website, and find the DNS, connection (TLS) and request timings for the first request.
**Cost and teardown:** no cost; nothing to stop or delete.
**Progression check:** New: the vocabulary and the picture. Reused: nothing. Jump size: small; it is listening plus one drawing, and every term returns later with code attached.
**Architect's question:** where should a check live, at the gateway (once, for every service) or inside each service (closer to the data)? Rate limits and API keys usually go at the edge; "may this user see this document" usually cannot, because only the service knows the data.

<details><summary>Recap questions</summary>

1. Q: In order, what happens between typing a URL and seeing a page? A: DNS turns the name into an IP address, the browser opens a TCP connection and a TLS handshake secures it, the browser sends an HTTP request, the server (often behind a load balancer) returns a response, and the browser renders it.
2. Q: What is the difference between a load balancer and an API gateway? A: A load balancer spreads traffic across copies of a service; an API gateway is the single front door for many APIs and adds routing, authentication, throttling and similar policies. In practice one product often does both.
3. Q: In an LLM application, where do RAG, tools and guardrails sit relative to the model? A: Around it, in the orchestration code: retrieval adds relevant passages to the prompt before the call, tools are functions the model can ask the code to run, and guardrails check what goes into and comes out of the model.

</details>

---

## Block 1: First LLM call

**What you build:** One Python script, in its own virtual environment, that reads an API key from a `.env` file, sends one question to a hosted model and prints the answer.
**New layer:** model API and API keys in environment variables. **Reuses:** the Block 0 map (this is the "Model" box).
**Needs:** nothing from this track. One-time installs: Python 3.11 or later, VS Code, and an OpenAI account with an API key and a small prepaid credit (an Anthropic key works too; see the optional row).
**Architecture so far:**
```
 * your terminal
      |
 * ask.py  (python-dotenv reads .env -> OPENAI_API_KEY)
      |  HTTPS
      v
 * hosted model API
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 1.1 | Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments with the Built-In venv Module | Corey Schafer | https://www.youtube.com/watch?v=Kg1Yvry_Ydk | length ? | Start | DESK | How to create, activate and delete a virtual environment with Python's built-in venv module; from 2019 but venv has not changed, and the description links a Windows version. | verified; description |
| 1.2 | Call Your First AI Model in Python with OpenAI API | Data with Dylan | https://www.youtube.com/watch?v=VumrSUvEnDc | length ? | Start | DESK | Per its chapters, a 2026 step-by-step first call: a virtual environment, installing the packages, setting up the API key, calling a GPT model, system and user prompts and the messages parameter, then a small content-idea generator. A small channel, chosen because it matches this block step for step. | verified; description |

**Code:** 1.1: no public repo; type along from the video. 1.2: the description links the starter and finished code on GitHub under `github.com/dylans0ng/` (the link is cut off on the watch page, so open it from the video description; I could not check its date).
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 1.O1 | Python AI Chatbot with Anthropic’s Claude API | Code Yoga | https://www.youtube.com/watch?v=i-EZvYfWWUA | length ? | Start | DESK | The Anthropic version of this block in a few minutes (2025): creating an Anthropic API key, installing the anthropic package, the first call, and a preview of Block 2's conversation memory. A small channel. | verified; description |

**Build it (follow the video):**
1. Follow 1.1: make a folder `llm-hello/`, run `python3 -m venv .venv`, activate it, and check that `which python` points inside `.venv`.
2. Install the packages the video installs (the OpenAI SDK and python-dotenv) with `pip install openai python-dotenv`, then `pip freeze > requirements.txt`.
3. Create an API key in the OpenAI dashboard, put it in a file `.env` as `OPENAI_API_KEY=...`, and add `.env` and `.venv/` to `.gitignore` before your first commit.
4. Type the video's script: load the `.env`, create the client, send one question, print the answer. Make sure your code uses the current SDK (`client = OpenAI()` and then a `client.chat.completions.create(...)` or `client.responses.create(...)` call); if you ever see `openai.ChatCompletion.create`, that is the pre-2024 API and will not run.
5. Run it; you should see a model's answer printed in the terminal.
6. Add a system message (as the video does) and see how the same question changes tone; then change the model name to a smaller, cheaper one and compare.
7. Break it on purpose: rename the key in `.env` and run again, so you recognise the authentication error later.

**Carry it into DocDesk:**
- In `docdesk/`, create the same `.venv`, `.env`, `.gitignore` and `requirements.txt`.
- Add `docdesk/smoke_test.py`: one call that asks "Reply with the word OK" and prints the reply. You will rerun it whenever a later block changes keys, models or providers.
- Put the model name in `.env` too (`DOCDESK_MODEL=...`) and read it with `os.getenv`, so no model name is hard-coded.

**Done when:** `python smoke_test.py` prints OK from the model, and `git status` shows that `.env` is not tracked.
**Stretch:** make the same call to Anthropic with the anthropic SDK (`client.messages.create`, following 1.O1) and print both answers side by side.
**Cost and teardown:** a few short calls with a small model cost a fraction of a cent each; the whole block stays well under a dollar. Set a monthly usage limit in the provider's billing settings now. Nothing to stop; delete keys you no longer use.
**Progression check:** New: venv, the SDK, an API key, one call. Reused: only the Block 0 picture. Jump size: small; one file and one call, with every step on screen in the video.
**Architect's question:** who owns the API key? On a laptop it is one key in a `.env` file; in a bank, keys sit in a secrets manager, are scoped per team and environment, rotated, and usually never reach application code directly because a gateway holds them (Blocks 13, 15 and 16).

<details><summary>Recap questions</summary>

1. Q: Why use a virtual environment for every project? A: It keeps each project's packages and versions separate from the system Python and from other projects, so `requirements.txt` describes exactly what this project needs.
2. Q: Why does the key go in `.env` (or an environment variable) and not in the script? A: So it is never committed to Git or shared with the code; the code reads it at run time and each environment can supply its own key.
3. Q: How do you recognise a tutorial written for the old OpenAI SDK? A: It calls `openai.ChatCompletion.create(...)` on the module; the current SDK (1.0 and later) creates a client object and calls `client.chat.completions.create(...)` or `client.responses.create(...)`.

</details>

---

## Block 2: Terminal chatbot with memory, streaming, tokens and cost

**What you build:** A terminal chatbot that keeps the conversation in a list of messages, streams each answer as it is generated, and prints the tokens used and the cost of every call.
**New layer:** conversation memory, streaming, tokens and cost. **Reuses:** the Block 1 call, venv and `.env`.
**Needs:** Block 1 working (a call that prints an answer).
**Architecture so far:**
```
 terminal  (input loop)
      |
 chat.py
   * messages = [system, user, assistant, user, ...]
   * stream=True  -> print each chunk
   * usage -> tokens -> cost
      |
 hosted model API
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 2.1 | How to Add Memory to Your AI Chatbot in Python with OpenAI API | Data with Dylan | https://www.youtube.com/watch?v=wVodSD_7n4A | length ? | Start | DESK | The direct sequel to 1.2 (2026): why the model forgets, then a growing conversation history that stores both user and assistant messages, a full memory demo and the limit of this approach. | verified; description |
| 2.2 | How to Stream OpenAI Responses in Python (Sync & Async) | Raj Kapadia | https://www.youtube.com/watch?v=FJJn3ZVm3VA | length ? | Deeper | DESK | Streaming OpenAI responses in synchronous and asynchronous code, side by side, plus reading the usage numbers to work out what a call cost (2025). | verified; description |

**Code:** 2.1: the same `github.com/dylans0ng/` repository as 1.2 (starter and finished code; the link is cut off on the watch page, so open it from the description). 2.2: the description links a repository under `github.com/RajKKapadia/` that is cut off on the watch page; open it from the description, or type along from the video.
**Optional (extra):** none for this block.
**Build it (follow the video):**
1. Copy your Block 1 script to `chat.py` in the same venv.
2. Follow 2.1: wrap the call in a `while True` loop that reads input, and keep a `messages` list; append each user message before the call and each assistant reply after it.
3. Run the video's recall test: tell the bot your name, ask it two turns later, and watch it fail before you store assistant replies and pass after.
4. Add a system message at position 0 of the list and an `exit` command.
5. Follow 2.2 (the synchronous part first): set `stream=True`, loop over the chunks and print each piece with `print(..., end="", flush=True)`; collect the pieces into one string and append that to `messages`.
6. Read the usage numbers the video shows (input and output tokens); for a streamed Chat Completions call you must ask for them with `stream_options={"include_usage": True}`, and the Responses API reports them in the final event.
7. Look up your model's price per million input and output tokens on the provider's pricing page, store both in constants, and print `tokens in, tokens out, cost` after every answer.
8. Watch the input-token count grow every turn: that is the cost of memory.

**Carry it into DocDesk:** (DocDesk is born here.)
- Create `docdesk/chat.py` from your Block 2 code.
- System prompt: "You are DocDesk. You answer questions about consumer banking documents (account fees, overdrafts, deposit insurance, credit reports) in plain English. If you are not sure, say so." Keep it in `docdesk/prompts/system.md` and load it from the file.
- Commands: `/reset` clears the history (keeping the system message), `/cost` prints the running total for the session.
- Keep only the last N turns (for example 10) when sending, so the history cannot grow without limit.

**Done when:** DocDesk remembers a fact from three turns earlier, the answer appears word by word, and every answer ends with a line like `in=412 out=96 cost=$0.0003`.
**Stretch:** count tokens before sending with `tiktoken` (OpenAI's tokenizer library) and trim the oldest turns when the history would pass a budget you choose.
**Cost and teardown:** a chat session with a small model costs cents; long sessions cost more because every turn resends the whole history, which your cost line now shows you. Nothing to stop.
**Progression check:** New: a messages list, a loop, streaming and the usage numbers. Reused: the Block 1 client, key and venv. Jump size: small; 2.1 continues the exact code of 1.2, and 2.2 adds one flag and one loop.
**Architect's question:** where does conversation memory live at scale? In the client (sent with every request, so the server stays stateless) or on the server (a session store, so you can audit, trim and summarise it)? Each choice changes cost, privacy and how you scale the API; Block 10 moves it into a database.

<details><summary>Recap questions</summary>

1. Q: Why does a chat model "forget" unless you send the history? A: Each API call is stateless; the model sees only the messages in that request, so memory is your code resending earlier turns.
2. Q: What does streaming change, and what does it not change? A: It changes when the user sees text (piece by piece, so the first words arrive sooner); it does not change the total tokens, the cost or the final answer.
3. Q: Why does cost per turn rise during a long chat? A: Every call resends the whole history as input tokens, so input tokens (and cost) grow with each turn unless you trim or summarise.

</details>

---

## Block 3: Prompt templates and structured output

**What you build:** Prompts kept in template files, and calls whose answers come back as JSON that your code validates with a Pydantic model; plus a small extractor that pulls named fields out of a short document.
**New layer:** the prompt layer and an output contract (Pydantic). **Reuses:** the Block 2 chatbot, client and cost line.
**Needs:** Blocks 1 and 2 working. One-time: `pip install pydantic` (the course repo uses `uv`; plain `pip` in your venv works too).
**Architecture so far:**
```
 terminal
      |
 chat.py
   messages + streaming + cost          (Block 2)
   * prompts/*.md  -> prompt template
   * schema: Pydantic model  -> validated object
      |
 hosted model API
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 3.1 | Prompting 101 \| Code w/ Claude | Anthropic | https://www.youtube.com/watch?v=ysPbXH0LpIE | 24:52 | Start | BIKE | Anthropic applied-AI staff (Hannah Moran, Christian Ryan) on how to structure a good prompt: role and task, context, examples, output format, iterating on failures. Concepts carry across vendors. | verified; also in Track C 2.1; watch once |
| 3.2 | Pydantic Crash Course - Build Reliable Python & AI Applications | Dave Ebbelaar | https://www.youtube.com/watch?v=PkQIREapb9o | length ? | Start | DESK | A 2026 course in eight chapters: type hints, your first model, validation and fields, nested models, settings from environment variables, and structured output from an LLM validated into a Pydantic model. | verified; description |

**Code:** 3.2: https://github.com/daveebbelaar/pydantic-crash-course (last updated 2026-01; it matches the description's cut-off link and its README follows the same chapters; chapter 7 uses `client.responses.parse(..., text_format=YourModel)`).
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 3.O1 | Pydantic is STILL all you need: Jason Liu | AI Engineer | https://www.youtube.com/watch?v=pZ4DIH2BVqg | 15:21 | Deeper | BIKE | Why typed, validated outputs (schemas) are the bridge from LLM to application code, plus business use cases and where the field was heading. Provider-native structured-output modes have since matured, so treat the library specifics as possibly dated. | verified; also in Track C 2.2; watch once |

**Build it (follow the video):**
1. Watch 3.1 away from the keyboard and write down its prompt parts (role and task, context, examples, output format) as a checklist.
2. Clone the course repo for 3.2 or type along in your Block 2 venv; work through chapters 2 to 4 (type hints, your first model, validation and fields) and run each example.
3. Chapter 5 (nested models): build a model that contains a list of another model, and print `model_dump_json(indent=2)`.
4. Chapter 6 (settings): move your API key and model name into a `Settings(BaseSettings)` class that reads `.env`; this replaces the scattered `os.getenv` calls.
5. Chapter 7 (structured output): define a model, call the API with it as the expected format, and print the typed fields of the parsed result; then feed it text that does not fit and watch validation fail.
6. Build the mini extractor: paste one paragraph from one of your DocDesk PDFs (for example a fee table) and extract a `list[Fee]` where `Fee` has `name: str`, `amount: float | None` and `when_charged: str`.
7. Move every prompt string out of your code into `prompts/*.md` files with `{placeholders}`, and fill them with `str.format` or a small helper.

**Carry it into DocDesk:**
- Add `docdesk/schemas.py` with `class DocDeskAnswer(BaseModel)`: `answer: str`, `confidence: Literal["low", "medium", "high"]`, `follow_up_question: str`.
- Add `docdesk/core.py` with two functions: `ask(history, question) -> DocDeskAnswer` (structured) and `ask_stream(history, question)` (yields text, from Block 2). `chat.py` now only handles input and printing.
- Update `prompts/system.md` with the 3.1 checklist: role, scope (consumer banking documents), how to judge confidence, and "suggest one useful follow-up question".
- Print each answer as three labelled lines, plus the cost line from Block 2.

**Done when:** every DocDesk answer prints as `answer / confidence / follow-up`, `DocDeskAnswer.model_validate(...)` never raises on ten varied questions, and the extractor returns a list of `Fee` objects for your sample paragraph.
**Stretch:** add `pydantic.Field(description=...)` to every field and compare the quality of the follow-up questions with and without the descriptions.
**Cost and teardown:** a few cents; structured output adds a little prompt overhead per call. Nothing to stop.
**Progression check:** New: prompt files, Pydantic models, a schema-constrained call. Reused: the Block 2 client, history and cost line. Jump size: medium; Pydantic is new, but 3.2 starts from type hints and only reaches LLM output in its last chapter, by which point you have used every piece.
**Architect's question:** structured output and streaming pull against each other: a JSON object is only valid when it is complete, so a typed answer is harder to stream token by token. Which screens need the contract (anything another system reads) and which need the speed (anything a person reads)?

<details><summary>Recap questions</summary>

1. Q: What does Pydantic add over asking the model to "reply in JSON"? A: A schema the provider can enforce and a validation step in your code, so you get typed fields or a clear error instead of hoping the text parses.
2. Q: Why keep prompts in files instead of strings in code? A: They can be reviewed, versioned and changed without touching code, and later evaluated and released like any other artifact (Block 19).
3. Q: Name the four prompt parts from 3.1. A: Role and task, context, examples, and the output format (then iterate on failures).

</details>

---

## Block 4: Chat web UI with Streamlit

**What you build:** A chat web page in Streamlit over the same `core.py`: chat bubbles, history kept between reruns, and the answer streamed into the page.
**New layer:** user interface. **Reuses:** Blocks 2 and 3 as functions (`ask`, `ask_stream`).
**Needs:** Block 3 working, with the logic in `core.py` rather than in the input loop. One-time: `pip install streamlit`.
**Architecture so far:**
```
 * browser (localhost:8501)
      |
 * app.py (Streamlit: st.chat_message, st.chat_input, st.session_state)
      |  import
 core.py  ask() / ask_stream()          (Blocks 2-3)
      |
 hosted model API
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 4.1 | Introducing Streamlit Chat Elements | Streamlit | https://www.youtube.com/watch?v=4sPnOqeUDmk | length ? | Start | DESK | Streamlit's own short introduction of `st.chat_message` and `st.chat_input`, the two building blocks of a chat page (2023; these two elements are still the current API). | verified; description |
| 4.2 | Build AI Chatbot with Streamlit & OpenAI! | AI DevBytes | https://www.youtube.com/watch?v=UKclEtptH6k | length ? | Start | DESK | A full type-along (2024) from a starter repo: a config file, a separate LLM helper module, a chat page with model choice, temperature and max-token settings, and streamed answers. A small channel; its separation of UI and LLM helper is the pattern you want. | verified; description |

**Code:** 4.1: no repo (the description links the Streamlit docs). 4.2: https://github.com/AIDevBytes/Streamlit-OpenAI-Chatbot (the finished project, last updated 2024-03; the description also links a starter repo whose address is cut off on the watch page). It uses the current SDK (`client.chat.completions.create`, `st.write_stream`) but 2024 model names; put a current model name in its config.
**Optional (extra):** none for this block.
**Build it (follow the video):**
1. Watch 4.1, then make `hello_chat.py` with one `st.chat_input` that echoes your message back inside `st.chat_message("assistant")`; run `streamlit run hello_chat.py`.
2. Follow 4.2: clone or create the starter structure (a config file, a `helpers/` module for the LLM call, and the page).
3. Put the key in environment variables as the video does, and keep `.env` out of Git.
4. Type the LLM helper: a function that takes the messages and returns a streaming response.
5. Type the page: keep the history in `st.session_state.messages`, redraw every message on each rerun, append the user's message, then stream the reply with `st.write_stream` and append it.
6. Add the sidebar controls the video adds (model, temperature, max tokens) and see the page rerun when you change them.
7. You should see a ChatGPT-like page at `localhost:8501` that remembers the conversation until you refresh the browser.

**Carry it into DocDesk:**
- Add `docdesk/app.py` that imports `core.py`; the page contains no API calls of its own.
- Keep the history in `st.session_state`, and add a "New chat" button that clears it.
- Stream with `ask_stream` and `st.write_stream`; add a sidebar toggle "Structured answers" that switches to `ask` and shows confidence as a small badge and the follow-up question as a button that sends it.
- Show the running session cost from Block 2 in the sidebar.

**Done when:** `streamlit run app.py` opens DocDesk in the browser, an answer streams in, the history survives the next question, and the terminal `chat.py` still works unchanged against the same `core.py`.
**Stretch:** build the same page in Gradio with `gr.ChatInterface` and compare how much code each needs.
**Cost and teardown:** the same per-call cost as Block 3; stop Streamlit with Ctrl+C. Nothing else runs.
**Progression check:** New: Streamlit's rerun model, chat elements and session state. Reused: `core.py` from Blocks 2-3 unchanged. Jump size: small; only the screen is new, and 4.1 is a two-element warm-up before the full app.
**Architect's question:** Streamlit runs your Python on the server and reruns the script on every interaction, with state per browser session. That is perfect for an internal tool; what breaks when a thousand people use it at once, and what would you put between the page and the model?

<details><summary>Recap questions</summary>

1. Q: Why does a Streamlit chat need `st.session_state`? A: Streamlit reruns the whole script on every interaction, so ordinary variables reset; session state keeps the message list between reruns for that browser session.
2. Q: What does `st.write_stream` do? A: It writes a stream of text chunks to the page as they arrive and returns the full text when done, so you can append it to the history.
3. Q: Why keep the LLM call in `core.py` or a helper module and not in the page? A: The same logic then serves the terminal, the web page and (next block) an API, and you can test it without a UI.

</details>

---

## Block 5: Your own API with FastAPI

**What you build:** An HTTP API in FastAPI with typed request and response models, its automatic `/docs` page and a `POST /chat` endpoint that calls the model; then the Streamlit page calls this API instead of the model.
**New layer:** API service, HTTP and JSON, OpenAPI docs. **Reuses:** Pydantic models from Block 3, `core.py`, and the Block 4 page.
**Needs:** Blocks 3 and 4 working. One-time: `pip install "fastapi[standard]"` (Corey Schafer's repos use `uv`, which his Part 1 description links a tutorial for; plain `pip` works too) and `curl`.
**Architecture so far:**
```
 browser
   |
 app.py (Streamlit)        * now a client: httpx.post(...)
   |  * HTTP + JSON
   v
 * api.py (FastAPI, uvicorn :8000)
     * POST /chat   ChatRequest -> ChatResponse
     * GET  /health, /docs
   |  import
 core.py  ask() / ask_stream()          (Blocks 2-3)
   |
 hosted model API
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 5.1 | Python FastAPI Tutorial (Part 1): Getting Started - Web App + REST API | Corey Schafer | https://www.youtube.com/watch?v=7AMjmCTumuo | length ? | Start | DESK | The first episode of a 2026 series: install FastAPI, create an app, add JSON routes, run it from the command line and explore the automatic docs page, then a first API endpoint over dummy data. | verified; description |
| 5.2 | Python FastAPI Tutorial (Part 4): Pydantic Schemas - Request and Response Validation | Corey Schafer | https://www.youtube.com/watch?v=9GHxnttXxrA | length ? | Start | DESK | Request and response models in a schemas file, field validation such as minimum and maximum length, response models on GET routes, and a first POST endpoint: Pydantic as the API's contract. | verified; description |
| 5.3 | FastAPI for AI: Build an AI Endpoint in 30 Minutes | pixegami | https://www.youtube.com/watch?v=uDUfZyNXFX0 | length ? | Deeper | DESK | A FastAPI service in front of an LLM (2025): project setup, the model call, a custom system prompt from a file and running the server, followed by rate limiting and JWT authentication. Uses Google's Gemini; the pattern is the same for OpenAI. | verified; description |

**Code:** 5.1: https://github.com/CoreyMSchafer/FastAPI-01-Getting-Started (last updated 2026-01). 5.2: https://github.com/CoreyMSchafer/FastAPI-04-Pydantic-Schemas (last updated 2026-01); Part 4 continues from Parts 2 and 3 (HTML templates, path parameters), so start from https://github.com/CoreyMSchafer/FastAPI-03-Path-Parameters (last updated 2026-01) and ignore the HTML routes. 5.3: https://github.com/pixegami/fastapi-gemini-ai (last updated 2025-06).
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 5.O1 | Fullstack Python - simple Streamlit app to consume a FastAPI API | Kokchun Coding Tutorials | https://www.youtube.com/watch?v=nGRtRqZSVkY | length ? | Start | DESK | A Streamlit front end that calls a FastAPI back end over HTTP (2026, a books example, no LLM): exactly the client-server split DocDesk makes in this block. | verified; description |
| 5.O2 | OpenAI Next.js FastAPI Streamlit Python Typescript: GPT 4 Chatbot - 3 Frontends & Python Backend | HTMLFiveDev | https://www.youtube.com/watch?v=By7BQgsUsnI | length ? | Deeper | DESK | One FastAPI back end with OpenAI behind three front ends, one of them Streamlit with streamed answers (2024); no repo is linked, and only the Streamlit part matters here. | verified; description |

**Build it (follow the video):**
1. Follow 5.1: create the app with a list of dummy posts and a `GET /api/posts` route that returns them as JSON, run it with `fastapi dev main.py` and open `http://127.0.0.1:8000/docs`.
2. Call the route from a second terminal with `curl http://127.0.0.1:8000/api/posts` and compare with what the browser and `/docs` show.
3. Skip Part 2 (HTML templates). For 5.2, open the Part 3 repo as your starting point, then type along: a `schemas.py` with a create model and a response model, field limits, `response_model=` on the routes, and a POST endpoint.
4. Send a POST with `curl -X POST -H "Content-Type: application/json" -d '{...}'`, then send one with a field that is too long and read the 422 validation error.
5. Follow 5.3 up to the end of "Run the Server" (the chapters after that, rate limiting and JWT, belong to Block 13; watch them now if you like, but do not build them yet).
6. In your copy of 5.3, swap the Gemini class for an OpenAI one with the same `chat(prompt) -> str` method (the repo already has an abstract `AIPlatform` base class for exactly this).
7. You should see `POST /chat` in `/docs`, try it there, and get a JSON response back.

**Carry it into DocDesk:**
- Add `docdesk/api.py` with `POST /chat`: request `ChatRequest(question: str, history: list[Message])`, response `ChatResponse(answer, confidence, follow_up_question, tokens_in, tokens_out, cost_usd)`, reusing `DocDeskAnswer` from Block 3.
- The server stays stateless: the client sends the history with each request (as in Block 2).
- Add `GET /health` returning `{"status": "ok"}`.
- Change `app.py` to call `httpx.post("http://localhost:8000/chat", json=...)` instead of importing `core.py`; the page no longer needs the API key.
- Run both: `fastapi dev api.py` in one terminal and `streamlit run app.py` in another.

**Done when:** `curl -X POST localhost:8000/chat -H "Content-Type: application/json" -d '{"question":"What is an overdraft fee?","history":[]}'` returns JSON with `answer`, `confidence` and `follow_up_question` fields, and the Streamlit page works with the API key removed from its own environment.
**Stretch:** add `POST /chat/stream` that returns a `StreamingResponse` from `ask_stream`, and read it in Streamlit with `httpx.stream` so the page streams again.
**Cost and teardown:** the same model cost as before; stop both servers with Ctrl+C. Nothing runs in the background.
**Progression check:** New: FastAPI, routes, HTTP status codes, the `/docs` page, a client calling a server. Reused: Pydantic models (Block 3), `core.py` (Blocks 2-3), the page (Block 4). Jump size: medium; this is the first split into two programs, so the block goes plain API (5.1), then the contract (5.2), then an LLM behind it (5.3) before DocDesk combines them.
**Architect's question:** the API is now the contract of the system. How do you version it (`/v1/chat`) so that a mobile app, a web page and another team can upgrade at different times, and who is allowed to change `ChatResponse`?

<details><summary>Recap questions</summary>

1. Q: What does FastAPI give you from a Pydantic request model? A: Parsing and validation of the JSON body (a 422 error with details when it does not fit), type hints in your handler, and the schema in the automatic OpenAPI `/docs` page.
2. Q: Why make the Streamlit page call the API instead of the model? A: The model key and logic live in one place, other clients (curl, another app, a test) can use the same contract, and UI and API can be deployed and scaled separately.
3. Q: What does "stateless API" mean for DocDesk here? A: The server keeps no conversation between requests; each request carries the history it needs, so any copy of the API can answer it.

</details>

---

## Block 6: Local models with Ollama and a provider switch

**What you build:** A model running on your own machine with Ollama, called from Python, and a setting that switches DocDesk between the hosted model and the local one without changing the API.
**New layer:** model abstraction (provider switch). **Reuses:** the Block 5 API, `core.py` and the Block 3 schema.
**Needs:** Block 5 working. One-time: install Ollama from ollama.com and pull a small model (the video uses `llama3.2`); a few GB of free disk and 8 GB or more of RAM.
**Architecture so far:**
```
 browser -> app.py (Streamlit) -> api.py (FastAPI)          (Blocks 4-5)
                                     |
                                  core.py
                                     |
                         * get_provider()  <- DOCDESK_PROVIDER
                          /                 \
                hosted model API      * Ollama (localhost:11434)
                                         * local model (llama3.2)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 6.1 | Run AI Models Locally With Ollama and Python | Real Python | https://www.youtube.com/watch?v=pL2GVrcKD30 | length ? | Start | DESK | A 2026 step-by-step: install Ollama and check its version, pull llama3.2, set up a virtual environment, install the ollama Python library, call `chat()`, and steer the answer with a system message. | verified; description |
| 6.2 | Ollama adds OpenAI API support | Learn Data with Mark | https://www.youtube.com/watch?v=Zgb2TjZ5zTk | length ? | Deeper | DESK | Ollama's OpenAI-compatible endpoint: an existing app is changed to talk to a local model through the OpenAI library just by pointing it at Ollama (2024; the app happens to use Chainlit, another chat UI). | verified; description |

**Code:** 6.1: no project repo; the description links the library itself, https://github.com/ollama/ollama-python (last updated 2026-10; its `examples/` folder has chat, streaming, history and structured-output scripts). 6.2: https://github.com/mneedham/LearnDataWithMark, folder `ollama-openai/` (last updated 2025-04).
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 6.O1 | Use Any LLM Provider with LiteLLM \| Use ChatGPT, Claude, Gemini, Ollama with One API | Venelin Valkov | https://www.youtube.com/watch?v=4mye7oi0CXk | length ? | Deeper | DESK | LiteLLM as one OpenAI-style call for many providers, including local Ollama (2025): prompting two hosted models, structured output with Pydantic, and tool calling. | verified; description |
| 6.O2 | Use the OpenAI API to call Mistral, Llama, and other LLMs (works with local AND serverless models) | Deploying AI | https://www.youtube.com/watch?v=37nf3VgjFCk | length ? | Deeper | DESK | One OpenAI-style client for local Ollama models and hosted providers, with demos of streaming and of swapping between five models (2024); its tool-calling and agent parts belong to Blocks 11-12. | verified; description |

**Build it (follow the video):**
1. Follow 6.1: install Ollama, run `ollama --version`, then `ollama pull llama3.2` and try it in the terminal with `ollama run llama3.2`.
2. In a fresh venv, `pip install ollama`, and type the video's script that calls `ollama.chat(model="llama3.2", messages=[...])` and prints the reply.
3. Add a system message as the video does and compare the answer with your hosted model's answer to the same question.
4. Follow 6.2: point the OpenAI client at Ollama with `OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")` (the key is required by the SDK but ignored), and run your Block 2 `chat.py` against the local model by changing only the client and model name.
5. Stream from the local model the same way as in Block 2 and note how fast it is on your machine.
6. Run your Block 1 `smoke_test.py` against both providers.

**Carry it into DocDesk:**
- Add `DOCDESK_PROVIDER=openai|ollama` and `DOCDESK_MODEL` to the Block 3 `Settings` class.
- In `core.py`, add a small `Provider` base class (like pixegami's `AIPlatform` in 5.3) with `OpenAIProvider` and `OllamaProvider`, and a `get_provider()` that reads the setting; `api.py` does not change.
- For structured answers on Ollama, pass `format=DocDeskAnswer.model_json_schema()` to `ollama.chat` and validate with `DocDeskAnswer.model_validate_json(...)` (see `examples/structured-outputs.py` in the ollama-python repo); on a validation error, retry once, then return `confidence="low"`.
- Report the provider and model in `GET /health` and in every `ChatResponse`; set `cost_usd` to 0 for local calls but keep the token counts (Ollama returns `prompt_eval_count` and `eval_count`).

**Done when:** restarting the API with `DOCDESK_PROVIDER=ollama` makes the same `curl -X POST localhost:8000/chat ...` return a valid `ChatResponse` from the local model (shown in `/health`), and switching back to `openai` needs no code change.
**Stretch:** replace the two provider classes with LiteLLM (6.O1) and compare: fewer lines of your own code against one more dependency to trust.
**Cost and teardown:** local calls cost no API fees, only your laptop's power and a few GB of disk per model. Free the disk with `ollama rm llama3.2` when done, and quit Ollama (or stop its service) so it does not hold memory.
**Progression check:** New: Ollama, a local model, the OpenAI-compatible endpoint, a provider setting. Reused: the Block 5 API unchanged, `core.py`, the Block 3 schema and settings. Jump size: small; the same API with a different engine behind it, which is exactly how Bedrock arrives in Block 17.
**Architect's question:** when is a local or self-hosted model the right answer for a bank (data that may not leave, predictable cost at volume, offline use) and what do you give up (quality, the operations work of serving models, GPUs)? Where should the switch live: in each app's code, as here, or in a shared gateway (Track E Block 7)?

<details><summary>Recap questions</summary>

1. Q: What makes switching between OpenAI and Ollama a one-line change? A: Ollama serves an OpenAI-compatible endpoint at `localhost:11434/v1`, so the OpenAI client works with a different `base_url` and model name.
2. Q: Why read the provider from a setting rather than an `if` in each function? A: One place decides, the API and UI do not change, and tests or environments can pick a provider without code changes.
3. Q: Why validate structured output more carefully with a small local model? A: Small models follow schemas less reliably, so the code must validate, retry and degrade gracefully instead of trusting the JSON.

</details>

<!-- Pages to check (Blocks 0-6): none; every new row's watch page was read (the oEmbed endpoint was refused by the fetch allowlist, so title and channel come from the watch-page metadata). Row 0.2 is reused title-based from Track D 3.O4. -->

---

## Block 7: Embeddings and semantic search

**What you build:** A small semantic search: a few pages of your DocDesk PDFs turned into vectors (embeddings), stored in a Chroma collection on disk, and searched by meaning through a new `POST /search` endpoint. Retrieval only; the model does not answer yet.
**New layer:** embeddings and a vector store. **Reuses:** the Block 5-6 API, the Block 3 settings class and Ollama from Block 6 (for local embeddings).
**Needs:** Block 6 working. One-time: `pip install chromadb pypdf`, and `ollama pull nomic-embed-text` (a small local embedding model); or use OpenAI's `text-embedding-3-small` with your existing key. The vectors and cosine similarity from Track A help but are not required: 7.2 teaches them.
**Architecture so far:**
```
 browser -> app.py (Streamlit) -> api.py (FastAPI)          (Blocks 4-6)
                                     |
                POST /chat -> core.py -> provider (OpenAI | Ollama)
              * POST /search
                     |
              * embed(text) -> [0.12, -0.03, ...]   (nomic-embed-text or text-embedding-3-small)
                     |
              * Chroma collection "docdesk"  (./chroma on disk)
                  ids, passages, metadata {source, page}

 * ingest.py: a few PDF pages -> paragraphs -> embeddings -> Chroma
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 7.1 | Vector databases are so hot right now. WTF are they? | Fireship | https://www.youtube.com/watch?v=klTvEwg3oJ4 | length ? | Start | BIKE | A fast concept pass (2023): what an embedding is, why a vector database differs from SQL lookups, and how it gives a model a kind of long-term memory; the product names have moved on, the idea has not. | verified; description |
| 7.2 | Vector Databases Full Course for Beginners – Embeddings, Similarity Search & ChromaDB | freeCodeCamp.org | https://www.youtube.com/watch?v=lR931Iz8Z6U | length ? | Start | DESK | Per its chapters, a 2026 course: vectors, cosine similarity and Euclidean distance, tokens, embedding models, a demo that creates embeddings (with Google's Gemini model), how a vector database indexes them (IVF, HNSW), and a closing project that stores and searches embeddings in ChromaDB. | verified; description |
| 7.3 | ChromaDB Crash Course - Intro to Vector Databases | Alejandro AO | https://www.youtube.com/watch?v=god8Pox1laE | length ? | Start | DESK | A 2025 hands-on Chroma session: a local client, adding, getting, updating and upserting items, managing collections, saving to disk with `PersistentClient`, and embedding locally with Sentence Transformers or with OpenAI. A mid-sized AI-engineering channel; the code is a Colab notebook. | verified; description |

**Code:** 7.1: none (concept). 7.2: the description links course resources on Gumroad (cut off on the watch page); no GitHub repo, so type along. 7.3: the description links a Colab notebook (cut off on the watch page, so open it from the description); no GitHub repo.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 7.O1 | The Illustrated Word2vec - A Gentle Intro to Word Embeddings in Machine Learning | Jay Alammar | https://www.youtube.com/watch?v=ISPId9Lhc1g | 8:44 | Start | BIKE | Embeddings from first principles; watch before 4.1 [Track B; row 7.2 here] if "embedding" feels vague. | verified; also in Track B 4.O1; watch once |
| 7.O2 | OpenAI's NEW Embedding Models | James Briggs | https://www.youtube.com/watch?v=cUyw5eG-VtM | length ? | Deeper | DESK | OpenAI's `text-embedding-3-small` and `-large` against the older Ada model (2024): quality, cost, and the `dimensions` parameter that shortens vectors to save storage, with code. Watch if you embed with OpenAI rather than Ollama. | verified; description |

**Build it (follow the video):**
1. Watch 7.1 away from the keyboard. Write one line: "an embedding is a list of numbers where similar meanings sit close together".
2. Follow 7.2 from "What are vectors" (0:22:40) to the end of "Embeddings and embedding models" (1:11:48); compute a cosine similarity by hand in Python with NumPy for two short vectors, as the video does.
3. In the embeddings demo, use the model you already have instead of Gemini if you prefer: `ollama.embed(model="nomic-embed-text", input=["..."])` or `client.embeddings.create(model="text-embedding-3-small", input=["..."])`. Embed "overdraft fee", "charge for spending more than your balance" and "deposit insurance", and print the three pairwise cosine similarities: the first pair should score highest.
4. Skim the index chapter (IVF and HNSW, 1:22:07) for the idea only, then follow the closing ChromaDB project in 7.2.
5. Follow 7.3: create a client, a collection, add a handful of sentences with ids and metadata, and `query(query_texts=[...], n_results=3)`; read the distances that come back.
6. Switch to `chromadb.PersistentClient(path="./chroma")`, restart Python, and check the data is still there.
7. Try the same query with two different embedding models in two collections and see that the rankings differ: the model is part of the index.

**Carry it into DocDesk:**
- Add `EMBED_PROVIDER` and `EMBED_MODEL` to the Block 3 `Settings` class, and an `embed(texts) -> list[list[float]]` function next to `get_provider()` (Ollama or OpenAI, like the chat switch in Block 6).
- Add `docdesk/ingest.py`: read three to five pages from your PDFs with `pypdf` (`PdfReader(path).pages[i].extract_text()`), split each page on blank lines into paragraphs, and add them to a Chroma collection with ids like `fdic-guide.pdf:3:2` and metadata `{source, page}`. Proper chunking waits for Block 8.
- Create the collection with cosine distance (check the Chroma docs for the current option name) and pass your own embeddings, so Chroma's built-in default model is not used by accident.
- Add `POST /search` to `api.py`: `SearchRequest(query: str, k: int = 3)` returns `list[Passage(id, source, page, text, score)]`. `POST /chat` does not change.
- Record the embedding model name in the collection's metadata, and refuse to query if it does not match the setting.

**Done when:** `curl -X POST localhost:8000/search -H "Content-Type: application/json" -d '{"query":"how much can a bank charge if I overdraw?","k":3}'` returns three passages from your PDFs about overdrafts, with page numbers, even though none of them contains the word "overdraw".
**Stretch:** add a keyword search over the same paragraphs (count shared words, or `rank-bm25`) and print both rankings side by side for ten questions; note where each one wins (exact names and numbers versus paraphrases).
**Cost and teardown:** local embeddings with Ollama cost nothing; OpenAI's small embedding model costs a fraction of a cent for a few pages (check the pricing page). Delete the `./chroma` folder to start over; `ollama rm nomic-embed-text` frees the disk.
**Progression check:** New: embeddings, cosine similarity, a vector store, one search endpoint. Reused: the API, settings and provider switch from Blocks 3-6. Jump size: small to medium; the concept comes first (7.1), the maths and a first Chroma project second (7.2), Chroma in depth third (7.3), and no generation is added, so RAG in Block 8 joins two things you already have.
**Architect's question:** the vector store is a derived copy of your documents. When you change the embedding model, every vector must be rebuilt; when a document changes or is withdrawn, its vectors must follow. Who owns that pipeline, how is the index versioned, and can an embedding service outside the bank see the text?

<details><summary>Recap questions</summary>

1. Q: What is an embedding, in one sentence? A: A fixed-length list of numbers produced by a model so that texts with similar meaning get vectors that are close together.
2. Q: Why can you not mix vectors from two embedding models in one collection? A: Each model has its own vector space (and often its own dimension), so distances between vectors from different models are meaningless; changing the model means re-embedding everything.
3. Q: What does a vector store add over a Python list and a loop of cosine similarities? A: Storage on disk with ids and metadata, filtering, and an approximate nearest-neighbour index (for example HNSW) so search stays fast when there are millions of vectors.

</details>

---

## Block 8: RAG over your PDFs with citations, behind your API

**What you build:** Retrieval-augmented generation (RAG): every PDF in `docdesk/docs/` loaded, cut into overlapping chunks and embedded; a question retrieves the top chunks, the prompt carries them, and the model answers with numbered citations that point to file and page. It runs behind a new `POST /ask` endpoint.
**New layer:** chunking, the retrieval pipeline and citations. **Reuses:** Block 7 embeddings, Chroma and `/search`; the Block 6 provider switch for generation; the Block 3 schema and prompt files.
**Needs:** Blocks 6 and 7 working. One-time: for 8.3, `pip install langchain-community langchain-text-splitters langchain-chroma langchain-ollama pypdf pytest` and `ollama pull mistral` (or use `llama3.2`, which you already have).
**Architecture so far:**
```
 browser -> app.py (Streamlit: answer + * sources panel)
              |
           api.py
             POST /chat   (Blocks 5-6)
             POST /search (Block 7)
           * POST /ask
                |
           * retrieve top-k chunks          (Chroma, Block 7)
           * prompt = rules + numbered chunks + question
           * generate                       (provider switch, Block 6)
           * AskResponse: answer + citations [source, page, chunk]

 * ingest.py: all PDFs -> pages -> chunks (size, overlap) -> embeddings -> Chroma
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 8.1 | RAG From Scratch: Part 1 (Overview) | LangChain | https://www.youtube.com/watch?v=wd7TZ4w1mSw | 5:13 | Start | BIKE | The idea of RAG (give the model private or fresh data at question time) and the plan for indexing, retrieval and generation. Only part 1 of the series is verified here; code in the series uses 2024 LangChain APIs (may be dated). | verified; also in Track C 3.1; watch once |
| 8.2 | RAG from Scratch without any Frameworks | Prompt Engineering | https://www.youtube.com/watch?v=bmduzd1oY7U | length ? | Start | DESK | The whole pipeline in plain Python with no framework and no vector store (2024): prepare and chunk the data, embed the chunks, retrieve the closest ones, and generate the answer from them. A mid-sized channel; the code is a Colab notebook. | verified; description |
| 8.3 | Python RAG Tutorial (with Local LLMs): AI For Your PDFs | pixegami | https://www.youtube.com/watch?v=2TJxpyO3ei4 | length ? | Deeper | DESK | The framework version (2024): load a folder of PDFs, split them into chunks, embed and store them in Chroma with stable ids so the database can be updated, answer locally through Ollama with the source ids listed, and unit-test the answers. | verified; description |

**Code:** 8.1: none (concept; the series notebooks are linked from LangChain's channel). 8.2: a Colab notebook linked from the description; no GitHub repo. 8.3: https://github.com/pixegami/rag-tutorial-v2 (last updated 2024-05; matches the description's cut-off link). Two warnings: its `get_embedding_function.py` uses Amazon Bedrock by default, so switch to the commented `OllamaEmbeddings(model="nomic-embed-text")` line; and it imports from `langchain.vectorstores`, `langchain.document_loaders`, `langchain.prompts` and `langchain.schema`, paths that LangChain 1.0 (late 2025) no longer has. Use `langchain_chroma.Chroma`, `langchain_community.document_loaders.PyPDFDirectoryLoader`, `langchain_core.prompts.ChatPromptTemplate`, `langchain_core.documents.Document` and `langchain_ollama` instead, or pin `langchain<1.0` while you follow the video.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 8.O1 | Learn RAG From Scratch – Python AI Tutorial from a LangChain Engineer | freeCodeCamp.org | https://www.youtube.com/watch?v=sVcwVQRHIc8 | 2:33:11 | Start | DESK | Follow-along coding of the full RAG pipeline; do it after 3.1-3.3 [Track C; rows 8.1 to 8.3 here] so the code has a mental model to land on. 2024-era LangChain (may be dated). | verified; also in Track C 3.D1; watch once |
| 8.O2 | Semantic Chunking - 3 Methods for Better RAG | James Briggs | https://www.youtube.com/watch?v=7JS0pqXvha8 | 10:13 | Deeper | DESK | Per the description and chapters (2024): a simple RAG example, then three semantic chunkers (statistical, consecutive and cumulative) and chunking for video and multimodal use; Python code on screen, so a desk video, and the only dedicated chunking row in this track. | verified; content per watch-page description and chapters; also in Track G 6.O1; watch once |
| 8.O3 | Deploy RAG to Production Faster Than You Think | pixegami | https://www.youtube.com/watch?v=ldFONBo2CR0 | length ? | Deeper | DESK | The sequel to 8.3 (2024): wrapping the RAG code in FastAPI, then a Docker image, AWS infrastructure with the CDK, Lambda and an asynchronous API. Here, only up to the end of "Adding FastAPI" (18:44). | verified; description |

**Build it (follow the video):**
1. Watch 8.1 and sketch the three stages (indexing, retrieval, generation) on your Block 0 sheet.
2. Follow 8.2 in the Colab notebook, then copy it into a local script in your venv: chunk a text, embed the chunks, take the top three by cosine similarity, and paste them into the prompt. Swap its embedding and chat calls for your own `embed()` and provider from Blocks 6-7 if they differ.
3. Change the chunk size (for example 200, 800 and 2,000 characters) and the overlap (0 and 80), ask the same question, and note how the retrieved text and the answer change.
4. Follow 8.3: clone the repo, fix the embedding function and the imports as described under **Code**, put two PDFs in `data/`, and run `python populate_database.py`.
5. Read how 8.3 builds chunk ids (`source:page:chunk`) and why that lets `populate_database.py` add only new chunks on the next run; add a third PDF and rerun to see it.
6. Run `python query_data.py "your question"` and check that the printed sources point to the pages that really hold the answer.
7. Follow the unit-test chapter (15:12): write two `pytest` tests, one that must find a known fact and one that must not invent an answer.

**Carry it into DocDesk:**
- Turn `ingest.py` into the real pipeline: all PDFs, page metadata, `RecursiveCharacterTextSplitter` (or your 8.2 splitter) with `CHUNK_SIZE` and `CHUNK_OVERLAP` in `Settings`, ids `source:page:chunk`, and only new ids added on each run.
- Add `prompts/rag.md`: "Answer only from the numbered context. Cite every claim as [n]. If the context does not contain the answer, say you could not find it in the documents."
- Add `POST /ask`: `AskRequest(question, k=4)` returns `AskResponse(answer, confidence, citations: list[Citation(n, source, page, chunk_id, text, score)], tokens_in, tokens_out, cost_usd)`. Generation goes through the Block 6 provider switch, so it works with OpenAI and Ollama.
- Return only the citations the answer actually uses (parse the `[n]` markers); keep `/chat` and `/search` as they are.
- In `app.py`, add a "Ask the documents" mode that calls `/ask` and shows each citation in an `st.expander` with file, page and the chunk text.

**Done when:** a question whose answer is in one of your PDFs returns an answer with at least one citation pointing to the right file and page, and a question the PDFs do not cover ("What is the bank's stock price today?") returns "could not find it in the documents" instead of a guess.
**Stretch:** write ten question-and-expected-page pairs and measure how often the right page is in the top four for chunk sizes 400, 800 and 1,200 (this small evaluation set returns in Block 19).
**Cost and teardown:** with Ollama, nothing; with OpenAI, each `/ask` sends about k chunks as input tokens, so it costs several times a plain chat call (your cost line shows how much). Delete `./chroma` and re-ingest whenever you change the chunk settings or the embedding model.
**Progression check:** New: PDF loading, chunk size and overlap, prompt assembly with context, citations, and LangChain as a helper. Reused: embeddings and Chroma (Block 7), the provider switch (Block 6), the API (Block 5). Jump size: medium; it joins search (Block 7) and generation (Blocks 1-6), and the block goes concept (8.1), plain pipeline (8.2), then the framework version (8.3), so LangChain arrives only after you have written every step without it.
**Architect's question:** a RAG answer is only as good as what retrieval returned. Who decides chunk size, k and which documents are in the index; how will you know that an answer was grounded and not invented (Block 19); and what stops a user from retrieving a passage they are not allowed to see (Blocks 13 and 20)?

<details><summary>Recap questions</summary>

1. Q: What are the steps of a RAG request? A: Embed the question, retrieve the top-k most similar chunks from the index, put them into the prompt with instructions, generate the answer, and return it with the sources it used.
2. Q: What does chunk overlap protect against, and what does it cost? A: It keeps a sentence or fact that sits on a chunk boundary whole in at least one chunk; it costs extra storage and duplicate text in the prompt.
3. Q: Why give every chunk a stable id such as `source:page:chunk`? A: The ingestion can add only new chunks and update or delete changed ones, and a citation can point the user to the exact file and page.

</details>

---

## Block 9: Containers with Docker and Docker Compose

**What you build:** DocDesk in containers: one image for the API, one for the Streamlit page, and a `docker-compose.yml` that starts them together with Ollama and the Chroma data, so `docker compose up` runs the whole app on any machine with Docker.
**New layer:** containers and a multi-service runtime. **Reuses:** the Block 8 app unchanged (code, settings, `.env`).
**Needs:** Block 8 working. One-time: Docker Desktop (Mac or Windows) or Docker Engine with the Compose plugin (Linux); a Docker Hub account is not needed.
**Architecture so far:**
```
 * docker compose up
   +-------------------- * compose network "docdesk" --------------------+
   |  * ui  (Streamlit :8501) --HTTP http://api:8000--> * api (FastAPI :8000)  |
   |                                                    |          \          |
   |                                    * volume ./chroma   * ollama (:11434)  |
   |                                                         * volume: models  |
   +----------------------------------------------------------------------+
 .env -> env_file: (keys are passed in at run time, never baked into an image)
 browser -> localhost:8501
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 9.1 | Docker Crash Course for Absolute Beginners [NEW] | TechWorld with Nana | https://www.youtube.com/watch?v=pg19Z8LL06w | 1:07:39 | Start | DESK | A 2023 course, sponsored by a vendor, that mixes animations with demos: Docker versus a VM, images versus containers, registries, the main commands, port binding, a Dockerfile, and building an image. The Dockerfile example is a Node.js app (per the chapter title), so redo it for a Spring Boot jar in the lab [Track E lab; Build it step 3 here]. Watch from 02:54 to 1:03:39. | verified; content per watch-page description and chapters; also in Track E 3.1; watch once |
| 9.2 | Docker Tutorial For Beginners - How To Containerize Python Applications | Patrick Loeber | https://www.youtube.com/watch?v=bi0cKgmRuiA | length ? | Start | DESK | The Python version of 9.1's Dockerfile: first a plain Python script, then a FastAPI web app in a container, and how the virtual environment fits in. From 2020, so base-image tags are old (may be dated); the steps are unchanged. | verified; description |
| 9.3 | How To Use Docker To Make Local Development A Breeze | ArjanCodes | https://www.youtube.com/watch?v=zkMRWDQV4Tg | length ? | Start | DESK | A small Python API server built and run in a container, why that beats running it straight on your laptop, then a docker-compose file for it and how to handle data that changes (2022). | verified; description |

**Code:** 9.1: no repo needed (the demo app is Node.js; you redo it for DocDesk). 9.2: no repo; type along. 9.3: https://github.com/ArjanCodes/2022-docker (last updated 2022-07; it has a `Dockerfile`, a `docker-compose.yaml` and the Python server; matched by name with the description's cut-off link "2022-do...").
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 9.O1 | Docker Compose Tutorial - Docker in Practice \|\| Docker Tutorial 9 | TechWorld with Nana | https://www.youtube.com/watch?v=MVIcrmeV_6c | length ? | Start | DESK | A short 2019 explainer: how each `docker run` option maps to a field in a Compose file, a demo with two containers, and how Compose puts them on one network so they find each other by name. Old but the mapping has not changed (the `version:` line it may show is now unnecessary). | verified; description |

**Build it (follow the video):**
1. Follow 9.1 from 02:54 to 1:03:39: run a public image, list and stop containers, bind a port, and read the logs. Its last part builds a Node.js image (the row's note about a Spring Boot jar belongs to Track E); you do the Python version in step 3.
2. Note the four words you will use daily: image (the packaged app), container (a running image), port mapping (`-p host:container`), environment variable (`-e` or `--env-file`).
3. Follow 9.2's web-app example (09:14): a `Dockerfile` with a slim Python base image, `COPY requirements.txt`, `RUN pip install`, `COPY . .`, and a `CMD` that starts the server on `0.0.0.0`; build it with `docker build -t hello-api .` and run it with `docker run -p 8000:8000 hello-api`. Use a current base tag such as `python:3.12-slim`.
4. Break it on purpose: start the server on `127.0.0.1` inside the container and see that the browser cannot reach it.
5. Follow 9.3: clone the repo, build and run it with `docker run`, then with its `docker-compose.yaml` (`docker compose up --build`), and change a data file to see what the video says about mounted volumes.
6. Run `docker compose down` and `docker compose down -v` and note which one deletes the volume's data.

**Carry it into DocDesk:**
- Add `.dockerignore` (`.venv/`, `.env`, `chroma/`, `__pycache__/`, `.git/`).
- Add `Dockerfile.api` (runs `fastapi run api.py --port 8000`) and `Dockerfile.ui` (runs `streamlit run app.py --server.address=0.0.0.0 --server.port=8501`); `docker init` can generate a starting Python Dockerfile if you prefer.
- Read the API address in `app.py` from `DOCDESK_API_URL` (default `http://localhost:8000`); in Compose set it to `http://api:8000`, the service name.
- Add `docker-compose.yml` with `api`, `ui` and `ollama` (image `ollama/ollama`, a named volume for `/root/.ollama`); point the API at `http://ollama:11434`, mount `./chroma` into the API container, and pass keys with `env_file: .env`.
- Add a `healthcheck` on `GET /health` for `api` and `depends_on` with `condition: service_healthy` for `ui`.
- On a Mac, Ollama in a container cannot use the GPU and is slow; in that case leave Ollama on the host, drop the `ollama` service, and use `http://host.docker.internal:11434`.

**Done when:** on a fresh clone, after creating `.env`, the single command `docker compose up --build` starts DocDesk, `localhost:8501` answers a question with citations, and `docker compose ps` shows `api` as healthy. Nothing is installed on the laptop except Docker.
**Stretch:** make the API image smaller with a multi-stage build, run it as a non-root user, and compare `docker images` sizes before and after.
**Cost and teardown:** no cloud cost. Images and model volumes use several GB: `docker compose down` stops everything, `docker compose down -v` also deletes volumes (your Chroma data and Ollama models), and `docker system prune` removes unused images.
**Progression check:** New: Dockerfiles, images, containers, ports, environment variables, Compose services, networks and volumes. Reused: the Block 8 code, unchanged except for reading the API address from a setting. Jump size: medium; the concepts come first in a general course (9.1), then the same steps for a Python web app (9.2), then Compose for a Python app (9.3), before DocDesk combines three services.
**Architect's question:** the image is now the unit you ship. What belongs inside it (code and dependencies) and what must stay outside (secrets, data, model weights, configuration per environment)? How will the same image move unchanged from your laptop to the cloud in Block 15?

<details><summary>Recap questions</summary>

1. Q: What is the difference between an image and a container? A: An image is the read-only package (code, runtime, dependencies, start command); a container is a running instance of it with its own process, file system layer and network.
2. Q: Why must the server listen on `0.0.0.0` inside a container? A: `127.0.0.1` inside the container is the container's own loopback, so traffic forwarded from the host port would never reach a server bound only there.
3. Q: How does the `ui` container find the `api` container in Compose? A: Compose puts the services on one network with built-in DNS, so `http://api:8000` resolves to the API service by its name.

</details>

---

## Block 10: Postgres for users, chat history and vectors (pgvector)

**What you build:** A Postgres database in the Compose stack: SQLAlchemy models for users, conversations and messages, created and changed with Alembic migrations, so DocDesk keeps chat history on the server; then the pgvector extension, so the chunk embeddings live in the same database and Chroma is retired.
**New layer:** a SQL database, persistence and migrations; then vectors in SQL. **Reuses:** the Block 9 Compose stack, the Block 5 API and schemas, the Block 8 ingestion and retrieval.
**Needs:** Block 9 working. SQL you already know from work (tables, keys, joins). One-time: `pip install sqlalchemy "psycopg[binary]" alembic pgvector` (10.2 uses the async driver `asyncpg`), and a database viewer if you like one (pgAdmin, DBeaver or `psql`).
**Architecture so far:**
```
 ui -> api                                    (Compose, Block 9)
        |  * SQLAlchemy session (DATABASE_URL)
        v
 * postgres  (image pgvector/pgvector, named volume pgdata)
     * users, conversations, messages          (* Alembic migrations)
     * chunks(id, source, page, text, embedding vector(768))   <- replaces Chroma
        ^
 ingest.py -> embeddings                       (Block 8)
 ollama / hosted model                         (Block 6)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 10.1 | Python FastAPI Tutorial (Part 5): Adding a Database - SQLAlchemy Models and Relationships | Corey Schafer | https://www.youtube.com/watch?v=NvOV3ig2tGY | length ? | Start | DESK | The next episode of the Block 5 series (2026): SQLAlchemy models and a relationship between two tables, a database session in FastAPI, and routes that read and write real rows instead of dummy data (on SQLite). | verified; description |
| 10.2 | Setting Up a Dev Environment for FastAPI, PostgreSQL, SQLAlchemy & Alembic with Docker | Ssali Jonathan | https://www.youtube.com/watch?v=JWQEostzy60 | length ? | Deeper | DESK | Per its chapters, a 2025 build: a FastAPI app in Docker, Postgres as a second Compose service with a volume, settings from environment variables, an async SQLAlchemy connection and a first table, Compose Watch for hot reload, then Alembic set up from scratch with a first migration. A smaller channel, chosen because it matches this block step for step. | verified; description |
| 10.3 | PGVector: Turn PostgreSQL into Vector Database (Python Tutorial) | Sunny Solanki - CoderzColumn | https://www.youtube.com/watch?v=erNoI9COOn0 | length ? | Deeper | DESK | Per its chapters (2025): install and enable the pgvector extension, store OpenAI embeddings in a table, query by cosine distance from Python, compare distance metrics, and speed searches up with IVFFlat and HNSW indexes. | verified; description |

**Code:** 10.1: https://github.com/CoreyMSchafer/FastAPI-05-Database (last updated 2026-01; matched by name with the description's cut-off link; like Part 4 it carries the HTML templates from Parts 2-3, which you can ignore). 10.2: the description links a repository under `github.com/jod35/` that is cut off on the watch page; open it from the description, or type along. 10.3: the description links a repository under `github.com/sunny2309/` that is cut off on the watch page; type along.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 10.O1 | Python FastAPI Tutorial (Part 15): PostgreSQL and Alembic - Database Migrations for Production | Corey Schafer | https://www.youtube.com/watch?v=e8NnDz8uT7o | length ? | Deeper | DESK | Moving the same series' app from SQLite to a locally installed Postgres and replacing `create_all` with Alembic migrations (2026). It builds on Parts 6 to 14 (auth, uploads, pagination), so watch it for the migration steps, not as a type-along. | verified; description |
| 10.O2 | pgvector: Stylish Hierarchical Navigable Small World Indexes (Jonathan Katz) | CMU Database Group | https://www.youtube.com/watch?v=YU66YlZW6dA | 1:10:37 | Scholar | BIKE | A university database seminar on how HNSW indexes work and how pgvector implements them: design decisions, performance work, trade-offs. Dense and database-oriented, so best after Block 3 [Track C; Blocks 7 and 8 here]. Fits a bank that already runs Postgres. 2023, so pgvector features have moved on; the index ideas have not. | verified; content per CMU page description; also in Track C G7; watch once |

**Build it (follow the video):**
1. Follow 10.1 from its repo (or your Block 5 copy): define two models with a relationship, create the tables, add a session dependency, and turn the dummy-data routes into real database reads and writes on SQLite.
2. Create, read and delete a few rows through `/docs`, then open the SQLite file in a viewer and find them.
3. Follow 10.2 in a new folder: Dockerfile, a `db` service on Postgres with a named volume, `DATABASE_URL` from the environment, the connection and a first table; run `docker compose up` and connect with your viewer or `docker compose exec db psql -U ...`.
4. Use the `pgvector/pgvector` image (for example tag `pg17`) instead of plain `postgres` for the `db` service now; it is Postgres with the extension included, so step 7 needs no new service.
5. Continue 10.2 into Alembic: `alembic init`, point `env.py` at your models and URL, `alembic revision --autogenerate -m "init"`, read the generated file, then `alembic upgrade head`. Add a column, generate a second revision and upgrade again.
6. Stop and restart the stack with `docker compose down` and `up`: the rows survive because they are in the volume. Then try `down -v` and see them go.
7. Follow 10.3: `CREATE EXTENSION IF NOT EXISTS vector;`, a table with a `vector(n)` column, insert a few embeddings from Python, and query with `ORDER BY embedding <=> :query LIMIT 3` (cosine distance). Add an HNSW index and run `EXPLAIN` to see it used.

**Carry it into DocDesk:**
- Add the `db` service (pgvector image, volume `pgdata`) to the Block 9 Compose file and `DATABASE_URL` to `Settings`; the API waits for it with a healthcheck.
- Add `docdesk/models.py` with SQLAlchemy models `User(id, name)`, `Conversation(id, user_id, created_at)` and `Message(id, conversation_id, role, content, tokens_in, tokens_out, cost_usd, created_at)`, and an Alembic migration that creates them. No login yet (Block 13); a `user` name in the request is enough.
- Change `POST /chat` to take `conversation_id` (or create one), load the history from the database and save both turns; add `GET /conversations/{id}`. The server is no longer stateless, as Block 2's architect's question predicted.
- Second migration: enable `vector` and add `Chunk(id, source, page, text, embedding vector(d))` where `d` matches your embedding model (768 for `nomic-embed-text`, 1536 for `text-embedding-3-small`), with an HNSW index using cosine distance.
- Point `ingest.py` and retrieval at the `chunks` table (`pgvector.sqlalchemy.Vector` and `.cosine_distance()`), keep `/search` and `/ask` responses identical, then remove Chroma and its volume.

**Done when:** after `docker compose down` and `docker compose up`, a conversation started before the restart can be continued (`GET /conversations/{id}` shows all turns with tokens and cost), `alembic current` shows the latest revision, and `/ask` returns the same citations from Postgres that it returned from Chroma.
**Stretch:** add a keyword column (`tsvector`) to `chunks` and combine full-text rank with vector distance in one SQL query (hybrid search), then compare against vector-only on your ten Block 8 questions.
**Cost and teardown:** no cloud cost. `docker compose down` keeps the data; `down -v` deletes `pgdata` (history and vectors), so back up with `pg_dump` first if you want to keep it.
**Progression check:** New: SQLAlchemy models and sessions, Postgres in Compose, Alembic migrations, server-side history; then the pgvector column, distance operator and index. Reused: Compose (Block 9), the API and schemas (Block 5), ingestion and retrieval (Block 8). Jump size: medium; ordinary database work comes first (10.1 on SQLite, then 10.2 in Compose with migrations) and vectors second (10.3), and the retrieval API does not change when Chroma is swapped out.
**Architect's question:** one database for relational data and vectors (pgvector) or a dedicated vector database? Postgres gives you transactions, backups, access control and a team that already runs it in a bank; a dedicated store may scale search further. At what number of vectors or queries per second would you revisit the choice, and what would you measure first?

<details><summary>Recap questions</summary>

1. Q: Why use Alembic migrations instead of `create_all()`? A: `create_all()` only creates missing tables; migrations record every schema change as a versioned script that can be reviewed, applied in order to every environment and rolled back.
2. Q: What does `ORDER BY embedding <=> :q LIMIT 5` do in pgvector? A: It sorts rows by cosine distance between each stored embedding and the query vector and returns the five nearest, using an HNSW or IVFFlat index if one exists.
3. Q: What changed in DocDesk's API contract when history moved into Postgres? A: The client now sends a conversation id instead of the whole history; the server loads and saves the turns, so it is stateful and must be backed up, secured and scaled with its database.

</details>

---

## Block 11: Tool calling

**What you build:** Tool calling by hand: you describe your own Python functions to the model as JSON schemas, the model asks for a call, your code checks the arguments and runs the function, and the result goes back to the model for the final answer. DocDesk gets a `lookup_fee(product)` tool over a small fees table in Postgres.
**New layer:** the tool layer (one loop written by you, no agent framework). **Reuses:** the Block 5 API, the Block 6 provider switch, the Block 10 database and the Block 3 Pydantic models.
**Needs:** Blocks 5 and 10 working. A model that supports tools: OpenAI's small models do; on Ollama, `llama3.2` and `qwen` models accept a `tools` list.
**Architecture so far:**
```
 ui -> api.py  POST /chat
         |
       core.py
         * tool loop (at most 5 steps):
             model --> "call lookup_fee(product='checking')"
             * validate arguments (Pydantic) -> run the function
             * tool result --> model --> final answer
         * tools.py: lookup_fee (SQL on fees), calculator
         |
 postgres: * fees(product, fee_name, amount, source, page)  + Block 10 tables
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 11.1 | What is Tool Calling? Connecting LLMs to Your Data | IBM Technology | https://www.youtube.com/watch?v=h8gMhXYAv1k | length ? | Start | BIKE | A short 2025 whiteboard explainer of tool calling: the model does not run anything itself, it asks your application to call a tool and uses the result, which is how it reaches live data. | verified; description |
| 11.2 | Building AI Agents in Pure Python - Beginner Course | Tech With Tim | https://www.youtube.com/watch?v=c9AnqCeyxbI | length ? | Start | DESK | Per its chapters, a 2026 build with no framework: calling the API, keeping conversation history, then tool calling and a full loop that lets the model call tools until it can answer. Its first two steps repeat Blocks 1-2. Sponsor segments; the code sits on Skool behind a sign-up. | verified; description |

**Code:** 11.1: none (concept). 11.2: the description links the code inside a Skool community (sign-up required); type along from the video, it is short.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 11.O1 | Claude Function Calling Made Dead Simple (Anthropic Tool Use) | Nodematic Tutorials | https://www.youtube.com/watch?v=2HsmNeT8TCg | length ? | Start | DESK | The Anthropic version of this block (2025): an API key, a basic call, then a tool definition the model calls and the result sent back, plus a few optimizations. A small channel; the description links its demo code on GitHub (cut off on the watch page). | verified; description |
| 11.O2 | Build Hour: Agentic Tool Calling | OpenAI | https://www.youtube.com/watch?v=7E-qdsVEoB8 | length ? | Deeper | DESK | OpenAI's own session (2025): the Responses API, hosted tools and the Agents SDK, reasoning with tool calls over long tasks, and a live demo that works through a backlog of tickets; the Agents SDK part previews Block 12. Code: https://github.com/openai/build-hours, folder `12-agentic-tool-calling/` (last updated 2026-11). | verified; description |
| 11.O3 | Function Calling is All You Need — Full Workshop, with Ilan Bigio of OpenAI | AI Engineer | https://www.youtube.com/watch?v=KUEmEb71vzQ | 1:42:54 | Deeper | DESK | Hands-on function calling: the history, building an agent loop, memory, delegation and agent-written tools. Do this at a desk after Block 4's concept videos [Track C; row 11.1 here]. | verified; also in Track C 2.D1; watch once |

**Build it (follow the video):**
1. Watch 11.1 and draw the round trip on your sheet: user -> model -> "please call X with these arguments" -> your code -> result -> model -> answer.
2. In 11.2, skim Steps 1 and 2 (you built them in Blocks 1-2) and type along from "Step 3: Tool Calling" (17:08).
3. Define one tool as the video does (name, description, JSON-schema parameters), send it with the request, and print the raw response so you see the tool call (name and arguments as a JSON string) instead of text.
4. Run the function yourself, append the model's tool-call message and then a tool message with the result and the matching call id, and call the model again; you should get a normal answer that uses the result.
5. Follow "Full Agent Build" (28:09): wrap this in a loop that stops when the model answers without asking for a tool. Add a step limit (for example 5) so a confused model cannot loop forever.
6. Add a second tool (a calculator that evaluates `a op b` with an allow-list of operators, never Python's `eval`) and ask a question that needs both.
7. Send arguments that do not fit the schema on purpose (edit them before running) and make your code return an error message to the model instead of crashing.

**Carry it into DocDesk:**
- Add a migration with a `fees` table (`product`, `fee_name`, `amount`, `source`, `page`) and seed ten rows by hand from your public PDFs; the `source` and `page` let the tool cite like `/ask` does.
- Add `docdesk/tools.py`: `lookup_fee(product: str) -> list[Fee]` runs a fixed, parameterised SQL query (no SQL written by the model), plus the calculator; each tool has a Pydantic input model that produces its JSON schema and validates the arguments.
- In `core.py`, add the loop from 11.2 to `POST /chat` behind a setting `TOOLS_ENABLED`: at most 5 steps, every tool call logged with its name, arguments, duration and result size, and saved in the `messages` table (role `tool`).
- Make it work on both providers (OpenAI and Ollama both accept a `tools` list); if a provider or model does not support tools, fall back to plain chat.
- Show tool calls in the Streamlit page as a small "used lookup_fee(checking)" note under the answer.

**Done when:** "What is the monthly fee on the basic checking account, and how much is that per year?" makes DocDesk call `lookup_fee` and the calculator (both visible in the log and in the page) and answer with the right numbers, and a question that needs no tool makes no tool call.
**Stretch:** add a `run_readonly_sql(query)` tool that runs under a Postgres role with `SELECT` rights on `fees` only, try to make the model drop a table, and write down why the fixed-query tool is the safer default.
**Cost and teardown:** each tool round trip is one more model call, so a tool question costs two to three times a plain answer (your cost line shows it); local models cost nothing. Nothing new to stop.
**Progression check:** New: tool schemas, the tool-call message format, a loop with a step limit. Reused: the API (Block 5), the provider switch (Block 6), the database (Block 10), Pydantic (Block 3). Jump size: small to medium; the concept comes first (11.1) and 11.2 starts from the same first call and history you built, adding only tools and the loop, with no framework.
**Architect's question:** a tool is an API the model can call on a user's behalf. Which tools may only read, which may change things, and which need a human to approve each call? Should the model ever write SQL, or only choose among fixed, reviewed queries, and how does a tool learn who the user is (Block 13)?

<details><summary>Recap questions</summary>

1. Q: Who runs the function in tool calling, the model or your code? A: Your code. The model only returns the tool name and arguments; your application validates them, runs the function and sends the result back.
2. Q: What must you send back after running a tool? A: The model's tool-call message followed by a tool-result message carrying the result and the id of the call it answers, then call the model again.
3. Q: Why put a step limit on the loop? A: A model can keep asking for tools (or repeat a failing call) indefinitely; a limit bounds cost and latency and turns a loop into a clear error.

</details>

---

## Block 12: Agents and your own MCP server

**What you build:** An agent built with a framework (the OpenAI Agents SDK) that decides on its own between searching the documents and looking up a fee, and your own MCP server that exposes DocDesk's `search_documents` tool so any MCP client (the MCP Inspector, Claude Desktop or a Python client) can use it.
**New layer:** an agent loop from a framework, and MCP (a standard protocol for tools). **Reuses:** the Block 11 tools and loop idea, Block 8/10 retrieval, the Block 5 API.
**Needs:** Block 11 working. One-time: `pip install openai-agents "mcp[cli]"`; Node.js for the MCP Inspector (`mcp dev` starts it with `npx`); Claude Desktop is optional. pixegami's repo uses `uv`; plain `pip` works too.
**Architecture so far:**
```
 ui -> api.py
         POST /chat, /ask, /search        (Blocks 5-11)
       * POST /agent
           * Agent (OpenAI Agents SDK, max_turns)
               chooses: search_documents (Blocks 8, 10) | lookup_fee (Block 11)
               model via provider settings (Block 6)

 * docdesk_mcp.py  (FastMCP server, stdio)
       tools: search_documents, lookup_fee  -> same functions, same Postgres
         ^
         |  MCP
       * MCP Inspector / Claude Desktop / Python MCP client
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 12.1 | How We Build Effective Agents: Barry Zhang, Anthropic | AI Engineer | https://www.youtube.com/watch?v=D7_ipDqhtwk | 15:09 | Start | BIKE | Anthropic's short, opinionated guide: what an agent loop is, when a simple workflow beats an agent, and how to design around the model's view of the world. Watch first; it is the "when NOT to use agents" video. (Summary of its principles taken from third-party write-ups seen in search; the page itself gave only title and length.) | verified; also in Track C 4.1; watch once |
| 12.2 | How to Build an Agent with the OpenAI Agents SDK | Sam Witteveen | https://www.youtube.com/watch?v=0Z7u6DTDZ8o | length ? | Deeper | DESK | Per its chapters (2025): a first agent in a Colab, streaming runs, adding your own function tools and a web-search tool, agents used as tools by another agent, and chat memory: Block 11's loop, now run by a framework. | verified; description |
| 12.3 | Why we built—and donated—the Model Context Protocol (MCP) | Anthropic | https://www.youtube.com/watch?v=PLyCki2K0Lg | 35:32 | Start | BIKE | Anthropic's Stuart Ritchie interviews MCP co-creator David Soria Parra on what MCP is (an open standard for connecting AI to tools and data) and why it was donated to the Linux Foundation. | verified; also in Track C 4.2; watch once |
| 12.4 | Build an MCP Server in 20 Minutes (with Python) | pixegami | https://www.youtube.com/watch?v=vzGkSn59rDU | length ? | Start | DESK | Per its chapters (2025): what an MCP server is, creating one in Python with a tool, a second example over Google Sheets, and using the tools from Claude Desktop. | verified; description |

**Code:** 12.1 and 12.3: none (talks). 12.2: the Colab notebook linked from the description; the GitHub link in the description (https://github.com/samwit/llm-tutorials) was last updated 2023-06 and does not hold this notebook, so use the Colab. 12.4: https://github.com/pixegami/mcp-python-tutorial (last updated 2025-06; a weather tool built with `FastMCP` from the official `mcp` package; matched by name with the description's cut-off link "mcp-pytho..."). The weather tool needs a free OpenWeatherMap key; you can skip it and write your own tool.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 12.O1 | LangChain vs. LangGraph vs. Deep Agents: When to Use Each One | LangChain | https://www.youtube.com/watch?v=ty8i2zl9q2c | 3:03 | Start | BIKE | Per the description and chapters: LangChain's own comparison of its three open-source agent frameworks, from LangGraph as a durable runtime to the ReAct-style agent loop to Deep Agents, with a "when to use each" section and a note on taking agents to production. A very short vendor video, so use it to see the framework-choice question, not as neutral advice. | verified; content per watch-page description and chapters; also in Track G 7.O3; watch once |
| 12.O2 | Build Reliable AI Agents with LangGraph | AWS Developers | https://www.youtube.com/watch?v=E0BtW2yt2pA | length ? | Start | BIKE | A few minutes with LangChain's Lance Martin (2025): a code overview of a LangGraph agent and a LangGraph Studio demo, enough to see the graph style before choosing it over the Agents SDK. | verified; description |
| 12.O3 | Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic | AI Engineer | https://www.youtube.com/watch?v=kQmXtrmQ5Zg | 1:44:11 | Deeper | DESK | Hands-on MCP workshop: build servers and an agent that uses them. Do it after 4.2-4.3 [Track C; row 12.3 here]. Workshop code predates later MCP spec changes (may be dated). | verified; also in Track C 4.D1; watch once |

**Build it (follow the video):**
1. Watch 12.1 and write down two DocDesk questions a fixed workflow handles fine and one where letting the model choose the steps could help.
2. Follow 12.2 in its Colab, then locally: `Agent(name=..., instructions=..., tools=[...])` and `Runner.run_sync(agent, "...")`; print `result.final_output`.
3. Turn two plain Python functions into tools with `@function_tool` (the docstring and type hints become the schema; compare with the schema you wrote by hand in Block 11), stream a run, and read the trace of which tool was called when.
4. Set `max_turns` on the run and ask something impossible, so you see the limit stop the loop.
5. Watch 12.3 for the "why": one protocol so any client can use any server.
6. Follow 12.4: create a `FastMCP` server with one `@mcp.tool()` (your own tool if you skip the weather key), run `mcp dev server.py` to open the MCP Inspector, list the tools and call one from the browser.
7. If you use Claude Desktop, add the server to its configuration as the video shows and ask Claude a question that makes it call your tool.

**Carry it into DocDesk:**
- Add `docdesk/agent.py`: one agent with instructions from `prompts/agent.md` and two tools wrapping existing code, `search_documents(query, k)` (Block 8/10 retrieval returning cited chunks) and `lookup_fee(product)` (Block 11); `max_turns=6`.
- Add `POST /agent` returning the answer, the citations it used and the list of tool calls; keep `/ask` and `/chat` as the cheaper fixed paths.
- To run the agent on Ollama or another provider, use the SDK's LiteLLM model option (check its docs); otherwise keep it on OpenAI and say so in `/health`.
- Add `docdesk/docdesk_mcp.py`: a `FastMCP("docdesk")` server exposing `search_documents` and `lookup_fee` with clear docstrings, calling the same functions and database; run it over stdio.
- Test it in the MCP Inspector, then from a 20-line Python client (`ClientSession` and `stdio_client` from the `mcp` package, as in the SDK's README) that lists the tools and calls `search_documents`.

**Done when:** `POST /agent` answers "Is my money insured if my bank fails, and what does the basic checking account cost per year?" by calling `search_documents` and `lookup_fee` (both listed in the response, with citations), and the MCP Inspector and your Python client can both call `search_documents` on `docdesk_mcp.py` and get the same chunks.
**Stretch:** connect the agent to your own MCP server instead of the local functions (the Agents SDK can use an MCP server over stdio) and confirm the answers do not change; then rebuild the agent in LangGraph (12.O2) and compare the code and the traces.
**Cost and teardown:** an agent run makes several model calls (each tool step is one), so it costs more than `/ask`; watch the per-request cost. The MCP server runs only while a client starts it over stdio; remove it from Claude Desktop's configuration when you are done.
**Progression check:** New: an agent framework (Agent, Runner, function tools, max turns) and MCP (a server, tools over a protocol, the Inspector). Reused: the Block 11 tools and the loop you wrote by hand, Block 8/10 retrieval, the API. Jump size: medium; the agent loop arrives after you built the same loop yourself, and MCP comes as a concept (12.3) before a 20-minute server (12.4), with both wrapping functions that already work.
**Architect's question:** MCP turns your tools into a shared service that any approved client can call. Who decides which MCP servers are allowed in the bank, how does a server know which user is calling and what they may see (Block 13), and when is an agent worth its extra cost and unpredictability compared with the fixed `/ask` path?

<details><summary>Recap questions</summary>

1. Q: What does an agent framework add over the loop you wrote in Block 11? A: The loop itself (call model, run tools, repeat until an answer or a limit), tool schemas generated from functions, tracing, memory, handoffs between agents and guardrail hooks; the decisions and the tools are still yours.
2. Q: What does an MCP server expose, and who calls it? A: Tools (and also resources and prompts) described in a standard way; an MCP client inside an application such as Claude Desktop, an IDE, the Inspector or your own Python code connects to it and calls them.
3. Q: Why keep both `/ask` and `/agent` in DocDesk? A: `/ask` is a fixed, cheap, predictable workflow for most questions; `/agent` costs more and varies more, so it is used only where choosing between tools adds value.

</details>

<!-- Pages to check (Blocks 7-12): every new row's watch page was read (oEmbed was again refused by the fetch allowlist; title and channel come from the watch-page metadata). The fetch tool sometimes returned another video's page for a requested ID, so a row was kept only when the page's title matched the search result; these candidate IDs were skipped for that reason and are not in the file: SXwC9fSwct8 (search title "Ultimate Docker Compose Tutorial", TechWorld with Nana per search), hAdEuDBN57g, bZzyPscbtI8, 8rieuXTvBtM, Ek8JHgZtmcI, tc713anE3UY, j63xRV52IMk. Repos were checked with git ls-remote and a shallow clone (last commit date); the GitHub API was not reachable from this session. -->

---

## Block 13: Users, auth and a gateway, all local

**What you build:** Real users for DocDesk on your laptop: registration and login with hashed passwords, a JWT access token on every request, routes that know the current user, chats that only their owner can read, an API key for scripts, a rate limit, and Nginx in front of everything in the Compose stack as the single front door.
**New layer:** authentication and authorization, and a gateway (reverse proxy) in front of the services. **Reuses:** the Block 5 API, the Block 9 Compose stack and the Block 10 `users`, `conversations` and `messages` tables.
**Needs:** Block 10 working (12 is not required). One-time: `pip install pyjwt "pwdlib[argon2]" pydantic-settings` (the libraries Corey Schafer's Part 10 repo uses; pixegami's 5.3 repo uses `python-jose` instead, which does the same job). No new account or cloud service: Nginx runs as the `nginx` image in Compose. Corey Schafer's Parts 10 and 11 continue his series from Parts 6 to 9 (async database, routers), which you have not built; start from his Part 10 repo, as the Build steps say, rather than from your Block 5 copy.
**Architecture so far:**
```
 browser / curl / script
   |  :80 only (the one published port)
   v
 * nginx (reverse proxy)  /  -> ui:8501     /api/ -> api:8000
   * limit_req (per-IP rate limit), request size limit, access log
   |
 ui (Streamlit) ---- Authorization: Bearer <JWT> ----> api (FastAPI)
                                                         * POST /auth/register, /auth/token
                                                         * get_current_user dependency (JWT or X-API-Key)
                                                         * per-user rate limit
                                                         /chat, /ask, /agent  -> only your own conversations
 postgres: users(* email, * password_hash), * api_keys(user_id, key_hash),
           conversations(user_id ...), messages            (Block 10)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 13.1 | Session Vs JWT: The Differences You May Not Know! | ByteByteGo | https://www.youtube.com/watch?v=fyTxwIa-1U0 | length ? | Start | BIKE | An animated explainer (2024) of the two ways a server remembers a logged-in user: a session id that points to state on the server, or a signed token that carries the claims itself, and what each costs you for logout, scaling and security. | verified; description |
| 13.2 | OAuth and OpenID Connect in Plain English • Nate Barbettini • GOTO 2020 | GOTO Conferences | https://www.youtube.com/watch?v=sSy5-3IkXHE | 18:44 | Start | BIKE | Fast lane: per the chapters, why OAuth exists (delegated authorisation), the flow vocabulary, how OpenID Connect adds identity on top, and current practice. You will know most of it; use it to check that your words match the common ones. | verified; content per watch-page description and chapters; also in Track D 5.1; watch once |
| 13.3 | Python FastAPI Tutorial (Part 10): Authentication - Registration and Login with JWT | Corey Schafer | https://www.youtube.com/watch?v=Go4wYJJhR3k | length ? | Start | DESK | The Block 5 series continues (2026): user registration with Argon2 password hashing, login that returns a JWT, settings with pydantic-settings, and the client keeping the token. | verified; description |
| 13.4 | Python FastAPI Tutorial (Part 11): Authorization - Protecting Routes and Verifying Current User | Corey Schafer | https://www.youtube.com/watch?v=MY0TFMMm9B0 | length ? | Start | DESK | The next episode (2026): a reusable `get_current_user` dependency that checks the token, the user id taken from the token instead of the request body, and ownership checks so users can only change their own posts: the pattern for per-user chats. | verified; description |
| 13.5 | NGINX Explained - What is Nginx | TechWorld with Nana | https://www.youtube.com/watch?v=iInUBOVeBCc | length ? | Start | BIKE | Per its chapters (2024): Nginx as web server, reverse proxy and load balancer, how its configuration is organised, caching and TLS termination, and how an Nginx load balancer compares with a cloud load balancer (the Block 16 question). | verified; description |
| 13.6 | Docker and Nginx Reverse Proxy | Wes Doyle | https://www.youtube.com/watch?v=hxngRDmHTM0 | length ? | Deeper | DESK | Per its chapters, a Compose file where one Nginx container routes paths to two Python Flask APIs and a front-end container, with the `nginx.conf` written line by line. From 2020 and Flask, not FastAPI; the Compose and Nginx parts are unchanged. | verified; description |

**Code:** 13.1, 13.2 and 13.5: none (concepts). 13.3: https://github.com/CoreyMSchafer/FastAPI-10-Authentication (last updated 2026-01; `auth.py` with `OAuth2PasswordBearer`, PyJWT and `pwdlib`; matched by name with the description's cut-off link). 13.4: https://github.com/CoreyMSchafer/FastAPI-11-Authorization (last updated 2026-01; matched by name the same way). 13.6: the description links a repository under `github.com/productive-dev/` that is cut off on the watch page; type along. Rate limiting and a second JWT example: the Block 5 repo for 5.3, https://github.com/pixegami/fastapi-gemini-ai (last updated 2025-06; `src/auth/throttling.py` is a small in-memory per-user limiter and `src/auth/dependencies.py` checks the JWT).
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 13.O1 | Create a Nginx Reverse Proxy for a Node Server with Docker Compose | WittCode | https://www.youtube.com/watch?v=U60MdJeov_0 | length ? | Start | DESK | Per its chapters (2023), the same reverse proxy as 13.6 with a newer Compose file: a Node server, the Nginx configuration, both images, debugging and a look inside the running Nginx container. A smaller channel; the Node part is short. | verified; description |
| 13.O2 | API Gateway Pattern & Kong in a Microservices World | The Linux Foundation | https://www.youtube.com/watch?v=OUUiS28hZuw | 41:45 | Deeper | BIKE | The only API-gateway concept talk I verified; it is a vendor (Kong) talk, judged from the title only, so keep the pattern and discount the product. | verified; title-based; also in Track D 3.O1; watch once |
| 13.O3 | Rate Limiter using Spring Cloud Gateway and Redis example \| Tech Primers | Tech Primers | https://www.youtube.com/watch?v=0LoqPg6h6wc | 15:15 | Deeper | DESK | By title, an API gateway in Spring Cloud Gateway with a Redis-backed rate limiter, which ties Block 1's Redis to the gateway pattern [Track E; Redis arrives in Block 18 here]. I could not read the watch page, and a gateway tutorial of this kind may be several Spring versions old. | verified; title-based; also in Track E 2.5; watch once |

**Build it (follow the video):**
1. Watch 13.1 and 13.2. On your sheet, write one line each for: authentication (who are you), authorization (what may you do), session, JWT, OAuth 2.0 (delegated access) and OpenID Connect (login on top of OAuth). Mark which one DocDesk uses in this block (a password login that issues its own JWT, no outside identity provider yet; Cognito comes in Block 22).
2. Clone the Part 10 repo, open it in VS Code and run it as its README says (`uv sync` and `fastapi dev main.py`, or plain `pip`). Then follow 13.3 against that code: read `config.py` (settings and `SECRET_KEY`), `auth.py` (hash, verify, create and verify a token) and the register and token routes, pausing the video to find each piece.
3. In `/docs`, register a user, then press "Authorize" and log in: FastAPI's password flow form calls the token route for you. Copy the `access_token` and paste it into https://jwt.io (or decode it with `python -c "import jwt; print(jwt.decode(TOKEN, options={'verify_signature': False}))"`): you see the `sub` and `exp` claims, readable by anyone, which is why a JWT is signed but never holds secrets.
4. Follow 13.4 with the Part 11 repo: the `get_current_user` dependency, a protected route that returns 401 without a token, and the ownership check that returns 403 when you edit someone else's post. Make one of each with `curl` and note which status code means "who are you?" and which means "not yours".
5. Go back to 5.3 (Block 5) and watch from 12:51 (Rate Limiting) to 22:38: read `throttling.py` and `dependencies.py` in its repo, run it, and send requests in a loop until you get 429. Note that the counter lives in one Python process's memory.
6. Watch 13.5 for the "why", then follow 13.6: a Compose file with an `nginx` service that is the only one with a published port, and an `nginx.conf` with `location` blocks that forward paths to the services by their Compose names. Run `docker compose up` and check that the services are no longer reachable on their own ports.

**Carry it into DocDesk:**
- Migration: add `email` (unique) and `password_hash` to `users`, and a table `api_keys(id, user_id, key_hash, name, created_at, revoked_at)`. Store only hashes, never the password or the key itself.
- Add `docdesk/auth.py` modelled on 13.3: `hash_password`, `verify_password`, `create_access_token` (15-minute expiry) and `get_current_user`. Add `POST /auth/register` and `POST /auth/token` (the OAuth2 password flow form, so `/docs` can log in). Put `SECRET_KEY` in `.env` (generate it with `python -c "import secrets; print(secrets.token_hex(32))"`), never in the code.
- Per-user data: `/chat`, `/ask`, `/agent` and `GET /conversations/{id}` take `user = Depends(get_current_user)`; the user id comes from the token, not the request body; every conversation query filters on `user_id`, and a conversation that belongs to someone else returns 404 (do not reveal that it exists). Add `GET /conversations` that lists only your own.
- API keys for scripts: `POST /api-keys` creates a random key (`secrets.token_urlsafe(32)`), shows it once and stores its hash; `get_current_user` also accepts an `X-API-Key` header and looks up the hash. Use a key from a small `scripts/ask.py` that calls `/ask` without a password.
- Rate limit in the API, as in 5.3, but per user and only on the model-calling routes (for example 20 questions per minute per user), returning 429 with a `Retry-After` header. Like 5.3's limiter it lives in memory; Block 18 moves the counter to Redis so several API copies share it.
- Streamlit: a login form that stores the token in `st.session_state` and sends `Authorization: Bearer ...` on each call; on 401, show the login form again.
- Nginx in Compose: an `nginx` service with `nginx/nginx.conf`, `ports: ["80:80"]` on Nginx only (remove the published ports of `api`, `ui`, `db` and `ollama`), `location /api/` proxied to `http://api:8000/` and `location /` to `http://ui:8501` with the WebSocket headers Streamlit needs (`proxy_http_version 1.1`, `proxy_set_header Upgrade $http_upgrade`, `proxy_set_header Connection "upgrade"`). Set `DOCDESK_API_URL` for the UI to `http://api:8000` (inside the network) as before.
- At the gateway: `limit_req_zone` with a per-IP limit on `/api/` (coarse protection for everyone), `client_max_body_size` for uploads, and an access log line that includes the request time. The per-user limit stays in the API, because only the API knows who the user is.

**Done when:** with `docker compose up`, only port 80 answers on your laptop; you can register two users in the page, each sees only their own conversations, and `curl localhost/api/conversations/<other user's id>` with your token returns 404; a request without a token returns 401; `scripts/ask.py` works with an API key and stops working after you revoke it; and a burst of 30 fast questions gets 429 responses from the API, while a flood of unauthenticated requests is cut by Nginx's `limit_req` (503 by default, or the status you set).
**Stretch:** add refresh tokens (a long-lived token stored server-side that can be revoked, as in 13.1's trade-off), or replace your own login with Keycloak in Compose and validate its JWTs in FastAPI; this is the OIDC pattern from 13.2 that Block 22 repeats with Cognito.
**Cost and teardown:** no cloud cost; one more small container (Nginx). `docker compose down` as before. Rotate `SECRET_KEY` if you ever commit it: every token issued with it becomes invalid, which is also how you log everyone out.
**Progression check:** New: password hashing, JWT access tokens, a current-user dependency, ownership checks, API keys, rate limits at two places, and a reverse proxy as the only door. Reused: the Block 5 API, the Block 9 Compose stack, the Block 10 tables, the Block 5 video (5.3) for rate limiting. Jump size: medium; the concepts come first (13.1-13.2), then the same series you used in Blocks 5 and 10 adds login (13.3) and then authorization (13.4), and the gateway (13.5-13.6) is configuration in front of code that already works, with no cloud yet.
**Architect's question:** you now check identity in the API and limit traffic in two places. In a bank, which checks belong at the gateway (TLS, coarse rate limits, API-key validation, request size), which must stay in the service (may this user see this conversation or this document), and what happens to your design when the identity provider is the bank's single sign-on and DocDesk never sees a password?

<details><summary>Recap questions</summary>

1. Q: What is the difference between authentication and authorization, and which HTTP status codes go with each? A: Authentication establishes who the caller is (401 Unauthorized when it is missing or invalid); authorization decides what that caller may do (403 Forbidden, or 404 when you should not reveal that the resource exists).
2. Q: Why can anyone read a JWT, and why can they still not forge one? A: The header and claims are only Base64-encoded, not encrypted; the signature over them is made with a secret (or private key) only the server has, so a changed claim no longer matches the signature and the server rejects it.
3. Q: Why keep a per-user rate limit in the API when Nginx already limits requests? A: Nginx sees IP addresses, not users, so it can only throttle coarse traffic; the API knows the authenticated user and can apply a fair per-user limit on the expensive model calls.

</details>

---

## Block 14: AWS foundations: a safe account, IAM, the CLI, a budget and S3

**What you build:** A personal AWS account set up the safe way (root user locked away behind MFA, a monthly budget with email alerts before anything else, a separate admin identity for daily work), the AWS CLI signed in without long-lived access keys, and an S3 bucket that holds the DocDesk PDFs, which `ingest.py` now reads with boto3. Nothing is deployed yet.
**New layer:** the cloud account, identity (IAM) and object storage. **Reuses:** the DocDesk PDFs from Block 0 and `ingest.py` from Blocks 8 and 10; the app itself still runs in Compose on your laptop.
**Needs:** Block 13 working (only the ingestion step changes here). A phone with an authenticator app (or a hardware security key) for MFA, an email address used only for this account, and a payment card in case the sign-up asks for one (the sign-up screens change; follow what they show). One-time: AWS CLI version 2 (14.4's description says `aws login` needs version 2.32.0 or later; `aws --version` shows yours) and `pip install boto3`. Personal account only: nothing from work, no work credentials.
**Architecture so far:**
```
 * AWS account (one Region for the whole track)
     * root user: MFA, no access keys, locked away
     * AWS Budgets: monthly cost budget -> email at 50% / 80% / 100% (actual and forecast)
     * IAM: admin identity for you (console + `aws login`), MFA on
            * policy docdesk-s3-read (ListBucket, GetObject on the docs prefix)  -> used in Block 15
     * S3 bucket  docdesk-docs-<random>   (Block Public Access on, encryption on)
          docs/*.pdf
              ^
              | boto3 (list_objects_v2, get_object)
 laptop:  ingest.py --source s3://docdesk-docs-.../docs/  -> Postgres + pgvector (Compose, Block 10)
          nginx -> ui / api  (Block 13, unchanged)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 14.1 | AWS IAM Core Concepts You NEED to Know | Be A Better Dev | https://www.youtube.com/watch?v=_ZCTvmaPgao | length ? | Start | BIKE | A whiteboard-style introduction (2021) to IAM through one practical example: users and groups, policies and permissions, roles and the trust relationship that lets a service assume one. The console has moved on; the ideas have not. | verified; description |
| 14.2 | How to Set Up & Secure an New Free Tier AWS Account | cloudmancer | https://www.youtube.com/watch?v=SOOuSNG23No | length ? | Start | DESK | Per its chapters (2025): signing up, signing in as the root user and protecting it with MFA, creating an IAM user for daily work and signing in as that user, then creating a budget. A small channel, chosen because it covers exactly this sequence on the current console. | verified; description |
| 14.3 | How to Set up a cost budget using AWS Budgets & Get $20 in Credits | BeSA Cloud Academy | https://www.youtube.com/watch?v=CnBGRrYCksg | length ? | Start | DESK | A two-minute walk through a monthly cost budget with email alerts at thresholds (2025), which on the newer free plan also earns a credit. A small community channel; watch it right after the root user is protected, before you create anything else. | verified; description |
| 14.4 | The Safest Way to Authenticate AWS CLI in 2026 (No Access Keys Needed) | Tech With Yeshwanth | https://www.youtube.com/watch?v=OvDsVD6nshw | length ? | Start | DESK | Per its description (2026): why long-lived access keys are risky, signing the CLI in with your console identity using `aws login`, checking who you are, session expiry and `aws logout`, and how older SDKs can share the session through `credential_process`. A small channel; check each command against the AWS CLI documentation it links. | verified; description |
| 14.5 | Working with AWS S3 using boto3 and Python | Hands-On-Cloud | https://www.youtube.com/watch?v=AT9tEHuhg68 | length ? | Start | DESK | Per its chapters (2022), a long boto3 session in sections: list and create buckets, upload files, list and filter objects, download them, delete, and pre-signed URLs. Watch only the sections the Build steps name. A smaller channel; boto3's S3 calls have not changed. | verified; description |

**Code:** 14.1 to 14.4: none (console and CLI); for 14.4 keep the AWS CLI user guide page "Login for AWS local development using console credentials" open (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html, read 2026-11-17): it confirms the 2.32.0 minimum, says an IAM user needs the `SignInLocalDevelopmentAccess` managed policy (an administrator already has it covered), and shows the `credential_process` profile for SDKs that cannot read the session yet. 14.5: no repo; the description links a written article on hands-on.cloud (cut off on the watch page); type along.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 14.O1 | How do I use the AWS CLI to get temporary credentials for an IAM Identity Center user? | Amazon Web Services | https://www.youtube.com/watch?v=Ts8qbicxjcs | length ? | Deeper | DESK | A two-minute AWS Knowledge Center clip (2025): where the CLI caches an IAM Identity Center sign-in and how to turn it into temporary credentials. Only for the Stretch path (Identity Center instead of an IAM user). | verified; description |

**Build it (follow the video):**
1. Watch 14.1 and write on your sheet, in one line each: principal (who), policy (what is allowed, on which resource), role (a set of permissions something can assume for a while), trust policy (who may assume the role). Then add the one that matters most from Block 15 on: "a container gets permissions from a role, never from a key in its environment".
2. Follow 14.2 to 2:28: sign up, sign in as the root user and turn on MFA for root. Do not create access keys for root, ever.
3. Before anything else, follow 14.3 (and 14.2 from 5:11): a monthly cost budget with an amount you choose, email alerts at 50%, 80% and 100% of actual cost and at 100% of forecast cost. Check that the alert email address is one you read.
4. Back to 14.2 at 2:28: create your admin identity (the video's IAM user), turn on MFA for it, sign out of root, and sign in with the new identity's sign-in URL. From now on, root stays unused.
5. Follow 14.4: update the CLI, run `aws login`, then `aws sts get-caller-identity` and read the ARN: it must be your admin identity, not root. Run `aws s3 ls` (empty is fine) and `aws logout`, then log in again.
6. In the S3 console, create a bucket with a globally unique name (for example `docdesk-docs-` plus a few random characters) in your chosen Region; leave Block Public Access on and default encryption on. Upload one PDF by hand.
7. Follow 14.5 for "Listing and filtering buckets" (0:56), "Uploading files and objects" (33:00), "Listing and filtering objects" (51:00) and "Downloading objects" (59:49), typing the calls against your own bucket with `boto3.client("s3")`; skip versioning, deletes, copies and pre-signed URLs for now.

**Carry it into DocDesk:**
- `aws s3 sync docs/ s3://<your-bucket>/docs/` uploads all DocDesk PDFs; `aws s3 ls s3://<your-bucket>/docs/` shows them.
- Add `docdesk/storage.py` with `list_pdfs(prefix) -> list[str]` (`list_objects_v2` with a paginator) and `read_pdf(key) -> bytes` (`get_object(...)["Body"].read()`), and give `ingest.py` a `--source` option: a local folder as before, or `s3://bucket/prefix/`; pass the bytes to your PDF reader through `io.BytesIO`. Chunk ids and citations now use the S3 key as the source.
- Settings: `AWS_REGION`, `DOCDESK_BUCKET`, `DOCDESK_PREFIX=docs/`. No keys in `.env`: boto3 finds the credentials from your CLI sign-in through `AWS_PROFILE`. If your boto3 cannot read the `aws login` session, add the `credential_process` profile from the CLI guide page in Code (`aws configure export-credentials ... --format process`) and point `AWS_PROFILE` at it.
- To run `ingest.py` inside the Compose `api` container, mount `~/.aws` read-only into it and set `AWS_PROFILE`; this is for the laptop only, and Block 15 replaces it with a role.
- Create (but do not attach yet) a customer-managed IAM policy `docdesk-s3-read`: `s3:ListBucket` on the bucket with a condition on the `docs/` prefix, and `s3:GetObject` on `arn:aws:s3:::<bucket>/docs/*`. Block 15 attaches it to the container's role.
- In `docdesk/README.md`, write down the Region, the bucket name and the budget amount, and the rule "no access keys in files, ever".

**Done when:** the root user has MFA and you are signed in day to day as your admin identity; the budget shows in AWS Budgets with its alert thresholds; `aws sts get-caller-identity` shows your admin identity; `python ingest.py --source s3://<bucket>/docs/` loads all PDFs into Postgres; and `/ask` cites the S3 keys as sources with the same answers as before.
**Stretch:** do it the enterprise way: enable IAM Identity Center, create a user with an `AdministratorAccess` permission set, sign the CLI in with `aws configure sso` and `aws sso login` (14.O1 shows where those credentials live), and remove the IAM user. Then turn on S3 versioning and see an overwritten PDF come back.
**Cost and teardown:** nothing in this block runs by the hour. S3 charges for the storage and requests you use, which is very little for a few PDFs; check the S3 pricing page and your free-plan credits. Keep the bucket and the budget: Blocks 15 to 17 use them. At the end of the track, empty and delete the bucket (`aws s3 rb s3://<bucket> --force`), and if you ever created access keys, deactivate and delete them in IAM.
**Progression check:** New: the account, the root user and MFA, a budget, IAM identities and policies, CLI sign-in, an S3 bucket and boto3. Reused: the PDFs, `ingest.py` and the whole local stack, unchanged apart from where the PDFs are read from. Jump size: medium but flat; many small console steps, each with its own short video, and no deployment, networking or running cost yet.
**Architect's question:** in a bank, a developer never gets an account like this one: there are many accounts (per team and per environment) under AWS Organizations, people sign in through the bank's identity provider, and service control policies forbid whole classes of action. Which of today's steps would the platform team do for DocDesk, and which permissions would you still have to ask for, in writing, for Block 15?

<details><summary>Recap questions</summary>

1. Q: Why lock away the root user and use a separate admin identity? A: Root has unlimited power that policies cannot restrict, so it is protected with MFA, has no access keys and is used only for the few tasks that need it; daily work uses an identity whose permissions can be limited, logged and revoked.
2. Q: What is the difference between an IAM user and an IAM role? A: A user is a long-lived identity for one person or system with its own credentials; a role has no credentials of its own and is assumed for a limited time by a trusted principal (a person, a service such as ECS, or another account), which receives temporary credentials.
3. Q: Why create the budget before anything else? A: Cloud resources charge while they exist, not only while you use them; a budget with actual and forecast alerts is the earliest warning that something was left running, and it takes ten minutes to set up.

</details>

---

## Block 15: DocDesk's containers on AWS: ECR, ECS Fargate, RDS and secrets

**What you build:** The same three images from Blocks 9 and 13 (Nginx, API, Streamlit) pushed to Amazon ECR and running as one ECS service on Fargate, talking to a managed Postgres (RDS for PostgreSQL with pgvector) in private subnets, reading the PDFs from S3 through a role, and getting its passwords and API keys from Secrets Manager or Parameter Store instead of a `.env` file. You reach it by the task's public IP address for now; the proper front door is Block 16.
**New layer:** a cloud runtime, a managed database and managed secrets, on top of a first VPC. **Reuses:** the Block 9 images and Compose layout, the Block 10 schema and migrations, the Block 13 Nginx and auth, and the Block 14 account, CLI sign-in, bucket and `docdesk-s3-read` policy.
**Needs:** Block 14 done (budget alerts on). Docker on the laptop. A hosted model key for the cloud (Ollama does not come along: Fargate has no GPU and the model is too large to ship in an image; Bedrock arrives in Block 17). AWS App Runner, once the simplest way to run one container, is closed to new customers: the App Runner developer guide's availability-change page (read on 2026-11-17, in its Japanese edition; the English page could not be fetched here) says existing customers can keep using it, no new features are planned, and recommends Amazon ECS Express Mode instead. This block therefore uses ECS on Fargate, by hand first, with Express Mode as the optional shortcut (15.O1).
**Architecture so far:**
```
 laptop: docker build --platform linux/amd64 ... ; docker push --> * ECR: docdesk-nginx, docdesk-api, docdesk-ui
                                                                         |
 * VPC (2 Availability Zones)                                            v
   * public subnets:  * ECS service "docdesk" (Fargate, 1 task, public IP)
                        task = nginx :80  +  api :8000  +  ui :8501   (share localhost)
                        * task role: docdesk-s3-read (Block 14)  -> S3 bucket docs/
                        * execution role: pull from ECR, read secrets, write logs
                        * security group sg-app: port 80 from YOUR IP only
   * private subnets: * RDS for PostgreSQL (pgvector), not public
                        * security group sg-db: 5432 from sg-app only
 * Secrets Manager / Parameter Store: DB password, OPENAI_API_KEY, SECRET_KEY
 * CloudWatch Logs: one log stream per container
 browser --> http://<task public IP>/        (no domain, no HTTPS yet: Block 16)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 15.1 | AWS Networking Fundamentals | Amazon Web Services | https://www.youtube.com/watch?v=hiKPPy584Mg | length ? | Start | BIKE | An AWS session (2019) on VPC basics: planning IP ranges, subnets, routing, security groups and network ACLs, and NAT, followed by connecting a VPC to a data centre with VPN or Direct Connect, which can wait. Older, but these building blocks have not changed. | verified; description |
| 15.2 | Docker to AWS ECS: Deploy Your First Container Step by Step | Cloud Guru | https://www.youtube.com/watch?v=xCjs7qXP-mE | length ? | Start | DESK | Per its chapters (2026): an ECR repository, CLI and IAM setup, building and pushing an image, then a VPC with public and private subnets and route tables, an ECS cluster, a task definition and a service, followed by a load balancer and a NAT gateway (Block 16 picks those up). A smaller channel; its chapters match this block step for step. | verified; description |
| 15.3 | How to Create an Amazon RDS Database & Get Free $20 in Credits | BeSA Cloud Academy | https://www.youtube.com/watch?v=QF0J3VroFs8 | length ? | Start | DESK | A short console walk-through (2025) of creating an RDS database with PostgreSQL: engine, master credentials, the default settings, and then deleting the instance so it stops costing money. A small community channel. | verified; description |
| 15.4 | AWS Systems Manager Parameter Store - Use Credentials with ECS Environment Variables (Hands-On) | Ethereum-Blockchain-Developer \| BlockOnAir | https://www.youtube.com/watch?v=a6B9nF9nBiY | length ? | Deeper | DESK | Per its chapters, Parameter Store compared with Secrets Manager (00:00), then a hands-on lab that stores a credential and hands it to an ECS container as an environment variable (03:40). From a 2020 ECS course, so the console looks different; the task-definition `secrets` mechanism is the same. | verified; description |

**Code:** none of these videos needs a repo: 15.2's description does not link one, and the code you deploy is DocDesk's own. Keep the AWS documentation for ECS task definitions (`secrets`, `taskRoleArn`, `executionRoleArn`) open while you type.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 15.O1 | Build production-ready applications with Amazon ECS Express Mode | Containers from the Couch | https://www.youtube.com/watch?v=z9JUEQjpGgY | length ? | Start | DESK | An AWS-run live show (2025) where AWS developer advocates introduce ECS Express Mode: one command turns a container image into a running, scaling service with its own URL. Watch it after you built the pieces by hand, to see what the shortcut creates for you. | verified; description |
| 15.O2 | Getting Started With pgvector and Amazon Aurora PostgreSQL | AWS Developers | https://www.youtube.com/watch?v=e9SHaO9RNzk | length ? | Deeper | BIKE | AWS's own introduction (2023) to the pgvector extension on Aurora PostgreSQL: storing embeddings next to ordinary tables and running similarity searches; the same extension you enable on RDS for PostgreSQL here, and one of Bedrock's vector stores in Block 17. | verified; description |

**Build it (follow the video):**
1. Watch 15.1 up to the part on VPN and Direct Connect. Draw one VPC on your sheet with two public and two private subnets in two Availability Zones, an internet gateway, and two security groups (`sg-app`, `sg-db`) with an arrow "5432 from sg-app only". Write the rule: a security group allows traffic in by source; the default is deny.
2. Follow 15.2 from 02:40 to 13:38 with its own sample (or straight away with `docdesk-api`): create an ECR repository, log Docker in to ECR (`aws ecr get-login-password ... | docker login ...`), tag and push an image, and find it in the console. On an Apple-silicon Mac, build with `--platform linux/amd64` (or choose ARM64 in the task definition).
3. Continue 15.2 from 13:38 to 31:07: the VPC, subnets and route tables, an ECS cluster, a task definition and a service. Stop at 31:07; Block 16 picks up the load balancer from there. To reach the task without a load balancer, run it in a public subnet with "Assign public IP" on and a security group that allows its port from your own IP address only, then open `http://<public IP>:<port>`.
4. Note what 15.2 does at 39:31 (a NAT gateway so tasks in private subnets can reach the internet and ECR): you do not need it while the task sits in a public subnet, and it is charged by the hour (see Cost and teardown).
5. Follow 15.3: create an RDS for PostgreSQL database, but change three defaults: "Public access: No", put it in your VPC's private subnets with `sg-db`, and choose "Manage master credentials in AWS Secrets Manager" so RDS creates and stores the password for you. Note the endpoint name.
6. Follow 15.4 (from 03:40) for the mechanism: a value stored outside the image, an execution role allowed to read it, and a `secrets` entry in the task definition that turns it into an environment variable inside the container. Do the same for the RDS secret (Secrets Manager) and for one value of your own in Parameter Store (a SecureString).

**Carry it into DocDesk:**
- Three ECR repositories (`docdesk-nginx`, `docdesk-api`, `docdesk-ui`); build the Nginx image with your `nginx.conf` copied in; tag each image with the Git commit, not only `latest`, and push.
- One task definition `docdesk` with the three containers (Fargate, `awsvpc` network mode). Containers in one task share `localhost`, so in a cloud copy of `nginx.conf` the upstreams become `127.0.0.1:8000` and `127.0.0.1:8501`, and `DOCDESK_API_URL` becomes `http://127.0.0.1:8000`. Only Nginx exposes port 80. Log driver `awslogs`, one stream per container.
- Settings from the environment: `DB_HOST` (the RDS endpoint), `DB_NAME`, `DB_USER`, and `DB_PASSWORD` from the RDS-managed secret (`valueFrom` with the secret's ARN and the `password` key); `OPENAI_API_KEY` and `SECRET_KEY` from Parameter Store SecureStrings or Secrets Manager; `DOCDESK_PROVIDER=openai`; `AWS_REGION`, `DOCDESK_BUCKET`. Build `DATABASE_URL` in `Settings` from the parts. No `.env` file and no `~/.aws` mount in the cloud.
- Roles: the task execution role (pull from ECR, write logs, read exactly these secrets and parameters) and a task role with `docdesk-s3-read` attached, so boto3 inside the API gets S3 access with no keys at all.
- One-off tasks with the API image and a command override (`aws ecs run-task ... --overrides`): first `alembic upgrade head` (your Block 10 migrations, including `CREATE EXTENSION vector`), then `python ingest.py --source s3://<bucket>/docs/`. They run inside the VPC, so they can reach the private database that your laptop cannot.
- Service `docdesk` with desired count 1 in a public subnet, public IP on, `sg-app` allowing port 80 from your IP only; `sg-db` allowing 5432 from `sg-app` only.

**Done when:** `http://<task public IP>/` shows the DocDesk login page; you can register, log in and ask a question that comes back with citations to S3 keys; the answer and the conversation are in RDS (a second task started later still sees the conversation); CloudWatch Logs shows the API's request lines; and `grep -ri "sk-\|password" ` over the task definition JSON finds no secret values, only ARNs.
**Stretch:** recreate the same service with ECS Express Mode (15.O1) from your `docdesk-api` image and list everything it created for you (service, load balancer, security groups, scaling); then delete it. Or move the task to a private subnet and give it VPC endpoints for ECR, S3, CloudWatch Logs and Secrets Manager instead of a NAT gateway, and compare what each option costs on the pricing pages.
**Cost and teardown:** from this block on, things cost money while they exist. Charged while running (check each pricing page for your Region): Fargate tasks (by vCPU and memory for as long as the task runs), the RDS instance (by the hour while it runs, plus storage), public IPv4 addresses, Secrets Manager secrets, and ECR storage. If you follow 15.2's NAT gateway step: "you are charged for each hour that your NAT gateway is available and each gigabyte of data that it processes" (Amazon VPC User Guide, "Pricing for NAT gateways", read 2026-11-17), so delete it at the end of every session. After each session: set the service's desired count to 0 and stop the RDS instance. The RDS guide's page on stopping an instance (read 2026-11-17) says a stopped instance still pays for its provisioned storage and backups (and a public IPv4 address if it has one), and that RDS starts it again automatically after seven consecutive days, so stop it again or delete it. At the end of Block 16 (or now, if you pause the track): delete the service and cluster, deregister the task definitions, delete the RDS instance (take a final snapshot only if you want the data), the ECR repositories, the secrets and parameters, any NAT gateway and its Elastic IP, the security groups and the VPC. Watch the budget email for the next few days.
**Progression check:** New: ECR, a VPC with subnets and security groups, ECS clusters, task definitions and services on Fargate, RDS, IAM roles for tasks, and managed secrets. Reused: the same images (Blocks 9 and 13), the same migrations and ingestion (Blocks 10 and 14), the S3 policy (Block 14). Jump size: large, the biggest so far, so it is split: networking as a concept first (15.1), then one image pushed and run (15.2), then the database (15.3), then secrets (15.4); the application code changes only in how it reads its settings.
**Architect's question:** the same image now runs on your laptop and in AWS with different settings. Which differences are allowed between environments (addresses, secrets, sizes) and which are not (code, dependencies, schema)? And for a bank: why would the database's password be managed and rotated by RDS and Secrets Manager rather than chosen by you, and who should be able to read it?

<details><summary>Recap questions</summary>

1. Q: What is the difference between an ECS task's execution role and its task role? A: The execution role is used by ECS itself to start the task (pull the image from ECR, fetch secrets for the `secrets` entries, write logs); the task role is assumed by your code inside the container for its own AWS calls, such as reading from S3.
2. Q: Why is the database in a private subnet with a security group that only allows the app's security group? A: Nothing on the internet can reach it, and inside the VPC only tasks that carry `sg-app` can open a connection on port 5432, so a leaked password alone is not enough to connect.
3. Q: How does a secret reach the container without being in the image or the task definition? A: The task definition holds only the secret's ARN in a `secrets` entry; when the task starts, ECS uses the execution role to fetch the value from Secrets Manager or Parameter Store and injects it as an environment variable.

</details>

---

## Block 16: The internet edge: your domain, HTTPS, a load balancer, a CDN and a firewall

**What you build:** A proper front door for the service from Block 15: a name (`docdesk.<your-domain>`) in Route 53, a free public TLS certificate from AWS Certificate Manager (ACM), an Application Load Balancer that terminates HTTPS and forwards to the ECS service, CloudFront in front of it as the CDN, and AWS WAF with AWS managed rules and a rate-based rule. The ECS task loses its public IP: only the load balancer can reach it.
**New layer:** DNS, TLS, the cloud load balancer and the edge (CDN and firewall). **Reuses:** the Block 15 VPC, ECS service and security groups; the Block 13 Nginx, auth and rate limits; the Block 0 picture of the request walk.
**Needs:** Block 15 running. A domain you control: register a cheap one in Route 53 (a domain is charged every year) or use a subdomain of one you already own by delegating it to a Route 53 hosted zone. Nothing to install.
**Architecture so far:**
```
 browser: https://docdesk.<your-domain>
   |  * DNS: Route 53 hosted zone, ALIAS docdesk -> CloudFront
   v
 * CloudFront (HTTPS with an ACM certificate in us-east-1)  + * AWS WAF web ACL
     managed rules (common, known bad inputs, IP reputation) + rate-based rule
   |  HTTPS to the origin  (origin.docdesk.<your-domain> -> ALB)
   v
 * Application Load Balancer (public subnets, sg-alb: 443 from CloudFront)
     listener 443 (ACM certificate in your Region), listener 80 -> redirect to 443
     target group (type ip, port 80, health check /api/health)
   v
 ECS service "docdesk" (private or public subnet, NO public IP; sg-app: 80 from sg-alb only)
   nginx -> ui / api  (Block 15)  ->  RDS (sg-db), S3, secrets
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 16.1 | CNAME vs Alias Records in Route 53 \| Explained with Examples | KnoDAX | https://www.youtube.com/watch?v=R5AnTB5gf1c | length ? | Start | BIKE | A short comparison (2024) of the two ways to point a name at something else in Route 53: what a CNAME and an Alias record are, where each is allowed, and why Alias is the choice for AWS resources such as a load balancer or CloudFront and for the bare domain. A small channel. | verified; description |
| 16.2 | Secure AWS ECS Apps with ALB & SSL/TLS (ACM + Route 53) \| Hands-On AWS Tutorial \| #11 | Learn It Right Way | https://www.youtube.com/watch?v=a7mfpc1BWNY | length ? | Start | DESK | Per its chapters (2025): what TLS and a certificate are, ACM, where the certificate attaches, HTTPS termination at the ALB and the HTTP-to-HTTPS redirect (theory to 09:13), then a hands-on demo with a Fargate service, the ALB, the certificate and a Route 53 record. Episode 11 of a series; you built its starting point (an ECS service behind an ALB) with 15.2. | verified; description |
| 16.3 | Protecting your endpoints with AWS Web Application Firewall (WAF) | Majestic.cloud | https://www.youtube.com/watch?v=RyVfisoZwMQ | length ? | Start | DESK | A 2023 walk-through of AWS WAF as a filter in front of an endpoint: rules against SQL injection, cross-site scripting and other common attacks, attached to an API Gateway in the demo; the same web ACL attaches to CloudFront or an ALB. A smaller channel. | verified; description |
| 16.4 | How to prevent direct access to CloudFront origins with custom headers and AWS WAF | Majestic.cloud | https://www.youtube.com/watch?v=9TlWF0-Ah8Q | length ? | Deeper | DESK | The next step from the same channel (2023): CloudFront adds a secret custom header, and a WAF web ACL on the load balancer or API Gateway blocks every request that lacks it, so nobody can go around the CDN and its firewall. | verified; description |

**Code:** none; this block is console configuration. Keep the AWS hands-on tutorial "How to Register a Domain Name with Amazon Route 53" (https://docs.aws.amazon.com/hands-on/latest/get-a-domain/get-a-domain.html) open for the domain step.
**Optional (extra):** none for this block (the API-gateway concept talk is 13.O2).

**Build it (follow the video):**
1. Watch 16.1 and add to your Block 0 sheet the records you will create: `NS` (who answers for your domain), `CNAME` (name to name, never at the apex), and Route 53 `ALIAS` records for `origin.docdesk` (to the ALB) and `docdesk` (to CloudFront). Run `dig +short example.com A` and `dig +short www.example.com CNAME` on any public site to see real records.
2. Get the name: register a domain in Route 53 following the AWS hands-on tutorial in Code (the hosted zone is created for you), or create a hosted zone for a subdomain such as `aws.<your-existing-domain>` and add its four `NS` records at your current DNS provider. Wait until `dig NS <name>` shows the Route 53 name servers.
3. Watch 16.2 to 09:13 (TLS, ACM, where certificates attach, termination at the ALB, redirect). Then request the ACM certificate in your Region for `docdesk.<domain>` and `origin.docdesk.<domain>` with DNS validation, press "Create records in Route 53", and wait for the status "Issued".
4. The load balancer: go back to 15.2 at 31:07 and follow it to 39:31 with DocDesk (ALB in the public subnets, a target group of type `ip`, the ECS service registered with it, health checks), then follow 16.2's demo from 09:13: an HTTPS listener with your certificate, the HTTP listener redirecting to HTTPS, and a Route 53 Alias record `origin.docdesk` pointing at the ALB. Open `https://origin.docdesk.<domain>` and look at the certificate in the browser.
5. The CDN (no follow-along video was verified for this step, so use the console wizard and the Carry list below): request a second certificate for `docdesk.<domain>` in us-east-1, create a CloudFront distribution with `origin.docdesk.<domain>` as an HTTPS-only custom origin and caching disabled for the app, add `docdesk.<domain>` as an alternate name, and point an Alias record `docdesk` at the distribution. Wait for "Deployed", then open `https://docdesk.<domain>`.
6. Follow 16.3: create a web ACL (for DocDesk, scope CloudFront; the video attaches its ACL to an API Gateway), add AWS managed rule groups, send a request with `?q=' OR 1=1--` and find it in the sampled requests, then add a rate-based rule and watch it trigger with a quick loop of `curl` calls.
7. Follow 16.4: CloudFront adds a secret custom header to every origin request, and the origin rejects requests without it (the video uses a WAF web ACL on the origin; an ALB listener rule that returns 403 does the same job without a second web ACL). Confirm that `https://origin.docdesk.<domain>` called directly now returns 403 while `https://docdesk.<domain>` works.

**Carry it into DocDesk:**
- DNS: a public hosted zone for your domain (or delegated subdomain); write down its four name servers and check them with `dig NS <domain>`.
- Certificates: one ACM certificate for `docdesk.<domain>` and `origin.docdesk.<domain>` in your Region (for the ALB), and one for `docdesk.<domain>` in us-east-1 (CloudFront only accepts certificates from that Region); validate both with DNS records that ACM creates in Route 53 for you.
- ALB: in the public subnets, security group `sg-alb`; a target group of type `ip` on port 80 with health check `/api/health`; listener 443 with the certificate forwarding to the target group, and listener 80 that redirects to 443. Update the ECS service to register with the target group, turn "Assign public IP" off, and change `sg-app` to allow port 80 from `sg-alb` only. If the tasks move to private subnets they need a way to reach ECR, S3, Bedrock and Secrets Manager: VPC endpoints or a NAT gateway (see Cost and teardown).
- Route 53: an ALIAS record `origin.docdesk` pointing at the ALB. Test `https://origin.docdesk.<domain>/` before adding CloudFront.
- CloudFront: a distribution with the ALB (as `origin.docdesk.<domain>`, HTTPS only) as the origin, alternate name `docdesk.<domain>` with the us-east-1 certificate, viewer protocol "Redirect HTTP to HTTPS", and two behaviours: `/api/*` and the Streamlit app paths with caching disabled and all headers, cookies and query strings forwarded (they are per-user and must never be cached; CloudFront passes WebSocket connections through, which Streamlit needs), and only truly static files (if you add any, for example `/static/*`) cached. Then an ALIAS record `docdesk` pointing at the distribution.
- Lock the origin: allow 443 on `sg-alb` only from CloudFront (the AWS-managed prefix list for CloudFront origin-facing addresses), and have CloudFront add a secret custom header that an ALB listener rule checks, so nobody can bypass the edge by calling the ALB directly.
- WAF: a web ACL on the CloudFront distribution with the AWS managed rule groups for common threats, known bad inputs and the IP reputation list, plus a rate-based rule on `/api/` per IP; start the rules in Count mode, read the sampled requests, then switch them to Block. Keep Nginx's and the API's limits from Block 13: three layers, three different jobs.
- Settings: Streamlit and FastAPI behind proxies need to know they are on HTTPS (for example `--forwarded-allow-ips` for uvicorn); check that login redirects and links use `https://docdesk.<domain>`.

**Done when:** `https://docdesk.<your-domain>` shows a valid certificate in the browser, `http://` redirects to `https://`, you can log in and get cited answers; the ALB's own DNS name and the task's former public IP no longer answer from your laptop; `dig docdesk.<domain>` returns CloudFront addresses; and a loop of fast requests to `/api/` from one machine shows up as blocked in the WAF metrics.
**Stretch:** put Amazon API Gateway (an HTTP API with a VPC link to the ALB) in front of `/api/*` instead, with usage plans or a Lambda authorizer, and list what it gave you that the ALB plus WAF did not, and what it cost you (limits, latency, another place for configuration).
**Cost and teardown:** charged while they exist (check each pricing page): the Application Load Balancer is charged "for each hour or partial hour" it runs plus Load Balancer Capacity Units used per minute, with a free-tier allowance for new customers (Elastic Load Balancing pricing page, read 2026-11-17); a NAT gateway, if you add one, is charged per hour available and per gigabyte processed (Block 15); VPC interface endpoints, CloudFront and AWS WAF have their own charges (check their pricing pages before you create them); a Route 53 hosted zone is billed monthly, when it is created and on the first day of each month, not prorated, except that a zone deleted within 12 hours of creation is not charged, and a registered domain is billed per year (Amazon Route 53 pricing page, read 2026-11-17); alias queries to the ALB and to CloudFront are free per the same page. ACM public certificates used with the ALB and CloudFront cost nothing extra (check the ACM pricing page). After each session: scale the ECS service to 0 and stop RDS (Block 15); the ALB still charges while it exists, so delete it if you pause for more than a day or two and recreate it from your notes. At the end of the track: delete the WAF web ACL, the CloudFront distribution (disable, wait, then delete), the ALB and target group, any NAT gateway and VPC endpoints, the ACM certificates, then the Block 15 resources; keep or delete the hosted zone (deleting it stops the monthly charge; the domain renews yearly unless you turn off auto-renew).
**Progression check:** New: DNS records and hosted zones, ACM certificates and DNS validation, the ALB with listeners and target groups, CloudFront behaviours and origins, AWS WAF rules. Reused: the Block 15 service, VPC and security groups (only their rules change), the Block 13 gateway and limits, the Block 0 map. Jump size: medium; five pieces, but each is configuration in front of a service that already works, added in the order a request meets them in reverse (name, certificate, load balancer, CDN, firewall), and each is tested on its own URL before the next.
**Architect's question:** an ALB, Amazon API Gateway and your own Nginx can each route, throttle and check something. For DocDesk in a bank, which one owns TLS, which owns rate limits per client, which owns authentication, and why might the bank's central edge (its own CDN, WAF and API gateway, run by another team) replace CloudFront and WAF entirely?

<details><summary>Recap questions</summary>

1. Q: Why does Route 53 offer ALIAS records when CNAME records exist? A: A CNAME cannot sit at the root of a domain (the zone apex) and costs a lookup; an ALIAS record points a name, including the apex, straight at an AWS resource such as a load balancer or CloudFront, follows its changing addresses, and Route 53 does not charge for those queries.
2. Q: Where is TLS terminated in this design, and why are there two certificates? A: At CloudFront for the browser and again at the ALB for the CloudFront-to-origin hop; CloudFront only uses certificates from us-east-1, while the ALB needs one in its own Region.
3. Q: What does AWS WAF add that the Block 13 Nginx limit does not? A: It runs at the edge before traffic reaches your VPC, uses managed rule groups that AWS maintains against common attacks and bad IP addresses, and applies rate-based rules across all edge locations, while Nginx only sees what already reached your task.

</details>

---

## Block 17: Amazon Bedrock: a third provider, then a managed RAG to compare with yours

**What you build:** Amazon Bedrock as a third model provider behind the Block 6 switch (`DOCDESK_PROVIDER=bedrock`), called with boto3's Converse API from the laptop and then from the ECS task through its role, with no API key at all; then a Bedrock Knowledge Base over the same S3 PDFs, queried side by side with your own Block 8/10 RAG on the same questions, and a short build-versus-buy table you fill in yourself.
**New layer:** managed GenAI services (a model API inside your cloud account, and managed retrieval). **Reuses:** the Block 6 provider switch, the Block 8 questions and `/ask`, the Block 10 pgvector retrieval, the Block 14 bucket and IAM, the Block 15 task role and the Block 16 site.
**Needs:** Block 15 done (Block 16 is not required for the code, only for the public URL). One-time: `pip install -U boto3` (the Converse API needs a recent boto3), and in the Bedrock console for your Region, check that the chat model and the embeddings model you want are available to your account; some model providers ask for a short use-case form the first time. IAM: your admin identity can do everything here; the ECS task role needs `bedrock:InvokeModel` (and `bedrock:InvokeModelWithResponseStream` for streaming) on the chosen model, and `bedrock:Retrieve` / `bedrock:RetrieveAndGenerate` for the Knowledge Base.
**Architecture so far:**
```
 browser -> CloudFront + WAF -> ALB (HTTPS) -> ECS task: nginx -> ui / api        (Blocks 15-16)
                                                   |
                                         get_provider()  <- DOCDESK_PROVIDER     (Block 6)
                                           openai | ollama (laptop) | * bedrock
                                                                        |
                                              * boto3 "bedrock-runtime" converse(modelId, messages, system)
                                                (task role, no key)
   POST /ask          -> your RAG: pgvector on RDS + prompt + provider            (Blocks 8, 10)
 * POST /ask?engine=kb -> * Bedrock Knowledge Base  (boto3 "bedrock-agent-runtime"
                             retrieve / retrieve_and_generate)
                               * data source: S3 bucket docs/   (Block 14)
                               * embeddings model + * vector store (S3 Vectors or Aurora PostgreSQL)
```
**Follow the video:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 17.1 | AWS re:Invent 2025 - Mastering model choice: The 3-step Amazon Bedrock advantage (AIM391) | AWS Events | https://www.youtube.com/watch?v=Vu91YwZxskY | 56:43 | Deeper | BIKE | The product angle on model families and trade-offs: how a team picks among many models (quality, latency, price) and switches between them, with a customer example. Vendor-framed, so keep the criteria and discount the sales parts. | verified; also in Track C 1.5; watch once |
| 17.2 | AI Conversations Made Simple: Overview of Amazon Bedrock Converse API | AWS Developers | https://www.youtube.com/watch?v=wNyih2j0IbE | length ? | Start | DESK | Per its chapters (2024), an AWS developer advocate shows why calling each model in its own request format hurts, then the Converse API as one call for many models, multi-turn conversations and tool use, with code on screen. | verified; description |
| 17.3 | AWS re:Invent 2024 - Build scalable RAG applications using Amazon Bedrock Knowledge Bases (AIM305) | AWS Events | https://www.youtube.com/watch?v=jSlNfr8Uuco | 56:51 | Deeper | BIKE | The AWS product angle on managed enterprise knowledge bases (ingestion, chunking, vector store, retrieval). Content judged from the title only. May be dated: Bedrock Knowledge Bases has changed a lot since Dec 2024. | verified (existence); content per title only; also in Track C 3.5; watch once |
| 17.4 | Build a Full-Stack RAG App with Amazon Bedrock (Knowledge Base & S3 Vectors) - Deploy in AWS Console | Cumulus Cycles | https://www.youtube.com/watch?v=BciUpLuyb3k | length ? | Deeper | DESK | Per its description (2026): a Knowledge Base built in the console over an S3 bucket of documents, with S3 Vectors as the vector store instead of OpenSearch and Titan embeddings, synced and then called from a Lambda function behind API Gateway with a React page. A smaller channel; only the Knowledge Base part is needed here. | verified; description |

**Code:** 17.1 and 17.3: none (talks). 17.2: no repo is linked; the code is short and on screen, and the Converse API pages of the Amazon Bedrock user guide have the same calls. 17.4: the description links a repository under `github.com/CumulusCycles/` that is cut off on the watch page; open it from the description for the console settings, or follow the video.
**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|---|---|---|---|---|---|---|---|
| 17.O1 | Amazon Bedrock Knowledge Bases - how to build RAG on AWS in 2025 | AWS Polska | https://www.youtube.com/watch?v=It769ydwS-k | 1:01:15 | Start | DESK (assumed from title) | A build-along for RAG on Bedrock Knowledge Bases. Regional AWS channel; content and mode judged from the title only. | verified (existence); content per title only; also in Track C 8.D1; watch once |
| 17.O2 | AWS re:Invent 2025 - Bridging from POC to production: An intro to Amazon Bedrock AgentCore (AIM2204) | AWS Events | https://www.youtube.com/watch?v=oDjESsByBmM | 59:01 | Start | BIKE | The map of AgentCore (runtime, identity, gateway, memory and related pieces) from its product lead, an AWS tech lead and an Ericsson customer (Vivek Singh, Mark Roy, Sarbashish Das). Start here for the AWS agent platform. | verified; also in Track C 8.1; watch once |

**Build it (follow the video):**
1. Watch 17.1 on the bike and write five model-choice criteria on your sheet (for example quality on your task, latency, price per thousand tokens, context length, availability in your Region). You will use them to pick DocDesk's Bedrock model.
2. In the Bedrock console, in the Region you chose in Block 14, open the model catalog, pick one chat model and one embeddings model that are available to your account, and try the chat model in the playground with a DocDesk question.
3. Follow 17.2: watch 02:06 to 08:22 to see the problem (every model family has its own request body), then type along from 08:22: `bedrock-runtime` client, `converse(modelId=..., messages=[...], system=[...])`, and the multi-turn part (11:40) where you append the assistant's reply and the next user turn.
4. In a `bedrock_smoke.py` like your Block 1 smoke test, send the same question to two different models by changing only `modelId`, and print `usage` (input and output tokens) and the latency. If a model id is rejected, use the inference profile id the console shows for it.
5. Watch 17.3 for the vocabulary of managed RAG (data source, ingestion and sync, chunking, vector store, retrieve, retrieve and generate) and write next to each word the file or function in your Blocks 7, 8 and 10 code that does the same job.
6. Follow 17.4 for the Knowledge Base part only: an S3 data source, S3 Vectors as the vector store, a Titan embeddings model, "Sync", and a test question in the console. Skip the Lambda, API Gateway and React parts: DocDesk's own API and page play those roles.
7. Call the Knowledge Base from Python: `boto3.client("bedrock-agent-runtime").retrieve_and_generate(...)` with its id and a model ARN, print the answer and each citation's S3 location, then `retrieve(...)` to see the raw chunks and scores.

**Carry it into DocDesk:**
- Add `BedrockProvider` next to `OpenAIProvider` and `OllamaProvider` in `core.py`: `boto3.client("bedrock-runtime").converse(modelId=settings.model, system=[{"text": ...}], messages=[...], inferenceConfig={"maxTokens": ..., "temperature": ...})`. Map your message list to Converse's `{"role", "content": [{"text": ...}]}` shape, read the answer from `output.message.content`, and the token counts from `usage` (`inputTokens`, `outputTokens`) for the cost line. `DOCDESK_PROVIDER=bedrock` with `DOCDESK_MODEL=<model id or inference profile id>`; `/health` shows it.
- Keep the Block 3 contract: ask for the same JSON as before and validate it with the same Pydantic model; if your model supports Converse tool use, you can also pass the schema as a tool, as in Block 11.
- In ECS: add a policy to the task role that allows `bedrock:InvokeModel` on that one model (or inference profile) ARN, set the two settings in the task definition, and remove `OPENAI_API_KEY` from the secrets when Bedrock is the default. Redeploy and check that `/ask` works with no model key anywhere.
- Knowledge Base: create one in the console with your bucket's `docs/` prefix as the S3 data source, an embeddings model, and a quick-create vector store; choose Amazon S3 Vectors (or Aurora PostgreSQL Serverless), not OpenSearch Serverless (see Cost and teardown). Run "Sync", then test it in the console's chat panel.
- Add `docdesk/kb.py` with `kb_ask(question)` calling `boto3.client("bedrock-agent-runtime").retrieve_and_generate(...)` with your Knowledge Base id and model ARN, and returning answer and citations (the S3 URI and the retrieved text) in your `AskResponse` shape; expose it as `POST /ask` with `engine=kb` (default stays `engine=own`). Also try `retrieve(...)` alone and feed its chunks to your own prompt: managed retrieval with your own generation.
- Run your ten Block 8 Stretch questions (question plus expected file and page; write them now if you skipped that Stretch) through `engine=own` and `engine=kb` (same model for both) and fill in `docs/build-vs-buy.md`:

  | | Your RAG (Blocks 8-10) | Bedrock Knowledge Base |
  |---|---|---|
  | Quality (correct answers with correct citations, out of 10) | | |
  | Cost (per question, and fixed monthly pieces) | | |
  | Control (chunking, prompts, filters, where data lives, tests) | | |
  | Effort (hours to build, and to run and change it) | | |
  | Verdict for DocDesk | | |

**Done when:** `DOCDESK_PROVIDER=bedrock` answers `/chat` and `/ask` both on the laptop and on the deployed site with no model API key in any secret; `/ask?engine=kb` returns answers with citations to the same S3 PDFs; and `docs/build-vs-buy.md` has numbers in every cell and a one-paragraph verdict.
**Stretch:** add a Bedrock Guardrail to the Converse call and see which of your questions it blocks (a preview of Block 20); or put a metadata filter on the Knowledge Base query (for example only one PDF) and compare with a `WHERE source = ...` in your own SQL.
**Cost and teardown:** Bedrock models are charged per input and output token on demand (check the Bedrock pricing page for your model and Region); a Knowledge Base adds the embeddings tokens for every sync and the cost of its vector store. Choose the vector store with care: the Amazon OpenSearch Service pricing page (read 2026-11-17) says classic OpenSearch Serverless collections are billed "at least for a minimum of 2 OCUs" for the first collection in an account (half that with the dev-test option), while its newer NextGen collections scale to zero after 10 minutes without traffic. The Bedrock user guide's page on creating a knowledge base (read 2026-11-17) lists Amazon S3 Vectors and Amazon Aurora PostgreSQL Serverless as quick-create vector stores, so pick one of those for this experiment and check its pricing page. Teardown after the comparison: delete the Knowledge Base and its data source, then delete the vector store it created (the S3 vector bucket and index, or the Aurora cluster, which deleting the Knowledge Base does not necessarily remove), and remove the extra IAM permissions. Switch `DOCDESK_PROVIDER` back if you want to stop Bedrock charges, and tear down the Block 15-16 resources as listed there when you pause.
**Progression check:** New: Bedrock model access, the Converse API, IAM permissions for a model, a Knowledge Base (data source, sync, vector store, retrieve and generate). Reused: the provider switch (Block 6), the eval questions and `/ask` (Block 8), pgvector retrieval (Block 10), the bucket (Block 14), the task role (Block 15). Jump size: small for the provider (one more class behind a switch built for this in Block 6), medium for the Knowledge Base, which is a managed version of what you built in Blocks 7, 8 and 10, so every setting in its console has a name you already know.
**Architect's question:** build or buy? Your own RAG gives you control over chunking, prompts, filtering and tests; the Knowledge Base gives you less code to run and AWS's roadmap. For a bank, weigh where the data and embeddings live, how you test and explain a retrieval result to an auditor, what happens when the managed service changes its defaults, and how hard it is to leave. Which parts of DocDesk would you buy, and which must stay yours?

<details><summary>Recap questions</summary>

1. Q: What does Bedrock's Converse API give you over calling each model's own request format? A: One request and response shape (system prompt, messages, inference settings, tool use, usage counts) for all supported models, so switching models is a change of model id instead of new code.
2. Q: How does the ECS task call Bedrock without an API key? A: Its task role has an IAM policy that allows `bedrock:InvokeModel` on the chosen model; boto3 in the container gets temporary credentials for that role automatically, and every call is signed and logged in CloudTrail.
3. Q: What does a Bedrock Knowledge Base do for you, and what does it still need from you? A: It reads the documents from the data source, chunks and embeds them, stores the vectors in a vector store, and retrieves (and optionally generates) at query time; you still choose the data, the embeddings model, the vector store and its cost, the chunking settings, the prompt, and you still have to evaluate the answers.

</details>

<!-- Pages to check (Blocks 13-17): every new row's watch page was read (oEmbed was refused by the fetch allowlist again; title and channel come from the watch-page metadata); YouTube rate-limited the fetch tool for long stretches, so several candidates could not be read. Kept rows whose page title matched the search result. Skipped because the page returned did not match the searched title or ID: VL9DNCDzJBY (search title "NGINX Explained"; the page read was "NGINX Explained | Reverse Proxy & Load Balancer (Complete Guide)", SYA Academy), bVjwu1WN42I (search "Set Up AWS IAM Identity Center"), iF9fs8Rw4Uo (search "AWS Identity and Access Management (IAM) Basics"), 7r2z3Qn3Qz8 and O3LCsq1g0GU (search "How to Use Python with AWS S3"), uzgJmnIR9qs (search "CloudFront with ALB as Custom Origin with SSL"). Read but not used: 7aOb0vZHT5k ("AWS Free Tier and the New AWS Experience", 2026; the page did not name the channel, only links to AWS Developers), TllCWtY7zRc (page title "AWS re:Invent 2025 - Launch web applications in seconds with Amazon ECS Express Mode (CNS379)", AWS Events; the search title differed slightly). Could not be read: oBJFf2VSizo, uM_yxhXn9ts, wzHH7FbBb9E, IHcYmNsJCuo, iWcS3q6Kwys, 8Fwrdlvqk2M, vv3tjd9ASyU, DL3fJMD-CRI, 3e_9JqPd7U4, YKT9bWvy_PI, 6-fhKSzePRc, QjQFN6qG5jk, YmZPqPEBUkY, JRZiQFVWpi8, vxvgpDZOuYw. Gap: no CloudFront follow-along (CloudFront with an ALB origin) was verified for Block 16; IHcYmNsJCuo, 6-fhKSzePRc, QjQFN6qG5jk and YmZPqPEBUkY are the candidates to re-check. Repos were checked with git ls-remote and a shallow clone (last commit date). -->

<!-- BLOCKS GO HERE -->
