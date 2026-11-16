# Track F: UT Austin MSAI course tracker

**What this track is.** Each block is one course of UT Austin's online MS in Artificial Intelligence. For each course it gives the official description, free public materials that match the content, a short video path, and recap questions. The video path is a prep and companion path: it does not replace the course, its assignments or its instructors' emphasis. Videos are for the bike; code, reading and pausing are for the desk (Mode column). This part holds Blocks 1 to 6; the remaining courses are added after it.

**Program structure, as stated on https://cdso.utexas.edu/msai (read on 2026-11-16).** The page describes a 30-hour program of 10 courses at 3 credit hours each, "consisting of 3 hours of required courses and 27 hours of electives". Only Ethics in AI is marked "(required)". Under the heading "Required and Foundational Courses" it lists Deep Learning, Ethics in AI, Machine Learning, Planning, Search, and Reasoning Under Uncertainty, and Reinforcement Learning; under "Elective Courses" it lists nine: Advances in Deep Generative Models, Advances in Deep Learning, AI in Astrophysics, AI in Healthcare, Automated Logical Reasoning, Case Studies in Machine Learning, Natural Language Processing, Online Learning and Optimization, and Optimization. It recommends completing the required and foundational courses at the beginning, before electives. **What is unclear:** the page does not say whether all four foundational courses are mandatory, and its heading ("Required and Foundational") and its credit-hour sentence (3 required plus 27 elective) read differently. I make no claim either way; check the program's degree requirements or an advisor before leaving any of them out. The page gives no course numbers or syllabus links and does not use the term "Option III" (Greg Durrett's UT page does, for UT's online master's programs).

**Suggested order (my judgement, not an official rule).** For someone aiming at GenAI architecture who starts with one course at a time alongside full-time work: Deep Learning first, which is the current leaning in your notes and the course closest to the GenAI core (Block 2); the alternative is Machine Learning first if the math and probability feel rusty (Block 1), since it carries the theory and shares gradient descent with Deep Learning. Then the other one of those two, then Ethics in AI (the one course marked required; concept and discussion heavy, per its outline), then Reinforcement Learning, with Planning, Search, and Reasoning Under Uncertainty last among these because its link to the stack is the weakest. Natural Language Processing is an elective and the most direct fit to the GenAI goal among the six courses here; if you follow the page's recommendation it comes after the foundational courses, and if the degree rules turn out to let you skip some foundational courses it could move up. A final elective ranking for the GenAI goal is added after all courses are written.

<!-- ELECTIVE RANKING GOES HERE -->

**Table legend.**
- Level: Start / Deeper / Scholar.
- Mode: BIKE = works mostly by listening (slide lectures need a glance at the screen). DESK = needs code, paper or pausing. Unlike a pure bike path, a DESK row appears in a main list where the course itself is hands-on (a coding demo); 4 of the 41 main rows are DESK.
- Status "verified" means the YouTube oEmbed endpoint returned the exact video ID I asked for, with the title and channel shown (copied as returned). It does not mean I watched the video. After "verified" the Status names what the "What you will get" sentence rests on: the watch-page description or chapter list, a named course page, or the title only ("title-based").
- Rows marked "also in Track X <id>; watch once" are reused from Tracks A to C: title, channel, link and length are copied from that row, and I did not re-verify them. Rows without that mark are new in this track and passed the oEmbed check in this session.
- Length: shown only where a page stated it (the source is named). "at least X" is a lower bound from a chapter marker. "length ?" means no page I read gave one. Nothing is estimated.
- "What you will get" is one sentence in my own words, based only on the source named in Status. I have not watched any of these videos.

**Honest accounting.** Blocks 1 to 6 have 41 main rows (28 reused from Tracks A to C, 13 new) and 24 optional rows (16 reused, 8 new). Of the main rows, 8 show some length figure and 33 read "length ?"; of the optional rows, 2 show one and 22 read "length ?". No total in hours can be stated from verified data. Nothing was watched. Several new rows rest on the title alone because their YouTube watch pages could not be read (YouTube rate-limited the page reads), and they are marked "title-based". The weakest rows are 4.7 (a demo whose content I could not read), 5.6 (speaker only), 5.1, 1.4 and 6.7 (title only), and the two optional rows 3.O4 and 4.O4 (title only).

---

## Block 1: Machine Learning

**Why it matters for the stack:** the vocabulary and theory (generalization, bias and variance, likelihood versus priors, clustering, learnability) behind every later decision about evaluation, model choice and data in a GenAI stack; the link to building the stack is indirect, because you will not build a retrieval or agent system in this course.

**Official description and outline:** Per the cdso page (instructors listed: Adam Klivans and Qiang Liu, Computer Science), an introduction to the core algorithms and statistical tools of machine learning: supervised and unsupervised learning, PAC learning, Bayesian methods and neural networks, with programming examples.

