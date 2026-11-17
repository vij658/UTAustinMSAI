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

<!-- BLOCKS GO HERE -->
