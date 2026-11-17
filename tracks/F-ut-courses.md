# Track F: UT Austin MSAI course tracker

**What this track is.** Each block is one course of UT Austin's online MS in Artificial Intelligence. For each course it gives the official description, free public materials that match the content, a short video path, and recap questions. The video path is a prep and companion path: it does not replace the course, its assignments or its instructors' emphasis. Videos are for the bike; code, reading and pausing are for the desk (Mode column). It covers all 15 courses: Blocks 1 to 6 are the four foundational courses, the required Ethics course and the elective Natural Language Processing; Blocks 7 to 14 are eight more electives (Advances in Deep Learning, Advances in Deep Generative Models, Case Studies in Machine Learning, Optimization, Online Learning and Optimization, Automated Logical Reasoning, AI in Healthcare, AI in Astrophysics); Block 15 is Agentic Software Engineering, which the 2027-2028 handbook lists with a title only.

**Program structure, as stated on https://cdso.utexas.edu/msai (read on 2026-11-16).** The page describes a 30-hour program of 10 courses at 3 credit hours each, "consisting of 3 hours of required courses and 27 hours of electives". Only Ethics in AI is marked "(required)". Under the heading "Required and Foundational Courses" it lists Deep Learning, Ethics in AI, Machine Learning, Planning, Search, and Reasoning Under Uncertainty, and Reinforcement Learning; under "Elective Courses" it lists nine: Advances in Deep Generative Models, Advances in Deep Learning, AI in Astrophysics, AI in Healthcare, Automated Logical Reasoning, Case Studies in Machine Learning, Natural Language Processing, Online Learning and Optimization, and Optimization. It recommends completing the required and foundational courses at the beginning, before electives. **What the handbook settles.** The MSAI Online Handbook (published for 2027-2028; you supplied it and I read all 30 pages on 2026-11-16) says that the coursework option is 30 credit hours made of 1 required course and 9 electives, that the only required course is Ethics in AI (AI 380E), and that the other 14 courses are electives. That list includes the four courses the cdso page calls foundational (Machine Learning, Deep Learning, Reinforcement Learning, Planning, Search, and Reasoning Under Uncertainty), so they are not mandatory. Grades: B- or higher for the required course, C or higher for electives, letter grades only, and a 3.0 GPA to graduate. A thesis option exists (1 required, 7 electives and 2 thesis courses), but the program does not help find a supervisor and one must come from the UT AI graduate faculty. Time limit: six years from the first semester; the program expects 1.5 to 3 years. At most 6 credit hours can transfer from another institution. The handbook lists 15 courses, one more than the cdso page: Agentic Software Engineering (AI 395T), which has a title and no description (Block 15). The handbook is dated 2027-2028, so check that it governs a Spring 2027 start. The cdso page still recommends completing the foundational courses first; the handbook states no prerequisites except for two courses (Blocks 8 and 14). The cdso page gives no course numbers or syllabus links and does not use the term "Option III" (Greg Durrett's UT page and the handbook do, for UT's online master's programs); course numbers are in the table of the next section and in each block.

**Suggested order (my judgement, not an official rule).** For someone aiming at GenAI architecture who starts with one course at a time alongside full-time work: Deep Learning first, which is the current leaning in your notes and the course closest to the GenAI core (Block 2); the alternative is Machine Learning first if the math and probability feel rusty (Block 1), since it carries the theory and shares gradient descent with Deep Learning. Then the other one of those two, then Ethics in AI (the one course marked required; concept and discussion heavy, per its outline), then Reinforcement Learning, with Planning, Search, and Reasoning Under Uncertainty last among these because its link to the stack is the weakest. Natural Language Processing is the most direct fit to the GenAI goal among the six courses here. The handbook lists it with Machine Learning, Deep Learning, Reinforcement Learning and Planning as electives, so only Ethics in AI is mandatory, and the cdso page's advice to take the foundational courses first is a recommendation I cannot find as a rule in the handbook. A program email of 2026-11-16 lists what runs in Spring 2027: Deep Learning, Machine Learning, Advances in Deep Learning, Advances in Deep Generative Models, Agentic Software Engineering, Ethics in AI, Optimization, Online Learning and Optimization, Automated Logical Reasoning, Case Studies and AI in Healthcare; it says Natural Language Processing, Reinforcement Learning and Planning do not run that term, and it does not mention AI in Astrophysics. The elective ranking for the GenAI goal follows in the next section.

## Which electives to consider for the GenAI-architect goal

**This is a judgement, not data.** I ranked the courses by how closely their outlines on the cdso page (and the public sites named in each block) match the end-to-end GenAI lifecycle of a large-company stack. I did not research salary, hiring or market data, so nothing here says what employers pay for or ask for. "Tier" means distance from the GenAI-architect goal, not the quality or difficulty of a course. Per the handbook only Ethics in AI is required and the four courses the cdso page calls foundational are electives, so the tiers are about fit to your goal, not about what the degree demands. Course numbers are from the handbook. Agentic Software Engineering is a 15th course that the cdso page did not list; I could not rate it, because the handbook gives only its title. Rows are in my order of priority within each tier.

| # | Course | Kind | Tier | GenAI lifecycle stage served | Prerequisites (handbook where stated, otherwise inferred from the outline) | Why |
|---|--------|------|------|------------------------------|--------------------------------------------|-----|
| 1 | Deep Learning (AI 394D; Block 2) | Elective (cdso page: foundational) | Core for GenAI | data and pretraining (training mechanics, transformers); multimodal and diffusion (Part 2) | Python, calculus and linear algebra, gradient descent from Block 1 | Backpropagation, PyTorch, convolutional networks and, per the cdso page and the UT Deep Learning Group site, transformers and generative models are the technology under every model you will host or adapt; the handbook says the course only touches on deep language models, so the LLM-specific material sits more in the Advances in Deep Learning and NLP rows. |
| 2 | Advances in Deep Learning (AI 395T; Block 7) | Elective | Core for GenAI | adaptation (LoRA, QLoRA); post-training (instruction tuning, RLHF, DPO); inference and serving (quantization, FlashAttention, speculative decoding); grounding and RAG; agents (tool use, structured outputs); data and pretraining (distributed training) | Deep Learning first (my assumption; neither the cdso page nor the handbook lists a prerequisite), PyTorch | The closest course to the engineering of large models, but the stage list rests on the public UT Deep Learning Group site, which may not match the online course. |
| 3 | Natural Language Processing (AI 388; Block 6) | Elective | Core for GenAI | data and pretraining; post-training (instruction tuning, RLHF); grounding and RAG (open-domain QA); evaluation | Python, probability, some deep-learning background (the public outline builds up from linear classifiers) | Tokens, embeddings, transformers, BERT-style pre-training and question answering are the model layer under every retrieval and agent application. |
| 4 | Advances in Deep Generative Models (AI 395T; Block 8; titled Advances in Generative Models in the handbook) | Elective | Core for GenAI | multimodal and diffusion; data and pretraining (autoregressive language models, one week) | Machine Learning and Deep Learning first (handbook: "ML and DL should be taken first"), probability (likelihood, KL divergence) | Diffusion, flows, GANs and VAEs explain image and video generation; only one of seven topics is language models, so for text-centred enterprise stacks it ranks below 2 and 3. |
| 5 | Machine Learning (AI 391L; Block 1) | Elective (cdso page: foundational) | Useful | evaluation | Probability, linear algebra, Python | Generalization, evaluation and learning theory shape how you judge any model; you will not build stack components in it. |
| 6 | Optimization (AI 388J; Block 10) | Elective | Useful | data and pretraining (optimizers and training dynamics) | Multivariable calculus, linear algebra, comfort with proofs | The theory behind SGD-style training; mostly convex and linear-programming theory, so the link is indirect. |
| 7 | Reinforcement Learning (AI 394R; Block 3) | Elective (cdso page: foundational) | Useful | post-training (RLHF-style methods); agents | Probability, Python, gradients | Policy gradients and exploration reappear in post-training and agent loops, but the course is mostly classic RL. |
| 8 | Ethics in AI (AI 380E; Block 5) | Required | Useful | safety and governance | None stated; reading and writing | Fairness, accountability and transparency are the vocabulary of governance and review layers; the one course the page marks required. |
| 9 | Case Studies in Machine Learning (AI 391M; Block 9) | Elective | Useful | evaluation (data preparation, iteration, reporting) | Python or R, ML basics | Applied habits (dataset preparation, tuning, client-style reporting), but the page mentions no deep learning or language models and gives no outline beyond learning outcomes. |
| 10 | Planning, Search, and Reasoning Under Uncertainty (AI 388U; Block 4) | Elective (cdso page: foundational) | Niche | agents (plan-act loops, search over options) | Graph search, probability, Python | Classical planning with a robotics flavour; its ideas reappear in agent design; the weakest link of the four foundational courses. |
| 11 | Online Learning and Optimization (AI 388K; Block 11) | Elective | Niche | evaluation (online experimentation); platform (routing between models), both my inference | Optimization (Block 10), probability, comfort with proofs | Bandits and regret are the maths of learning from feedback; proof-heavy, and the link to a stack is by inference only. |
| 12 | Automated Logical Reasoning (AI 389L; Block 12) | Elective | Niche | safety and governance (verifying code and constraints); agents (solver tools), both my inference | Propositional logic, discrete math, programming | SAT and SMT solving and software verification; classical computational logic, not machine learning. |
| 13 | AI in Healthcare (AI 380H; Block 13) | Elective | Niche | data and pretraining (clinical data standards); safety and governance (ethics in health); evaluation (explainable risk) | ML basics (Block 1); no clinical background (none listed) | A domain course; useful mainly if your systems will handle health data. |
| 14 | AI in Astrophysics (AI 395T; Block 14) | Elective | Niche | data and pretraining (training-set curation); evaluation (interpretability) | A B or higher in Machine Learning, and Deep Learning passed or taken at the same time (handbook); no astronomy needed | Science-domain machine learning that shares methods (flows, interpretability) with the stack, not products. |
| 15 | Agentic Software Engineering (AI 395T; Block 15) | Elective | Not rated | agents (tool use, agent workflows); LLMOps and platform (my reading of the title) | Not published; the on-campus CS 378 page of the same name expects systems programming (CS 439 or equivalent), a programming language (Python preferred) and git | The handbook gives only the title, so I cannot rank it by content. By title it is the course closest to working with AI coding agents, which fits the coding-plus-AI part of your goal; the CS 378 page describes homework done with AI coding agents and a systems half, but it may not be the online course. |

**Questions to ask the program coordinator:**
1. Which courses run in which semesters, and which electives will be open in the first year or two? The program's 2026-11-16 email lists the Spring 2027 courses (Natural Language Processing, Reinforcement Learning and Planning are not among them); AI in Astrophysics is in the handbook but not in that email's course list, so ask whether it is offered at all.
2. How many hours per week does each course really take, including assignments and any GPU access they need?
3. Answered by the handbook: only Ethics in AI is required; Machine Learning, Deep Learning, Reinforcement Learning and Planning are electives. Still ask: does the program recommend taking Machine Learning and Deep Learning before the other electives (the cdso page does), and which courses assume them besides Advances in Generative Models and AI in Astrophysics (the two where the handbook says so)?
4. Who teaches Advances in Deep Learning, and is the UT Deep Learning Group site (Block 7) what the online course uses? The handbook gives a one-sentence outline (memory-efficient optimization, diffusion and autoregressive generation, LLMs and vision) and no prerequisite.
5. What does Agentic Software Engineering (AI 395T) cover, who teaches it, and what does it assume? The handbook lists only the title.

## How to read the tables

**Table legend.**
- Level: Start / Deeper / Scholar.
- Mode: BIKE = works mostly by listening (slide lectures need a glance at the screen). DESK = needs code, paper or pausing. Unlike a pure bike path, a DESK row appears in a main list where the course itself is hands-on (a coding demo) or its material is proof-heavy; 18 of the 98 main rows are DESK.
- Status "verified" means the YouTube oEmbed endpoint returned the exact video ID I asked for, with the title and channel shown (copied as returned). It does not mean I watched the video. After "verified" the Status names what the "What you will get" sentence rests on: the watch-page description or chapter list, a named course page, or the title only ("title-based").
- Rows marked "also in Track X <id>; watch once" are reused from Tracks A to C and G: title, channel, link and length are copied from that row, and I did not re-verify them. Rows marked "also used in Block N, row N.M" repeat a row from an earlier block of this file, so watch that video once. Rows without either mark are new in this track and passed the oEmbed check when I added them.
- Length: read from the video's YouTube page on 2026-11-16 or 17 (no cookies, nothing played). A row shows no length only if that page could not be read; MORNING.md lists those.
- "What you will get" is one sentence in my own words, based only on the source named in Status. I have not watched any of these videos.

**Honest accounting.** All 15 blocks together have 98 main rows (48 reused from Tracks A to C and G, 2 repeated from earlier blocks of this file, 48 new) and 50 optional rows (25 reused, 3 repeated, 22 new): 148 rows and 134 distinct videos. Every row has a measured length (96 different main-path videos together 77 h 58 m, and 38 further optional videos together 38 h 31 m; videos used twice are counted once). Nothing was watched. YouTube watch pages could not be read for the descriptions of the rows added in Blocks 7 to 14 (the tool blocked them), so most of those rows are title-based, as the Status column says. Blocks 7 to 14 also lean on public course sites that may not match the online courses; Block 7 most of all, because the cdso page has no outline for it. The weakest rows are 4.7 (a demo whose content I could not read), 5.6 (speaker only), 5.1, 1.4 and 6.7 (title only), the optional rows 3.O4 and 4.O4 (title only), 8.2 (the only energy-based-model row, about latent-variable models and title-based), 9.5, 9.6, 11.O1, 13.5, 13.6 and 14.O3 (channels I did not vet), 14.2 (one day of a series I did not check) and 12.3 and 12.4 (a lecture series whose page I could not read).

---

## Block 1: Machine Learning

**Why it matters for the stack:** the vocabulary and theory (generalization, bias and variance, likelihood versus priors, clustering, learnability) behind every later decision about evaluation, model choice and data in a GenAI stack; the link to building the stack is indirect, because you will not build a retrieval or agent system in this course.

**Official description and outline:** Per the cdso page (instructors listed: Adam Klivans and Qiang Liu, Computer Science), an introduction to the core algorithms and statistical tools of machine learning: supervised and unsupervised learning, PAC learning, Bayesian methods and neural networks, with programming examples.

**Handbook (2027-2028):** AI 391L. The handbook's description is the older catalog wording: inductive classification (version space, decision tree, rule-based, neural network, Bayesian and instance-based methods), computational learning theory, explanation-based learning and knowledge refinement. It names computational learning theory but not PAC learning, boosting, PCA or EM, so treat the cdso outline above as the more specific one and confirm against the syllabus. Adam Klivans (graduate advisor) and Qiang Liu are on its faculty list.

**Public materials:**
- **Textbook, free from the authors:** Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (Cambridge University Press, 2014). The authors' page offers the full PDF: https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/ (the PDF itself loaded and showed this title and these authors). Theory-first; its PAC and VC chapters match the course's PAC topic (my background knowledge of the book, its contents not checked here).
- **Textbook, free download:** Christopher Bishop, *Pattern Recognition and Machine Learning* (Springer, 2006). Microsoft Research's page offers the full PDF: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ (the page states no license terms). Strong on Bayesian methods and graphical models.
- **Textbook, free PDFs from the authors:** Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani (Python edition with Jonathan Taylor), *An Introduction to Statistical Learning*, in an R edition (2nd edition) and a Python edition (ISLP): https://www.statlearning.com/ (added in part 2: the page offers both as free PDFs and states "All Rights Reserved"; I did not open the PDFs). Applied and example-driven, lighter on theory than the books above.
- **Textbook, free draft:** Kevin Murphy, *Probabilistic Machine Learning: An Introduction* (MIT Press, 2022). The book's page offers a free PDF draft dated 2025-04-18, licensed CC-BY-NC-ND per the page: https://probml.github.io/pml-book/book1.html (a draft, not the final print edition).
- **Instructor page:** Qiang Liu's UT homepage lists his own lecture notes (an undergraduate intro to ML, probabilistic learning and inference, learning theory) as PDFs hosted on Dropbox, which I could not open, so I list only the homepage: https://www.cs.utexas.edu/~lqiang/index.html. The page does not say the notes belong to the online course.
- **Older UT course by one instructor (on-campus version of a different, theory course; may differ from the online course):** Adam Klivans, CS 395T Computational Learning Theory, Fall 2006: https://www.cs.utexas.edu/~klivans/cl2.html. Useful only as a topic list for PAC learning, VC dimension and boosting.
- No public course site or lecture videos for the online Machine Learning course itself were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.1 | Machine Learning Fundamentals: Bias and Variance | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=EuBBz3bI-aA | 6:36 | Start | BIKE | Why a model can be too simple or too wiggly: the overfitting and underfitting picture that generalization theory later makes precise (title-based). | verified; title-based; also in Track B 1.2; watch once |
| 1.2 | Gradient Descent, Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=sDv4f4s2SB8 | 23:54 | Start | BIKE | Walking downhill on the loss with actual numbers, step size and learning rate included; the engine behind most training in the course (title-based). | verified; title-based; also in Track B 2.1 and Track A #39; watch once |
| 1.3 | StatQuest: Logistic Regression | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=yIYKR4sgzI8 | 8:47 | Start | BIKE | From a line to a probability: classification with the logistic curve, the first supervised classifier to know well (title-based). | verified; title-based; also in Track B 2.2; watch once |
| 1.4 | Machine Learning: Lecture 13: PAC learning | UofU Data Science | https://www.youtube.com/watch?v=p5xP8fWnPZw | 1:20:27 | Deeper | BIKE | A full lecture on PAC learning, by title, from a channel named "UofU Data Science" (I read that as the University of Utah; not confirmed). I could not read the watch page, so I do not know whether it reaches VC dimension or sample-complexity bounds. It is the most course-like PAC video I could verify; the Caltech VC lecture in the optional list goes further. | verified; title-based |
| 1.5 | Expectation Maximization: how it works | Victor Lavrenko | https://www.youtube.com/watch?v=iQoXFmbXRJA | 10:39 | Deeper | BIKE | The EM idea as a soft version of the k-means loop: clustering with probabilistic assignments instead of hard ones (title-based). | verified; title-based; also in Track B 2.10; watch once |
| 1.6 | Maximum A Posteriori (MAP) - Why L2 Regularization is Bayesian in Disguise | DataMListic | https://www.youtube.com/watch?v=Ovuszur2uzk | 4:01 | Deeper | BIKE | Maximum likelihood versus a Bayesian prior (MAP), and how a prior shows up as L2 regularization (title-based). | verified; title-based; also in Track B 2.13; watch once |
| 1.7 | Machine Learning for Everybody – Full Course | freeCodeCamp.org | https://www.youtube.com/watch?v=i_LwzRVP7bg | 3:53:53 | Start | DESK | Demo, not a ride: per the chapter list, Python and Colab implementations of k-nearest neighbours, naive Bayes, logistic regression, SVM, a neural network in TensorFlow, linear regression, k-means and PCA (course developed by Kylie Ying, per the description). Do not watch it end to end; take the chapters that match your week (logistic regression from 1:19:22, neural networks from 1:39:44, k-means from 3:13:13). | verified; content per watch-page description and chapter list |

