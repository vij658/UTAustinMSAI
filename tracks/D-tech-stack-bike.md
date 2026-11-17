# Track D: Enterprise tech stack (bike path)

A watch-while-biking ladder for the general enterprise technology stack that sits UNDER the GenAI stack in Track C: backend architecture, data, cloud platform, security, reliability and the ML platform, plus the judgement to choose between them. It is for someone who already knows enterprise Java and identity well, so beginner Java/Spring content is left out, and the blocks where you are expert (security and identity) are marked "fast lane" and kept short. It is not frontend or mobile, and it is not AWS service-by-service (you cover AWS at the desk); where a cloud is named it is only an example.

**Order logic.** Block 0 gives the vocabulary and how to read a system diagram. Block 1 (distributed systems fundamentals) is the physics under every later block: replication, partitioning, consistency, failure and time. Block 2 (the data layer) uses those ideas to explain why each store behaves the way it does. Block 3 (APIs, messaging and integration) builds on Blocks 1-2: sagas and outboxes exist because you cannot have one transaction across services. Block 4 (cloud-native platform) is what runs all of that. Block 5 (security and identity, a fast lane for you) and Block 6 (reliability and observability) are cross-cutting: they apply to every layer above. Block 7 (data and ML platform) is the bridge to Track C, and Block 8 (architecture judgement and case studies) is the capstone, ending in a design review of a whole stack. Inside each block, an intuition or overview talk comes before the deeper lecture.

**Table legend.**
- Level: Start / Deeper / Scholar. Scholar is used only in the optional lists.
- Mode: BIKE = works mostly by listening (some need a glance at slides). DESK = needs code, paper, or pausing. Every main-path video is BIKE; DESK items appear only in optional lists.
- Status "verified" means the YouTube oEmbed endpoint returned the exact video ID I asked for, with the title and channel shown (copied as returned). It does not mean I watched the video. After "verified" the Status says what the "What you will get" sentence is based on: the YouTube watch-page description or chapter list, a named third-party page (conference, InfoQ, ScyllaDB, AWS and similar), or the title only.
- Length: read from the video's YouTube page on 2026-11-16 or 17 (no cookies, nothing played).
- "What you will get" is one sentence in my own words, based only on the source named in Status. I have not watched any of these videos.
- Dated material is flagged in the sentence (talks from 2012-2018 are named by year); the concepts mostly hold, product details may not.

**Honest accounting.** The track has 53 main BIKE videos (Blocks 0-4: 30, Blocks 5-8: 23) and 32 optional videos (20 in Blocks 0-4, 12 in Blocks 5-8). Nothing was watched. All 53 main videos and all 32 optional videos have a measured length, read from the YouTube pages on 2026-11-16: 33 h 35 m for the main path and 22 h 35 m for the optional lists. Many rows rest on the title alone because the YouTube watch pages could not always be read; the Gaps and Not checked sections at the end list them. The companion hands-on path for this stack is Track E (DESK).

**Mode balance.** All 53 main videos are BIKE. Three optional videos are DESK (1.O4, 2.O2, 6.O4); everything else in the optional lists is BIKE. The longer or slide-heavy videos say so in their row.

---

## Block 0: Stack map and vocabulary

**Why it matters for the stack:** every later block is one layer of one system, and an architect needs the shared words (monolith, microservice, event-driven, container, component) and the habit of reading a diagram for boundaries before judging any technology.

The layer map below is my own framing for this track, not taken from a video. Track C's ten GenAI layers (data, embeddings, retrieval, agents, model hosting and so on) sit on top of it.

| # | Layer | One-line job |
|---|-------|--------------|
| 1 | Edge and API | Gateway, routing, rate limits, authentication at the door |
| 2 | Services and workflows | Business logic as a monolith, modules or microservices; synchronous calls and asynchronous events |
| 3 | Messaging and streaming | Queues and logs that decouple services in time |
| 4 | Data stores | Relational, NoSQL, cache, search, object storage: system of record versus derived copies |
| 5 | Analytics and ML platform | Warehouse or lakehouse, feature and training pipelines, model serving (Block 7) |
| 6 | Platform and runtime | Containers, orchestration, infrastructure as code, networks, regions |
| 7 | Security and identity (cross-cutting) | Authentication, authorisation, secrets, encryption, audit (Block 5) |
| 8 | Reliability and observability (cross-cutting) | SLOs, tracing, failover, capacity (Block 6) |

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 0.1 | The C4 Model: Visualizing Software Architecture • Simon Brown & Susanne Kaiser • GOTO 2026 | GOTO Conferences | https://www.youtube.com/watch?v=sfqHggWY5Ds | 27:35 | Start | BIKE | How to read an architecture diagram as levels (context, containers, components, code), why you usually need only the first two, and how team-owned services are drawn; Brown stresses the shared vocabulary over the notation. | verified; content per watch-page description and chapters |
| 0.2 | When To Use Microservices (And When Not To!) • Sam Newman & Martin Fowler • GOTO 2020 | GOTO Conferences | https://www.youtube.com/watch?v=GBTdnfD6s5Q | 38:44 | Start | BIKE | A conversation on when microservices are worth it, why not to make them a default, how to avoid a distributed monolith, independent deployment, and what to do about teams and data. | verified; content per watch-page description and chapters |
| 0.3 | The Many Meanings of Event-Driven Architecture • Martin Fowler • GOTO 2017 | GOTO Conferences | https://www.youtube.com/watch?v=STKCRSUsyP0 | 50:06 | Deeper | BIKE | Per the title, a talk that separates the several different things people mean by "event-driven", so you can ask which one a design is using. I did not read a description. | verified; title-based |
| 0.4 | Jessica Tai - How to Tame Your Microservices: Evolving Airbnb’s Architecture | ScaleConf | https://www.youtube.com/watch?v=4Qiba4isie4 | 36:50 | Deeper | BIKE | Case study (2020): Airbnb's migration to microservices worked, then hundreds of services produced a dependency graph too complicated to scale or change, and the talk shows how the read path is being re-architected. | verified; content per watch-page description |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 0.O1 | Lesson 93 - What is Software Architecture | Software Architecture Monday | https://www.youtube.com/watch?v=U6rfJjd8714 | 6:21 | Start | BIKE | A short lesson from Mark Richards' series on what "software architecture" means; the closest verified vocabulary video I found for the stack-map idea (see Gaps to be written). Watch page could not be read. | verified; title-based |
| 0.O2 | Modular Monoliths • Simon Brown • GOTO 2018 | GOTO Conferences | https://www.youtube.com/watch?v=5OjqD-ow8GE | 46:32 | Deeper | BIKE | Brown's argument that the design thinking behind good microservices is the same as for a well-structured monolith: modularity, boundaries, organising code by feature, and the gap between diagram and code. | verified; content per watch-page description and chapters |
| 0.O3 | Microservices, Where Did It All Go Wrong • Ian Cooper • GOTO 2024 | GOTO Conferences | https://www.youtube.com/watch?v=j2AQ9eTZ3-0 | 43:36 | Deeper | BIKE | A critical look at how microservices went wrong in practice, to pair with 0.2. I did not read a description. | verified; title-based |
| 0.O4 | Enterprise Architecture = Architecting the Enterprise? • Gregor Hohpe • YOW! 2018 | GOTO Conferences | https://www.youtube.com/watch?v=XiM3Chty94w | 1:03:28 | Deeper | BIKE | The role of enterprise architecture in a large company, from the author of The Architect Elevator (author link is my own background knowledge); watch page could not be read. | verified; title-based |