**Public materials:**
- **Textbook, free from the authors:** Shai Shalev-Shwartz and Shai Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (Cambridge University Press, 2014). The authors' page offers the full PDF: https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/ (the PDF itself loaded and showed this title and these authors). Theory-first; its PAC and VC chapters match the course's PAC topic (my background knowledge of the book, its contents not checked here).
- **Textbook, free download:** Christopher Bishop, *Pattern Recognition and Machine Learning* (Springer, 2006). Microsoft Research's page offers the full PDF: https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ (the page states no license terms). Strong on Bayesian methods and graphical models.
- **Textbook, free draft:** Kevin Murphy, *Probabilistic Machine Learning: An Introduction* (MIT Press, 2022). The book's page offers a free PDF draft dated 2025-04-18, licensed CC-BY-NC-ND per the page: https://probml.github.io/pml-book/book1.html (a draft, not the final print edition).
- **Instructor page:** Qiang Liu's UT homepage lists his own lecture notes (an undergraduate intro to ML, probabilistic learning and inference, learning theory) as PDFs hosted on Dropbox, which I could not open, so I list only the homepage: https://www.cs.utexas.edu/~lqiang/index.html. The page does not say the notes belong to the online course.
- **Older UT course by one instructor (on-campus version of a different, theory course; may differ from the online course):** Adam Klivans, CS 395T Computational Learning Theory, Fall 2006: https://www.cs.utexas.edu/~klivans/cl2.html. Useful only as a topic list for PAC learning, VC dimension and boosting.
- No public course site or lecture videos for the online Machine Learning course itself were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.1 | Machine Learning Fundamentals: Bias and Variance | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=EuBBz3bI-aA | length ? | Start | BIKE | Why a model can be too simple or too wiggly: the overfitting and underfitting picture that generalization theory later makes precise (title-based). | verified; title-based; also in Track B 1.2; watch once |
| 1.2 | Gradient Descent, Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=sDv4f4s2SB8 | length ? | Start | BIKE | Walking downhill on the loss with actual numbers, step size and learning rate included; the engine behind most training in the course (title-based). | verified; title-based; also in Track B 2.1 and Track A #39; watch once |
| 1.3 | StatQuest: Logistic Regression | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=yIYKR4sgzI8 | length ? | Start | BIKE | From a line to a probability: classification with the logistic curve, the first supervised classifier to know well (title-based). | verified; title-based; also in Track B 2.2; watch once |
| 1.4 | Machine Learning: Lecture 13: PAC learning | UofU Data Science | https://www.youtube.com/watch?v=p5xP8fWnPZw | length ? | Deeper | BIKE | A full lecture on PAC learning, by title, from a channel named "UofU Data Science" (I read that as the University of Utah; not confirmed). I could not read the watch page, so I do not know whether it reaches VC dimension or sample-complexity bounds. It is the most course-like PAC video I could verify; the Caltech VC lecture in the optional list goes further. | verified; title-based |
| 1.5 | Expectation Maximization: how it works | Victor Lavrenko | https://www.youtube.com/watch?v=iQoXFmbXRJA | 10:39 | Deeper | BIKE | The EM idea as a soft version of the k-means loop: clustering with probabilistic assignments instead of hard ones (title-based). | verified; title-based; also in Track B 2.10; watch once |
| 1.6 | Maximum A Posteriori (MAP) - Why L2 Regularization is Bayesian in Disguise | DataMListic | https://www.youtube.com/watch?v=Ovuszur2uzk | length ? | Deeper | BIKE | Maximum likelihood versus a Bayesian prior (MAP), and how a prior shows up as L2 regularization (title-based). | verified; title-based; also in Track B 2.13; watch once |
| 1.7 | Machine Learning for Everybody – Full Course | freeCodeCamp.org | https://www.youtube.com/watch?v=i_LwzRVP7bg | at least 3:33:54 (start of the last chapter marker; total not shown) | Start | DESK | Demo, not a ride: per the chapter list, Python and Colab implementations of k-nearest neighbours, naive Bayes, logistic regression, SVM, a neural network in TensorFlow, linear regression, k-means and PCA (course developed by Kylie Ying, per the description). Do not watch it end to end; take the chapters that match your week (logistic regression from 1:19:22, neural networks from 1:39:44, k-means from 3:13:13). | verified; content per watch-page description and chapter list |

