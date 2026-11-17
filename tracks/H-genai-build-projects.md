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

<!-- BLOCKS GO HERE -->