*Neural networks* are also a topic of this course; the video path for them is Block 2 (rows 2.1 to 2.3), because the Deep Learning course starts from the same ideas.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.O1 | StatQuest: K-means clustering | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=4b5d3muPQmA | 8:30 | Start | BIKE | The k-means loop: assign points, recompute centres; watch before 1.5 if clustering is new (title-based). | verified; title-based; also in Track B 2.9; watch once |
| 1.O2 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Start | BIKE | PCA walked through step by step, the other standard unsupervised method (title-based). | verified; title-based; also in Track B 2.7 and Track A #19; watch once |
| 1.O3 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | 18:40 | Start | BIKE | The visual picture of neurons, layers and weights, for the course's neural-networks topic (title-based). Block 2 goes deeper. | verified; title-based; also in Track B 3.1 (also used in Block 2, row 2.1); watch once |
| 1.O4 | Lecture 07 - The VC Dimension | caltech | https://www.youtube.com/watch?v=Dc0sr0kdBVI | 1:13:31 | Scholar | DESK | VC dimension from Caltech's Learning from Data: a full, long lecture that is the next step after 1.4. It builds on the two preceding Caltech lectures (Track B 2.O3, 2.O4); start there if you feel lost (title-based). | verified; title-based; also in Track B 2.5; watch once |

**Before you start:**
- Probability: conditional probability, Bayes' rule, expectation, a few distributions (Track A Blocks 4 and 5).
- Linear algebra and calculus: vectors, matrices, eigenvectors and SVD, partial derivatives and the gradient (Track A Blocks 2, 3 and 6).
- Python with NumPy, enough to follow the programming examples the cdso page mentions (the language and library are not stated there).
- The words train, validation and test set, overfitting, and loss function (Track B Block 1).

**Full circle:** you can explain why training error is not the number to trust, what a loss and a gradient step are, how logistic regression turns a line into a probability, what "PAC learnable" asks for, how a prior changes maximum likelihood into MAP, and how EM generalizes k-means.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does it mean for a problem to be PAC learnable? A: There is an algorithm that, for any accuracy ε and confidence δ you choose, returns with probability at least 1 − δ a hypothesis with true error at most ε, from a number of samples that grows only polynomially in 1/ε, 1/δ and the problem size.
2. Q: How does MAP estimation differ from maximum likelihood, and what does a zero-mean Gaussian prior on the weights do? A: Maximum likelihood maximizes the probability of the data given the parameters; MAP maximizes that times a prior over the parameters. A zero-mean Gaussian prior adds an L2 penalty, which is ridge regularization.
3. Q: What do the E-step and M-step of EM do in a Gaussian mixture? A: The E-step computes soft assignments of each point to each component under the current parameters; the M-step re-estimates the component parameters using those soft weights; repeating the pair never lowers the likelihood.
</details>

---

## Block 2: Deep Learning

**Why it matters for the stack:** this is the course closest to the core of GenAI engineering: backpropagation, training and debugging, PyTorch, convolutions, transformers and generative models are the technology under every model you will host, fine-tune or evaluate.

**Official description and outline:** Per the cdso page (instructor listed: Philipp Krähenbühl, Computer Science), deep learning from optimization through computer vision, language models and deep reinforcement learning. Part 1 covers building, training and debugging deep networks in PyTorch; Part 2 covers applications such as generative modeling and adversarial learning. Assignments include a vision system and a racing agent for the SuperTuxKart simulator.

**Handbook (2027-2028):** AI 394D. The handbook says: advanced topics in deep learning, from optimization to computer vision, computer graphics and unsupervised feature learning, touching on deep language models and deep learning for games. It mentions language models only in passing and does not name transformers, PyTorch or generative modelling; the transformer and generative material in this block comes from the cdso page and the UT Deep Learning Group site. Philipp Krähenbühl is on the faculty list.

**Public materials:**
- **UT course site (instructor and online/on-campus status not stated on the page, so check it against the syllabus when you enrol):** "Deep Learning Class" from the UT Austin Deep Learning Group, 2025: https://ut.philkr.net/deeplearning/. Slides and PyTorch notebooks for: introduction (tensors, gradients, PyTorch basics), first example (regression, classification, loss, logistic regression in PyTorch), deep networks, residuals and normalizations, convolution, transformers, and "making it work".
- **Earlier UT course page (a different run, Fall 2021; may differ from the online course; the page I read names no instructor):** CS 342 Neural Networks: https://philkr.github.io/cs342. Weekly topics from k-nearest neighbours through CNNs, optimization practice, computer vision, reinforcement learning and imitation learning, sequence modeling, embeddings, adversarial attacks, and bias, fairness and ethics; no textbook, no videos listed.
- **Textbook, online:** Aston Zhang, Zachary Lipton, Mu Li and Alex Smola, *Dive into Deep Learning*: https://d2l.ai. The site offers the full text online with PDF and notebook downloads, in PyTorch, NumPy/MXNet, JAX and TensorFlow; it shows version 1.0.3, and a Cambridge University Press print edition is listed as forthcoming.
- **Textbook, free to read as HTML only:** Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning* (MIT Press, 2016): https://www.deeplearningbook.org (the site says it stays free online and offers no PDF).
- **Tool tutorial:** PyTorch "Learn the Basics" (tensors, datasets and data loaders, building a model, autograd, the optimization loop, saving models): https://docs.pytorch.org/tutorials/beginner/basics/intro.html (the page I read is for PyTorch Tutorials 2.15.0).
- No public lecture videos by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.1 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | 18:40 | Start | BIKE | The visual picture of neurons, layers and weights (title-based). | verified; title-based; also in Track B 3.1; watch once |
| 2.2 | Gradient descent, how neural networks learn \| Deep Learning Chapter 2 | 3Blue1Brown | https://www.youtube.com/watch?v=IHZwWFHWa-w | 20:33 | Start | BIKE | Loss and gradient descent applied to a network (title-based); if gradient descent itself is new, watch Block 1 row 1.2 first. | verified; title-based; also in Track B 3.2 and Track A #38; watch once |
| 2.3 | Backpropagation, intuitively \| Deep Learning Chapter 3 | 3Blue1Brown | https://www.youtube.com/watch?v=Ilg3gGewQ5U | 12:47 | Start | BIKE | The intuition for how the error flows backward through the network and assigns blame to each weight (title-based). | verified; title-based; also in Track B 3.3 and Track A #42; watch once |
| 2.4 | Lecture 6 \| Training Neural Networks I | Stanford University School of Engineering | https://www.youtube.com/watch?v=wEoyxE0GP2M | 1:20:19 | Deeper | BIKE | Stanford CS231n (Spring 2017) lecture whose syllabus line reads "Activation functions, initialization, dropout, batch normalization"; the closest verified match to the course's "making it work" and debugging theme. Slide-heavy, so glance at the screen. | verified; content per CS231n 2017 syllabus line; also in Track B G2; watch once |
| 2.5 | Neural Networks Part 8: Image Classification with Convolutional Neural Networks (CNNs) | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=HGwBXDKFk9I | 15:23 | Start | BIKE | Convolution filters and pooling for images, shown visually (title-based); the course site lists convolutions, pooling and CNN design. | verified; title-based; also in Track B 3.5; watch once |
| 2.6 | Transformers, the tech behind LLMs \| Deep Learning Chapter 5 | 3Blue1Brown | https://www.youtube.com/watch?v=wjZofJX0v4M | 27:14 | Start | BIKE | A visual walk through how a GPT-style transformer is put together, including tokens and embeddings (title-based); the course site has a transformers unit (attention, multi-head attention, positional embeddings). | verified; title-based; also in Track B 4.1; watch once |
| 2.7 | The StatQuest Introduction to PyTorch | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FHdlXe1bSe4 | 23:22 | Start | DESK | Demo: PyTorch basics from StatQuest (title-based); have a laptop open and code along, ideally next to the PyTorch "Learn the Basics" tutorial listed above. | verified; title-based; also in Track B 3.O2; watch once |

Residual connections and normalization layers, which the course site lists, have no dedicated verified video here; Karpathy's makemore Part 3 (Track B 3.O3, a DESK video) is the closest. Deep reinforcement learning is in Block 3 (3.O3).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.O1 | Lecture 7 \| Training Neural Networks II | Stanford University School of Engineering | https://www.youtube.com/watch?v=_JB0AO7QxSA | 1:15:30 | Deeper | BIKE | The next CS231n lecture; the syllabus line reads "Update rules, ensembles, data augmentation, transfer learning". Slide-heavy; pause for any formulas. | verified; content per CS231n 2017 syllabus line; also in Track B G3; watch once |
| 2.O2 | The spelled-out intro to neural networks and backpropagation: building micrograd | Andrej Karpathy | https://www.youtube.com/watch?v=VMj-3S1tku0 | 2:25:52 | Deeper | DESK | Build backpropagation in code to make 2.3 concrete (title-based). | verified; title-based; also in Track B 3.O1; watch once |
| 2.O3 | But how do AI images and videos actually work? \| Guest video by Welch Labs | 3Blue1Brown | https://www.youtube.com/watch?v=iv-5mZ_9CPY | 37:20 | Start | BIKE | A visual explanation of how AI image generators work (diffusion family, by title); a bridge to Part 2 of the course (generative modeling). | verified; title-based; also in Track B 8.1; watch once |
| 2.O4 | Generative Adversarial Networks (GANs) - Computerphile | Computerphile | https://www.youtube.com/watch?v=Sw9r8CL98N0 | 21:21 | Start | BIKE | The generator-versus-discriminator idea; the course lists adversarial learning in Part 2 (title-based). | verified; title-based; also in Track B 8.2; watch once |

**Before you start:**
- Python and NumPy, and comfort running a notebook or script.
- The chain rule and the gradient of a function of many variables (Track A Blocks 1, 3 and 6); matrix-vector products (Track A Block 2).
- The training-loop picture from Block 1: model, loss, gradient step.
- A first look at PyTorch (tensors, autograd, an optimization loop); the cdso page says assignments run a SuperTuxKart simulator, so expect to set up a Python environment (setup details not on the page).

**Full circle:** you can say how a network turns inputs into outputs, how backpropagation assigns blame to each weight, why training needs the tricks in the "making it work" lectures, why CNNs suit images, and how attention lets a transformer mix information across a sequence; you can also read and write a short PyTorch training loop.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does backpropagation compute, and why is it cheap? A: The gradient of the loss with respect to every parameter, by applying the chain rule from the output back to the input and reusing values saved during the forward pass, so the cost is of the same order as one forward pass.
2. Q: Why do residual connections and normalization layers help very deep networks train? A: A skip connection gives gradients a short path to earlier layers and lets a block learn a correction to the identity, which eases vanishing gradients; normalization keeps activations in a stable range so larger learning rates work.
3. Q: In self-attention, what are queries, keys and values, and why can a transformer process all positions at once? A: Each token vector is projected into a query, a key and a value; softmax of query-key similarity gives weights that mix the values. This is a set of matrix multiplications over all positions, with no step-by-step recurrence as in an RNN.
</details>

---

## Block 3: Reinforcement Learning

**Why it matters for the stack:** the link to the GenAI stack is real but narrower than the course title suggests: reinforcement learning shows up in post-training (RLHF and related methods) and in agent policies, whereas this course is mostly classic RL (bandits, MDPs, temporal-difference methods).

**Official description and outline:** Per the cdso page (instructors listed: Peter Stone, instructor of record, and Scott Niekum), the theory and practice of reinforcement learning: bandits, dynamic programming, temporal-difference learning, policy gradient methods, and balancing exploration and exploitation.

**Handbook (2027-2028):** AI 394R, "Reinforcement Learning: Theory and Practice". The handbook adds model-free and model-based methods and names temporal-difference learning and policy gradients; it does not list bandits or dynamic programming. Peter Stone and Scott Niekum are on the faculty list.

**Public materials:**
- **Textbook, free from the authors:** Richard Sutton and Andrew Barto, *Reinforcement Learning: An Introduction*, 2nd edition (MIT Press, 2018). Full PDF on the authors' page: http://incompleteideas.net/book/the-book-2nd.html (PDF: http://incompleteideas.net/book/RLbook2020.pdf).
- **UT course page (on-campus version, may differ from the online course):** CS394R/ECE381V Reinforcement Learning: Theory and Practice, Spring 2024, taught by Amy Zhang and Peter Stone per that page: https://www.cs.utexas.edu/~pstone/Courses/394Rspring24/index.html. It uses Sutton and Barto chapters 1 to 13 and 16, then recent readings, and links other universities' RL course materials (I did not open those links).
- **Free online guide (2018, so dated on current methods):** OpenAI, *Spinning Up in Deep RL*: https://spinningup.openai.com/en/latest/. Three-part introduction to RL plus a key-papers list in 13 topic areas.
- **Public lecture series:** the DeepMind x UCL and David Silver RL lectures are the rows 3.2 to 3.5 and 3.O1 to 3.O3 below.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.1 | An introduction to Reinforcement Learning | Arxiv Insights | https://www.youtube.com/watch?v=JgvyzIkgxF0 | 16:27 | Start | BIKE | The agent, environment and reward picture before any formulas (title-based). | verified; title-based; also in Track B 5.1; watch once |
| 3.2 | DeepMind x UCL RL Lecture Series - Exploration & Control [2/13] | Google DeepMind | https://www.youtube.com/watch?v=aQJP3Z2Ho8U | 2:10:13 | Deeper | BIKE | Per the title, exploration and control: the bandit setting and exploration versus exploitation, as a full university-style lecture in the DeepMind x UCL series. | verified; title-based; also in Track B 5.2; watch once |
| 3.3 | DeepMind x UCL RL Lecture Series - MDPs and Dynamic Programming [3/13] | Google DeepMind | https://www.youtube.com/watch?v=zSOMeug_i_M | 1:43:56 | Deeper | BIKE | MDPs and dynamic programming in one lecture (per the title): the case where the model is known. | verified; title-based; also in Track B 5.3; watch once |
| 3.4 | RL Course by David Silver - Lecture 4: Model-Free Prediction | Google DeepMind | https://www.youtube.com/watch?v=PnHCvfgC_ZA | 1:37:01 | Deeper | BIKE | Monte Carlo and temporal-difference prediction (per the title, model-free prediction): the case where the model is not known. Full lecture. | verified; title-based; also in Track B 5.4; watch once |
| 3.5 | RL Course by David Silver - Lecture 7: Policy Gradient Methods | Google DeepMind | https://www.youtube.com/watch?v=KHZVXao4qXs | 1:33:58 | Deeper | BIKE | Optimising a policy directly, the policy-gradient family (title-based). Full lecture. | verified; title-based; also in Track B 5.5; watch once |
| 3.6 | AlphaGo - The Movie \| Full award-winning documentary | Google DeepMind | https://www.youtube.com/watch?v=WXuK6gekU1Y | 1:30:28 | Start | BIKE | Case study as a story, not a lecture: per the description, a film about the March 2016 match between Lee Sedol and DeepMind's AlphaGo in Seoul (directed by Greg Kohs). The description does not explain methods; that AlphaGo was trained with reinforcement learning is my own background knowledge, so treat the film as motivation for the course. | verified; content per watch-page description |