*Neural networks* are also a topic of this course; the video path for them is Block 2 (rows 2.1 to 2.3), because the Deep Learning course starts from the same ideas.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.O1 | StatQuest: K-means clustering | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=4b5d3muPQmA | length ? | Start | BIKE | The k-means loop: assign points, recompute centres; watch before 1.5 if clustering is new (title-based). | verified; title-based; also in Track B 2.9; watch once |
| 1.O2 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Start | BIKE | PCA walked through step by step, the other standard unsupervised method (title-based). | verified; title-based; also in Track B 2.7 and Track A #19; watch once |
| 1.O3 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | length ? | Start | BIKE | The visual picture of neurons, layers and weights, for the course's neural-networks topic (title-based). Block 2 goes deeper. | verified; title-based; also in Track B 3.1 (also used in Block 2, row 2.1); watch once |
| 1.O4 | Lecture 07 - The VC Dimension | caltech | https://www.youtube.com/watch?v=Dc0sr0kdBVI | length ? | Scholar | DESK | VC dimension from Caltech's Learning from Data: a full, long lecture that is the next step after 1.4. It builds on the two preceding Caltech lectures (Track B 2.O3, 2.O4); start there if you feel lost (title-based). | verified; title-based; also in Track B 2.5; watch once |

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

**Public materials:**
- **UT course site (instructor and online/on-campus status not stated on the page, so check it against the syllabus when you enrol):** "Deep Learning Class" from the UT Austin Deep Learning Group, 2025: https://ut.philkr.net/deeplearning/. Slides and PyTorch notebooks for: introduction (tensors, gradients, PyTorch basics), first example (regression, classification, loss, logistic regression in PyTorch), deep networks, residuals and normalizations, convolution, transformers, and "making it work".
- **Earlier UT course page (a different run, Fall 2021; may differ from the online course; the page I read names no instructor):** CS 342 Neural Networks: https://philkr.github.io/cs342. Weekly topics from k-nearest neighbours through CNNs, optimization practice, computer vision, reinforcement learning and imitation learning, sequence modeling, embeddings, adversarial attacks, and bias, fairness and ethics; no textbook, no videos listed.
- **Textbook, online:** Aston Zhang, Zachary Lipton, Mu Li and Alex Smola, *Dive into Deep Learning*: https://d2l.ai. The site offers the full text online with PDF and notebook downloads, in PyTorch, NumPy/MXNet, JAX and TensorFlow; it shows version 1.0.3, and a Cambridge University Press print edition is listed as forthcoming.
- **Textbook, free to read as HTML only:** Ian Goodfellow, Yoshua Bengio and Aaron Courville, *Deep Learning* (MIT Press, 2016): https://www.deeplearningbook.org (the site says it stays free online and offers no PDF).
- **Tool tutorial:** PyTorch "Learn the Basics" (tensors, datasets and data loaders, building a model, autograd, the optimization loop, saving models): https://docs.pytorch.org/tutorials/beginner/basics/intro.html (the page I read is for PyTorch Tutorials 2.15.0).
- No public lecture videos by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.1 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | length ? | Start | BIKE | The visual picture of neurons, layers and weights (title-based). | verified; title-based; also in Track B 3.1; watch once |
| 2.2 | Gradient descent, how neural networks learn \| Deep Learning Chapter 2 | 3Blue1Brown | https://www.youtube.com/watch?v=IHZwWFHWa-w | 20:33 | Start | BIKE | Loss and gradient descent applied to a network (title-based); if gradient descent itself is new, watch Block 1 row 1.2 first. | verified; title-based; also in Track B 3.2 and Track A #38; watch once |
| 2.3 | Backpropagation, intuitively \| Deep Learning Chapter 3 | 3Blue1Brown | https://www.youtube.com/watch?v=Ilg3gGewQ5U | 12:47 | Start | BIKE | The intuition for how the error flows backward through the network and assigns blame to each weight (title-based). | verified; title-based; also in Track B 3.3 and Track A #42; watch once |
| 2.4 | Lecture 6 \| Training Neural Networks I | Stanford University School of Engineering | https://www.youtube.com/watch?v=wEoyxE0GP2M | length ? | Deeper | BIKE | Stanford CS231n (Spring 2017) lecture whose syllabus line reads "Activation functions, initialization, dropout, batch normalization"; the closest verified match to the course's "making it work" and debugging theme. Slide-heavy, so glance at the screen. | verified; content per CS231n 2017 syllabus line; also in Track B G2; watch once |
| 2.5 | Neural Networks Part 8: Image Classification with Convolutional Neural Networks (CNNs) | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=HGwBXDKFk9I | length ? | Start | BIKE | Convolution filters and pooling for images, shown visually (title-based); the course site lists convolutions, pooling and CNN design. | verified; title-based; also in Track B 3.5; watch once |
| 2.6 | Transformers, the tech behind LLMs \| Deep Learning Chapter 5 | 3Blue1Brown | https://www.youtube.com/watch?v=wjZofJX0v4M | 27:14 | Start | BIKE | A visual walk through how a GPT-style transformer is put together, including tokens and embeddings (title-based); the course site has a transformers unit (attention, multi-head attention, positional embeddings). | verified; title-based; also in Track B 4.1; watch once |
| 2.7 | The StatQuest Introduction to PyTorch | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FHdlXe1bSe4 | length ? | Start | DESK | Demo: PyTorch basics from StatQuest (title-based); have a laptop open and code along, ideally next to the PyTorch "Learn the Basics" tutorial listed above. | verified; title-based; also in Track B 3.O2; watch once |