**Feeds:** Track C Block 0 (Big picture: the GenAI stack map is this same enterprise picture with a probabilistic component added) and Track C Block 9 (Enterprise architecture and operating at scale).

**Full circle:** you can look at any system diagram and say what each box owns, where the boundaries are, which arrows are synchronous calls and which are events, and whether the design is a monolith, a set of microservices or something in between; and you can say which "event-driven" is meant.

**Architect's question:** Which of these boxes is owned by which team, and which data does each box own?

<details>
<summary>Recap questions (3)</summary>

1. Q: What are the levels of the C4 model, and which two should you draw first? A: System context, containers, components and code; start with context and containers because they change slowly and are quick to draw.
2. Q: What is a "distributed monolith"? A: Services that are deployed separately but are so tightly coupled (shared data, lockstep releases) that you pay the cost of microservices without getting independent deployment.
3. Q: Why is "we use event-driven architecture" an incomplete statement? A: The phrase covers different patterns (for example, a notification that something happened versus events as the system's source of truth), with very different consequences, so you have to ask which one is meant.
</details>

---

## Block 1: Distributed systems fundamentals

**Why it matters for the stack:** replication, partitioning, consistency, failure and time are the reasons databases, queues and microservices behave the way they do, and every trade-off in Blocks 2-8 is one of these ideas in disguise.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.1 | Kyle Kingsbury - Call Me Maybe: Carly Rae Jepsen and the Perils of Network Partitions (RICON2013) | RICON | https://www.youtube.com/watch?v=vFDjTd9G6Xo | 38:49 | Start | BIKE | Per the description, what network partitions do to real systems, the ways important data gets lost, and why reliable behaviour under partitions is hard. A 2013 talk, so the databases tested are dated; the failure thinking is not. | verified; content per watch-page description |
| 1.2 | "How NOT to Measure Latency" by Gil Tene | Strange Loop Conference | https://www.youtube.com/watch?v=lJ8ydIuPFeU | 42:59 | Deeper | BIKE | Per the description, the common mistakes in measuring latency and response time and why badly measured data misleads; expect charts, so glance at the screen. | verified; content per watch-page description |
| 1.3 | Distributed Systems 5.1: Replication | Martin Kleppmann | https://www.youtube.com/watch?v=mBUCF1WGI_I | 25:20 | Deeper | BIKE | A lecture on replication from Kleppmann's Cambridge distributed-systems course (slides; the description is only course boilerplate and links to lecture notes). | verified; title and course notes |
| 1.4 | What is CONSISTENT HASHING and Where is it used? | Gaurav Sen | https://www.youtube.com/watch?v=zaRkONvyGr8 | 10:50 | Start | BIKE | Why plain hashing breaks when servers are added or removed, then consistent hashing and virtual servers as the way to partition load; chapters run from request hashing to applications. | verified; content per watch-page description and chapters |
| 1.5 | Latency and Consistency Tradeoffs in Modern Distributed Databases | ScyllaDB | https://www.youtube.com/watch?v=vnXXFpySYVE | 47:17 | Deeper | BIKE | A vendor webinar on PACELC, the extension of CAP, and how consistency trades against latency even when nothing is partitioned. ScyllaDB's page names Daniel Abadi but does not state who presents, and it mentions their cloud product, so expect some product talk. | verified; content per ScyllaDB webinar page |
| 1.6 | Distributed Systems 6.1: Consensus | Martin Kleppmann | https://www.youtube.com/watch?v=rN6ma561tak | 18:14 | Deeper | BIKE | Lecture 6.1 on getting machines to agree, in Kleppmann's Cambridge course (the matching notes section is "Introduction to consensus"). Slides, so glance. | verified; title and course notes |
| 1.7 | Distributed Systems 3.3: Causality and happens-before | Martin Kleppmann | https://www.youtube.com/watch?v=OKHIdpOAxto | 16:24 | Deeper | BIKE | How to order events across machines without a shared clock (the matching notes section is "Causality and happens-before"); slides, so glance. | verified; title and course notes |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.O1 | Distributed Systems 1.1: Introduction | Martin Kleppmann | https://www.youtube.com/watch?v=UEAMfLPZZhE | 14:35 | Start | BIKE | The opening lecture of the same course (notes section "About distributed systems"); watch it first if the vocabulary is rusty. Watch page could not be read. | verified; title and course notes |
| 1.O2 | Distributed Systems 7.2: Linearizability | Martin Kleppmann | https://www.youtube.com/watch?v=noUNH3jDLC0 | 18:43 | Deeper | BIKE | The strong-consistency lecture to follow 1.5; the course notes did not mention the CAP theorem in what I read, so do not expect it here. | verified; title and course notes |
| 1.O3 | "Raft - The Understandable Distributed Protocol" by Ben Johnson (2013) | Strange Loop Conference | https://www.youtube.com/watch?v=ro2fU8_mr2w | 36:32 | Deeper | BIKE | A second, algorithm-level view of consensus after 1.6, using Raft. 2013 talk; I did not read a description. | verified; title-based |
| 1.O4 | Lecture 1: Introduction | MIT 6.824: Distributed Systems | https://www.youtube.com/watch?v=cQP8WApzIQQ | 1:19:35 | Scholar | DESK | The first lecture of MIT's graduate distributed-systems course; a full university lecture that assumes you will code the labs. I did not read a description. | verified; title-based |

**Feeds:** Track C Block 4 (Agents and tools: durable execution, retries and idempotent tools are failure and consistency problems), Track C Block 7 (Customization and serving: replication, partitioning and tail latency decide serving capacity and cost) and Track C Block 3 (vector indexes are partitioned and replicated like any other data).

**Full circle:** you can explain why two copies of the same data can disagree, how a system decides which copy wins, what it costs in latency or availability to prevent that, and why "ordering" cannot rely on wall clocks. The same trade-off shows up in an authentication decision that must see a just-revoked credential everywhere.

**Architect's question:** Where do we need strong consistency, and what does it cost us in latency and availability?

<details>
<summary>Recap questions (3)</summary>

1. Q: Why is an average latency number a poor way to describe a service? A: Users feel the slow tail, not the mean; you need percentiles measured under realistic load, and careless measurement can hide the worst delays.
2. Q: What does PACELC add to CAP? A: CAP only speaks about behaviour during a partition (choose consistency or availability); PACELC adds that, Else (no partition), you still trade latency against consistency.
3. Q: Why can't machines order events by comparing their clocks, and what is used instead? A: Clocks drift and cannot be perfectly synchronised, so wall-clock order can be wrong; systems use causal ordering (happens-before, logical clocks) or consensus to agree on an order.
</details>

---

## Block 2: The data layer

**Why it matters for the stack:** most enterprise architecture arguments are really about where data lives, which copy is the truth, and which copies are derived and rebuildable.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.1 | Database Indexing Explained (with PostgreSQL) | Hussein Nasser | https://www.youtube.com/watch?v=-qNSXK7s7_w | 18:18 | Start | BIKE | Fast lane: what an index is and how it speeds a query, with PostgreSQL demos of when an index helps and when it does not (query demos are on screen; the point comes through by ear). | verified; content per watch-page description and chapters |
| 2.2 | Introduction to NoSQL • Martin Fowler • GOTO 2012 | GOTO Conferences | https://www.youtube.com/watch?v=qI_g07C_Q5I | 54:51 | Start | BIKE | Per a Class Central description: the history and the four data models (key-value, document, column-family, graph), consistency and the CAP theorem, and when to use them. 2012 talk; product names are dated, the families are not. This is also the closest verified item for "choosing a store". | verified; content per Class Central description |
| 2.3 | "Caching at Netflix: The Hidden Microservice" by Scott Mansfield | Strange Loop Conference | https://www.youtube.com/watch?v=Rzdxgx3RC0Q | 35:22 | Deeper | BIKE | Case study (2016): per the conference page, how Netflix built its caching tier (EVCache, a client library, Rend and Memcached) into a low-latency data layer for stateless services, not just a cache. | verified; content per Strange Loop page |
| 2.4 | Alex Brasetvik - Elasticsearch from the bottom up | EuroPython Conference | https://www.youtube.com/watch?v=LDyxijDEqj4 | 36:53 | Start | BIKE | Per the conference page, the inverted index first, then how Elasticsearch and Lucene build up to a distributed search cluster. A 2014 talk, so version details are dated; the inverted-index idea is what Track C's hybrid search builds on. May include live demos. | verified; content per pyvideo page |
| 2.5 | "Turning the database inside out with Apache Samza" by Martin Kleppmann | Strange Loop Conference | https://www.youtube.com/watch?v=fU9hR3kiOK0 | 47:42 | Deeper | BIKE | Per Kleppmann's own write-up: an append-only log of events as the source of truth (Kafka as one implementation), with indexes, caches and materialised views seen as derived data built by stream processing. 2014 talk. | verified; content per the author's page |
| 2.6 | Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics | CIDR DB | https://www.youtube.com/watch?v=RU2dXoVU8hY | 9:59 | Deeper | BIKE | The warehouse versus data-lake versus "lakehouse" argument, from the conference paper by four Databricks authors (open file formats such as Parquet, ML directly on the data). A vendor-side argument; who presents the video was not confirmed, and the watch page could not be read. | verified; content per CIDR paper abstract |
| 2.7 | AWS re:Invent 2023 - Netflix’s journey to an Apache Iceberg–only data lake (NFX306) | AWS Events | https://www.youtube.com/watch?v=jMFMEk8jFu8 | 51:51 | Deeper | BIKE | Case study (2023): Netflix engineers on moving a very large data lake from Hive to Apache Iceberg, the custom tooling, how migration was kept low-disruption, and the gains (ACID transactions, faster queries). AWS-hosted session, but the content is about the table format. | verified; content per AWS video page |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.O1 | Apache Kafka: What it is and where it’s going. | Confluent Developer | https://www.youtube.com/watch?v=9CrlA0Wasvk | 10:32 | Start | BIKE | A gentler vendor-channel introduction to Kafka before or after 2.5. I did not read a description. | verified; title-based |
| 2.O2 | 08 - B+Tree Indexes (CMU Intro to Database Systems / Fall 2022) | CMU Database Group | https://www.youtube.com/watch?v=9QPr8Ufzt5M | 1:22:47 | Scholar | DESK | A full university lecture on how B+tree indexes work inside the database, if 2.1 left you wanting the internals. I did not read a description. | verified; title-based |
| 2.O3 | NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence | OnSoftware | https://www.youtube.com/watch?v=ip7Xbwhl1s4 | 15:21 | Start | BIKE | Title-level match for "polyglot persistence" (using different stores for different jobs) to go with 2.2. The channel is small and I did not vet the content. | verified; title-based |
| 2.O4 | AWS re:Invent 2021 - How Netflix operates mission-critical data stores on AWS | AWS Events | https://www.youtube.com/watch?v=MtGYgilaPgo | 1:03:28 | Deeper | BIKE | A second Netflix case study, on running its critical databases at scale. I did not read a description. | verified; title-based |

**Feeds:** Track C Block 3 (Embeddings, vector search and RAG: the inverted index and search clusters in 2.4 are the keyword half of hybrid search, and vector indexes are another derived store), Track C Block 7 (Customization and serving: caching is a cost lever) and Track C Block 5 (evaluation data and traces are just more data in this layer).

**Full circle:** you can say which store is the system of record and which are derived and rebuildable (cache, search index, warehouse), name the four NoSQL families and when each fits, and explain a log-centred design where everything else is built from the log.

**Architect's question:** Which store is the system of record here, which stores are derived, and how do we rebuild a derived store when it is wrong?

<details>
<summary>Recap questions (3)</summary>

1. Q: Name two costs of adding an index. A: Slower writes (every insert and update also maintains the index) and extra storage; an index on a low-selectivity column may not help reads at all.
2. Q: Why does the "inside out" view treat caches, search indexes and materialised views as derived data? A: They can all be rebuilt by replaying the ordered log of changes, so the log is the source of truth and the others are disposable views of it.
3. Q: In one sentence each, how do a warehouse, a data lake and a lakehouse differ? A: A warehouse holds curated structured data with managed storage and fast SQL; a lake holds raw files cheaply with structure applied on read; a lakehouse puts open table formats (such as Iceberg) on lake storage to add transactions and warehouse-style performance.
</details>

---

## Block 3: APIs, messaging and integration

**Why it matters for the stack:** services are only as independent as their contracts and failure behaviour; this block is how systems talk, what happens when a call or a message goes wrong, and how a business transaction survives without a distributed transaction.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.1 | gRPC Crash Course - Modes, Examples, Pros & Cons and more | Hussein Nasser | https://www.youtube.com/watch?v=Yw4rkaTc0f8 | 1:19:38 | Start | BIKE | The motivation for gRPC (HTTP/2 and Protocol Buffers), its four call modes, then pros and cons (schema dependence, thick clients, no native browser support). A coding demo runs from 19:49 to 57:00, so skim or skip that part and split the rest over two rides. | verified; content per watch-page description and chapters |
| 3.2 | How Netflix Scales Its API with GraphQL Federation | InfoQ | https://www.youtube.com/watch?v=QrEOvHdH2Cg | 38:50 | Deeper | BIKE | Case study: two Netflix API engineers on consolidating the API layer with federated GraphQL, how the federation architecture works, and how it serves consumer and studio apps. | verified; content per InfoQ page |
| 3.3 | I Made Everything Loosely Coupled. Does My App Fall Apart? • Gregor Hohpe • GOTO 2022 | GOTO Conferences | https://www.youtube.com/watch?v=w9a7eI6BlVc | 48:10 | Deeper | BIKE | Per the GOTO page: the trade-offs of system integration (messages versus events, integration patterns, whether loose coupling is always good) and the hard parts that remain: partial failure, eventual consistency and idempotency. | verified; content per GOTO page |
| 3.4 | Rethinking Microservices with Stateful Streams • Ben Stopford • GOTO 2017 | GOTO Conferences | https://www.youtube.com/watch?v=6lONG_F76To | 40:25 | Deeper | BIKE | Per the GOTO page: why service interactions get tangled as they grow, and a proposal to build event-driven services on a distributed log such as Kafka. A Confluent speaker, so a log-vendor's view; use it for the queue-versus-log idea. | verified; content per GOTO page |
| 3.5 | Not Just Events: Developing Asynchronous Microservices • Chris Richardson • GOTO 2019 | GOTO Conferences | https://www.youtube.com/watch?v=kyNL7yCvQQc | 50:37 | Deeper | BIKE | Per the GOTO page: cross-service transactions as sagas (a chain of local transactions coordinated by events or commands) and CQRS to keep queryable replicas. The page does not mention the outbox pattern, so I cannot say whether it is covered. | verified; content per GOTO page |
| 3.6 | Modern Banking in 1500 Microservices | InfoQ | https://www.youtube.com/watch?v=t7iVCIYQbgk | 50:59 | Deeper | BIKE | Case study from a bank: Monzo engineers on how roughly 1,500 microservices are created, run, monitored and combined into features, with culture, deployment and incident tooling, and observability. | verified; content per InfoQ page |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.O1 | API Gateway Pattern & Kong in a Microservices World | The Linux Foundation | https://www.youtube.com/watch?v=OUUiS28hZuw | 41:45 | Deeper | BIKE | The only API-gateway concept talk I verified; it is a vendor (Kong) talk, judged from the title only, so keep the pattern and discount the product. | verified; title-based |
| 3.O2 | Event Sourcing • Greg Young • GOTO 2014 | GOTO Conferences | https://www.youtube.com/watch?v=8JKjvY4etTY | 54:24 | Deeper | BIKE | The event-sourcing talk usually cited alongside CQRS, to deepen 3.5. I did not read a description. | verified; title-based |
| 3.O3 | Beyond Microservices: Streams, State & Scalability • Gwen Shapira • GOTO 2020 | GOTO Conferences | https://www.youtube.com/watch?v=H0LUi51aCP8 | 36:35 | Deeper | BIKE | A second streaming-and-state view of microservices from a Confluent speaker, after 3.4. I did not read a description. | verified; title-based |
| 3.O4 | What is a REST API? | IBM Technology | https://www.youtube.com/watch?v=lsMQRaeKNDk | 9:12 | Start | BIKE | Fast lane: a short REST refresher, probably familiar to you; included so the REST, gRPC and GraphQL comparison has its third corner. | verified; title-based |

**Feeds:** Track C Block 4 (Agents and tools: a tool definition is an API contract, MCP is an integration protocol, and durable execution is the same problem as a saga) and Track C Block 9 (Enterprise architecture and operating at scale: the LLM gateway is the API-gateway pattern applied to models). Also Track C Block 6 (every extra tool call is an extra integration to secure).

**Full circle:** you can choose between a synchronous API style and an asynchronous message for a given interaction, say what happens when a message is delivered twice, late or never, explain how a saga replaces a distributed transaction, and say when a log beats a queue.

**Architect's question:** What happens to the business transaction if this message is delivered twice, delivered late, or never delivered?

<details>
<summary>Recap questions (3)</summary>

1. Q: Why can't a business process that spans several services use one ACID transaction, and what is used instead? A: Each service owns its own database, so there is no shared transaction; a saga runs a sequence of local transactions and undoes completed steps with compensating actions if a later step fails, accepting eventual consistency.
2. Q: What is the dual-write problem that an outbox is meant to solve? A: Updating a database and publishing a message are two separate operations that can fail independently; an outbox writes the event in the same database transaction as the change and a separate relay publishes it (this answer is general knowledge, because no page I read confirmed the outbox in these videos).
3. Q: When would you pick gRPC, GraphQL or REST? A: gRPC for typed, efficient service-to-service calls and streaming (but weak browser support and schema coupling); GraphQL when clients need to pull varied data from many backends in one request (federation helps); REST for simple, broadly consumable resource APIs.
</details>

---

## Block 4: Cloud-native platform

**Why it matters for the stack:** containers, orchestration and automation are how every service in Blocks 2-3, and later every model server in Track C, actually runs, scales and fails over.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.1 | Containers From Scratch • Liz Rice • GOTO 2018 | GOTO Conferences | https://www.youtube.com/watch?v=8fi7uSYlOdc | 42:53 | Start | BIKE | Per the GOTO page: what a container really is (are they "lightweight VMs"?), how namespaces and control groups work, shown by live-coding a basic container in Go. The concept comes through by ear; glance at the screen for the code. | verified; content per GOTO page |
| 4.2 | Keynote: Kubernetes by Kelsey Hightower, Staff Developer Advocate, Google | CNCF [Cloud Native Computing Foundation] | https://www.youtube.com/watch?v=8SvQqZNP6uo | 15:08 | Deeper | BIKE | A 2016 keynote that, per its description, presents Kubernetes as small components connected by one unified API and as a framework for building distributed systems, not just an app-management tool. This is the concept view, not a setup lab. | verified; content per watch-page description |
| 4.3 | Infrastructure as Actual Code • Gregor Hohpe • YOW! 2022 | GOTO Conferences | https://www.youtube.com/watch?v=uzc6p3qvH_k | 59:12 | Deeper | BIKE | Per the description: cloud automation as part of the delivery lifecycle, and the blurring line between application code and automation code. The speaker was at AWS and uses AWS CDK as the example, which is only one way to do the idea. | verified; content per watch-page description |
| 4.4 | The Service Mesh: Past, Present, and Future [B] - William Morgan, Buoyant | CNCF [Cloud Native Computing Foundation] | https://www.youtube.com/watch?v=2trOvMUuLkk | 35:56 | Deeper | BIKE | Per the title, a service-mesh overview from a mesh vendor's founder (the Linkerd side). Watch page could not be read, so I cannot say how much is history and how much is design. | verified; title-based |
| 4.5 | Where We’re Going, We Don’t Need Servers! • Sam Newman • GOTO 2020 | GOTO Conferences | https://www.youtube.com/watch?v=Mz-b-rQ9wL0 | 50:10 | Deeper | BIKE | Per the GOTO page: a critical look at the hype around microservices and serverless, why functions-as-a-service is powerful, how serverless and microservices fit together, and how to adopt it incrementally. | verified; content per GOTO page |
| 4.6 | AWS re:Invent 2018: Architecture Patterns for Multi-Region Active-Active Applications (ARC209-R2) | Amazon Web Services | https://www.youtube.com/watch?v=2e29I3dA8o4 | 58:37 | Deeper | BIKE | Per the title, patterns for running one application in several regions at once; AWS is the example cloud and the data-replication trade-offs apply anywhere. A 2018 session, and I could not read its page. | verified; title-based |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.O1 | Code to Current Account: A Tour of the Monzo Infrastructure | HashiCorp, an IBM Company | https://www.youtube.com/watch?v=i2eLhGeUslM | 20:36 | Deeper | BIKE | Case study from a bank: by title, the path from code to a running current account on Monzo's infrastructure. The watch page could not be read, so content is title-based. | verified; title-based |
| 4.O2 | On the Origin of Platforms: Evolution of a Capital One Enterpris... Bradley Whitfield & Jacob Walden | CNCF [Cloud Native Computing Foundation] | https://www.youtube.com/watch?v=BY-mQH9VKAo | 32:42 | Deeper | BIKE | A large US bank's internal platform story (title is cut off in the oEmbed result), relevant to how an enterprise runs shared platforms. I did not read a description. | verified; title-based |
| 4.O3 | AWS re:Invent 2023 - How Netflix uses AWS for multi-Region cache replication (NFX304) | AWS Events | https://www.youtube.com/watch?v=85TiFrDhCR4 | 59:17 | Deeper | BIKE | A multi-region case study at the cache layer; pair with 4.6. I did not read a description. | verified; title-based |
| 4.O4 | AWS re:Invent 2023 - Backup and disaster recovery strategies for increased resilience (ARC208) | AWS Events | https://www.youtube.com/watch?v=E073XISxrSU | 46:10 | Deeper | BIKE | Per the description: backup and disaster-recovery strategies, recovery point and time objectives of seconds and minutes, and ransomware recovery. Heavily about AWS Elastic Disaster Recovery, so use it for the vocabulary (RPO, RTO), not the product. | verified; content per watch-page description |

**Feeds:** Track C Block 7 (Customization and serving: model servers run in containers on an orchestrator, and autoscaling and GPU capacity are platform questions that set cost), Track C Block 8 (AWS GenAI specifically: the managed services are this platform with a model attached) and Track C Block 9 (Enterprise architecture and operating at scale: multi-region and failover for a model gateway).

**Full circle:** you can explain a container as a process with isolated views of the host, Kubernetes as a control loop that reconciles declared state to actual state, infrastructure as code as reviewable and repeatable change, when a mesh or serverless is worth its cost, and what recovery point and recovery time mean when a region fails.

**Architect's question:** If this region disappeared right now, what are our recovery time and recovery point, and when did we last test it?

<details>
<summary>Recap questions (3)</summary>

1. Q: How does a container differ from a virtual machine? A: A container is an ordinary process isolated by kernel features (namespaces for what it can see, control groups for what it can use) and shares the host kernel; a VM runs its own kernel on virtual hardware.
2. Q: What does the Kubernetes control loop do? A: You declare the desired state through the API, and controllers continually compare it with the actual state and act to close the gap (restart, reschedule, scale).
3. Q: What is the difference between RPO and RTO, and what makes active-active hard? A: RPO is how much data loss is tolerable and RTO is how long an outage is tolerable; active-active gives the fastest failover but needs replicated data and a plan for write conflicts across regions.
</details>

---

## Block 5: Security and identity (fast lane)

**Why it matters for the stack:** every layer in Blocks 1-4 needs an answer to "who is calling, what may they do, and what happens to the data on disk and on the wire". You already know enterprise identity and banking controls well, so this block is a FAST LANE: four videos, to fix the shared vocabulary (OAuth2/OIDC, zero trust, threat modelling, compliance by automation) and to see them from the architect's side rather than the implementer's. Secrets, KMS and encryption at rest and in transit have no strong main-path video (see Gaps); the optional list has the closest ones.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.1 | OAuth and OpenID Connect in Plain English • Nate Barbettini • GOTO 2020 | GOTO Conferences | https://www.youtube.com/watch?v=sSy5-3IkXHE | 18:44 | Start | BIKE | Fast lane: per the chapters, why OAuth exists (delegated authorisation), the flow vocabulary, how OpenID Connect adds identity on top, and current practice. You will know most of it; use it to check that your words match the common ones. | verified; content per watch-page description and chapters |
| 5.2 | Google on BeyondCorp: Empowering Employees with Security for the Cloud Era | RSAC Cybersecurity | https://www.youtube.com/watch?v=34VTSI_vgI0 | 40:27 | Deeper | BIKE | Fast lane: per the RSA Conference session page, Google's zero-trust model (treat every network as untrusted, work from any device without a VPN) with device trust and security keys; speaker Jennifer Lin, Google Cloud, 2018. Google's own account of where zero trust started. | verified; content per RSA Conference session page and Class Central description |
| 5.3 | Threat Modeling and The Four Question Framework - Adam Shostack | CyberRisk TV | https://www.youtube.com/watch?v=-OBgxD_Zhdw | 17:18 | Start | BIKE | Fast lane: an interview in which Shostack covers the history of threat modelling, his Four Question Framework and how it can fit inside organisations in the age of AI (recorded at the 2025 OWASP Global AppSec conference). An interview, so it works by ear. | verified; content per watch-page description |
| 5.4 | AWS re:Invent 2016: Compliance Architecture: How Capital One Automates the Guard Rails (ARC312) | Amazon Web Services | https://www.youtube.com/watch?v=wfzzJj3IiDc | 47:14 | Deeper | BIKE | Fast lane: per the title, a 2016 AWS session on how a large US bank automates compliance guard rails on AWS. Product details are dated and AWS-specific; the idea of compliance built in as automated checks is what to take. I could not read the watch page, so this is title-based. | verified; title-based |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.O1 | Advanced Data Protection With HashiCorp Vault | HashiCorp, an IBM Company | https://www.youtube.com/watch?v=bZ803OZabTg | 56:31 | Deeper | BIKE | The closest secrets-and-encryption item I verified: by title, data protection with Vault. It is a vendor channel, so keep the ideas (central key custody, encryption as a service) and discount the product. I did not read a description. | verified; title-based |
| 5.O2 | Compliance by design: Solving bank-grade security with a foundational component - Maryna Rybalko | Platform Engineering | https://www.youtube.com/watch?v=N8pxGO1ot8A | 14:08 | Deeper | BIKE | By title, a talk on building bank-grade security and compliance into one foundational platform component. I did not read a description or check who the speaker works for. | verified; title-based |
| 5.O3 | OAuth: When Things Go Wrong | OktaDev | https://www.youtube.com/watch?v=H6MxsFMAoP8 | 43:58 | Deeper | BIKE | By title, the failure modes of OAuth deployments, a follow-on to 5.1. Vendor channel; I did not read a description. | verified; title-based |

**Feeds:** Track C Block 6 (Safety, security and governance: prompt injection is a confused-deputy problem, and the model-risk story rests on the controls here), Track C Block 4 (Agents and tools: an agent calling a tool is a delegated-authorisation question) and Track C Block 8 (AWS GenAI specifically: AgentCore identity and gateway are these ideas as services). Also Track C Block 9 (Enterprise architecture and operating at scale: the LLM gateway is a policy enforcement point).

**Full circle:** you can say, for any call in a system diagram, whose identity it carries and how that identity was proved; explain why "inside the network" is not a reason to trust a caller; run a threat-modelling pass on a diagram by asking what can go wrong at each boundary; and describe how a bank turns written control requirements into automated checks that run on every deployment.

**Architect's question:** Whose identity does this call carry, what is the smallest set of things it can reach, and how would we know if it reached more?

<details>
<summary>Recap questions (3)</summary>

1. Q: What does OpenID Connect add to OAuth 2.0? A: OAuth 2.0 is about delegated authorisation (access tokens for calling an API on a user's behalf); OpenID Connect adds a standard way to authenticate the user, with an ID token that says who they are.
2. Q: What is the core idea of zero trust (BeyondCorp)? A: Network location does not grant trust; every request is judged on the user's identity and the state of the device, so no VPN or "trusted internal network" is needed.
3. Q: What are the four questions of Shostack's framework? A: What are we working on, what can go wrong, what are we going to do about it, and did we do a good enough job (this answer is background knowledge; the page I read names the framework but does not list the questions).
</details>

---

## Block 6: Reliability and observability

**Why it matters for the stack:** Blocks 1-4 explain how systems fail; this block is how you measure, see, survive and learn from failure. An architect who cannot state a reliability target, trace a request across services or say what happens when a whole cloud is gone has not finished the design. Capacity and cost thinking is thin here (see Gaps).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.1 | SLIs, SLOs, SLAs, oh my! (class SRE implements DevOps) | Google Cloud Tech | https://www.youtube.com/watch?v=tEylFyxbDLE | 8:05 | Start | BIKE | Liz Fong-Jones and Seth Vargo (2018) define the indicator (what you measure), the objective (the target) and the agreement (the business promise with penalties), and why they belong together. Short; watch it first. | verified; content per watch-page description |
| 6.2 | Is It Time To Version Observability? (Signs Point To Yes) • Charity Majors • GOTO 2024 | GOTO Conferences | https://www.youtube.com/watch?v=ag2ykPO805M | 35:25 | Deeper | BIKE | Majors argues that metrics-only telemetry no longer fits how teams ship and proposes "Observability 2.0" built on rich, granular events; chapters include the history of observability, how you debug, and the cost model. An opinionated view from a vendor CTO (Honeycomb), so treat it as one position. | verified; content per watch-page description and chapters |
| 6.3 | Why distributed tracing will replace (most) logging | Lightstep is now ServiceNow Cloud Observability | https://www.youtube.com/watch?v=Hv98hU3nj0U | 46:28 | Deeper | BIKE | By title, the case that tracing should carry what logs carry now. A same-titled 2021 article by Lightstep's Ben Sigelman argues that tracing joins data across services where logs cannot; I did not confirm that the video makes the same argument or who speaks. Vendor channel. | verified; title-based |
| 6.4 | SREcon19 Asia/Pacific - Getting More out of Postmortems and Making Them Less Painful to Do | USENIX | https://www.youtube.com/watch?v=MZEmdZHj2_I | 54:03 | Deeper | BIKE | Per the USENIX page, Ashar Rizqi of Blameless on what makes a postmortem effective, how to cut the effort and strain of running them, and case studies of teams that gained from them. The speaker's company sells incident tooling, so expect some of that angle. | verified; content per USENIX page |
| 6.5 | Chaos & Intuition Engineering at Netflix • Casey Rosenthal • GOTO 2016 | GOTO Conferences | https://www.youtube.com/watch?v=Q4nniyAarbs | 49:04 | Deeper | BIKE | Per the GOTO abstract, why Netflix puts development velocity first, what that does to availability, and how chaos engineering and "intuition engineering" are used to manage one of the largest deployments. A 2016 talk; the principles outlast the tooling. | verified; content per GOTO page |
| 6.6 | How Monzo tolerates full cloud outages \| Andrew Lawson & Daniel Chatfield \| LDX3 London 2025 | LeadDev | https://www.youtube.com/watch?v=R79IRXLS0JY | 20:46 | Deeper | BIKE | Case study from a bank: per LeadDev's page for the talk, Monzo "Stand-in", a separate always-on backup bank on a different cloud (main platform on AWS, stand-in on Google Cloud), kept current in near real time and tested continuously in production. Pairs with 3.6 and 4.6. | verified; content per LeadDev page for the talk |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.O1 | Solving Reliability Fears With Service Level Objectives | Datadog | https://www.youtube.com/watch?v=39ycBjCagTU | 33:33 | Deeper | BIKE | A second SLO talk after 6.1, about using objectives to remove fear of change. It came up in a search for Liz Fong-Jones talks, but I did not confirm the speaker. Vendor channel; I did not read a description. | verified; title-based |
| 6.O2 | Charity Majors - Observability and Complex Systems: What Got You Here Won’t Get You There | Association for Software Testing | https://www.youtube.com/watch?v=_5io6Px9-2A | 54:38 | Deeper | BIKE | A second Majors talk on observability for complex systems; it probably overlaps 6.2. I did not read a description. | verified; title-based |
| 6.O3 | OpenTelemetry Meetup: Yuri Shkuro on Distributed Tracing, Jaeger and OpenTelemetry | Aspecto | https://www.youtube.com/watch?v=OebhomcdJ4g | 56:36 | Deeper | BIKE | A tracing talk by the creator of Jaeger (author link is from the title only), to add a practitioner view to 6.3. A meetup recording, so slides may matter; I did not read a description. | verified; title-based |
| 6.O4 | SREcon25 Europe/Middle East/Africa - The SRE’s Crystal Ball: Predicting System Performance with... | USENIX | https://www.youtube.com/watch?v=SdxeGBS7290 | 37:35 | Scholar | DESK | The only capacity-and-performance-prediction item I found; the title is cut off in the oEmbed result, so I cannot say what method it uses. Mode DESK is an assumption that a prediction talk needs charts and pausing. | verified; title-based |

**Feeds:** Track C Block 5 (Evaluation and observability: LLM traces, online evals and cost per request are this block's SLIs and traces with new signals), Track C Block 9 (Enterprise architecture and operating at scale: resilience and fallback for a model gateway, and FinOps) and Track C Block 7 (Customization and serving: serving latency and capacity set the SLOs you can promise).

**Full circle:** you can propose an availability and latency objective for a service, explain the error budget as the way to trade reliability against change speed, name what you would need to trace one request across ten services, say why a postmortem should be blameless, and describe how a bank keeps customers served when a whole cloud region or provider is down.

**Architect's question:** What is the SLO for this service, who owns the error budget, and how would we notice a failure nobody predicted?

<details>
<summary>Recap questions (3)</summary>

1. Q: How do an SLI, an SLO and an SLA differ, and what is an error budget? A: The SLI is a measured indicator (for example the share of requests under 300 ms), the SLO is the target for it, the SLA is a customer-facing agreement with consequences; the error budget is the allowed shortfall (100% minus the SLO), which you spend on releases and risk (the budget definition is background knowledge, the first three come from 6.1's description).
2. Q: Why are metrics alone not enough for a failure nobody predicted? A: Pre-aggregated metrics answer only the questions you thought of in advance; rich per-request events and traces let you ask new questions and follow one request across services, which is the argument in 6.2 and 6.3.
3. Q: Why exercise failure on purpose, and what does Monzo's stand-in add? A: Chaos experiments find weaknesses before real outages do and build confidence; a stand-in on a different cloud, tested continuously, answers the case where the whole primary platform is unavailable.
</details>

---

## Block 7: Data and ML platform

**Why it matters for the stack:** this is the bridge to Track C. Before models were generative they were still trained on data, served through pipelines and monitored, and the platforms big companies built for that (Uber, Netflix and others) are what a GenAI platform grows from. Track C covers GenAI serving and RAG, so this block stays with the classic ML platform, the data underneath it, and data ownership.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.1 | Machine Learning, Technical Debt, and You - D. Sculley (Google) | PAPIs.io | https://www.youtube.com/watch?v=V18AsBIHlWs | 27:35 | Start | BIKE | By title, a Google engineer on the maintenance costs of ML systems. The widely cited paper "Hidden Technical Debt in Machine Learning Systems" is by Sculley and colleagues (my background knowledge); I did not read this video's description, so I cannot say how closely it follows the paper. | verified; title-based |
| 7.2 | The Story Behind Michelangelo \| ML Platform at Uber | neptune_ai | https://www.youtube.com/watch?v=6NDPAbDWqak | 9:16 | Start | BIKE | Case study: Mike Del Balso on building Uber's ML platform, covering early challenges, failures, strategic decisions and the lessons that shaped it. Short, so a quick way into the platform idea before the deeper talks. | verified; content per watch-page description |
| 7.3 | Uber - Accelerating ML at Uber with the Palette Feature Store - FS Summit 2022 | Feature Store Org | https://www.youtube.com/watch?v=VJYM0tpfiL0 | 25:14 | Deeper | BIKE | Per the Feature Store Summit page, Amit Nene of Uber on how Michelangelo uses the Palette feature store to cut inefficiencies in the model lifecycle. Slides likely; glance at the screen. | verified; content per Feature Store Summit page |
| 7.4 | Metaflow: The ML Infrastructure at Netflix | AICamp | https://www.youtube.com/watch?v=JCbOI_1ZA5E | 1:12:00 | Deeper | BIKE | By title, Netflix's ML infrastructure as seen through Metaflow, its workflow framework; the closest verified item for pipelines and orchestration in an ML setting. A meetup recording; I did not read a description. | verified; title-based |
| 7.5 | Real-time Machine Learning: Architecture and Challenges | Toronto Machine Learning Series (TMLS) | https://www.youtube.com/watch?v=S4A8QWN1G7s | 39:42 | Deeper | BIKE | Chip Huyen (2023), per the description: the value of fresh data for ML, the different architectures for it, and the challenges of online prediction. This is the batch-versus-real-time decision for classic ML. | verified; content per watch-page description |
| 7.6 | Data Lake Strategy via Data Mesh Architecture at JPMorgan Chase; Data Mesh Learning Meetup #005 | Data Mesh Learning | https://www.youtube.com/watch?v=7iazNKG8XQo | 1:23:28 | Deeper | BIKE | Case study from a bank: per the meetup page, JPMorgan executives on building a cloud data lake with a data mesh and treating data as products with owners. The closest verified item for data ownership and governance. | verified; content per meetup page |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.O1 | Data Mesh: Why, What and How - ZHAMAK DEHGHANI \| Craft Conference 2021 | CraftHub Events | https://www.youtube.com/watch?v=NWsa2vR_vrM | 39:05 | Deeper | BIKE | The originator's own explanation of data mesh, to go with 7.6 (author link is from the title only). I did not read a description. | verified; title-based |
| 7.O2 | Principles of Good Machine Learning Systems Design | Databricks | https://www.youtube.com/watch?v=g08qBcdk3Ss | 27:22 | Deeper | BIKE | A general ML-systems design talk; a search tied talks of this title to Chip Huyen, but I did not confirm the speaker on this upload. Vendor channel. | verified; title-based |

**Feeds:** Track C Block 3 (Embeddings, vector search and RAG: embedding and indexing jobs are pipelines like these, and a vector index is a derived store with an owner), Track C Block 5 (Evaluation and observability: monitoring, lineage of evaluation data and drift are the same operating loop), Track C Block 7 (Customization and serving: batch versus online serving and a model registry, now with larger models) and Track C Block 6 (Safety, security and governance: ownership and lineage of data are what audit asks for).

**Full circle:** you can draw the lifecycle of a model as a platform (data, features, training, registry, deployment as batch or online, monitoring, retraining), say what a feature store is for, choose between batch and real-time prediction for a use case, and say who owns a dataset and how you would show where it came from. You can also say which parts of that loop a GenAI team no longer owns (training) and which it still owns (data, evaluation, serving, monitoring).

**Architect's question:** Who owns this dataset, how fresh must it be for this prediction, and how do we know if the model or its inputs have drifted?

<details>
<summary>Recap questions (3)</summary>

1. Q: What problem does a feature store solve? A: It gives training and serving one definition of each feature, with an offline store for training and an online store for low-latency lookups, so models are not trained on one computation and served on another (this answer is background knowledge; the pages I read name the feature store but do not spell this out).
2. Q: When would you choose batch prediction, and when online? A: Batch when predictions can be computed ahead for a known set of entities and staleness is acceptable (cheaper, simpler); online when the input only exists at request time or freshness changes the answer, at the cost of latency budgets and serving infrastructure.
3. Q: What does "data as a product" mean in a data mesh? A: A domain team owns its datasets like a product, with a named owner, documented meaning, quality commitments and discoverability, instead of one central team owning all data (from the 7.6 page and general knowledge).
</details>

---

## Block 8: Architecture judgement and case studies

**Why it matters for the stack:** this is the capstone. Blocks 0-7 gave you the parts; this block is how architects decide, record, test and defend decisions, and how a big company's whole stack fits together. Cost thinking, build versus buy and Shopify/Stripe-style case studies are thin (see Gaps).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.1 | Software Architecture: The Hard Parts (Teaser) • Neal Ford & Mark Richards • GOTO 2023 | GOTO Conferences | https://www.youtube.com/watch?v=SrOdAjXKvRk | 2:54 | Start | BIKE | By title, a teaser for the "Hard Parts" book and workshop by two well-known architecture authors, whose theme is analysing trade-offs (my background knowledge). I did not read a description, so the depth is unknown. | verified; title-based |
| 8.2 | Lesson 168 - ADRs and Architecture Stories | Software Architecture Monday | https://www.youtube.com/watch?v=DGUv_bgLmXo | 10:13 | Start | BIKE | By title, a short lesson on architecture decision records (the written record of a decision, its context and its consequences) and on telling architecture stories. Same channel as 0.O1; I did not read a description. | verified; title-based |
| 8.3 | Building Evolutionary Architectures • Neal Ford • YOW! 2018 | GOTO Conferences | https://www.youtube.com/watch?v=DloJCWdB7_o | 49:23 | Deeper | BIKE | By title, Ford on evolutionary architecture. A GOTO Bookclub page for the book of the same name describes protecting architectural characteristics with fitness functions, but I did not read a description of this video. | verified; title-based |
| 8.4 | Platforms: Build Abstractions, not Illusions • Gregor Hohpe • GOTO 2025 | GOTO Conferences | https://www.youtube.com/watch?v=mRoWGqcBSzk | 46:08 | Deeper | BIKE | Per the GOTO page: why hiding complexity in a platform can create "dangerous illusions", with examples from two decades of distributed systems where abstractions helped and where they disappointed. Useful when judging a vendor service or an internal platform (that framing is mine). | verified; content per GOTO page |
| 8.5 | Modern Enterprise Architecture: Architecting for Outcomes • Simon Rohrer • GOTO 2025 | GOTO Conferences | https://www.youtube.com/watch?v=UMaZ-O2KRCw | 37:52 | Deeper | BIKE | Per the GOTO page: Rohrer (Saxo Bank's enterprise architecture lead) on why classic enterprise-architecture principles no longer fit, bringing agile, DevOps and socio-technical practice to the enterprise, and removing dependencies instead of managing them. | verified; content per GOTO page |
| 8.6 | What I Wish I Had Known Before Scaling Uber to 1000 Services • Matt Ranney • GOTO 2016 | GOTO Conferences | https://www.youtube.com/watch?v=kb-m2fasdDY | 46:38 | Deeper | BIKE | Case study (2016): per the GOTO page, Uber's chief systems architect on growth past 1,000 production services and what he would do differently. A good counterweight to the Netflix story. | verified; content per GOTO page |
| 8.7 | Microservices at Netflix Scale • Ruslan Meshenberg • GOTO 2016 | GOTO Conferences | https://www.youtube.com/watch?v=57UK46qfBLY | 48:34 | Deeper | BIKE | Case study (2016): by title, how Netflix runs its microservice estate at scale. The conference page could not be read, so this is title-based; pair it with 2.3, 3.2 and 6.5 for more of the Netflix stack. | verified; title-based |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.O1 | AWS re:Invent 2021 - How JPMC modernized its core risk management platform | AWS Events | https://www.youtube.com/watch?v=3ygPF-Qshkc | 54:29 | Deeper | BIKE | A bank case study on modernising a core risk platform, by title. AWS-hosted, so expect an AWS slant. I did not read a description. | verified; title-based |
| 8.O2 | FinOps X 2026 Keynote Day 1: The Wild West of AI, Token Economics and the New Job of FinOps | FinOps Foundation | https://www.youtube.com/watch?v=W4g8xvduIbs | 1:37:52 | Deeper | BIKE | Also in Track C (Block 9, item 9.6), watch once. The only cost and FinOps item I verified; by title it is AI-focused, so it covers cost at the architecture level only in part. | verified; title-based |
| 8.O3 | Software Architecture: The Hard Parts - Neal Ford | Developer Summit | https://www.youtube.com/watch?v=Q6RfMmMwhvM | 57:05 | Deeper | BIKE | A fuller "Hard Parts" talk by title, to follow 8.1. The channel is a small conference channel I did not vet; I did not read a description. | verified; title-based |

**Feeds:** Track C Block 9 (Enterprise architecture and operating at scale: build versus buy, the gateway and platform-team pattern, FinOps, ownership), Track C Block 0 (Big picture: the stack map and where the probabilistic component sits) and Track C Block 8 (AWS GenAI specifically: judging a managed service against the alternatives).

**Full circle:** the whole track in one scene. You are in a design review of a proposed system, for example a customer-facing service in a bank with a model in it. You ask for the C4 context and container diagrams (Block 0); trace one request through the edge, the identity and authorisation checks (Block 5), the services and the contracts between them (Block 3); ask which store is the system of record and what happens under replica lag or a partition (Blocks 1-2); ask where it runs, what happens if a region goes, and what the recovery time and point are (Block 4); ask for the SLOs, the traces and the on-call story (Block 6); ask who owns the data, how features and models are produced and monitored (Block 7). For each choice you ask for the decision record, the trade-off accepted, the fitness function that will catch it going wrong, and the cost, and you can say which two or three decisions you would push back on and why.

**Architect's question:** What decision are we making, what did we trade away to make it, what would make us reverse it, and what check will tell us when that moment arrives?

<details>
<summary>Recap questions (3)</summary>

1. Q: What goes into an architecture decision record, and why keep them? A: The context, the decision, the alternatives considered and the consequences, kept with the code, so later teams know why something is as it is and can tell when the reasons no longer hold (general knowledge; 8.2 is title-based).
2. Q: What is a fitness function in an evolutionary architecture? A: An automated check of an architectural property (for example a latency limit, a dependency rule or a security policy) that runs continuously, so the architecture is protected as it changes (per the GOTO Bookclub page for the book, not confirmed in the video).
3. Q: What is the risk of a platform or vendor service that hides complexity? A: Teams start to rely on an illusion (for example that failures, cost or data location no longer matter), so you judge an abstraction by what it still lets through and what it costs to leave (from the 8.4 page).
</details>

---

## Gaps

Honest list of what this track does not cover well, from Block 0 to Block 8.

- **Block 0:** no real enterprise-stack-layers video. The eight-layer map in Block 0 is the author's own framing, and 0.O1 is only a title-level vocabulary item. 0.3 is title-based.
- **Block 1:** no primary-source CAP video; CAP appears only through the ScyllaDB PACELC webinar (1.5), which is a vendor webinar. There is no plain latency-versus-throughput explainer (1.2 is about measuring latency, not about the difference).
- **Block 2:** coverage of choosing a store is partial (2.2 is a 2012 talk). The caching and search talks (2.3, 2.4) date from 2014-2016. There is no gentle warehouse-versus-lake explainer (2.6 is a vendor argument, and who presents was not confirmed). Kafka basics appear only in optional 2.O1.
- **Block 3:** the outbox pattern is unconfirmed in any video (recap question 2 rests on general knowledge). The API gateway appears only in the optional vendor talk 3.O1. There is no neutral REST, gRPC and GraphQL comparison (3.O4 is a title-level REST refresher). Queues versus logs is covered only indirectly (3.4).
- **Block 4:** the service mesh talk (4.4) and the multi-region talk (4.6) are title-only. There is no cloud-neutral disaster-recovery video (4.O4 is AWS-centred). There is no neutral Kubernetes-concepts video; 4.2 is a 2016 keynote.
- **Block 5:** secrets management, KMS and encryption at rest and in transit have no main-path video; only the optional 5.O1 (a vendor channel, title-based) comes close, and there is no neutral envelope-encryption or key-management explainer (the search results were AWS KMS tutorials, which I excluded as service-specific). 5.4 is title-based and from 2016. Regulatory frameworks (PCI DSS, SOX, DORA and the like) are not covered by any verified video; 5.O2 is title-only. Threat modelling is covered only by an interview (5.3), not a worked example.
- **Block 6:** capacity planning and cost thinking have no real video (6.O4 is cut off and title-only). 6.3 is title-based from a vendor channel, so the tracing coverage is weak; I did not find a neutral CNCF or OpenTelemetry overview whose page I could read. Incident response in the live sense (roles, communication, on-call) is not covered; 6.4 is about postmortems only. 6.1 is a short 2018 explainer, and burn-rate alerting is not covered.
- **Block 7:** there is no gentle MLOps-lifecycle overview whose page I could read; 7.1, 7.2 and 7.3 together stand in for it, and 7.1 and 7.4 are title-based. Data quality and lineage have no main-path video (my searches returned mostly vendor webinars that I did not use); data ownership is covered through the data-mesh case (7.6). Orchestration with an Airflow-type tool has no verified item; 7.4 is Metaflow. Stripe, Spotify, Airbnb and Capital One ML-platform case studies were not found in a usable form. The platforms in 7.2 to 7.4 have changed since these were recorded, so treat them as case studies of ideas, not current descriptions.
- **Block 8:** build versus buy and technology selection have no direct video; 8.4 and 8.5 are indirect. Cost and FinOps at the architecture level is only the optional 8.O2, which is AI-focused. There is no Shopify, Stripe or Capital One whole-stack case study; Netflix and Uber (8.6, 8.7) are 2016 talks, and 8.7 is title-based. Simon Brown and Martin Fowler appear in Block 0 and not here. Several architecture-judgement items (8.1, 8.2, 8.3) are title-based, so check them against your own notes after the first ride.
- **Whole track:** most "What you will get" sentences rest on descriptions, not on watching; and the channels for 5.2 (RSAC), 6.3 (Lightstep) and 7.2 (neptune_ai) are partly vendor-run.

## Not checked

- I watched nothing. Every "What you will get" sentence comes from a title, a watch-page description or chapter list, or a named non-YouTube page (conference, USENIX, LeadDev, Feature Store Summit, Data Mesh Learning, Class Central and similar).
- Lengths were read from the YouTube pages on 2026-11-16 for every row, so the earlier notes about conference-slot times are no longer needed.
- Title-only rows (Status says "title-based"), new in Blocks 5-8: 5.4, 5.O1, 5.O2, 5.O3, 6.3, 6.O1, 6.O2, 6.O3, 6.O4, 7.1, 7.4, 7.O1, 7.O2, 8.1, 8.2, 8.3, 8.7, 8.O1, 8.O2, 8.O3. In Blocks 0-4 the title-only rows are the ones marked "title-based" in their Status, carried over from the earlier pass and not re-checked.
- Speakers and authorship I did not confirm: 6.3 (the speaker is not confirmed; the Sigelman argument comes from a same-titled article), 6.O1, 6.O3 and 7.O1 (names come from the title only), and 7.O2 (a search tied the title to Chip Huyen, not confirmed on this upload).
- The YouTube watch pages for many new rows returned errors or rate limits, which is why so many are title-based. I did not work around this.
- Availability, ordering and region-locking of every video are unverified; the oEmbed check shows only that the ID exists and returns that title and channel. Titles and channels are copied as oEmbed returned them (trailing spaces removed, escaped characters decoded).
- Dated material: 2012-2018 talks (including 5.4, 6.5, 8.6 and 8.7) are named by year in their rows or Gaps; product details in them may be out of date, and vendor speakers' views should be read as positions, not consensus.
- Recap answers marked "background knowledge" are mine, not taken from a video.