For the place where RL meets language models, see the RLHF lecture in Block 6 (6.O2).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.O1 | RL Course by David Silver - Lecture 1: Introduction to Reinforcement Learning | Google DeepMind | https://www.youtube.com/watch?v=2pWv7GOvuf0 | 1:28:12 | Deeper | BIKE | A formal introduction lecture to watch before 3.2 if you want the full vocabulary (title-based). | verified; title-based; also in Track B 5.O1; watch once |
| 3.O2 | DeepMind x UCL RL Lecture Series - Model-free Control [6/13] | Google DeepMind | https://www.youtube.com/watch?v=t9uf9cuogBo | 1:40:40 | Scholar | DESK | Per the title, model-free control: the step after prediction (3.4). Full lecture; pause for formulas. | verified; title-based; also in Track B 5.O2; watch once |
| 3.O3 | DeepMind x UCL RL Lecture Series - Deep Reinforcement Learning #1 [12/13] | Google DeepMind | https://www.youtube.com/watch?v=cVzvNZOBaJ4 | 47:05 | Scholar | BIKE | Per the title, deep reinforcement learning: neural networks inside RL. Full lecture. | verified; title-based; also in Track B 5.6; watch once |
| 3.O4 | RI Seminar: Peter Stone : Robot Skill Learning: From the Real World to Simulation and Back | CMU Robotics Institute | https://www.youtube.com/watch?v=84t_dQpdTEo | 1:03:46 | Deeper | BIKE | A research seminar by Peter Stone, whom the cdso page lists as the course's instructor of record. I could not read the watch page, so I know only the title (robot skill learning, simulation to real world); treat it as an optional look at the instructor's research, not as course content. | verified; title-based |

**Before you start:**
- Probability and expectation; what a Markov chain is (Track A Block 4).
- A feel for gradients and gradient ascent (needed for policy gradients; Track A Block 6).
- Python, since the Spring 2024 on-campus run's week 1 slides mention short-answer and programming assignments (the online course's assignments are not described on the cdso page).
- Read Sutton and Barto chapters 1 and 2 first; those week 1 slides assign them.

**Full circle:** you can describe the agent-environment loop, the exploration versus exploitation trade-off in a bandit, how an MDP is solved by dynamic programming when the model is known and by Monte Carlo or temporal-difference methods when it is not, and what a policy gradient does differently from learning values.

<details>
<summary>Recap questions (3)</summary>

1. Q: Why is exploration needed in a multi-armed bandit? A: Each arm's payoff is unknown and learned only by pulling it, so always pulling the arm that looks best can lock you onto a worse one; strategies such as epsilon-greedy, UCB or Thompson sampling trade some reward now for information.
2. Q: How do dynamic programming and temporal-difference learning differ? A: Dynamic programming needs the model (transition probabilities and rewards) and sweeps over states; temporal-difference learning learns from sampled experience and moves a value estimate toward the reward plus the discounted estimate of the next state (bootstrapping).
3. Q: Why do policy-gradient estimates have high variance, and what is the usual remedy? A: They use sampled returns that differ a lot between episodes; subtracting a baseline, for example a learned value function, keeps the estimate unbiased while lowering variance, which leads to actor-critic methods.
</details>

---

## Block 4: Planning, Search, and Reasoning Under Uncertainty

**Why it matters for the stack:** the link to a typical enterprise GenAI stack is weak: this is classical planning, search and decision theory with a robotics and autonomy flavor, though its ideas (plan-act loops, search over options, belief about hidden state) reappear in agent design and in reasoning about uncertainty.

**Official description and outline:** Per the cdso page (instructor listed: Joydeep Biswas, Computer Science), defining and solving planning problems, search-based and sample-based planning, adversarial planning, probabilistic reasoning, and decision-making with Markov and partially observable Markov decision processes.

**Handbook (2027-2028):** AI 388U. The handbook matches the cdso page in broad terms (planning domains and algorithms, search, reasoning about sensing and actuation, modelling uncertainty) and mentions autonomous systems; it does not name MDPs or POMDPs. Joydeep Biswas is on the faculty list.

**Public materials:**
- **UT course page (on-campus version, Spring 2023, instructor Joydeep Biswas; may differ from the online course):** CS 395T Planning, Search and Reasoning Under Uncertainty: https://amrl.cs.utexas.edu/CS395T-S23. The page lists topics as planning domains (symbolic and path planning), search algorithms, decision-making for autonomous systems and reasoning under uncertainty, with suggested textbooks AIMA and LaValle; the week-by-week schedule is a Google Sheet that I did not open.
- **Textbook, free online:** Steven LaValle, *Planning Algorithms* (Cambridge University Press, 2006): http://lavalle.pl/planning/ (HTML and PDF). Matches the sample-based planning topic.
- **Textbook, free PDF:** Mykel Kochenderfer, Tim Wheeler and Kyle Wray, *Algorithms for Decision Making* (MIT Press, 2022): https://algorithmsbook.com/ (the page says full PDFs are free). Scope per my background knowledge: probabilistic reasoning, MDPs and POMDPs; I did not open the PDF.
- **Textbook, not free:** Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th US edition. The companion site offers pseudocode, figures, exercises and code on GitHub: https://aima.cs.berkeley.edu/ (the page does not offer the book itself).
- **Public lectures:** the Berkeley CS188 lectures are rows 4.1, 4.3 to 4.5 and 4.O1 to 4.O3 below. No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.1 | Step-by-Step: A Star Search | CS188Spring2013 | https://www.youtube.com/watch?v=sAoBeujec74 | 22:17 | Start | BIKE | A worked A* example from the Berkeley CS188 channel (title-based). | verified; title-based; also in Track B 6.1; watch once |
| 4.2 | Sampling-based Methods [Lecture, Marija Popović] | Marija Popović | https://www.youtube.com/watch?v=CrQJAtPn8sY | 1:33:07 | Deeper | BIKE | Per the description, robotic motion planning with sampling-based methods, including PRM and RRT, plus extensions for kinodynamic constraints and asymptotic optimality; fills the "sample-based planning" topic that the Berkeley lectures do not cover. Probably slide-based, so glance at the screen. | verified; content per watch-page description |
| 4.3 | CS 188 Lecture 5: Adversarial Search | CS 188 | https://www.youtube.com/watch?v=_3djr6ZXLzQ | 1:23:00 | Deeper | BIKE | Berkeley lecture on adversarial (game) search (title-based). Full lecture. | verified; title-based; also in Track B 6.3; watch once |
| 4.4 | CS 188 Lecture 18: Hidden Markov Models | CS 188 | https://www.youtube.com/watch?v=0u80UvCAKVo | 58:25 | Deeper | BIKE | Bayesian state estimation with hidden Markov models: keeping a belief about a hidden state over time (title-based). Full lecture; assumes Bayes nets (see 4.O2). | verified; title-based; also in Track B 6.4; watch once |
| 4.5 | Lecture 8: Markov Decision Processes (MDPs) | CS188Spring2013 | https://www.youtube.com/watch?v=i0o-ui1N35U | 1:07:10 | Deeper | DESK | Berkeley's lecture on Markov decision processes, the planning-side companion to Block 3's 3.3 (title-based). | verified; title-based; also in Track B 6.O3; watch once |
| 4.6 | DLRLSS 2019 - POMDPs - Pascal Poupart | Amii | https://www.youtube.com/watch?v=K0wcWi38IGA | 1:28:30 | Scholar | BIKE | POMDPs from a summer-school lecture; per Track B the only POMDP source from a recognised expert that it verified. Long and mathematical, so keep it for the end. | verified; title-based; also in Track B 6.5; watch once |
| 4.7 | UT Austin Path Planning and Collision Avoidance Demonstration at Lockheed Martin | Lockheed Martin | https://www.youtube.com/watch?v=WYA4m9ZVZ1I | 2:17 | Start | BIKE | Demo, title only: a demonstration video of path planning and collision avoidance. I could not read the watch page, so I do not know what is shown, who built it, or whether it is related to the course; weak row, replace it if you find a better case study. | verified; title-based |

No verified video covers the first topic in the official outline, defining planning problems in a symbolic (PDDL-style) form; the two textbooks above are the better route for that topic.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.O1 | COMPSCI 188 - 2018-08-30 - A* Search and Heuristics | Webcast Departmental | https://www.youtube.com/watch?v=Mlwrx7hbKPs | 1:25:00 | Deeper | BIKE | Berkeley lecture on A* and heuristics; the formal version of 4.1 (title-based). Full lecture. | verified; title-based; also in Track B 6.2; watch once |
| 4.O2 | Lecture 13: Bayes Nets | CS188Fall2013 | https://www.youtube.com/watch?v=VfyxPtlqZh4 | 1:02:24 | Deeper | DESK | Prerequisite for 4.4 if Bayes nets are rusty (title-based). | verified; title-based; also in Track B 6.O1; watch once |
| 4.O3 | CS 188 Lecture 19: Particle Filtering | CS 188 | https://www.youtube.com/watch?v=r-bHqY5gaPw | 1:19:06 | Scholar | DESK | Approximate state estimation with particles, the step after 4.4 (title-based). | verified; title-based; also in Track B 6.O2; watch once |
| 4.O4 | EI Seminar - Joydeep Biswas | MIT Embodied Intelligence | https://www.youtube.com/watch?v=0vPNN0J8M44 | 1:00:12 | Deeper | BIKE | A seminar talk by a speaker named Joydeep Biswas; the cdso page names a Joydeep Biswas as this course's instructor, but I could not read the watch page, so I cannot confirm it is the same person or what the topic is. | verified; title-based |

**Before you start:**
- Graph search basics (breadth-first, depth-first, Dijkstra) and big-O reading of algorithms.
- Probability: conditional probability, Bayes' rule, a Bayes net (Track A Block 4; Track B 2.14).
- The MDP idea (Block 3, row 3.3 below) before the POMDP lecture.
- Python for the programming side (not described on the cdso page).

**Full circle:** you can say how A* uses a heuristic and when it is optimal, how sampling-based planners such as PRM and RRT trade optimality for reach in high dimensions, how minimax with pruning handles an opponent, how an HMM keeps a belief about a hidden state, and how POMDPs extend MDPs to act on that belief.

<details>
<summary>Recap questions (3)</summary>

1. Q: Why do sampling-based planners such as RRT work in high-dimensional spaces where grid search does not, and what do they give up? A: Grid and graph search grow exponentially with the number of dimensions; RRT samples configurations and grows a tree into unexplored space, so it needs no full grid. It is probabilistically complete but its paths are not optimal; variants such as RRT* aim for asymptotic optimality.
2. Q: What does minimax assume about the opponent, and what does alpha-beta pruning add? A: Minimax assumes the opponent plays to minimize your utility; alpha-beta skips branches that cannot change the decision, giving the same answer with fewer nodes (how many fewer depends on move ordering).
3. Q: What is a belief state, and how does a POMDP differ from an MDP? A: In an MDP the state is observed; in a POMDP you only get observations, so you keep a probability distribution over states (the belief) and update it with Bayes' rule after each action and observation. A POMDP can be treated as an MDP over beliefs.
</details>

---

## Block 5: Ethics in AI

**Why it matters for the stack:** governance, fairness, transparency and accountability are the substance of the guardrails and governance layers of a production GenAI stack (model risk, responsible-AI review, audit); for someone designing stacks for a regulated enterprise this is the least technical course and still a real link.

**Official description and outline:** Per the cdso page (instructor listed: Ken Fleischmann, School of Information; the one course marked required), the history of AI and ethics, ethical theories applied to AI, and principles for ethical AI design, with weekly topics including fairness, accountability, transparency, power and agency.

**Handbook (2027-2028):** AI 380E, the one required course; a grade of B- or higher is needed (C for electives). The handbook adds non-Western and feminist perspectives to the history of ethics and AI, then the societal and technical dimensions (fairness, accountability, transparency, power and agency). Kenneth Fleischmann is on the faculty list.

**Public materials:**
- **UT course syllabus (on-campus version, may differ from the online course):** INF 385T.12 Ethics of AI, instructor Ken Fleischmann; the PDF does not state the semester (its file name says Fall 2024): https://ischool.utexas.edu/sites/default/files/syllabi/EthicsOfAISyllabusFall2024Final.pdf. Fourteen weeks: histories of ethics and of AI, then ethical traditions (Indian, Chinese, Buddhist, Islamic, Kantian, consequentialist, distributive justice, virtue, care, Ubuntu), value-sensitive design, codes of ethics, AI ethics guidelines, and fairness, accountability, transparency, power and agency. Readings are listed by author; I did not check which are free.
- **Textbook, free online:** Solon Barocas, Moritz Hardt and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities* (MIT Press, 2023): https://fairmlbook.org (full text and a PDF of the whole book, licensed CC BY-NC-ND 4.0). More technical and legal than the course's ethical-theory weeks, so it complements them.
- **Public lectures related to the course's themes:** Greg Durrett's NLP course ends with four short ethics lectures (bias, exclusion, dangers of automation, unethical use and paths forward), listed on his page given in Block 6.
- No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.1 | Michael Wooldridge - The story of AI - GDR IA - Journées Plénières 2021 | GDR RADIA | https://www.youtube.com/watch?v=JDZsK_N8s5M | 1:21:53 | Start | BIKE | History of AI, by title, from a plenary talk by Michael Wooldridge (a University of Oxford professor, per my own background knowledge). I could not read the watch page, so the coverage is unknown; the best-sourced history-of-AI talk I found, since the other results came from small channels. | verified; title-based |
| 5.2 | Justice: What's The Right Thing To Do? Episode 01 "THE MORAL SIDE OF MURDER" | Harvard University | https://www.youtube.com/watch?v=kBdfcR-8hEY | 54:56 | Start | BIKE | Ethical theory by example: per the description, Michael Sandel's opening dilemma (kill one to save five), a 19th-century shipwreck case, and an introduction to Bentham's utilitarianism; a classroom recording, so you can follow by ear. | verified; content per watch-page description |
| 5.3 | What is trustworthy AI? | DigitalEU | https://www.youtube.com/watch?v=Imv9SG-zfkU | 1:53 | Start | BIKE | A short orientation on trustworthy-AI guidelines from the channel named DigitalEU (title match only). | verified; title-based; also in Track B 7.1; watch once |
| 5.4 | FAT* 2018: Joy Buolamwini - Intersectional Accuracy Disparities in Commercial Gender Classification | ACM FAccT Conference | https://www.youtube.com/watch?v=Af2VmR-iGkY | 23:08 | Deeper | BIKE | Fairness, case-based: accuracy gaps across groups in commercial gender classification (title-based). | verified; title-based; also in Track B 7.2; watch once |
| 5.5 | Turing Lecture: Algorithmic Accountability: Professor Ben Shneiderman, University of Maryland | The Alan Turing Institute | https://www.youtube.com/watch?v=UWuDgY8aHmU | 1:21:32 | Deeper | BIKE | Accountability and transparency, from a university professor's lecture (title-based). | verified; title-based; also in Track B 7.4; watch once |
| 5.6 | CDAC Distinguished Speaker Series - Kate Crawford | UChicago Data Science Institute | https://www.youtube.com/watch?v=YhqYt7b8sFY | 1:07:42 | Deeper | BIKE | Power, by speaker only: a talk by Kate Crawford, whose book Atlas of AI is about the material and political cost of AI (background knowledge). I could not read the watch page, so I do not know the talk's topic; weak row for the "power" week. | verified; title-based |
| 5.7 | The Accuracy, Fairness, and Limits of Predicting Recidivism | Berkman Klein Center for Internet & Society | https://www.youtube.com/watch?v=G0OE8p-fc10 | 56:40 | Deeper | BIKE | Case study on fairness: a recidivism prediction tool and the limits of predicting it (title-based). | verified; title-based; also in Track B 7.3; watch once |

There is no verified video on the ethical-theory weeks beyond row 5.2 (utilitarianism by example); the syllabus above lists the other traditions if you want to read ahead.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.O1 | The E.U. AI Act: A Risk-Based Policy Approach to AI Applications | Stanford HAI | https://www.youtube.com/watch?v=OhBsDIG8ioM | 1:04:13 | Deeper | BIKE | A 17 June 2021 webinar on the European Commission's April 2021 proposal to regulate high-risk AI: US policy experts and an EU Cabinet member discuss its benefits, drawbacks and transatlantic implications. A panel about the draft proposal, not the final law. | verified; content per watch-page description; also in Track B G11; watch once |
| 5.O2 | What is our ethical responsibility with AI & Machine Learning? - Fei-Fei Li & Andrew Ng | Stanford Online | https://www.youtube.com/watch?v=Aws-cOIXsNQ | 1:00 | Start | BIKE | A conversational overview of ethical responsibility in AI from two prominent researchers (title-based). | verified; title-based; also in Track B 7.O1; watch once |
| 5.O3 | What is AI ethics? Oxford Professor Edward Harcourt explains | University of Oxford | https://www.youtube.com/watch?v=Gpf_ttt_c8M | 2:54 | Start | BIKE | A general introduction to AI ethics from the University of Oxford's channel (title-based; not specific to any one course topic). | verified; title-based |
| 5.O4 | The Turing Lectures: Can we trust AI? | The Alan Turing Institute | https://www.youtube.com/watch?v=7SyAC5TsEsQ | 1:46:11 | Start | BIKE | A public lecture on whether AI can be trusted, from the Alan Turing Institute (title-based; general rather than course-specific). | verified; title-based |

**Before you start:**
- No math or code. Comfort reading a short academic paper and writing a one-page argument is the real preparation.
- A picture of the ML pipeline (data, labels, training, evaluation, deployment) so you can say where bias enters (Track B Block 1).
- The idea of group-wise error rates versus overall accuracy (Track B Block 1 or 2).