Residual connections and normalization layers, which the course site lists, have no dedicated verified video here; Karpathy's makemore Part 3 (Track B 3.O3, a DESK video) is the closest. Deep reinforcement learning is in Block 3 (3.O3).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.O1 | Lecture 7 \| Training Neural Networks II | Stanford University School of Engineering | https://www.youtube.com/watch?v=_JB0AO7QxSA | length ? | Deeper | BIKE | The next CS231n lecture; the syllabus line reads "Update rules, ensembles, data augmentation, transfer learning". Slide-heavy; pause for any formulas. | verified; content per CS231n 2017 syllabus line; also in Track B G3; watch once |
| 2.O2 | The spelled-out intro to neural networks and backpropagation: building micrograd | Andrej Karpathy | https://www.youtube.com/watch?v=VMj-3S1tku0 | length ? | Deeper | DESK | Build backpropagation in code to make 2.3 concrete (title-based). | verified; title-based; also in Track B 3.O1; watch once |
| 2.O3 | But how do AI images and videos actually work? \| Guest video by Welch Labs | 3Blue1Brown | https://www.youtube.com/watch?v=iv-5mZ_9CPY | length ? | Start | BIKE | A visual explanation of how AI image generators work (diffusion family, by title); a bridge to Part 2 of the course (generative modeling). | verified; title-based; also in Track B 8.1; watch once |
| 2.O4 | Generative Adversarial Networks (GANs) - Computerphile | Computerphile | https://www.youtube.com/watch?v=Sw9r8CL98N0 | length ? | Start | BIKE | The generator-versus-discriminator idea; the course lists adversarial learning in Part 2 (title-based). | verified; title-based; also in Track B 8.2; watch once |

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

**Public materials:**
- **Textbook, free from the authors:** Richard Sutton and Andrew Barto, *Reinforcement Learning: An Introduction*, 2nd edition (MIT Press, 2018). Full PDF on the authors' page: http://incompleteideas.net/book/the-book-2nd.html (PDF: http://incompleteideas.net/book/RLbook2020.pdf).
- **UT course page (on-campus version, may differ from the online course):** CS394R/ECE381V Reinforcement Learning: Theory and Practice, Spring 2024, taught by Amy Zhang and Peter Stone per that page: https://www.cs.utexas.edu/~pstone/Courses/394Rspring24/index.html. It uses Sutton and Barto chapters 1 to 13 and 16, then recent readings, and links other universities' RL course materials (I did not open those links).
- **Free online guide (2018, so dated on current methods):** OpenAI, *Spinning Up in Deep RL*: https://spinningup.openai.com/en/latest/. Three-part introduction to RL plus a key-papers list in 13 topic areas.
- **Public lecture series:** the DeepMind x UCL and David Silver RL lectures are the rows 3.2 to 3.5 and 3.O1 to 3.O3 below.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.1 | An introduction to Reinforcement Learning | Arxiv Insights | https://www.youtube.com/watch?v=JgvyzIkgxF0 | length ? | Start | BIKE | The agent, environment and reward picture before any formulas (title-based). | verified; title-based; also in Track B 5.1; watch once |
| 3.2 | DeepMind x UCL RL Lecture Series - Exploration & Control [2/13] | Google DeepMind | https://www.youtube.com/watch?v=aQJP3Z2Ho8U | length ? | Deeper | BIKE | Per the title, exploration and control: the bandit setting and exploration versus exploitation, as a full university-style lecture in the DeepMind x UCL series. | verified; title-based; also in Track B 5.2; watch once |
| 3.3 | DeepMind x UCL RL Lecture Series - MDPs and Dynamic Programming [3/13] | Google DeepMind | https://www.youtube.com/watch?v=zSOMeug_i_M | length ? | Deeper | BIKE | MDPs and dynamic programming in one lecture (per the title): the case where the model is known. | verified; title-based; also in Track B 5.3; watch once |
| 3.4 | RL Course by David Silver - Lecture 4: Model-Free Prediction | Google DeepMind | https://www.youtube.com/watch?v=PnHCvfgC_ZA | length ? | Deeper | BIKE | Monte Carlo and temporal-difference prediction (per the title, model-free prediction): the case where the model is not known. Full lecture. | verified; title-based; also in Track B 5.4; watch once |
| 3.5 | RL Course by David Silver - Lecture 7: Policy Gradient Methods | Google DeepMind | https://www.youtube.com/watch?v=KHZVXao4qXs | length ? | Deeper | BIKE | Optimising a policy directly, the policy-gradient family (title-based). Full lecture. | verified; title-based; also in Track B 5.5; watch once |
| 3.6 | AlphaGo - The Movie \| Full award-winning documentary | Google DeepMind | https://www.youtube.com/watch?v=WXuK6gekU1Y | 1:30:28 (per watch page) | Start | BIKE | Case study as a story, not a lecture: per the description, a film about the March 2016 match between Lee Sedol and DeepMind's AlphaGo in Seoul (directed by Greg Kohs). The description does not explain methods; that AlphaGo was trained with reinforcement learning is my own background knowledge, so treat the film as motivation for the course. | verified; content per watch-page description |

For the place where RL meets language models, see the RLHF lecture in Block 6 (6.O2).

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.O1 | RL Course by David Silver - Lecture 1: Introduction to Reinforcement Learning | Google DeepMind | https://www.youtube.com/watch?v=2pWv7GOvuf0 | length ? | Deeper | BIKE | A formal introduction lecture to watch before 3.2 if you want the full vocabulary (title-based). | verified; title-based; also in Track B 5.O1; watch once |
| 3.O2 | DeepMind x UCL RL Lecture Series - Model-free Control [6/13] | Google DeepMind | https://www.youtube.com/watch?v=t9uf9cuogBo | length ? | Scholar | DESK | Per the title, model-free control: the step after prediction (3.4). Full lecture; pause for formulas. | verified; title-based; also in Track B 5.O2; watch once |
| 3.O3 | DeepMind x UCL RL Lecture Series - Deep Reinforcement Learning #1 [12/13] | Google DeepMind | https://www.youtube.com/watch?v=cVzvNZOBaJ4 | length ? | Scholar | BIKE | Per the title, deep reinforcement learning: neural networks inside RL. Full lecture. | verified; title-based; also in Track B 5.6; watch once |
| 3.O4 | RI Seminar: Peter Stone : Robot Skill Learning: From the Real World to Simulation and Back | CMU Robotics Institute | https://www.youtube.com/watch?v=84t_dQpdTEo | length ? | Deeper | BIKE | A research seminar by Peter Stone, whom the cdso page lists as the course's instructor of record. I could not read the watch page, so I know only the title (robot skill learning, simulation to real world); treat it as an optional look at the instructor's research, not as course content. | verified; title-based |

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

**Public materials:**
- **UT course page (on-campus version, Spring 2023, instructor Joydeep Biswas; may differ from the online course):** CS 395T Planning, Search and Reasoning Under Uncertainty: https://amrl.cs.utexas.edu/CS395T-S23. The page lists topics as planning domains (symbolic and path planning), search algorithms, decision-making for autonomous systems and reasoning under uncertainty, with suggested textbooks AIMA and LaValle; the week-by-week schedule is a Google Sheet that I did not open.
- **Textbook, free online:** Steven LaValle, *Planning Algorithms* (Cambridge University Press, 2006): http://lavalle.pl/planning/ (HTML and PDF). Matches the sample-based planning topic.
- **Textbook, free PDF:** Mykel Kochenderfer, Tim Wheeler and Kyle Wray, *Algorithms for Decision Making* (MIT Press, 2022): https://algorithmsbook.com/ (the page says full PDFs are free). Scope per my background knowledge: probabilistic reasoning, MDPs and POMDPs; I did not open the PDF.
- **Textbook, not free:** Stuart Russell and Peter Norvig, *Artificial Intelligence: A Modern Approach*, 4th US edition. The companion site offers pseudocode, figures, exercises and code on GitHub: https://aima.cs.berkeley.edu/ (the page does not offer the book itself).
- **Public lectures:** the Berkeley CS188 lectures are rows 4.1, 4.3 to 4.5 and 4.O1 to 4.O3 below. No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.1 | Step-by-Step: A Star Search | CS188Spring2013 | https://www.youtube.com/watch?v=sAoBeujec74 | 22:17 | Start | BIKE | A worked A* example from the Berkeley CS188 channel (title-based). | verified; title-based; also in Track B 6.1; watch once |
| 4.2 | Sampling-based Methods [Lecture, Marija Popović] | Marija Popović | https://www.youtube.com/watch?v=CrQJAtPn8sY | length ? (watch page showed no duration) | Deeper | BIKE | Per the description, robotic motion planning with sampling-based methods, including PRM and RRT, plus extensions for kinodynamic constraints and asymptotic optimality; fills the "sample-based planning" topic that the Berkeley lectures do not cover. Probably slide-based, so glance at the screen. | verified; content per watch-page description |
| 4.3 | CS 188 Lecture 5: Adversarial Search | CS 188 | https://www.youtube.com/watch?v=_3djr6ZXLzQ | length ? | Deeper | BIKE | Berkeley lecture on adversarial (game) search (title-based). Full lecture. | verified; title-based; also in Track B 6.3; watch once |
| 4.4 | CS 188 Lecture 18: Hidden Markov Models | CS 188 | https://www.youtube.com/watch?v=0u80UvCAKVo | length ? | Deeper | BIKE | Bayesian state estimation with hidden Markov models: keeping a belief about a hidden state over time (title-based). Full lecture; assumes Bayes nets (see 4.O2). | verified; title-based; also in Track B 6.4; watch once |
| 4.5 | Lecture 8: Markov Decision Processes (MDPs) | CS188Spring2013 | https://www.youtube.com/watch?v=i0o-ui1N35U | length ? | Deeper | DESK | Berkeley's lecture on Markov decision processes, the planning-side companion to Block 3's 3.3 (title-based). | verified; title-based; also in Track B 6.O3; watch once |
| 4.6 | DLRLSS 2019 - POMDPs - Pascal Poupart | Amii | https://www.youtube.com/watch?v=K0wcWi38IGA | length ? | Scholar | BIKE | POMDPs from a summer-school lecture; per Track B the only POMDP source from a recognised expert that it verified. Long and mathematical, so keep it for the end. | verified; title-based; also in Track B 6.5; watch once |
| 4.7 | UT Austin Path Planning and Collision Avoidance Demonstration at Lockheed Martin | Lockheed Martin | https://www.youtube.com/watch?v=WYA4m9ZVZ1I | length ? | Start | BIKE | Demo, title only: a demonstration video of path planning and collision avoidance. I could not read the watch page, so I do not know what is shown, who built it, or whether it is related to the course; weak row, replace it if you find a better case study. | verified; title-based |