**Full circle:** you can sketch the history of AI and of ethical theory in a few sentences, say what utilitarian and rule-based reasoning would each conclude about a concrete AI case, name two documented cases of bias, and say how fairness, accountability, transparency and power differ as lenses on the same system.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is the difference between consequentialist and rule-based (deontological) ethics, with an AI example? A: Consequentialism judges an action by its outcomes (utilitarianism: maximize overall welfare, for example a self-driving car minimizing total harm); deontology judges by duties and rules that hold regardless of outcomes (for example, never treat a person merely as a means).
2. Q: What did the gender-classification study in row 5.4 show, and what does it imply for how you evaluate a model? A: Error rates differed sharply across skin tone and gender groups even when overall accuracy looked high; evaluation must be disaggregated by group, because a single average hides who bears the errors.
3. Q: How do accountability and power differ as ways of looking at an AI system? A: Accountability asks who is answerable for outcomes and how a decision can be challenged or remedied; power asks who builds, owns and benefits from the system and whose interests it serves.
</details>

---

## Block 6: Natural Language Processing

**Why it matters for the stack:** the strongest link in this part of the file: tokens, embeddings, attention, pre-training, instruction tuning and question answering are the model layer under every retrieval and agent application; the course covers the models and methods, not application engineering.

**Official description and outline:** Per the cdso page (instructors listed: Greg Durrett and Jessy Li, Computer Science), statistical and deep learning methods for NLP: syntactic and semantic analysis, sequence tagging, parsing, machine translation, question answering, and pre-trained models such as BERT.

**Handbook (2027-2028):** AI 388. The handbook lists linguistics fundamentals, machine learning models, key inference algorithms and hands-on PyTorch work on text classification, syntactic analysis, language modeling, semantic parsing and question answering. It does not name BERT or machine translation, which the cdso outline above does. Jessy Li is on the faculty list; Greg Durrett is not, so check the instructor when the course is announced. A program email of 2026-11-16 says the course does not run in Spring 2027.