No verified video covers the first topic in the official outline, defining planning problems in a symbolic (PDDL-style) form; the two textbooks above are the better route for that topic.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.O1 | COMPSCI 188 - 2018-08-30 - A* Search and Heuristics | Webcast Departmental | https://www.youtube.com/watch?v=Mlwrx7hbKPs | length ? | Deeper | BIKE | Berkeley lecture on A* and heuristics; the formal version of 4.1 (title-based). Full lecture. | verified; title-based; also in Track B 6.2; watch once |
| 4.O2 | Lecture 13: Bayes Nets | CS188Fall2013 | https://www.youtube.com/watch?v=VfyxPtlqZh4 | length ? | Deeper | DESK | Prerequisite for 4.4 if Bayes nets are rusty (title-based). | verified; title-based; also in Track B 6.O1; watch once |
| 4.O3 | CS 188 Lecture 19: Particle Filtering | CS 188 | https://www.youtube.com/watch?v=r-bHqY5gaPw | length ? | Scholar | DESK | Approximate state estimation with particles, the step after 4.4 (title-based). | verified; title-based; also in Track B 6.O2; watch once |
| 4.O4 | EI Seminar - Joydeep Biswas | MIT Embodied Intelligence | https://www.youtube.com/watch?v=0vPNN0J8M44 | length ? | Deeper | BIKE | A seminar talk by a speaker named Joydeep Biswas; the cdso page names a Joydeep Biswas as this course's instructor, but I could not read the watch page, so I cannot confirm it is the same person or what the topic is. | verified; title-based |

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

**Public materials:**
- **UT course syllabus (on-campus version, may differ from the online course):** INF 385T.12 Ethics of AI, instructor Ken Fleischmann; the PDF does not state the semester (its file name says Fall 2024): https://ischool.utexas.edu/sites/default/files/syllabi/EthicsOfAISyllabusFall2024Final.pdf. Fourteen weeks: histories of ethics and of AI, then ethical traditions (Indian, Chinese, Buddhist, Islamic, Kantian, consequentialist, distributive justice, virtue, care, Ubuntu), value-sensitive design, codes of ethics, AI ethics guidelines, and fairness, accountability, transparency, power and agency. Readings are listed by author; I did not check which are free.
- **Textbook, free online:** Solon Barocas, Moritz Hardt and Arvind Narayanan, *Fairness and Machine Learning: Limitations and Opportunities* (MIT Press, 2023): https://fairmlbook.org (full text and a PDF of the whole book, licensed CC BY-NC-ND 4.0). More technical and legal than the course's ethical-theory weeks, so it complements them.
- **Public lectures related to the course's themes:** Greg Durrett's NLP course ends with four short ethics lectures (bias, exclusion, dangers of automation, unethical use and paths forward), listed on his page given in Block 6.
- No public lectures by the course's instructor were found.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.1 | Michael Wooldridge - The story of AI - GDR IA - Journées Plénières 2021 | GDR RADIA | https://www.youtube.com/watch?v=JDZsK_N8s5M | length ? | Start | BIKE | History of AI, by title, from a plenary talk by Michael Wooldridge (a University of Oxford professor, per my own background knowledge). I could not read the watch page, so the coverage is unknown; the best-sourced history-of-AI talk I found, since the other results came from small channels. | verified; title-based |
| 5.2 | Justice: What's The Right Thing To Do? Episode 01 "THE MORAL SIDE OF MURDER" | Harvard University | https://www.youtube.com/watch?v=kBdfcR-8hEY | 54:56 (per watch page) | Start | BIKE | Ethical theory by example: per the description, Michael Sandel's opening dilemma (kill one to save five), a 19th-century shipwreck case, and an introduction to Bentham's utilitarianism; a classroom recording, so you can follow by ear. | verified; content per watch-page description |
| 5.3 | What is trustworthy AI? | DigitalEU | https://www.youtube.com/watch?v=Imv9SG-zfkU | length ? | Start | BIKE | A short orientation on trustworthy-AI guidelines from the channel named DigitalEU (title match only). | verified; title-based; also in Track B 7.1; watch once |
| 5.4 | FAT* 2018: Joy Buolamwini - Intersectional Accuracy Disparities in Commercial Gender Classification | ACM FAccT Conference | https://www.youtube.com/watch?v=Af2VmR-iGkY | length ? | Deeper | BIKE | Fairness, case-based: accuracy gaps across groups in commercial gender classification (title-based). | verified; title-based; also in Track B 7.2; watch once |
| 5.5 | Turing Lecture: Algorithmic Accountability: Professor Ben Shneiderman, University of Maryland | The Alan Turing Institute | https://www.youtube.com/watch?v=UWuDgY8aHmU | length ? | Deeper | BIKE | Accountability and transparency, from a university professor's lecture (title-based). | verified; title-based; also in Track B 7.4; watch once |
| 5.6 | CDAC Distinguished Speaker Series - Kate Crawford | UChicago Data Science Institute | https://www.youtube.com/watch?v=YhqYt7b8sFY | length ? | Deeper | BIKE | Power, by speaker only: a talk by Kate Crawford, whose book Atlas of AI is about the material and political cost of AI (background knowledge). I could not read the watch page, so I do not know the talk's topic; weak row for the "power" week. | verified; title-based |
| 5.7 | The Accuracy, Fairness, and Limits of Predicting Recidivism | Berkman Klein Center for Internet & Society | https://www.youtube.com/watch?v=G0OE8p-fc10 | length ? | Deeper | BIKE | Case study on fairness: a recidivism prediction tool and the limits of predicting it (title-based). | verified; title-based; also in Track B 7.3; watch once |

There is no verified video on the ethical-theory weeks beyond row 5.2 (utilitarianism by example); the syllabus above lists the other traditions if you want to read ahead.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.O1 | The E.U. AI Act: A Risk-Based Policy Approach to AI Applications | Stanford HAI | https://www.youtube.com/watch?v=OhBsDIG8ioM | 1:04:13 (per the watch page) | Deeper | BIKE | A 17 June 2021 webinar on the European Commission's April 2021 proposal to regulate high-risk AI: US policy experts and an EU Cabinet member discuss its benefits, drawbacks and transatlantic implications. A panel about the draft proposal, not the final law. | verified; content per watch-page description; also in Track B G11; watch once |
| 5.O2 | What is our ethical responsibility with AI & Machine Learning? - Fei-Fei Li & Andrew Ng | Stanford Online | https://www.youtube.com/watch?v=Aws-cOIXsNQ | length ? | Start | BIKE | A conversational overview of ethical responsibility in AI from two prominent researchers (title-based). | verified; title-based; also in Track B 7.O1; watch once |
| 5.O3 | What is AI ethics? Oxford Professor Edward Harcourt explains | University of Oxford | https://www.youtube.com/watch?v=Gpf_ttt_c8M | length ? | Start | BIKE | A general introduction to AI ethics from the University of Oxford's channel (title-based; not specific to any one course topic). | verified; title-based |
| 5.O4 | The Turing Lectures: Can we trust AI? | The Alan Turing Institute | https://www.youtube.com/watch?v=7SyAC5TsEsQ | length ? | Start | BIKE | A public lecture on whether AI can be trusted, from the Alan Turing Institute (title-based; general rather than course-specific). | verified; title-based |

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