**Public materials:**
- **UT's online-MS version, public (recordings from 2023-2024; the program's current run may differ):** Greg Durrett's CS388/AI388/DSC395T Natural Language Processing (online MS) course materials: https://www.cs.utexas.edu/~gdurrett/courses/online-course/materials.html. Twelve parts, from linear classification and neural networks through embeddings, language models, transformers, BERT and seq2seq, tagging and parsing, modern LLMs, explanations, question answering, machine translation and summarization, to multilinguality and ethics; slides and notes archive, four assignments with code, and a final project. The page says the materials are for online master's students in UT's "Option III" programs and that anyone may consult them. Jessy Li is also listed on the cdso page; I found no public materials from her.
- **Lecture videos:** the course playlist "Natural Language Processing at UT Austin, 2023-2024 version (Greg Durrett)", 98 videos per the playlist page: https://www.youtube.com/playlist?list=PLofp2YXfp7TZZ5c7HEChs0_wfEfewLDs7. The course page says the Introduction video comes from an older run.
- **Main reading named on that page:** Jacob Eisenstein's NLP notes (PDF in a GitHub repository): https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf (the page loaded; it shows no license).
- **Textbook, free draft:** Dan Jurafsky and James Martin, *Speech and Language Processing*, 3rd edition draft: https://web.stanford.edu/~jurafsky/slp3/ (chapters posted free; the page shows a release dated 19 August 2026; some chapters are stubs).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.1 | The Illustrated Word2vec - A Gentle Intro to Word Embeddings in Machine Learning | Jay Alammar | https://www.youtube.com/watch?v=ISPId9Lhc1g | 8:44 | Start | BIKE | Embeddings from first principles (title-based): the idea that words become vectors, which the course reaches in its week 3 after linear and neural classification. | verified; title-based; also in Track B 4.O1; watch once |
| 6.2 | Attention in transformers, step-by-step \| Deep Learning Chapter 6 | 3Blue1Brown | https://www.youtube.com/watch?v=eMlx5fFNoYc | 26:09 | Deeper | BIKE | The attention mechanism, step by step, visually (title-based); intuition first, before the lecture version in 6.3. | verified; title-based; also in Track B 4.2 and Track C 1.3; watch once |
| 6.3 | Transformer Architecture (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=sLsUD-RcDqg | 7:45 | Deeper | BIKE | Durrett's own lecture on the transformer, from the week titled "Transformers and Decoding" in his lecture outline; the instructor-recorded version of what 6.2 shows visually. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.4 | BERT: Masked Language Modeling (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=dya_QNFvtiQ | 7:44 | Deeper | BIKE | Pre-training with masked language modeling (the "Pre-training and Seq2seq LMs" week), the BERT-style model the course description names. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.5 | Part-of-Speech Tagging (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=Llw6qfeAWDs | 17:00 | Deeper | BIKE | Sequence tagging, the start of the course's "Structured Prediction" weeks (tagging, HMMs, parsing). | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.6 | Open-Domain QA (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=P-j_zeS0Pa8 | 6:58 | Deeper | BIKE | Question answering over a large collection of documents (the "Question Answering and Dialogue" week); the closest course topic to retrieval-augmented generation. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.7 | The pipeline function | Hugging Face | https://www.youtube.com/watch?v=tiZFewofSLM | 4:35 | Start | DESK | Demo, title only: from Hugging Face's own channel, the pipeline function of its Transformers library. I could not read the watch page, so do not assume which tasks it shows; code along with a laptop open. | verified; title-based |

Rows 6.3 to 6.6 and the optional rows come from the instructor's own public playlist, so they match the course's order and emphasis best; they are slide lectures, so glance at the screen. The playlist holds more lectures (n-gram and neural language models, beam search, parsing, dialogue, summarization) than fit here.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.O1 | Instruction Tuning (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=YT3VSlDjrVU | 5:49 | Deeper | BIKE | The "Modern Large Language Models" week: how pre-trained models are tuned to follow instructions. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O2 | Reinforcement Learning from Human Feedback (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=DwAdhx6GFh8 | 8:13 | Deeper | BIKE | The same week: RLHF, the place where Block 3's reinforcement learning meets language models. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O3 | Neural and Pretrained Machine Translation (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=bcP4b_4HQ8A | 7:51 | Deeper | BIKE | Machine translation with neural and pre-trained models ("Machine Translation and Summarization" week). | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O4 | CKY Algorithm (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=QeDb6mSDSqs | 14:28 | Scholar | BIKE | Constituency parsing with the CKY dynamic program (the structured-prediction weeks); the most formal row of the block, safe to skip for GenAI purposes. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |

**Before you start:**
- Python, and PyTorch basics (Block 2); the course builds neural networks from linear classifiers up, per its outline, so deep learning is not a hard prerequisite on that evidence.
- Gradient descent and logistic regression (Block 1, rows 1.2 and 1.3).
- Probability: conditional probability, Bayes' rule, maximum likelihood (Track A Blocks 4 and 5); HMM and tagging lectures use them.
- The idea of a transformer (Block 2, row 2.6), so that the week 4 and 5 attention and transformer lectures are a second pass.

**Full circle:** you can say how words become vectors, how self-attention and the transformer architecture work, how BERT-style masked pre-training differs from next-token pre-training, how sequence tagging is solved with dynamic programming, and how open-domain question answering combines retrieval with a reader model.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does self-attention do that an RNN cannot do as easily? A: An RNN compresses the history into a state, step by step; self-attention lets every token look directly at every other token's representation in parallel, so long-range dependencies are one hop away.
2. Q: How does BERT's masked-language-model pre-training differ from a GPT-style objective, and what is each good at? A: BERT hides some input tokens and predicts them from context on both sides, giving strong representations for classification, tagging and question answering; a GPT-style model predicts the next token left to right, which suits generation.
3. Q: Why is HMM part-of-speech tagging decoded with the Viterbi algorithm instead of scoring every tag sequence? A: The number of tag sequences grows exponentially with sentence length; the HMM factorization lets dynamic programming find the best sequence in time roughly proportional to the sentence length times the square of the tag count.
</details>

---

## Block 7: Advances in Deep Learning

**Why it matters for the stack:** if the public UT site described below is what the online course teaches (not confirmed), this is the most direct course in the program for the engineering of large models: distributed and memory-efficient training, adapters and quantization, attention kernels, instruction tuning and RLHF, fast inference, retrieval and structured outputs, and vision-language models.

**Official description and outline:** Per the cdso page (instructor listed: Philipp Krähenbühl, Computer Science), the course gives an in-depth exploration of the technologies behind some of the most advanced deep learning models, and its hands-on assignments have students re-implement smaller versions of those models. **The page states that the course outline "will be posted soon", so the cdso page has no detailed topic list (the handbook later gives a one-sentence outline, quoted next).** Everything below about topics comes from the UT Deep Learning Group's public site (next section), not from the cdso page.

**Handbook (2027-2028):** AI 395T. The handbook gives a one-sentence outline: memory-efficient optimization, generative models (diffusion, autoregressive generation), and frontier models in language (LLMs) and computer vision. That fits the topics taken from the UT Deep Learning Group site below, but the handbook names no instructor and no prerequisite, so the match with that site is still unconfirmed (Philipp Krähenbühl, whose group runs it, is on the faculty list).

**Public materials:**
- **UT course site, titled "Advances in Deep Learning" (footer: "© 2025 UT Austin - Deep Learning Group"):** https://ut.philkr.net/advances_in_deeplearning/. The page names no instructor and does not say whether it is the online course; the title matches the cdso course and the slide deck of its diffusion-models lesson names Philipp Krähenbühl, UT Austin. Treat it as the best available guess at the content, which may differ from the online course. Sections and lessons: Introduction (structures of deep networks, training deep networks, modern GPU architectures); Advanced Training (training large models, mixed precision, distributed training, zero redundancy training, low-rank adapters, quantization, quantized low-rank adapters, low-rank projections, checkpointing, FlashAttention, open-source infrastructure for model training); Generative Models (VAEs, GANs, flow-based models, auto-regressive generation, vector quantization, DALL-E, diffusion models, latent diffusion and state-of-the-art models, "Which generative model should I use?"); Large Language Models (architectures, generation, instruction tuning, RLHF, DPO, tasks and datasets, efficient LLM training and inference, sequence parallelism, paged attention, speculative decoding, open-source infrastructure, tool use, structured outputs, constrained decoding, long context, retrieval-augmented generation, structured dialogues, limitations, a bonus lesson on reinforcement learning and LLMs); Computer Vision (classification, detection, segmentation, open-vocabulary recognition, vision-language models).
- **What a lesson page holds:** the two lesson pages I read (Low-Rank Adapters and Diffusion Models) each show a slides link, an embedded lecture video hosted on UT's Panopto (utexas.hosted.panopto.com) and references to the original papers. I loaded the diffusion slides PDF (about 16 slides: forward and reverse process, ELBO training, U-Net, score-based models, guided diffusion). I did not open the Panopto player, so I do not know whether the videos play without a UT login.
- **Reference text:** *Dive into Deep Learning* (https://d2l.ai, see Block 2) as a general companion; I did not map its chapters to these lessons.
- No public lecture videos on YouTube by the course's instructor were found, and no site for the online run itself.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.1 | Distributed Data Parallel (DDP) with PyTorch: complete tutorial with cloud infrastructure and code | Umar Jamil | https://www.youtube.com/watch?v=toUSzwR0EV8 | 1:12:53 | Deeper | DESK | Demo: training one model across several GPUs with PyTorch's DDP, with code and cloud setup (title-based); matches the "Distributed Training" lesson; code along with a laptop open. | verified; title-based |
| 7.2 | ZeRO & Fastest BERT: Increasing the scale and speed of deep learning training in DeepSpeed | Microsoft Research | https://www.youtube.com/watch?v=zqsOEzKZX2Y | 1:05:10 | Scholar | BIKE | The title names ZeRO and DeepSpeed; that ZeRO splits optimizer state, gradients and parameters across GPUs so larger models fit is my background knowledge. Matches the "Zero Redundancy Training" lesson; glance at the slides. | verified; title-based |
| 7.3 | What is LoRA? Low-Rank Adaptation for finetuning LLMs EXPLAINED | AI Coffee Break with Letitia | https://www.youtube.com/watch?v=KEv-F5UkhxU | 8:21 | Deeper | BIKE | A short explainer; per its chapter list: why finetuning is costly, how LoRA works, and LoRA versus other approaches; matches the "Low-Rank Adapters" lesson. | verified; content per watch-page chapter list; also in Track B G5; watch once |
| 7.4 | FlashAttention - Tri Dao \| Stanford MLSys #67 | Stanford MLSys Seminars | https://www.youtube.com/watch?v=gMOAud7hZg4 | 58:58 | Scholar | BIKE | A seminar talk on FlashAttention by Tri Dao (named in the title; he is the method's first author per my background knowledge); matches the "FlashAttention" lesson; technical, so glance at the slides. | verified; title-based |
| 7.5 | State of GPT \| BRK216HFS | Microsoft Developer | https://www.youtube.com/watch?v=bZQun8Y4L2A | 42:40 | Deeper | BIKE | Karpathy's Build 2023 talk: per third-party notes, the assistant training pipeline (pre-training, supervised fine-tuning, reward modelling, RLHF) and then how to use such models; the nearest match to the "Instruction Tuning" and "RLHF" lessons. | verified; content per third-party notes gist (section headings); also in Track B G4; watch once |
| 7.6 | Speculation is all you need: Intro to Speculative Decoding for High Performance Inference | Modal | https://www.youtube.com/watch?v=kdo7KMAQcrE | 40:19 | Deeper | BIKE | An introduction to speculative decoding for faster LLM inference, from the channel of a cloud-compute company (title-based); matches the "Speculative Decoding" lesson. | verified; title-based |
| 7.7 | RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models | IBM Technology | https://www.youtube.com/watch?v=zYGDpG-pTho | 13:10 | Start | BIKE | A comparison of the three ways to adapt a model to a task (what each costs and can add); a decision frame that sits next to the "Retrieval Augmented Generation" and "Instruction Tuning" lessons. | verified; content per sozai transcript page; also in Track B G6; watch once |

The "Modern GPU Architectures", mixed precision, checkpointing, sequence parallelism, paged attention, structured output and constrained decoding lessons have no dedicated verified video here (vLLM serving is in Track C 7.4), and the Computer Vision lessons are covered only by 7.O3 and Block 2 (2.5).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.O1 | Transformers, the tech behind LLMs \| Deep Learning Chapter 5 | 3Blue1Brown | https://www.youtube.com/watch?v=wjZofJX0v4M | 27:14 | Start | BIKE | The prerequisite picture (title-based): how a GPT-style transformer is put together; watch first if the architecture and attention lessons move fast. | verified; title-based; also in Track B 4.1 (also used in Block 2, row 2.6); watch once |
| 7.O2 | 8-bit Methods for Efficient Deep Learning -- Tim Dettmers (University of Washington) | Center for Language & Speech Processing(CLSP), JHU | https://www.youtube.com/watch?v=2ETNONas068 | 47:47 | Scholar | BIKE | A research talk on 8-bit methods for efficient deep learning by the speaker named in the title (title-based); matches the "Quantization" and "Quantized Low-Rank Adapters" lessons. | verified; title-based |
| 7.O3 | OpenAI CLIP: ConnectingText and Images (Paper Explained) | Yannic Kilcher | https://www.youtube.com/watch?v=T9XSU0pKX2E | 48:06 | Deeper | BIKE | A paper walk-through of CLIP (title-based), the image-text model behind open-vocabulary recognition and early vision-language models in the Computer Vision lessons; a solo creator's channel, not a university. | verified; title-based |
| 7.O4 | Deep Dive into LLMs like ChatGPT | Andrej Karpathy | https://www.youtube.com/watch?v=7xTGNNLPyMI | 3:31:23 | Deeper | BIKE | The long end-to-end story (per Track B: pre-training, then post-training, then RLHF), best taken over several rides by its chapters; a case-study-style frame for the whole LLM section. | verified; content per Track B note and chapter list; also in Track B 4.4; watch once |

**Before you start:**
- Block 2 (Deep Learning) first: PyTorch, the training loop, backpropagation, transformers. The site's first lessons recap them, but its pace is unknown.
- Python at a level where you can read a training script; assignments re-implement models (cdso page), so expect to write a lot of PyTorch.
- Basic ideas of GPU memory (parameters, gradients, optimizer state, activations) help with the "Advanced Training" lessons; no video here is a prerequisite for that.
- For the generative-model lessons, Block 8 goes deeper; for instruction tuning and RLHF, Block 6 rows 6.O1 and 6.O2.

**Full circle:** you can say why training a large model needs more than one GPU and what data parallelism and ZeRO-style sharding each save, how LoRA and quantization make adaptation and serving cheaper, what FlashAttention changes about attention's memory use, how a base model becomes an instruction-following assistant, and why speculative decoding speeds up generation without changing the output distribution.

<details>
<summary>Recap questions (3)</summary>

1. Q: Why does LoRA make fine-tuning cheaper, and what is actually trained? A: The pre-trained weights stay frozen and two small low-rank matrices are trained whose product is added to selected weight matrices, so far fewer parameters need gradients and optimizer state; the adapter can be merged into the weights or swapped out.
2. Q: What does FlashAttention change, and what does it leave unchanged? A: It computes exact attention in tiles that fit in fast on-chip memory and avoids writing the full attention matrix to GPU main memory; the numerical result is the same as standard attention, with less memory traffic.
3. Q: How can speculative decoding speed up generation without changing the output distribution? A: A small draft model proposes several tokens, the large model checks them in one parallel pass, and an acceptance rule keeps those consistent with the large model's own distribution; on average more than one token is produced per large-model pass.
</details>

---

## Block 8: Advances in Deep Generative Models

**Why it matters for the stack:** this is the elective closest to generation itself: autoregressive models are the LLM family, diffusion and flow models drive image and video generators, and VAE latent spaces sit inside both; for an architect it explains what each family costs to train and to sample from, though the course covers modelling rather than serving or application stacks.

**Official description and outline:** Per the cdso page (instructor listed: Qiang Liu, Computer Science), modern techniques for generative modelling, with implementation in PyTorch or JAX. Outline with the page's week counts: overview of probabilistic modelling (1 week); energy-based models (2); generative adversarial networks (2); invertible and flow-based models (2); autoencoder models (1); diffusion generative models (2); autoregressive language models (1).

**Handbook (2027-2028):** AI 395T, titled "Advances in Generative Models". The handbook describes the theory and practice of deep generative models, including GANs, VAEs and diffusion models, and says "ML and DL should be taken first". It does not mention energy-based models, flows or autoregressive language models, which the cdso outline above does. Qiang Liu is on the faculty list.

**Public materials:**
- **Instructor's own tutorial (UT page):** Qiang Liu, "Rectified Flow" (© 2022), a Jupyter Book: https://www.cs.utexas.edu/~lqiang/rectflow/html/intro.html. Sections: learning transport maps, the rectified-flow method, reflow for fast generation with straight flows, nonlinear rectified flows, diffusion models, optimal transport. Two Colab notebooks are linked, no video. His UT homepage (Block 1) lists no generative-models course materials.
- **Stanford CS236 Deep Generative Models (Fall 2023, Stefano Ermon):** https://deepgenerativemodels.github.io/. The notes index (https://deepgenerativemodels.github.io/notes/index.html) lists chapters on the introduction, autoregressive models, variational autoencoders, normalizing flow models and GANs; I saw no chapter on energy-based or score-based models there. The page says recordings go on Canvas, so assume the videos are behind a Stanford login except what Stanford Online posts (see 8.O1).
- **MIT 6.S184 Introduction to Flow Matching and Diffusion Models (a different course, not UT):** the 2025 page https://diffusion.csail.mit.edu/2025/index.html lists six lectures (flow and diffusion models, constructing a training target, training flow and diffusion models, building an image generator, and two guest lectures) with a YouTube link for each, and the 2026 page https://diffusion.csail.mit.edu/2026/index.html adds score matching, classifier-free guidance, latent spaces and discrete diffusion. Free lecture notes by Peter Holderrieth and Ezra Erives are at https://diffusion.csail.mit.edu/docs/lecture-notes.pdf (the file I opened is the 2026 edition, with sections on flow matching, score matching, guidance, large-scale image and video generators with VAE latent spaces, and discrete diffusion).
- **UT Deep Learning Group "Advances in Deep Learning" (Block 7, a different course):** its Generative Models section has lessons on VAEs, GANs, flow-based models, auto-regressive generation, vector quantization, DALL-E, diffusion, latent diffusion and "Which generative model should I use?", with slides: https://ut.philkr.net/advances_in_deeplearning/generative_models/.
- **Blog post, free:** Lilian Weng, "What are Diffusion Models?" (2021): https://lilianweng.github.io/posts/2021-07-11-diffusion-models/ (sections on forward and reverse diffusion, training loss, guidance, speed-ups, architectures).
- No public site or lecture videos for the online course itself were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.1 | But how do AI images and videos actually work? \| Guest video by Welch Labs | 3Blue1Brown | https://www.youtube.com/watch?v=iv-5mZ_9CPY | 37:20 | Start | BIKE | A visual explanation of how AI image generators work (diffusion family, by title); a first picture before the overview week. | verified; title-based; also in Track B 8.1 (also used in Block 2, row 2.O3); watch once |
| 8.2 | 05L – Joint embedding method and latent variable energy based models (LV-EBMs) | Alfredo Canziani (冷在) | https://www.youtube.com/watch?v=xIn-Czj1g2Q | 1:51:31 | Scholar | BIKE | A lecture on latent-variable energy-based models, apparently from Alfredo Canziani's NYU deep learning course (the title does not name the course); the closest verified match to the energy-based-models weeks, but by title it is about joint embedding and latent-variable EBMs, not EBMs in general. Slide-heavy; weak row. | verified; title-based |
| 8.3 | Generative Adversarial Networks (GANs) - Computerphile | Computerphile | https://www.youtube.com/watch?v=Sw9r8CL98N0 | 21:21 | Start | BIKE | The generator-versus-discriminator idea (title-based). | verified; title-based; also in Track B 8.2 (also used in Block 2, row 2.O4); watch once |
| 8.4 | What are Normalizing Flows? | Ari Seff | https://www.youtube.com/watch?v=i7LjDvsLWCg | 12:30 | Deeper | BIKE | Invertible transformations as generative models, by title; the introduction to the flow-based weeks. | verified; title-based |
| 8.5 | Variational Autoencoders - EXPLAINED! | CodeEmporium | https://www.youtube.com/watch?v=fcvYpzHmhvA | 17:36 | Deeper | BIKE | Autoencoders and the variational twist (title-based). | verified; title-based; also in Track B 8.3; watch once |
| 8.6 | MIT 6.S184: Flow Matching and Diffusion Models - Lecture 01 - Generative AI with SDEs (2025) | Peter Holderrieth | https://www.youtube.com/watch?v=GCoP2w-Cqtg | 1:25:11 | Deeper | DESK | Per the MIT course page: generative-model basics, ODEs and SDEs, and sampling, the base of the diffusion and flow weeks; pause for the maths and keep the lecture notes open. | verified; content per MIT 6.S184 2025 course page (lecture list) and the title |
| 8.7 | MIT 6.S184: Flow Matching and Diffusion Models - Lecture 04 - Building an Image Generator (2025) | Peter Holderrieth | https://www.youtube.com/watch?v=nfrZ30mnwP0 | 1:24:26 | Deeper | BIKE | Per the MIT course page: guidance and conditional generation, network architectures and a survey of state-of-the-art generators; the most architect-relevant lecture of the series. | verified; content per MIT 6.S184 2025 course page (lecture list) and the title |

Autoregressive language models, the last topic of the course, are covered by Block 6 (rows 6.2 and 6.3), Block 2 (row 2.6) and optional row 8.O4. MIT lectures 2 and 3 (constructing a training target; training flow and diffusion models) carry the maths between 8.6 and 8.7; 8.O3 lists lecture 3.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.O1 | Stanford CS236: Deep Generative Models I 2023 I Lecture 1 - Introduction | Stanford Online | https://www.youtube.com/watch?v=XZ0PMRWXBEU | 57:27 | Scholar | DESK | A university introduction to the families of generative models; a full, formal lecture for the overview week (title-based). | verified; title-based; also in Track B 8.O1; watch once |
| 8.O2 | Generative Modeling by Estimating Gradients of the Data Distribution - Stefano Ermon | Institute for Advanced Study | https://www.youtube.com/watch?v=8TcNXi3A5DI | 1:20:59 | Scholar | BIKE | A talk by Stefano Ermon (the CS236 instructor above) on score-based generative modelling (title-based); the line of work that diffusion models grew out of, per my background knowledge. | verified; title-based |
| 8.O3 | MIT 6.S184: Flow Matching and Diffusion Models - Lecture 03 - Training Flow/Diffusion Models (2025) | Peter Holderrieth | https://www.youtube.com/watch?v=HhfLo1_yza4 | 1:16:14 | Scholar | DESK | Per the MIT course page: flow matching, score matching and diffusion approaches; it builds on lecture 2 (see Gaps for its ID). Keep the notes open. | verified; content per MIT 6.S184 2025 course page (lecture list) and the title |
| 8.O4 | Let's build GPT: from scratch, in code, spelled out. | Andrej Karpathy | https://www.youtube.com/watch?v=kCc8FmEb1nY | 1:56:20 | Scholar | DESK | Code a tiny autoregressive transformer language model, the course's last topic (title-based). | verified; title-based; also in Track B 4.O3; watch once |

**Before you start:**
- Probability and Gaussians, expectation, and the idea of maximum likelihood (Track A Blocks 4 and 5; Block 1 rows 1.5 and 1.6 for EM and MAP).
- A feel for KL divergence and for a loss as a likelihood bound; no video here is dedicated to it.
- Block 2 (PyTorch, convolutions, transformers); the course implements models in PyTorch or JAX (cdso page).
- Block 7's Generative Models section gives a second, UT-flavoured pass if you take Advances in Deep Learning first.

**Full circle:** you can say in one sentence how each family generates (EBM: low energy means likely, sampled by iterative search; GAN: adversarial game; flow: invertible map from noise; VAE: decode a sampled latent; diffusion and flow matching: integrate a learned vector field from noise to data; autoregressive: next token), which ones give exact likelihoods, and why diffusion needs many sampling steps unless distilled or straightened.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is the ELBO and where is it used? A: A lower bound on the log-likelihood: the expected reconstruction term under the encoder's distribution minus the KL divergence from that distribution to the prior. VAEs maximize it directly, and the diffusion training loss can be derived from a similar variational bound.
2. Q: Why can a normalizing flow give exact likelihoods, and what does that cost? A: It is an invertible map with a tractable Jacobian determinant, so log p(x) = log p(z) + log |det J| by the change-of-variables rule; every layer must be invertible with a cheap determinant, which constrains the architecture.
3. Q: How do diffusion and flow matching relate? A: Both learn a time-dependent field (a noise or score predictor, or a velocity) that carries samples from noise to data. Diffusion simulates a reverse SDE or ODE built from a noise schedule; flow matching regresses a velocity along chosen paths, such as straight lines, which can allow fewer sampling steps.
</details>

---

## Block 9: Case Studies in Machine Learning

**Why it matters for the stack:** the link to GenAI engineering is weak: the page describes a broad applied machine-learning course (data preparation, supervised and unsupervised methods, reports and client-style presentations) with housing and transportation examples, and mentions no deep learning or language models; what carries over is the discipline of data preparation, iteration and reporting.

**Official description and outline:** Per the cdso page (instructor listed: Junfeng Jiao, School of Architecture), a broad introduction to the principles and paradigms of machine learning, with applications in housing-market analysis and transportation. **The page lists no syllabus or topic outline**, only a "What You Will Learn" list: ML terminology; the most common ML methods; how to prepare datasets; supervised versus unsupervised learning; script implementation in Python or R; applying software, interpreting results and refining and tuning supervised models on real-world datasets; discussing important ML papers; applying ML to real problems and presenting to "mini clients"; writing reports that relate results to aims, methods and data. The page lists no prerequisites.

**Handbook (2027-2028):** AI 391M. The handbook description matches the cdso page in substance: a broad introduction to machine learning with applications such as housing-market analysis and transportation, and a real-world data analysis problem. Junfeng Jiao, the instructor named by the cdso page, is not on the handbook's faculty list, so check the instructor when the course is announced.

**Public materials:**
- **Textbook, free PDFs from the authors:** Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani (Python edition with Jonathan Taylor), *An Introduction to Statistical Learning*, in an R edition (2nd edition) and a Python edition (ISLP): https://www.statlearning.com/ (the page offers both as free PDFs and states "All Rights Reserved"; I did not open the PDFs). Applied and example-driven; I did not check how it maps to this course.
- **Dataset and API reference:** the scikit-learn page for the California housing dataset, 20,640 samples and 8 features, target the median house value: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html (documentation for scikit-learn 1.9.1). Housing regression is the course's named theme; the page does not say the course uses this dataset.
- The cdso page links only to the instructor's faculty profile; no course site, syllabus or lecture videos were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 9.1 | Supervised vs. Unsupervised Learning | IBM Technology | https://www.youtube.com/watch?v=W01tIRP_Rqs | 7:08 | Start | BIKE | A short explainer on supervised learning (classification, regression) versus unsupervised learning (clustering, association, dimensionality reduction); the distinction the course page names. | verified; content per tubescript transcript page; also in Track B G1; watch once |
| 9.2 | Machine Learning Fundamentals: Cross Validation | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=fSytzGwwBVw | 6:04 | Start | BIKE | Train and test splits and cross-validation: how to estimate performance on unseen data and tune a model, the "refine and tune" skill on the page (title-based). | verified; title-based; also in Track B 1.3; watch once |
| 9.3 | Decision and Classification Trees, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=_L39rN6gz7Y | 18:08 | Start | BIKE | How a tree picks its splits (title-based): a common method for tabular problems such as housing data. | verified; title-based; also in Track B 2.3; watch once |
| 9.4 | A Chat with Andrew on MLOps: From Model-centric to Data-centric AI | DeepLearningAI | https://www.youtube.com/watch?v=06-AZXmwHjo | 1:00:10 | Deeper | BIKE | A conversation about moving effort from tuning the model to improving the data (title-based); fits the page's "prepare datasets correctly" goal. | verified; title-based |
| 9.5 | House Price Prediction in Python - Full Machine Learning Project | NeuralNine | https://www.youtube.com/watch?v=Wqmtf9SA_kk | 40:39 | Start | DESK | Demo, title only: an end-to-end house-price project in Python, a template for the course's housing theme. I could not read the watch page, so I do not know the dataset or methods; an independent programming channel I did not vet. | verified; title-based |
| 9.6 | Paweł Gora: Applications of machine learning in traffic optimization | ML in PL | https://www.youtube.com/watch?v=gTOum29eEy0 | 1:11:18 | Deeper | BIKE | A talk, by title, on machine learning for traffic optimization, the nearest verified match to the transportation theme; from a community channel named ML in PL. I could not read the watch page, so I do not know the methods or the speaker's affiliation. | verified; title-based |

There is no verified video on writing reports or presenting results to a client, two outcomes the page lists.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 9.O1 | Linear Regression, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=7ArmBVF2dCs | 27:26 | Start | BIKE | Least-squares line fitting; watch before 9.5 if regression is rusty (title-based). | verified; title-based; also in Track B 2.O1; watch once |
| 9.O2 | StatQuest: K-means clustering | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=4b5d3muPQmA | 8:30 | Start | BIKE | The k-means loop, the standard first unsupervised method (title-based). | verified; title-based; also in Track B 2.9 (also used in Block 1, row 1.O1); watch once |
| 9.O3 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Start | BIKE | PCA walked through step by step, the other standard unsupervised method (title-based). | verified; title-based; also in Track B 2.7 and Track A #19 (also used in Block 1, row 1.O2); watch once |
| 9.O4 | Machine Learning for Everybody – Full Course | freeCodeCamp.org | https://www.youtube.com/watch?v=i_LwzRVP7bg | 3:53:53 | Start | DESK | Demo, not a ride: per the chapter list, Python implementations of common methods (regression, classification, clustering); take the chapters that match your week (see Block 1, row 1.7). | verified; content per watch-page description and chapter list; also used in Block 1, row 1.7; watch once |

**Before you start:**
- Python (or R; the page names both) with a data-frame library such as pandas, and a notebook to work in.
- Train, validation and test sets, overfitting and a loss function (Track B Block 1).
- Block 1's rows 1.2 and 1.3 (gradient descent, logistic regression), since the first half of the course repeats them.

**Full circle:** you can take a tabular dataset from raw file to a tuned, cross-validated model, say how you avoided leaking test information, choose between a supervised and an unsupervised approach for a housing or traffic question, and summarize the result in a short report that states aims, methods, data and limits.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is data leakage, and how does it show up in a housing-price project? A: Information from the test period or from the target sneaks into the features or into preprocessing (for example, scaling on the full dataset before splitting, or using a feature computed from the sale price), which inflates test scores; split first and fit every preprocessing step on the training part only.
2. Q: Why use cross-validation instead of one train and test split when tuning a model? A: One split gives a noisy estimate that depends on which rows landed in the test set; k-fold cross-validation averages over several splits, which gives a steadier estimate for choosing hyperparameters, at the cost of training k times.
3. Q: Give one housing-market question for a supervised method and one for an unsupervised method. A: Supervised: predict a home's sale price from its features (regression). Unsupervised: group neighbourhoods by their price, size and demographic profile (clustering) without a target label.
</details>

---

## Block 10: Optimization

**Why it matters for the stack:** gradients, convexity, duality and the convergence of gradient methods are the theory behind every optimizer used in training; the course is mostly convex theory and linear programming, while deep networks are not convex, so the link to building a GenAI stack is indirect.

**Official description and outline:** Per the cdso page (instructors listed: Sujay Sanghavi and Constantine Caramanis, Electrical and Computer Engineering), linear programming and convex optimization: duality, constrained and unconstrained methods, and variants of gradient descent. Twelve one-week topics: convex sets, functions and programs; linear programs, their geometry and duality; weak and strong duality and complementary slackness; applications of LP duality (robust LP, two-person zero-sum games, max-flow min-cut); semidefinite programming and duality in convex programs; sensitivity, KKT conditions and maximum entropy; SVMs, the kernel trick, conjugates and gradient descent; line search and gradient-descent convergence; Frank-Wolfe, coordinate descent and subgradients; subgradient descent, proximal gradient and Newton's method; Newton convergence, quasi-Newton methods and the barrier method; accelerated gradient descent, SGD, mini-batches and variance reduction.

**Handbook (2027-2028):** AI 388J. The handbook matches the cdso page (linear programming and convex optimization, duality, gradient descent variants) and also names second-order cone and semidefinite programming, the Newton method and momentum methods. Constantine Caramanis is on the faculty list; Sujay Sanghavi is not.

**Public materials:**
- **Instructor's recorded second course (on-campus version of a different course, "Optimization II: Algorithms for Large Scale Convex Optimization", last taught Spring 2020; may differ from the online course):** Constantine Caramanis's teaching page https://caramanis.github.io/teaching links the YouTube playlist "Optimization Algorithms", 58 videos, described as "Lectures on Algorithms for Convex Optimization -- a second course in Optimization": https://www.youtube.com/playlist?list=PLXsmhnDvpjORzPelSDs0LSDrfJcqyLlZc. It matches the algorithm half of the outline; I could read only two of its titles (rows 10.5 and 10.O3). The same page lists his "Optimization I" (last taught Fall 2024) with no site, notes or videos.
- **Instructor's page:** Sujay Sanghavi's teaching page lists ECE381V Optimization (Fall 2018 and Fall 2014) with no links: https://sites.utexas.edu/sanghavi/teaching.
- **Stanford EE364A Convex Optimization I (Boyd):** https://web.stanford.edu/class/ee364a/ links the textbook (Boyd and Vandenberghe, *Convex Optimization*), a full slide set and supplementary notes such as a CVXPY tutorial; I did not open the book or slide links (the book's own page could not be fetched in this session). The Stanford Engineering Everywhere page https://see.stanford.edu/Course/EE364A lists 19 lectures with durations (it does not state the term), which I use for rows 10.2 to 10.4 and 10.O2.
- **CMU 10-725 Convex Optimization (Spring 2015, Ryan Tibshirani):** https://www.stat.cmu.edu/~ryantibs/convexopt-S15/. The page lists 27 sessions with notes PDFs (gradient descent, subgradients, proximal gradient and acceleration, LP and general duality, KKT, Newton, barrier and interior-point methods, coordinate descent, conditional gradient, fast stochastic methods) and says each lecture links to a YouTube video; I did not extract those video IDs.
- No public site or videos for the online course itself were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 10.1 | Convexity 101 [Optimization Bootcamp] | Steve Brunton | https://www.youtube.com/watch?v=9WXVgQFFsDI | 14:57 | Deeper | BIKE | A first look at convex sets and functions and why convexity makes optimization easy; the on-ramp to week 1 (title-based). | verified; title-based; also in Track A #41; watch once |
| 10.2 | Lecture 5 \| Convex Optimization I (Stanford) | Stanford | https://www.youtube.com/watch?v=Ry5i8DGZrJs | 1:16:10 | Deeper | DESK | Convex optimization problems, per the SEE lecture list (the YouTube title carries only the number; I assume the numbering matches); Boyd's class lecture, so pause and work along. | verified; content per SEE lecture list and the title |
| 10.3 | Lecture 8 \| Convex Optimization I (Stanford) | Stanford | https://www.youtube.com/watch?v=FJVmflArCXc | 1:16:30 | Scholar | DESK | Duality, per the SEE lecture list: the weak and strong duality weeks of the outline. | verified; content per SEE lecture list and the title |
| 10.4 | Lecture 9 \| Convex Optimization I (Stanford) | Stanford | https://www.youtube.com/watch?v=3Q9mMluX3Gw | 1:16:35 | Scholar | DESK | Duality continued, with KKT conditions and sensitivity analysis, per the SEE lecture list: the outline's "Duality and Sensitivity, KKT" week. | verified; content per SEE lecture list and the title |
| 10.5 | 1.1 Introduction | Constantine Caramanis | https://www.youtube.com/watch?v=G27vjNQUoh4 | 15:58 | Deeper | BIKE | The opening lecture of Caramanis's recorded "Optimization Algorithms" playlist (a second course in optimization, per the playlist description; on-campus recording, may differ). Title only; he is also an instructor listed on the cdso page. | verified; content per playlist description and the title |
| 10.6 | Stochastic Gradient Descent, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=vMh0zPT0tLI | 10:53 | Start | BIKE | Why a random subset of the data per step still works: the SGD and mini-batch week (title-based). | verified; title-based; also in Track A #40; watch once |

No verified video covers the geometry of linear programs, LP-duality applications (zero-sum games, max-flow min-cut), semidefinite programming, quasi-Newton methods, the barrier method or variance reduction; the textbook and the CMU notes above are the route for those.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 10.O1 | Convexity Implies that Local Minima are Global Minima | Steve Brunton | https://www.youtube.com/watch?v=D-Qy9QfJgQg | 20:25 | Deeper | BIKE | The short argument for why convexity is such a strong property, after 10.1 (title-based). | verified; title-based; also in Track A optional extras (Block 6); watch once |
| 10.O2 | Lecture 1 \| Convex Optimization I (Stanford) | Stanford | https://www.youtube.com/watch?v=McLq1hEq3UY | 1:20:32 | Deeper | DESK | Boyd's introduction to the class, per the SEE lecture list; useful before 10.2 if you want the framing. Track A also lists the 2023 Lecture 1 (kV1ru-Inzl4). | verified; content per SEE lecture list and the title |
| 10.O3 | 5.12 Frank Wolfe | Constantine Caramanis | https://www.youtube.com/watch?v=tIywqa-OgoI | 33:32 | Scholar | DESK | The Frank-Wolfe method, a topic in the outline, from Caramanis's recorded course (title only; the number looks like chapter 5, lecture 12 of the playlist, my inference). | verified; title-based |
| 10.O4 | L12.3 SGD with Momentum | Sebastian Raschka | https://www.youtube.com/watch?v=gMxvefj0YAM | 9:04 | Deeper | BIKE | Momentum added to SGD, the first step toward the accelerated methods in the last week (title-based). | verified; title-based; also in Track A G5; watch once |

**Before you start:**
- Multivariable calculus (gradient, Hessian) and linear algebra (eigenvalues, positive semidefinite matrices); Track A Blocks 2, 3 and 6.
- Track A Block 6 for gradient descent and SGD intuition (rows #38 to #40).
- Comfort with proofs: the outline is theorem-driven (duality, convergence rates), so expect to write short arguments by hand.

**Full circle:** you can say what makes a set or function convex, write a linear program and its dual, state weak duality and the KKT conditions, say how step size and strong convexity control gradient-descent convergence, and explain why SGD trades per-step cost against noise.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does weak duality say, and when does strong duality hold? A: The dual optimal value is never greater than the primal optimal value (for minimization), so any dual feasible point gives a lower bound; strong duality (equal values) holds for linear programs when the primal is feasible and bounded, and for convex programs under a condition such as Slater's.
2. Q: What are the KKT conditions? A: Primal feasibility, dual feasibility (nonnegative multipliers for inequalities), complementary slackness (each multiplier times its constraint is zero) and stationarity of the Lagrangian; for convex problems with strong duality they are necessary and sufficient for optimality.
3. Q: Why does gradient descent on a smooth convex function use a step size of about 1/L, and what does strong convexity add? A: L is the gradient's Lipschitz constant, and a step of 1/L guarantees the objective decreases each iteration; with only convexity the error shrinks like 1/k, while strong convexity gives a faster geometric (linear) rate.
</details>

---

## Block 11: Online Learning and Optimization

**Why it matters for the stack:** regret and bandit algorithms are the maths of choosing between options while learning from feedback, which shows up in online experimentation and in routing requests between models (my inference, not stated on the cdso page); the course itself is proof-heavy theory, so treat the link to building a stack as weak to moderate.

**Official description and outline:** Per the cdso page (instructors listed: Constantine Caramanis and Sanjay Shakkottai, Electrical and Computer Engineering), two themes: algorithms for convex optimization and algorithms for online learning. Optimization part: convexity, smoothness and strong convexity; first-order optimality; gradient and subgradient descent; oracle lower bounds; accelerated, proximal and projected methods (ISTA, FISTA); mirror descent; Frank-Wolfe; stochastic gradient descent. Online part: stochastic bandits (explore and commit, UCB, regret analysis); adversarial bandits (exponential weighting, Exp3); bandit lower bounds; contextual bandits (Exp4, LinUCB); online linear optimization; follow the leader and follow the regularized leader; online classification (halving, weighted majority, perceptron, Winnow); other topics (combinatorial bandits, pure exploration, Bayesian bandits and Thompson sampling, Newton and quasi-Newton methods).

**Handbook (2027-2028):** AI 388K. Two themes, as on the cdso page: algorithms for large-scale convex optimization with a machine-learning focus, then online learning. Constantine Caramanis and Sanjay Shakkottai are both on the faculty list.

**Public materials:**
- **Textbook, free on arXiv:** Elad Hazan, *Introduction to Online Convex Optimization*, 2nd edition (arXiv v3, August 2023): https://arxiv.org/abs/1909.05207 (the abstract page loaded with the book's text; it covers expert advice, regret, mirror descent and applications).
- **Textbook, free online edition:** Tor Lattimore and Csaba Szepesvári, *Bandit Algorithms*: https://tor-lattimore.com/downloads/book/book.pdf (the PDF says it is the free online edition; parts on stochastic, adversarial, contextual and linear bandits and on lower bounds).
- **A near-match course (other university, public schedule):** Yu-Xiang Wang, UCSB CS292F Convex Optimization, Spring 2020: https://sites.cs.ucsb.edu/~yuxiangw/classes/CS292F-2020Spring/. Its schedule covers gradient descent, subgradient and proximal methods, SGD, duality, Newton's method, then online learning (expert advice, online gradient descent, follow the regularized leader, online Newton), with readings from Boyd and Vandenberghe and from Hazan. The page links no videos; YouTube lectures of this course turned up in search but failed the oEmbed check, so I list none.
- **Bandit lectures (University of Bristol, "Stochastic Optimisation", Ayalvadi Ganesh and Vladislav Tadic):** https://people.maths.bris.ac.uk/~maajg/stoch_opt.html. Notes on the introduction, the UCB algorithm and Thompson sampling; the first half of the unit covers multi-armed bandits, based on the books by Bubeck and Cesa-Bianchi and by Lattimore and Szepesvári; the page links a YouTube channel of recorded lectures and warns that they "may not map 1-1" to the in-person ones (rows 11.4 and 11.5).
- **Optimization half:** Caramanis's recorded optimization playlist and the CMU and Stanford materials in Block 10.
- No public site was found for the online course itself or for Sanjay Shakkottai's teaching.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 11.1 | Stochastic Gradient Descent, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=vMh0zPT0tLI | 10:53 | Start | BIKE | Why a random subset of the data per step still works: the SGD topic of the optimization half (title-based). | verified; title-based; also in Track A #40 (also used in Block 10, row 10.6); watch once |
| 11.2 | 5.12 Frank Wolfe | Constantine Caramanis | https://www.youtube.com/watch?v=tIywqa-OgoI | 33:32 | Scholar | DESK | The Frank-Wolfe topic of the outline, from a recorded course by an instructor listed on the cdso page (title only; on-campus recording, may differ). | verified; title-based; also used in Block 10, row 10.O3; watch once |
| 11.3 | DeepMind x UCL RL Lecture Series - Exploration & Control [2/13] | Google DeepMind | https://www.youtube.com/watch?v=aQJP3Z2Ho8U | 2:10:13 | Deeper | BIKE | Per the title, exploration and control: the bandit setting and exploration versus exploitation, the gentle entry to the bandit weeks. | verified; title-based; also in Track B 5.2 (also used in Block 3, row 3.2); watch once |
| 11.4 | Lecture 3: The UCB algorithm | Ayalvadi Ganesh | https://www.youtube.com/watch?v=nFabqFcCH7U | 37:59 | Deeper | DESK | The UCB algorithm, matched by title to the Bristol unit's "The UCB algorithm" notes (the page says the videos may not map 1-1 to lectures); pause to follow the argument. | verified; content per Bristol course page (notes list) and the title |
| 11.5 | Lecture 4: Analysis of the UCB algorithm | Ayalvadi Ganesh | https://www.youtube.com/watch?v=Fuwzv1iM3Mc | 53:18 | Scholar | DESK | The regret analysis of UCB (title-based), the proof the outline calls "UCB algorithm and regret analysis"; assumes 11.4. | verified; content per Bristol course page (notes list) and the title |
| 11.6 | Online Learning and Online Convex Optimization I | Simons Institute for the Theory of Computing | https://www.youtube.com/watch?v=C26gciixFHk | 44:15 | Scholar | BIKE | Nicolò Cesa-Bianchi (University of Milan) at a Simons Institute boot camp in August 2016; per the abstract on the Simons page: online convex optimization as a framework for online learning, regret and regularization, Mirror Descent, AdaGrad and Online Newton Step. | verified; content per Simons Institute talk page abstract |

No verified video covers Exp3 and adversarial bandits, Exp4 and LinUCB, Thompson sampling, the halving and weighted-majority algorithms, Perceptron and Winnow, oracle lower bounds, or ISTA and FISTA.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 11.O1 | Introduction to Online Learning | Theja Tulabandhula | https://www.youtube.com/watch?v=sxObOjrBBfU | 1:27:47 | Start | BIKE | An introduction to online learning, by title only, from an individual lecturer's channel I did not vet; a first pass before 11.6 if regret is new. | verified; title-based |
| 11.O2 | 1.1 Introduction | Constantine Caramanis | https://www.youtube.com/watch?v=G27vjNQUoh4 | 15:58 | Deeper | BIKE | The opening lecture of Caramanis's recorded optimization course (title only), for the first half of this course as for Block 10. | verified; content per playlist description and the title; also used in Block 10, row 10.5; watch once |

**Before you start:**
- Block 10's convexity and gradient-descent rows (10.1, 10.6), and basic probability and expectation (Track A Block 4).
- The idea of regret: your cumulative loss minus that of the best fixed choice in hindsight. Hazan's book and 11.6 define it formally.
- Comfort reading short proofs; the outline is analysis-heavy (regret bounds, lower bounds).

**Full circle:** you can define regret and say what sublinear regret means, explain how UCB balances exploration and exploitation, say how online gradient descent and mirror descent achieve low regret, and name the difference between stochastic and adversarial feedback.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is regret, and what does it mean for it to be sublinear? A: Regret is the learner's cumulative loss minus the cumulative loss of the best fixed action in hindsight; sublinear regret means the average regret per round goes to zero, so the learner eventually performs as well as that best action.
2. Q: How does the UCB algorithm balance exploration and exploitation? A: It plays the arm with the highest upper confidence bound, the empirical mean plus a bonus that shrinks as the arm is pulled more; rarely tried arms keep a large bonus and get explored, while arms that look good and are well measured get exploited.
3. Q: Why does online gradient descent get regret of order the square root of T on convex, Lipschitz losses over a bounded set? A: With a step size proportional to 1 over the square root of T, the movement and the gradient-noise terms in the standard analysis balance at order the square root of T; SGD for stochastic optimization inherits the same rate by averaging.
</details>

---

## Block 12: Automated Logical Reasoning

**Why it matters for the stack:** the link to GenAI engineering is weak: this is classical computational logic (SAT and SMT solving, first-order theorem proving, software verification), not machine learning; the slivers that connect are checking program or specification correctness, constraint solving, and symbolic reasoning tools that an agent could call, and those connections are my inference, not something the course page says.

**Official description and outline:** Per the cdso page (instructor listed: Işıl Dillig, Computer Science), computational logic and its applications in computer science, particularly software verification, covering logical theories and satisfiability algorithms. Outline with the page's durations: normal forms, decision procedures for propositional logic and SAT solvers (2 weeks); applications of SAT solvers and binary decision diagrams (1); semantics of first-order logic and its theoretical properties (1); first-order theorem proving (1.5); introduction to first-order theories (0.5); the theory of equality (0.5); decision procedures for rationals and integers (1.5); the DPLL(T) framework and SMT solvers (1); basics of software verification (1); automating software verification (2).

**Handbook (2027-2028):** AI 389L. Matches the cdso page: computational logic and its use in software verification, logical theories and satisfiability algorithms. Işıl Dilig is on the faculty list.

**Public materials:**
- **UT course page (on-campus version, "ALR Spring 2021", Işıl Dillig; may differ from the online course):** https://cs.utexas.edu/~isil/cs389L. The syllabus runs from propositional logic, normal forms, DPLL, CDCL SAT solvers and BDDs, through first-order logic, unification and theorem proving, the theories of equality and of rational and integer arithmetic with Nelson-Oppen, to DPLL(T), Hoare logic, verification conditions and Dafny, and (beyond the cdso outline) abstract interpretation, predicate abstraction and CEGAR, termination, concurrency and program synthesis. It links slide PDFs (several lectures have none) and no lecture videos. Optional textbooks it names: Bradley and Manna, *The Calculus of Computation*, and Kroening and Strichman, *Decision Procedures*; I did not confirm that either is free.
- **A near-match course at another university:** Stanford CS 257 Introduction to Automated Reasoning (Winter 2026, Caroline Trippel): https://web.stanford.edu/class/cs257/. Topics: propositional logic, DPLL and CDCL, first-order logic and unification, theories and DPLL(T), SMT, and applications such as model checking and proof automation in Lean. The page says recordings are on Canvas (probably behind a Stanford login) and that the books are available through a Stanford account.
- No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 12.1 | Propositional Logic: The Complete Crash Course | TrevTutor | https://www.youtube.com/watch?v=AVl3wK2yTEc | 53:48 | Start | DESK | Propositions, truth tables, logical equivalence, conditionals and contrapositives and basic inference, per the chapter list recorded in Track A; the prerequisite for everything below. | verified; content per Track A chapter-list note; also in Track A #44; watch once |
| 12.2 | Lecture 4A: DPLL & Modern SAT Solvers | UCLA Automated Reasoning Group | https://www.youtube.com/watch?v=ki7rzvonbOs | 36:05 | Deeper | DESK | DPLL and modern SAT-solver techniques, from a university research group's channel (title-based); matches the SAT-solver weeks. Work an example on paper. | verified; title-based |
| 12.3 | Logic and Proof, Lecture 6: Clause Form Methods | Lawrence Paulson | https://www.youtube.com/watch?v=Os8vJcy0IN0 | 46:15 | Deeper | DESK | A lecture on clause-form methods, by title, from a Cambridge lecture series on the channel of Lawrence Paulson; the nearest match to "normal forms" and first-order theorem proving. I could not read the course page, so I do not know exactly what it covers. | verified; title-based |
| 12.4 | Logic and Proof, Lecture 9: Decision Procedures. Live version | Lawrence Paulson | https://www.youtube.com/watch?v=6EAAPjsoVTs | 40:37 | Scholar | DESK | A lecture on decision procedures from the same series (title-based); I do not know which procedures it covers. | verified; title-based |
| 12.5 | The Varied Forms of Verification with Z3 | Microsoft Research | https://www.youtube.com/watch?v=wHSmAThRBHg | 1:03:27 | Deeper | BIKE | The Z3 SMT solver applied to several kinds of verification (title-based); the speaker is not named in the title. The nearest match to the SMT and verification weeks. | verified; title-based |
| 12.6 | 005. Program Analysis using Efficient Satisfiability Modulo Theories Solvers - Nikolaj Bjorner | Yandex for ML | https://www.youtube.com/watch?v=HqlMSnY0b2w | 1:25:49 | Scholar | BIKE | SMT solvers applied to program analysis, by the speaker named in the title (a Z3 author, per my background knowledge); a conference-style talk (title-based). | verified; title-based |
| 12.7 | Basics of specification and verification: Lecture 1, loop invariants | Verification Corner | https://www.youtube.com/watch?v=J0FGb6PyO_k | 20:56 | Deeper | DESK | Specifications and loop invariants, the heart of the "basics of software verification" week (title-based). Write the invariants yourself before the video does. | verified; title-based |

Most of this block is DESK because the material is proof- and algorithm-heavy; none of the rows works well as pure listening except 12.5 and 12.6. No verified video covers binary decision diagrams, the theory of equality (congruence closure), decision procedures for integers, or Nelson-Oppen and DPLL(T) as such (12.2 is SAT-level; 12.5 and 12.6 are applications).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 12.O1 | Basics of specification and verification: Lecture 2, binary search | Verification Corner | https://www.youtube.com/watch?v=-_tx3lk7yn4 | 21:14 | Deeper | DESK | The next lecture in the series on 12.7: verifying a binary search (title-based). | verified; title-based |
| 12.O2 | PLSE: Leonardo de Moura, "The Lean Theorem Prover" | Paul G. Allen School | https://www.youtube.com/watch?v=69ytTKfSSgc | 1:02:02 | Scholar | BIKE | A research-seminar talk on the Lean theorem prover by the speaker named in the title (its creator and a Z3 author, per my background knowledge). It is an interactive proof assistant, adjacent to the course's automated first-order theorem proving, not part of the outline (title-based). | verified; title-based |

**Before you start:**
- Propositional logic and truth tables (row 12.1; Track A Block 7), and the proof ideas in Track A Block 7 (induction, counting).
- Some programming experience and recursion, since the algorithms are short programs; the cdso page does not say which language the assignments use.
- Graphs and trees at the level of an algorithms course; no machine-learning background is needed.

**Full circle:** you can convert a formula to CNF, run DPLL by hand and say what unit propagation and clause learning add, say what a theory solver adds in DPLL(T), write a small constraint in an SMT solver such as Z3 and read its answer, and say what a loop invariant must satisfy.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does unit propagation do in a DPLL SAT solver? A: When all but one literal of a clause are false, the remaining literal must be true, so the solver sets it and repeats; this prunes the search tree and often settles most variables without branching.
2. Q: How does DPLL(T) combine a SAT solver with a theory solver? A: The SAT solver treats theory atoms (such as x + y < 3) as Boolean variables and proposes an assignment; the theory solver checks whether that conjunction of atoms is satisfiable in the theory and, if not, returns a conflict clause that the SAT solver learns.
3. Q: What three things must be shown for a loop invariant? A: It holds before the loop starts; it is preserved by each iteration (if it holds and the loop condition is true, it holds after the body); and together with the negated loop condition it implies the postcondition.
</details>

---

## Block 13: AI in Healthcare

**Why it matters for the stack:** this is a domain course: its first half is health-IT standards and vocabularies (ICD-10, SNOMED CT, LOINC, RxNorm, FHIR, OMOP), and its second half is AI applications in health (explainable risk prediction, medical NLP, imaging, drug discovery, ethics); the link to a general GenAI stack is weak, and it becomes relevant if you design systems that handle health data, where these standards and the ethics week are the context.

**Official description and outline:** Per the cdso page (instructor listed: Ying Ding, School of Information), the major components of health IT systems (data semantics with ICD-10, interoperability with FHIR, SNOMED CT, clinical decision support), then how AI is changing health care: drug discovery, medical image diagnosis, explainable AI for health risk prediction and ethics. Thirteen topics: evidence-based care, i2b2 and OMOP; EMR semantics (ICD-10 including COVID codes and ICD-9 as used in MIMIC; SNOMED CT in two parts and SNOMED versus ICD-10; LOINC; RxNorm); clinical decision support systems; data sharing with FHIR; ML and DL for health (explainable AI and multimodal fusion); advanced medical NLP; medical imaging diagnosis; AI in drug discovery; ethics of AI in health. The page lists no prerequisites.

**Handbook (2027-2028):** AI 380H. Matches the cdso page: health IT systems (ICD-10, FHIR, SNOMED CT, clinical decision support), then drug discovery, medical image diagnosis, explainable AI for health risk prediction and ethics. Ying Ding is on the faculty list.

**Public materials:**
- **Instructor's own course pages (on-campus INF 385T "AI Health", Spring 2021; may differ from the online course):** https://yingding.ischool.utexas.edu/INF385TAIHealthSpring2021.html. Its sixteen-session schedule matches the cdso outline (MIMIC introduction; evidence-based care, i2b2 and OMOP; ICD-10, SNOMED CT, LOINC, RxNorm; clinical decision support; FHIR; ML and DL; imaging; drug discovery; final project). Recommended readings it names: Eric Topol, *Deep Medicine* (2019); Matheny and colleagues (eds.), *Artificial Intelligence in Health Care* (National Academy of Medicine, 2019); and MIT Critical Data, *Secondary Analysis of Electronic Health Records* (Springer Open). The page also points to the MIMIC-III clinical dataset on PhysioNet and lists no videos. I could not open the report, the book or the dataset links in this session.
- **Course site:** https://aihealth.ischool.utexas.edu/resources/course/resources_course.html shows the same topic list as the cdso page and no downloadable resources.
- **Public lecture series that overlaps the first topics:** MIT OpenCourseWare's "6.S897 Machine Learning for Healthcare, Spring 2019" appears as a YouTube playlist in search results (rows 13.1, 13.2 and 13.O2 are numbered lectures from it, judged by the channel and the lecture numbers, not from a page that says so); I did not open the playlist.
- No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 13.1 | 2. Overview of Clinical Care | MIT OpenCourseWare | https://www.youtube.com/watch?v=DS97JV_o0Fs | 1:20:08 | Start | BIKE | An overview of how clinical care works, by title, from a numbered MIT OpenCourseWare lecture; a plain-language background for the "evidence-based care" week. | verified; title-based |
| 13.2 | 3. Deep Dive Into Clinical Data | MIT OpenCourseWare | https://www.youtube.com/watch?v=0UFwGJe6ubg | 1:23:26 | Deeper | BIKE | A look at what clinical data contains, by title, from the next lecture in the same numbered series; the background for the EMR-semantics weeks. | verified; title-based |
| 13.3 | Tutorial: Introduction to SNOMED CT - Ian Spiers and Jon Zammit (202069) | SNOMED International | https://www.youtube.com/watch?v=ELgXwo324pk | 1:06:44 | Start | BIKE | An introductory SNOMED CT tutorial from the organization that maintains the standard (title and channel); matches the two SNOMED CT weeks. | verified; title-based |
| 13.4 | OHDSI2023 Tutorial: Introduction to OHDSI | OHDSI | https://www.youtube.com/watch?v=7-T9a8I1uN8 | 3:26:10 | Start | BIKE | An introduction to OHDSI from its own channel (title-based); that OHDSI is the community behind the OMOP common data model is my background knowledge. Matches the "i2b2 and OMOP" week. | verified; title-based |
| 13.5 | Introduction to HL7 FHIR: A Tutorial for Beginners | Dr Chris Paton - Digital Health, Informatics & AI | https://www.youtube.com/watch?v=wxXe1g2YjHo | 38:23 | Start | BIKE | A beginner's tutorial on FHIR (title-based); matches the "Data Share: FHIR" week. An individual educator's channel, not HL7 itself; I did not vet it. | verified; title-based |
| 13.6 | Week 2: Pranav Rajpurkar, Deep Learning for Radiology (Stanford ML Group) | Seminar in Artificial Intelligence in Healthcare | https://www.youtube.com/watch?v=IkngsvWgfiQ | 45:36 | Deeper | BIKE | A seminar talk on deep learning for radiology by the speaker named in the title (title-based); matches the medical-imaging week. I did not vet the channel. | verified; title-based |
| 13.7 | Regina Barzilay: AI For Drug Design - USC AI Futures Symposium on AI and Data Science 2021 | USC Information Sciences Institute | https://www.youtube.com/watch?v=LG7DocXT_8Q | 49:03 | Deeper | BIKE | A symposium talk on AI for drug design by the speaker named in the title (an MIT professor, per the title of another search result); matches the drug-discovery week. | verified; title-based |

No verified video covers ICD-10 coding, LOINC, RxNorm, clinical decision support systems, medical NLP, multimodal fusion, or the ethics of AI in health; Block 5 (ethics) is the general substitute for the last.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 13.O1 | Tutorial1Part6 -Overview of the OMOP CDM | StanfordSTARR | https://www.youtube.com/watch?v=oa-bAVHBog8 | 11:10 | Deeper | BIKE | An overview of the OMOP common data model from a Stanford group's tutorial series (title-based); a second pass after 13.4. | verified; title-based |
| 13.O2 | 4. Risk Stratification, Part 1 | MIT OpenCourseWare | https://www.youtube.com/watch?v=_shuV1tJbTU | 1:12:44 | Deeper | BIKE | Risk prediction from the same numbered series as 13.1 (title-based); the nearest verified match to "health risk prediction", though not about explanation as such. | verified; title-based |
| 13.O3 | Introduction to Interpretable Machine Learning I - Cynthia Rudin | Institute for Advanced Study | https://www.youtube.com/watch?v=nAvcQnnIvn8 | 57:18 | Deeper | BIKE | An introduction to interpretable machine learning by the speaker named in the title (title-based); general, not health-specific, and a stand-in for the explainable-AI week. | verified; title-based |

**Before you start:**
- Block 1 for ML basics (supervised learning, overfitting, evaluation) and Python for the project work; no clinical background is assumed on the cdso page.
- A first look at what an electronic health record holds (rows 13.1 and 13.2); the outline starts straight into coding systems.
- Access to the MIMIC datasets, if you want to practise on real records, goes through PhysioNet's own registration steps (the page that explains them could not be opened here).

**Full circle:** you can say what each of ICD-10, SNOMED CT, LOINC and RxNorm is used to code, what a FHIR resource is, what a common data model such as OMOP standardizes, why a medical-imaging model needs external validation, and where explainability and ethics enter a health-AI project.

<details>
<summary>Recap questions (3)</summary>

1. Q: How do SNOMED CT and ICD-10 differ? A: SNOMED CT is a detailed clinical terminology of concepts with relationships, used to record what is observed and done in care; ICD-10 is a classification that groups diagnoses into categories for statistics and billing.
2. Q: What is a FHIR resource? A: A standard, small unit of health data (for example Patient, Observation or Medication) with a defined structure, exchanged as JSON or XML through a web API so that different systems can share records.
3. Q: Why must a medical-imaging model be tested on data from other hospitals before it is trusted? A: Scanners, protocols and patient populations differ between sites, and a model can learn site-specific artefacts instead of disease, so accuracy on the development hospital's data can overstate how it performs elsewhere.
</details>

---

## Block 14: AI in Astrophysics

**Why it matters for the stack:** this is a niche, science-domain course and its link to GenAI engineering is weak; what overlaps is methodological (neural networks on large datasets, curating training data, interpretability, normalizing flows for simulation-based inference, unsupervised exploration), and none of it is about language models or products. Take it only if the subject interests you.

**Official description and outline:** Per the cdso page (instructors listed: Stella Offner, Oden Institute, and Changhoon Hahn, Department of Astronomy), practical AI skills for scientific data analysis, predictive modelling and research in the physical sciences, centred on astrophysical data; **no background in astronomy is required** (the cdso page lists no formal prerequisites; the handbook does, see the next paragraph). Five topics: applying machine learning and deep learning to astronomy data; creating and curating training sets from scientific data; explainable AI methods; simulation-based inference techniques; data exploration with unsupervised machine learning.

**Handbook (2027-2028):** AI 395T. The handbook states prerequisites that the cdso page does not: a B or higher in Machine Learning, and Deep Learning passed or taken at the same time. No astronomy background is needed (both sources agree). The course is not in the course list of the program's 2026-11-16 email, so check that it will be offered. Stella Offner is on the faculty list; Changhoon Hahn is not.

**Public materials:**
- No course site, syllabus or lectures were found, and the cdso page links only to directory pages for the instructors.
- **A research paper that shows the main topic in use:** ChangHoon Hahn and nine co-authors, "SIMBIG: A Forward Modeling Approach To Analyzing Galaxy Clustering" (arXiv 2211.00723, November 2022): https://arxiv.org/abs/2211.00723. By its abstract it applies simulation-based inference with normalizing flows, trained on 20,000 simulated galaxy samples, to galaxy power spectra. The first author has the same name as the instructor listed on the cdso page; I did not check that they are the same person.
- The documentation pages I tried for the `sbi` toolkit and for astroML could not be opened in this session, so neither is listed.

**Short prep path (this course is niche, so this is a path, not a full video list):** (1) PCA and k-means for data exploration (row 14.1; Block 9 rows 9.O2 and 9.O3); (2) a convolutional network (Block 2, row 2.5); (3) two overviews of machine learning on astronomy data (rows 14.2 and 14.3); (4) interpretability (row 14.4); (5) normalizing flows (Block 8, row 8.4, as optional row 14.O1), then simulation-based inference (rows 14.5 and 14.6).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 14.1 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Start | BIKE | PCA walked through step by step, the standard way to explore high-dimensional data (title-based); matches the unsupervised data-exploration topic. | verified; title-based; also in Track B 2.7 and Track A #19 (also used in Block 1, row 1.O2); watch once |
| 14.2 | Introduction to Machine Learning in Astronomy (Day 3) | Facultad de Cs. Astronómicas y Geofísicas - UNLP | https://www.youtube.com/watch?v=gXmVn7Gp8Yk | 1:50:50 | Deeper | BIKE | One day of an introductory course on machine learning in astronomy, from a university faculty's channel (title-based); I do not know what days 1 and 2 cover or what day 3 covers. | verified; title-based |
| 14.3 | Dr Francois Lanusse - Exploring the Cosmos with Deep Learning | The Alan Turing Institute | https://www.youtube.com/watch?v=lCxYejIzJus | 59:14 | Deeper | BIKE | A talk on deep learning applied to cosmology by the speaker named in the title (title-based); the best verified overview of the first topic. | verified; title-based |
| 14.4 | Introduction to Interpretable Machine Learning I - Cynthia Rudin | Institute for Advanced Study | https://www.youtube.com/watch?v=nAvcQnnIvn8 | 57:18 | Deeper | BIKE | An introduction to interpretable machine learning by the speaker named in the title (title-based); stands in for the explainable-AI topic. | verified; title-based; also used in Block 13, row 13.O3; watch once |
| 14.5 | Kyle Cranmer - Simulation-based Inference for Gravitational Wave Astronomy - IPAM at UCLA | Institute for Pure & Applied Mathematics (IPAM) | https://www.youtube.com/watch?v=As62uZVVXBk | 48:39 | Scholar | BIKE | A talk on simulation-based inference applied to gravitational-wave astronomy (title-based); technical, and the nearest verified match to the simulation-based-inference topic. | verified; title-based |
| 14.6 | Jakob Macke: Simulation-based inference and the places it takes us | Finnish Center for Artificial Intelligence FCAI | https://www.youtube.com/watch?v=pGN4HVjotrE | 49:02 | Scholar | BIKE | A talk on simulation-based inference by the speaker named in the title (title-based); not specific to astronomy, so it gives the general method. | verified; title-based |

No verified video is about creating and curating training sets from scientific data, the second topic.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 14.O1 | What are Normalizing Flows? | Ari Seff | https://www.youtube.com/watch?v=i7LjDvsLWCg | 12:30 | Deeper | BIKE | Invertible transformations as density models (title-based); the SIMBIG abstract says it uses normalizing flows, so this is the method behind that application. | verified; title-based; also used in Block 8, row 8.4; watch once |
| 14.O2 | Kyle Cranmer: Navigating the Design Space of Simulation-Based Inference | STAMPS@CMU Research Center | https://www.youtube.com/watch?v=2FGXAlUATs0 | 48:09 | Scholar | BIKE | A second talk on simulation-based inference by the speaker named in the title (title-based), about the choices among methods. | verified; title-based |
| 14.O3 | Week 6: Machine Learning Basics for Astronomy | BRICS Astronomy | https://www.youtube.com/watch?v=lPKZsUx4B-I | 2:12:18 | Start | BIKE | A week of a course on machine-learning basics for astronomy, from a channel I did not vet (title-based); I do not know the course or the level. | verified; title-based |

**Before you start:**
- Block 1 (supervised and unsupervised learning, overfitting) and Python with NumPy; no astronomy is required per the cdso page.
- Probability: likelihood, posterior and Bayes' rule (Track A Blocks 4 and 5) for the simulation-based-inference topic.
- A convolutional network and the idea of a training loop (Block 2) for the deep-learning-on-images topic.

**Full circle:** you can say how PCA and clustering help explore a large survey, why a model trained on simulations can fail on real observations, what simulation-based inference does when the likelihood cannot be written down, and what a feature-attribution method does and does not tell you.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is simulation-based inference, and why use it? A: When you can simulate data from parameters but cannot write the likelihood, you train a neural density estimator (for example a normalizing flow) on many simulated (parameter, data) pairs so that, given real data, it returns an approximate posterior over the parameters.
2. Q: Why is the choice of training set critical in scientific machine learning? A: Simulations differ from real observations (noise, selection effects, missing physics), so a model that learns the simulator's quirks fails on real data; training sets must be curated and checked for this domain shift, and class imbalance and labelling errors matter too.
3. Q: What does a feature-attribution method such as SHAP tell you, and what does it not? A: It tells you which inputs the trained model relied on for a prediction; it does not show that the model's reasoning is physically correct or causal, so attributions should be checked against domain knowledge.
</details>

---

## Block 15: Agentic Software Engineering

**Why it matters for the stack:** by title this is the one course about building software with AI coding agents, which is the coding-plus-AI half of the goal of designing GenAI systems for large companies; the agent, tool and reliability ideas it likely uses are covered from the system-design side in Track G Block 7. Treat that as a guess from the title: the handbook gives no description.

**Official description and outline:** the handbook (2027-2028) lists "Agentic Software Engineering - AI 395T (3 SCH)" in the course listing and again in the elective list, with no description, no instructor and no prerequisite. The cdso page does not list the course. A program email of 2026-11-16 includes it among the courses running in Spring 2027.

**Handbook (2027-2028):** title only. Emmett Witchell (spelled Witchel on the course page), who is on the handbook's faculty list, teaches an on-campus course of the same name (below); I could not confirm that he teaches the online one.

**Public materials:**
- **A related on-campus course page (not confirmed to be this course):** "CS 378 Agentic Software Engineering", Fall 2026, instructor Emmett Witchel: https://www.cs.utexas.edu/~witchel/378AC/ . It is numbered as an undergraduate class and does not mention AI 395T or the online MSAI. Per the page it treats working with AI coding agents as a skill to practise: students learn to decompose a problem into what they specify, what they delegate and what they verify, do several homeworks with AI assistance and build a final project alone or in a pair, and it also covers secrets management, source control, cloud services and crash-safe workflows. Class time by share: agent tools and architecture 30%, systems (fault tolerance, concurrency, recovery, backpressure and rate limiting) 25%, software engineering 20%, tooling and workflow 15%, how AI models work 10%. Prerequisites listed: systems programming at the level of CS 439, proficiency in one language (Python preferred), and familiarity with git and the command line; no AI or machine-learning background is required. Tools: Codex and Claude Code through university accounts. No textbook is listed. Grading: homeworks 58%, final project 30%, quizzes 12%.

**Short prep path (a guess from the title and from the page above):** (1) when to use an agent and when a plain workflow is better (row 15.1); (2) how tools are described to an agent and how a tool protocol works (rows 15.2 and 15.3); (3) how several agents are organized and where that fails (row 15.4); (4) durable, restartable runs, which match the "crash-safe workflows" topic (row 15.5). All five rows are reused from Track G Block 7 (and Track C Block 4), where the same videos carry a build step.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 15.1 | How We Build Effective Agents: Barry Zhang, Anthropic | AI Engineer | https://www.youtube.com/watch?v=D7_ipDqhtwk | 15:09 | Start | BIKE | Anthropic's short, opinionated guide: what an agent loop is, when a simple workflow beats an agent, and how to design around the model's view of the world. Watch first; it is the "when NOT to use agents" video. (Summary of its principles taken from third-party write-ups seen in search; the page itself gave only title and length.) | verified; also in Track G 7.1 (Track C 4.1); watch once |
| 15.2 | Tool Calling Is Not Just Plumbing for AI Agents — Roy Derks | AI Engineer | https://www.youtube.com/watch?v=zuMw0pkPXpU | 25:17 | Deeper | BIKE | Per the talk page: a tool definition (name, description, input and output schema) is a behavioural contract; who owns the model-tool loop (your app or the agent framework); hosting tools behind MCP or a tool platform so you can swap frameworks; the risk of letting the model generate queries instead of using fixed tools. Architect-level, no live coding. | verified; also in Track G 7.4 (Track C G3); watch once |
| 15.3 | Why we built—and donated—the Model Context Protocol (MCP) | Anthropic | https://www.youtube.com/watch?v=PLyCki2K0Lg | 35:32 | Start | BIKE | Anthropic's Stuart Ritchie interviews MCP co-creator David Soria Parra on what MCP is (an open standard for connecting AI to tools and data) and why it was donated to the Linux Foundation. | verified; also in Track G 7.3 (Track C 4.2); watch once |
| 15.4 | The Multi-Agent Architecture That Actually Ships — Luke Alvoeiro, Factory | AI Engineer | https://www.youtube.com/watch?v=ow1we5PzK-o | 18:30 | Deeper | BIKE | A taxonomy of five multi-agent strategies and a three-role design (orchestrator, workers, validators) with validation contracts and structured handoffs, drawn from one vendor's production data. | verified; also in Track G 7.5 (Track C 4.4); watch once |
| 15.5 | Why Every AI Agent Needs Durable Execution \| Temporal, Samar Abbas | Lightspeed Venture Partners | https://www.youtube.com/watch?v=w4spcXq5uCw | 45:52 | Deeper | BIKE | Workflow orchestration for agents: why long-running, failure-prone agent runs need durable state, retries and resumption. An interview with the Temporal CEO, so a vendor's argument, but the underlying idea is sound. | verified; also in Track G 7.O2 (Track C 4.6); watch once |

**Optional (extra):** none added. Track G Block 7 has further optional rows (an MCP deep dive, an agent-framework comparison and a DESK MCP workshop) if you want more.

**Before you start:**
- Comfort with Python and git; no AI or machine-learning background is required by the CS 378 page, so Blocks 1 and 2 are not prerequisites on that evidence.
- Basic reliability ideas (retries, idempotency, rate limits) from Track D Block 6 help with the systems half of the page.

**Full circle:** you can say what you would specify, delegate and verify when handing a software task to an agent, why an agent loop is not always better than a fixed workflow, what a tool definition has to contain, and why long agent runs need saved progress.

<details>
<summary>Recap questions (3)</summary>

1. Q: In the CS 378 framing, what three decisions do you make about each part of a software problem when you work with a coding agent? A: What you specify, what you delegate to the agent, and what you verify yourself.
2. Q: When is a plain workflow a better design than an agent loop? A: When the steps are known in advance; an agent loop earns its extra cost and unpredictability only when the path cannot be fixed ahead of time (the argument of row 15.1, as I understand it from its title and third-party summaries).
3. Q: Why would a course on coding agents spend about a quarter of its time on systems topics such as fault tolerance, concurrency and rate limiting? A: Agent-written software still has to be correct under failures, parallel work and limits, and checking those properties stays the engineer's job; the CS 378 page lists them as 25% of class time.
</details>

---

## Gaps

Honest list of what is missing or weak, course by course. "Title-based" means I read no description of the video.

**Blocks 1 to 6 (written in part 1):**
- **1 Machine Learning:** row 1.4 (PAC) comes from a channel named "UofU Data Science" and its watch page could not be read, so I do not know whether it reaches VC dimension or sample-complexity bounds; 1.O4 is the longer fallback. No public site or lecture videos exist for the online Machine Learning course itself. Qiang Liu's lecture notes (hosted on Dropbox) could not be opened, so only his homepage is listed. *An Introduction to Statistical Learning* (including the Python edition, ISLP) was left out in part 1 because the free PDFs were unconfirmed; the authors' page offers them, so it is now listed in Blocks 1 and 9 (the PDFs themselves were not opened).
- **2 Deep Learning:** no public lectures by the course's instructor; the UT site's instructor and online status are not stated on the page. Residual connections and normalization layers have no dedicated verified video (Track B 3.O3 is the closest, a DESK video). Row 2.4 rests on a syllabus line, not on the video.
- **3 Reinforcement Learning:** rows 3.O4 (a seminar by the instructor of record) and several lecture rows are title-based; no public site or videos exist for the online RL course itself (the on-campus Spring 2024 page is the only course page).
- **4 Planning, Search, and Reasoning Under Uncertainty:** row 4.7 (a Lockheed Martin demonstration) is title-based and I could not tell what it shows or whether it relates to the course; I made no new search for a replacement in part 2. 4.O4 (a seminar by a speaker with the instructor's name) is title-based. Symbolic (PDDL-style) planning has no video. No public site or videos exist for the online course itself.
- **5 Ethics in AI:** rows 5.1, 5.6, 5.O3 and 5.O4 are title-based (5.6 is by speaker only). Ethical theories beyond utilitarianism are covered only by the syllabus, not by a video. No public site or videos exist for the online ethics course itself.
- **6 Natural Language Processing:** row 6.7 (Hugging Face pipeline) is title-based; the 98-video playlist holds many lectures that are not listed; no public materials from Jessy Li were found.

**Blocks 7 to 14 (this part):**
- **7 Advances in Deep Learning:** the cdso page has no outline, so the topic list comes from the UT Deep Learning Group's public 2025 site, which may not be the online course (the page names no instructor; its title matches the cdso course and its diffusion slides name Philipp Krähenbühl). I did not open the Panopto lecture videos, so I do not know whether they play without a UT login. Mixed precision, checkpointing, GPU architecture, sequence parallelism, paged attention, structured outputs, constrained decoding and long context have no dedicated verified video, and neither do the computer-vision lessons beyond CLIP (7.O3) and Block 2; all new rows here are title-based.
- **8 Advances in Deep Generative Models:** no public site or lecture videos for Qiang Liu's online course; the energy-based-models weeks have only one weak row (8.2, about latent-variable EBMs, title-based) and no EBM-specific verified video; the MIT 6.S184 lectures belong to a different course; I tried one later Stanford CS236 lecture (lecture 8) and it failed the oEmbed check, so none beyond lecture 1 is listed, and the CS236 notes index shows no EBM or diffusion chapter. *Understanding Deep Learning* (Simon Prince) is not listed because I could not confirm a free PDF. Verified but not listed, to stay within the optional cap: MIT 6.S184 lecture 2 "Constructing a Training Target" (https://www.youtube.com/watch?v=yFD-JSSG-D0, Peter Holderrieth), "Variational Autoencoders" by Arxiv Insights (https://www.youtube.com/watch?v=9zKuYvjFFS8), "Introduction to Normalizing Flows (ECCV2020 Tutorial)" by Marcus Brubaker (https://www.youtube.com/watch?v=u3vVyFVU_lI) and "Lecture 13 | Generative Models" from Stanford CS231n (https://www.youtube.com/watch?v=5WoItGTWV54).
- **9 Case Studies in Machine Learning:** the cdso page lists no syllabus; there is no public course site. Rows 9.5 (NeuralNine) and 9.6 (ML in PL) are title-based, from channels I did not vet, and I do not know the speaker's affiliation in 9.6. There is no verified video from a university on transportation machine learning, and none on report writing or presenting to a client.
- **10 Optimization:** five UCSB CS292F lecture videos failed the oEmbed check and were dropped (see Block 11). Boyd's lecture numbers and durations are matched by number to the Stanford Engineering Everywhere list, which is an assumption. CMU's 10-725 videos exist per its page but I did not extract their IDs. Caramanis's 58-video playlist is mostly unread (two titles only). The book's own page and the lecture slides link could not be opened. No verified video covers LP geometry, LP-duality applications, semidefinite programming, quasi-Newton methods, the barrier method or variance reduction.
- **11 Online Learning and Optimization:** no public site for the online course or for Shakkottai's teaching. Rows 11.4 and 11.5 are matched to the Bristol notes by title (the page warns the videos may not map to lectures). No verified video covers Exp3, Exp4, LinUCB, Thompson sampling, weighted majority, Perceptron and Winnow, oracle lower bounds, or ISTA and FISTA. Row 11.O1 comes from a channel I did not vet. Bubeck and Cesa-Bianchi's survey is named on the Bristol page but its own page was not opened, so it is not listed.
- **12 Automated Logical Reasoning:** no public videos by Işıl Dillig (her page links slides only). Paulson's lecture rows (12.3, 12.4) are title-based and I could not read the series' course page. No verified video covers BDDs, the theory of equality, integer decision procedures, or DPLL(T) as a topic; the verification videos are two lectures of one series plus talks. The two textbooks are not confirmed free.
- **13 AI in Healthcare:** no public lectures by Ying Ding. The National Academy of Medicine report, the MIT Critical Data book and the PhysioNet dataset page listed on her course page could not be opened. No verified video covers ICD-10 coding, LOINC, RxNorm, clinical decision support systems, medical NLP, multimodal fusion or the ethics of AI in health. The FHIR and imaging rows come from channels I did not vet; the MIT rows come from a playlist titled Spring 2019, so they may be dated.
- **14 AI in Astrophysics:** a niche course with no public course site; the only course-adjacent item is a paper whose first author shares the instructor's name. Rows 14.2 (day 3 of a series) and 14.O3 (a week of a course) are from series whose other parts I did not check. No verified video covers curating training sets from scientific data. Two other astronomy machine-learning videos (IDs 5n57qsyl6Qg and 1z2Typmfvew) failed the oEmbed check and were dropped. The documentation pages for `sbi` and astroML, and the arXiv review of simulation-based inference by Cranmer and colleagues, could not be opened in this session.
- **15 Agentic Software Engineering:** the handbook gives only the title, so there is no official outline, instructor or prerequisite; the CS 378 page is an on-campus course of the same name that may not match; the five rows are reused from Track G Block 7 and are chosen from the title and that page, not from the course. No verified video covers working with a coding agent in practice (Claude Code, Codex): the course uses those tools, but a hands-on video was not searched for in this part.

**Links dropped for failing the oEmbed check:** UCSB CS292F lectures 4, 6, 13, 15 and 19 (IDs ocTY-SC7nTw, rNcNiTVDeG8, gfhuVITwqoQ, cLeGBH0RDRo, JTYMRf_yuOo); "Stanford Seminar - Deep Learning for Medical Diagnoses" (nUk_P3G29tk); Stanford CS236 lecture 8 (qgTvgBCOyn8); the two astronomy videos named above.

## Not checked

- I have not watched any video. "What you will get" is from titles, chapter lists, course pages or transcript pages, as the Status column says; YouTube watch pages could not be read in this session, so most new rows are title-based.
- Lengths were read from each video's YouTube page on 2026-11-16 or 17; an earlier note about Stanford Engineering Everywhere durations is no longer needed.
- The MSAI Online Handbook (published for 2027-2028) was read in full on 2026-11-16. It gives no schedule, no weekly hours and no syllabus, and it is dated for the year after your first term, so I did not verify that it governs a Spring 2027 start. Course numbers, grade rules, the elective list and the prerequisites for Blocks 8 and 14 come from it; the Spring 2027 course list comes from a program email and is not in the handbook.
- Which semesters each course runs, the real weekly workload, and whether the public course sites above (UT Deep Learning Group, the on-campus pages, the MIT and Stanford pages) match the online courses: unverified; ask the program coordinator.
- Whether the YouTube channels of individual educators and seminar series are reliable; I labelled the ones I did not vet.
- Whether each video stays available, and whether the Level and Mode tags match the real pace.
- The Panopto lecture videos on the UT Deep Learning Group site were not opened.
- Pages that could not be opened in this session and so are not listed or relied on: the Boyd and Vandenberghe book page, the NAM report PDF, the PhysioNet MIMIC page, the sbi and astroML sites, the Cambridge Logic and Proof course page, and two arXiv pages (Cranmer and colleagues; Bubeck and Cesa-Bianchi).