**Public materials:**
- **UT's online-MS version, public (recordings from 2023-2024; the program's current run may differ):** Greg Durrett's CS388/AI388/DSC395T Natural Language Processing (online MS) course materials: https://www.cs.utexas.edu/~gdurrett/courses/online-course/materials.html. Twelve parts, from linear classification and neural networks through embeddings, language models, transformers, BERT and seq2seq, tagging and parsing, modern LLMs, explanations, question answering, machine translation and summarization, to multilinguality and ethics; slides and notes archive, four assignments with code, and a final project. The page says the materials are for online master's students in UT's "Option III" programs and that anyone may consult them. Jessy Li is also listed on the cdso page; I found no public materials from her.
- **Lecture videos:** the course playlist "Natural Language Processing at UT Austin, 2023-2024 version (Greg Durrett)", 98 videos per the playlist page: https://www.youtube.com/playlist?list=PLofp2YXfp7TZZ5c7HEChs0_wfEfewLDs7. The course page says the Introduction video comes from an older run.
- **Main reading named on that page:** Jacob Eisenstein's NLP notes (PDF in a GitHub repository): https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf (the page loaded; it shows no license).
- **Textbook, free draft:** Dan Jurafsky and James Martin, *Speech and Language Processing*, 3rd edition draft: https://web.stanford.edu/~jurafsky/slp3/ (chapters posted free; the page shows a release dated 19 August 2026; some chapters are stubs).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.1 | The Illustrated Word2vec - A Gentle Intro to Word Embeddings in Machine Learning | Jay Alammar | https://www.youtube.com/watch?v=ISPId9Lhc1g | length ? | Start | BIKE | Embeddings from first principles (title-based): the idea that words become vectors, which the course reaches in its week 3 after linear and neural classification. | verified; title-based; also in Track B 4.O1; watch once |
| 6.2 | Attention in transformers, step-by-step \| Deep Learning Chapter 6 | 3Blue1Brown | https://www.youtube.com/watch?v=eMlx5fFNoYc | length ? | Deeper | BIKE | The attention mechanism, step by step, visually (title-based); intuition first, before the lecture version in 6.3. | verified; title-based; also in Track B 4.2 and Track C 1.3; watch once |
| 6.3 | Transformer Architecture (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=sLsUD-RcDqg | length ? | Deeper | BIKE | Durrett's own lecture on the transformer, from the week titled "Transformers and Decoding" in his lecture outline; the instructor-recorded version of what 6.2 shows visually. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.4 | BERT: Masked Language Modeling (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=dya_QNFvtiQ | length ? | Deeper | BIKE | Pre-training with masked language modeling (the "Pre-training and Seq2seq LMs" week), the BERT-style model the course description names. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.5 | Part-of-Speech Tagging (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=Llw6qfeAWDs | length ? | Deeper | BIKE | Sequence tagging, the start of the course's "Structured Prediction" weeks (tagging, HMMs, parsing). | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.6 | Open-Domain QA (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=P-j_zeS0Pa8 | length ? | Deeper | BIKE | Question answering over a large collection of documents (the "Question Answering and Dialogue" week); the closest course topic to retrieval-augmented generation. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.7 | The pipeline function | Hugging Face | https://www.youtube.com/watch?v=tiZFewofSLM | length ? | Start | DESK | Demo, title only: from Hugging Face's own channel, the pipeline function of its Transformers library. I could not read the watch page, so do not assume which tasks it shows; code along with a laptop open. | verified; title-based |

Rows 6.3 to 6.6 and the optional rows come from the instructor's own public playlist, so they match the course's order and emphasis best; they are slide lectures, so glance at the screen. The playlist holds more lectures (n-gram and neural language models, beam search, parsing, dialogue, summarization) than fit here.

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.O1 | Instruction Tuning (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=YT3VSlDjrVU | length ? | Deeper | BIKE | The "Modern Large Language Models" week: how pre-trained models are tuned to follow instructions. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O2 | Reinforcement Learning from Human Feedback (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=DwAdhx6GFh8 | length ? | Deeper | BIKE | The same week: RLHF, the place where Block 3's reinforcement learning meets language models. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O3 | Neural and Pretrained Machine Translation (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=bcP4b_4HQ8A | length ? | Deeper | BIKE | Machine translation with neural and pre-trained models ("Machine Translation and Summarization" week). | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |
| 6.O4 | CKY Algorithm (Natural Language Processing at UT Austin) | Greg Durrett | https://www.youtube.com/watch?v=QeDb6mSDSqs | length ? | Scholar | BIKE | Constituency parsing with the CKY dynamic program (the structured-prediction weeks); the most formal row of the block, safe to skip for GenAI purposes. | verified; content per the lecture outline on Durrett's course-materials page (week and topic) and the title |

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

<!-- COURSES 7-14 GO HERE -->
