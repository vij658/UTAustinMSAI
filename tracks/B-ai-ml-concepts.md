# Track B: AI and ML concepts

A watch-while-biking ladder of 48 main videos (plus 30 optional ones, and 7 more bike videos added in the later gap-fill pass) that builds the mental models behind the UT MSAI foundational courses: ML basics, classical ML, deep learning, transformers and LLMs, reinforcement learning, planning and search, ethics, and generative models.

**Total time (honest accounting).** YouTube's oEmbed endpoint does not return duration, and the watch page showed a duration for only some videos. So lengths are known for 11 of the 48 main videos (summing to about 4 h 13 min), shown below as the page stated them. Two long Karpathy talks show only a lower bound taken from their chapter list. The other 35 read "length ?" and I did not estimate them. A total in hours cannot be stated from verified data; once the "length ?" cells are filled in (open each link once), the sum is the answer.

**Order logic.** Block 1 gives the vocabulary. Block 2 is classical ML. Block 3 builds on Block 2's gradient descent to get neural networks. Block 4 builds on Block 3's sequence models to get attention, transformers and LLMs. Block 5 (RL) uses the probability and gradient ideas from Blocks 1-3. Block 6 (planning) uses probability and MDPs from Blocks 2 and 5. Block 7 (ethics) comes after you have seen how models are built and fail. Block 8 closes by comparing generative model families, reusing Blocks 3-4. Inside each block, a visual/intuition video comes before a formal lecture.

**Table legend.**
- Level: Start / Deeper / Scholar.
- Mode: BIKE = works mostly by listening. DESK = needs code, paper, or pausing.
- Status "verified" means the YouTube oEmbed endpoint returned the exact video ID I asked for, with the title and channel shown (copied as returned). It does not mean I watched the video.
- Length: shown only where the YouTube watch page stated it. "length ?" means it was not available. "at least X" is a lower bound from the last chapter marker.
- "What you will get" is based on the video title and, where noted, on the chapter list on the watch page. I have not watched any of these videos.

**UT course mapping.** The block names follow the course topics in the task brief. I could not open https://cdso.utexas.edu/msai in this session (usage limit reached), so the syllabus mapping is not independently confirmed here. Please check it against that page.

**Mode balance.** All 48 original main videos are BIKE, and so are the 7 gap-fill additions on the main path. All DESK items are in the optional sub-lists (the gap-fill row G8, a long graduate lecture, is also optional).

---

## Block 1: What AI/ML is

**Why it matters for UT:** this is the vocabulary (features, loss, overfitting, train/validation/test) that every foundational MSAI course, starting with Machine Learning, assumes you already speak.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.1 | A Gentle Introduction to Machine Learning | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=Gv9_4yMHFhI | 12:45 | Start | BIKE | A plain-language first picture of what machine learning is, before any maths. | verified |
| 1.2 | Machine Learning Fundamentals: Bias and Variance | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=EuBBz3bI-aA | length ? | Start | BIKE | Why a model can be too simple or too wiggly: the overfitting / underfitting mental model. | verified |
| 1.3 | Machine Learning Fundamentals: Cross Validation | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=fSytzGwwBVw | length ? | Start | BIKE | Train/test split and cross-validation: how you estimate performance on unseen data. | verified |
| 1.4 | Lecture 01 - The Learning Problem | caltech | https://www.youtube.com/watch?v=mbyG85GZ0PI | length ? | Deeper | BIKE | Opening lecture of Caltech's Learning from Data course: what "the learning problem" is, including the kinds of learning. This is a full university lecture and is the only verified source here that frames supervised vs unsupervised vs reinforcement; a short animated alternative was not verified. | verified |

**Optional (extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 1.O1 | Lecture 1 "Supervised Learning Setup" - Cornell CS4780 Machine Learning for Decision Making SP17 | Kilian Weinberger | https://www.youtube.com/watch?v=MrLPzBxG95I | length ? | Deeper | BIKE | A second university framing of the supervised setup (data, labels, loss) if 1.4 felt abstract. | verified |

**Full circle:** you can explain, without maths, why a model that scores perfectly on its training data can still fail, and how holding data back (train/validation/test, cross-validation) is how we find out.

<details>
<summary>Recap questions (3)</summary>

1. Q: Why can't you judge a model by its error on the data it was trained on? A: Because it can memorise the training set (overfit); error on unseen data (validation/test) is the honest estimate of how it will behave in the world.
2. Q: What is the difference between the validation set and the test set? A: The validation set is used repeatedly to choose models and settings; the test set is touched once at the end so its score is not biased by those choices.
3. Q: In one sentence, what do bias and variance describe? A: Bias is error from a model being too simple to capture the pattern; variance is error from a model being so flexible that it chases noise in the particular training sample.
</details>

---

## Block 2: Classical machine learning

**Why it matters for UT:** these are the topics listed for the Machine Learning course in the brief (regression and gradient descent, trees, PAC/VC, perceptron, boosting, PCA/SVD, k-means and EM, maximum likelihood vs Bayesian, graphical models); each intuition video comes before the formal lecture.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.1 | Gradient Descent, Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=sDv4f4s2SB8 | length ? | Start | BIKE | Walking downhill on the loss, step by step; the engine behind most training later in the track. | verified |
| 2.2 | StatQuest: Logistic Regression | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=yIYKR4sgzI8 | length ? | Start | BIKE | From a line to a probability: classification with the logistic curve. | verified |
| 2.3 | Decision and Classification Trees, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=_L39rN6gz7Y | length ? | Start | BIKE | How a tree picks its splits. | verified |
| 2.4 | Lecture 5 "Perceptron" -Cornell CS4780 SP17 | Kilian Weinberger | https://www.youtube.com/watch?v=wl7gVvI-HuY | length ? | Deeper | BIKE | The perceptron update rule in a university lecture. | verified |
| 2.5 | Lecture 07 - The VC Dimension | caltech | https://www.youtube.com/watch?v=Dc0sr0kdBVI | length ? | Scholar | BIKE | VC dimension from Caltech's Learning from Data. A full, long lecture, used because I found no verified shorter source for VC dimension. It builds on Caltech lectures 5 and 6 (optional list below); do those first if you feel lost. My watch-page fetch for this ID failed, but oEmbed verified it. | verified |
| 2.6 | AdaBoost, Clearly Explained | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=LsK-xG1cLYA | 20:54 | Start | BIKE | Boosting as many weak learners that vote, with mistakes re-weighted. | verified |
| 2.7 | StatQuest: Principal Component Analysis (PCA), Step-by-Step | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FgakZw6K1QQ | 21:57 | Start | BIKE | PCA walked through step by step. | verified |
| 2.8 | Singular Value Decomposition (SVD): Mathematical Overview | Steve Brunton | https://www.youtube.com/watch?v=nbBvuuNVfco | length ? | Deeper | BIKE | SVD overview from a university professor; connects to PCA in 2.7. | verified |
| 2.9 | StatQuest: K-means clustering | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=4b5d3muPQmA | length ? | Start | BIKE | The k-means loop: assign points, recompute centres. | verified |
| 2.10 | Expectation Maximization: how it works | Victor Lavrenko | https://www.youtube.com/watch?v=iQoXFmbXRJA | 10:39 | Deeper | BIKE | The EM idea, a soft version of the k-means loop. | verified |
| 2.11 | Maximum Likelihood, clearly explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=XepXtl9YKwc | length ? | Start | BIKE | Picking parameters that make the observed data most probable. | verified |
| 2.12 | Bayes' Theorem, Clearly Explained!!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=9wCnvr7Xw4E | 13:59 | Start | BIKE | Updating a belief with evidence; the base of every Bayesian method after this. | verified |
| 2.13 | Maximum A Posteriori (MAP) - Why L2 Regularization is Bayesian in Disguise | DataMListic | https://www.youtube.com/watch?v=Ovuszur2uzk | length ? | Deeper | BIKE | Maximum likelihood vs a Bayesian prior (MAP), and how a prior appears as regularization. | verified |
| 2.14 | undergraduate machine learning 7: Bayesian networks, aka probabilistic graphical models | Nando de Freitas | https://www.youtube.com/watch?v=XgP2hmf7X4U | length ? | Deeper | BIKE | Intro to graphical models from a university course. | verified |

**Optional (desk, or extra if you have time):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 2.O1 | Linear Regression, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=7ArmBVF2dCs | length ? | Start | BIKE | Least-squares line fit; watch before 2.1 if regression is rusty. | verified |
| 2.O2 | PAC learning: the framework | Machine learning classroom | https://www.youtube.com/watch?v=Olqi2aMGdFg | length ? | Deeper | BIKE | Title-level match for the PAC framework. Small channel, content not reviewed; treat as a first pass before 2.5. | verified |
| 2.O3 | Lecture 05 - Training Versus Testing | caltech | https://www.youtube.com/watch?v=SEYAnnLazMU | length ? | Scholar | DESK | Caltech lecture before 2.5 in the course sequence. | verified |
| 2.O4 | Lecture 06 - Theory of Generalization | caltech | https://www.youtube.com/watch?v=6FWRijsmLtE | length ? | Scholar | DESK | Next Caltech lecture before 2.5. | verified |
| 2.O5 | Gradient Boost Part 1 (of 4): Regression Main Ideas | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=3CC4N4z3GJc | length ? | Deeper | BIKE | Gradient boosting after AdaBoost. | verified |
| 2.O6 | Machine Learning Lecture 32 "Boosting" -Cornell CS4780 SP17 | Kilian Weinberger | https://www.youtube.com/watch?v=dosOtgSdbnY | length ? | Scholar | DESK | Formal boosting lecture, after 2.6. | verified |
| 2.O7 | Lecture 7 "Estimating Probabilities from Data: Maximum Likelihood Estimation" - Cornell CS4780 SP17 | Kilian Weinberger | https://www.youtube.com/watch?v=RIawrYLVdIw | length ? | Scholar | DESK | Formal MLE lecture, after 2.11. | verified |
| 2.O8 | Clustering via Gaussian Mixture Models | Carlos Fernandez-Granda | https://www.youtube.com/watch?v=4g5kWmrqnN8 | length ? | Scholar | DESK | EM applied to Gaussian mixtures, after 2.10. | verified |

**Full circle:** you can describe a line fit, turn it into a probability (logistic), grow a tree, vote many weak models into a strong one, squash many features into a few (PCA/SVD), find groups (k-means/EM), and say how a prior (Bayesian) differs from maximum likelihood.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does gradient descent do, in one sentence? A: It repeatedly nudges the parameters in the direction that lowers the loss most steeply, using the slope of the loss at the current point.
2. Q: How is k-means related to EM? A: k-means gives each point a hard assignment to one centre; EM gives soft (probabilistic) assignments and then updates the parameters using those weights, alternating the two steps.
3. Q: What changes when you go from maximum likelihood to MAP? A: You maximise likelihood times a prior instead of likelihood alone, which pulls estimates toward the prior; with a Gaussian prior this acts like L2 regularization.
</details>

---

## Block 3: Neural networks and deep learning

**Why it matters for UT:** the Deep Learning course topics in the brief (neurons, backpropagation, training/tuning/debugging, CNNs, RNN/LSTM, PyTorch) all rest on the gradient-descent picture from Block 2.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.1 | But what is a neural network? \| Deep learning chapter 1 | 3Blue1Brown | https://www.youtube.com/watch?v=aircAruvnKk | length ? | Start | BIKE | The visual picture of neurons, layers and weights. | verified |
| 3.2 | Gradient descent, how neural networks learn \| Deep Learning Chapter 2 | 3Blue1Brown | https://www.youtube.com/watch?v=IHZwWFHWa-w | 20:33 | Start | BIKE | Loss and gradient descent applied to a network; reuses 2.1. | verified |
| 3.3 | Backpropagation, intuitively \| Deep Learning Chapter 3 | 3Blue1Brown | https://www.youtube.com/watch?v=Ilg3gGewQ5U | 12:47 | Start | BIKE | The intuition for how the error flows backward through the network. | verified |
| 3.4 | CS231n Winter 2016: Lecture 6: Neural Networks Part 3 / Intro to ConvNets | Andrej Karpathy | https://www.youtube.com/watch?v=hd_KFJ5ktUc | length ? | Deeper | BIKE | Closest verified fit for training practice plus the start of ConvNets, by title only; content not reviewed. See Gaps for training/tuning/debugging. | verified |
| 3.5 | Neural Networks Part 8: Image Classification with Convolutional Neural Networks (CNNs) | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=HGwBXDKFk9I | length ? | Start | BIKE | Convolution filters and pooling for images, visually. | verified |
| 3.6 | Lecture 5 \| Convolutional Neural Networks | Stanford University School of Engineering | https://www.youtube.com/watch?v=bNb2fEVKeEo | 1:08:56 | Deeper | BIKE | Stanford CS231n lecture on CNNs. A full lecture, used for the formal version after 3.5. | verified |
| 3.7 | Recurrent Neural Networks (RNNs), Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=AsNTP8Kwu80 | length ? | Start | BIKE | A network that carries a state across a sequence. | verified |
| 3.8 | Long Short-Term Memory (LSTM), Clearly Explained | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=YCzL96nL7j0 | 20:45 | Start | BIKE | Gates that let a network remember longer. | verified |

**Optional desk (code along, pause, or read):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 3.O1 | The spelled-out intro to neural networks and backpropagation: building micrograd | Andrej Karpathy | https://www.youtube.com/watch?v=VMj-3S1tku0 | length ? | Deeper | DESK | Build backprop in code to make 3.3 concrete. | verified |
| 3.O2 | The StatQuest Introduction to PyTorch | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=FHdlXe1bSe4 | length ? | Start | DESK | PyTorch basics; have a laptop open. | verified |
| 3.O3 | Building makemore Part 3: Activations & Gradients, BatchNorm | Andrej Karpathy | https://www.youtube.com/watch?v=P6sfmUTpUmc | length ? | Scholar | DESK | Diagnosing training (activations, gradients) in code; the closest verified item for "debugging". | verified |
| 3.O4 | Backpropagation calculus \| Deep Learning Chapter 4 | 3Blue1Brown | https://www.youtube.com/watch?v=tIeHLnjs5U8 | length ? | Deeper | DESK | The chain-rule maths behind 3.3; pause and follow with paper. | verified |
| 3.O5 | The Essential Main Ideas of Neural Networks | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=CqOfi41LfDw | length ? | Start | BIKE | A second, gentler pass over what a network is. | verified |
| 3.O6 | CS231n Winter 2016: Lecture 10: Recurrent Neural Networks, Image Captioning, LSTM | Andrej Karpathy | https://www.youtube.com/watch?v=yCC09vCHzF8 | length ? | Scholar | DESK | Formal sequence-model lecture after 3.8. | verified |

**Full circle:** you can say how a network turns inputs into outputs, how backprop assigns blame to each weight, why CNNs suit images, and why LSTMs were built to fix RNN memory.

<details>
<summary>Recap questions (3)</summary>

1. Q: What does backpropagation compute? A: The gradient of the loss with respect to every weight, by applying the chain rule backward through the layers and reusing intermediate results.
2. Q: Why do CNNs use small shared filters? A: Local patterns (edges, textures) matter and can appear anywhere, so one filter slid across the image detects them with far fewer parameters than a fully connected layer.
3. Q: What problem do LSTM gates address in a plain RNN? A: Vanishing gradients: information and gradients fade over many steps; gates control what is kept, written, and forgotten so long-range information survives.
</details>

---

## Block 4: Transformers and LLMs

**Why it matters for UT:** transformers are the base of nearly all modern deep-learning coursework and of today's LLMs; this block gives attention, pre-training, tokens, scaling and post-training at concept level.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.1 | Transformers, the tech behind LLMs \| Deep Learning Chapter 5 | 3Blue1Brown | https://www.youtube.com/watch?v=wjZofJX0v4M | 27:14 | Start | BIKE | A visual walk through how a GPT-style model is put together, including tokens and embeddings. | verified |
| 4.2 | Attention in transformers, step-by-step \| Deep Learning Chapter 6 | 3Blue1Brown | https://www.youtube.com/watch?v=eMlx5fFNoYc | length ? | Deeper | BIKE | The attention mechanism, step by step, visually. | verified |
| 4.3 | [1hr Talk] Intro to Large Language Models | Andrej Karpathy | https://www.youtube.com/watch?v=zjkBMFhNj_g | at least 59:23 (outro chapter starts there) | Deeper | BIKE | Chapter list on the watch page shows LLM inference and training, finetuning into an assistant, scaling laws (25:43), tool use, and security. Covers the concept-level story end to end. | verified |
| 4.4 | Deep Dive into LLMs like ChatGPT | Andrej Karpathy | https://www.youtube.com/watch?v=7xTGNNLPyMI | at least 3:21:46 (last chapter marker) | Deeper | BIKE | Long, but I found no shorter verified source for the full pre-training to post-training to RLHF story. Split it over three rides using the chapters on the page: 0:00 to 0:59 pre-training and tokenization; 0:59 to 2:07 post-training and hallucinations; 2:07 to 3:10 reinforcement learning and RLHF (chapter starts at 2:48:26). | verified |

**Optional desk or extra:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 4.O1 | The Illustrated Word2vec - A Gentle Intro to Word Embeddings in Machine Learning | Jay Alammar | https://www.youtube.com/watch?v=ISPId9Lhc1g | length ? | Start | BIKE | Embeddings from first principles; watch before 4.1 if "embedding" feels vague. | verified |
| 4.O2 | Decoder-Only Transformers, ChatGPTs specific Transformer, Clearly Explained!!! | StatQuest with Josh Starmer | https://www.youtube.com/watch?v=bQ5BoolX9Ag | length ? | Deeper | BIKE | A second angle on GPT-style models, after 4.2. | verified |
| 4.O3 | Let's build GPT: from scratch, in code, spelled out. | Andrej Karpathy | https://www.youtube.com/watch?v=kCc8FmEb1nY | length ? | Scholar | DESK | Code a tiny GPT; needs the laptop open. | verified |
| 4.O4 | Let's build the GPT Tokenizer | Andrej Karpathy | https://www.youtube.com/watch?v=zduSFxRajkE | length ? | Scholar | DESK | How tokenization works in code. | verified |
| 4.O5 | Post-Training and RLHF Overview \| Post-Training Book Course, Lecture 1 | Nathan Lambert | https://www.youtube.com/watch?v=o6l6tJQgUg4 | length ? | Scholar | DESK | Lecture-style RLHF and post-training overview, after 4.4. | verified |

**Full circle:** you can explain how text becomes tokens and embeddings, how attention mixes information, how pre-training on next-token prediction produces a base model, and why post-training and RLHF turn it into an assistant.

<details>
<summary>Recap questions (3)</summary>

1. Q: In one sentence, what does an attention layer compute? A: For each token, a weighted mix of other tokens' information, where the weights come from how well a query matches each other token's key.
2. Q: What is the pre-training objective of a GPT-style model? A: Predict the next token given the previous tokens, over a very large text corpus.
3. Q: Why is post-training needed after pre-training? A: A base model only continues text; supervised fine-tuning on conversations and preference training (RLHF) shape it to follow instructions and human preferences.
</details>

---

## Block 5: Reinforcement learning

**Why it matters for UT:** the Reinforcement Learning course topics in the brief (bandits, MDPs, dynamic programming, Monte Carlo, temporal-difference, policy gradients, deep RL) run in exactly this order, and RLHF in Block 4 is an application.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.1 | An introduction to Reinforcement Learning | Arxiv Insights | https://www.youtube.com/watch?v=JgvyzIkgxF0 | length ? | Start | BIKE | The agent, environment and reward picture, before any formulas. | verified |
| 5.2 | DeepMind x UCL RL Lecture Series - Exploration & Control [2/13] | Google DeepMind | https://www.youtube.com/watch?v=aQJP3Z2Ho8U | length ? | Deeper | BIKE | The bandit setting and exploration vs exploitation, from a university course (per the title). Full lecture. | verified |
| 5.3 | DeepMind x UCL RL Lecture Series - MDPs and Dynamic Programming [3/13] | Google DeepMind | https://www.youtube.com/watch?v=zSOMeug_i_M | length ? | Deeper | BIKE | MDPs and dynamic programming in one lecture (per the title). Full lecture. | verified |
| 5.4 | RL Course by David Silver - Lecture 4: Model-Free Prediction | Google DeepMind | https://www.youtube.com/watch?v=PnHCvfgC_ZA | length ? | Deeper | BIKE | Monte Carlo and temporal-difference prediction (per the title: model-free prediction). Full lecture. | verified |
| 5.5 | RL Course by David Silver - Lecture 7: Policy Gradient Methods | Google DeepMind | https://www.youtube.com/watch?v=KHZVXao4qXs | length ? | Deeper | BIKE | Optimising a policy directly. Full lecture. | verified |
| 5.6 | DeepMind x UCL RL Lecture Series - Deep Reinforcement Learning #1 [12/13] | Google DeepMind | https://www.youtube.com/watch?v=cVzvNZOBaJ4 | length ? | Scholar | BIKE | Deep RL: neural networks inside RL. Full lecture. | verified |

**Optional (desk or extra):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 5.O1 | RL Course by David Silver - Lecture 1: Introduction to Reinforcement Learning | Google DeepMind | https://www.youtube.com/watch?v=2pWv7GOvuf0 | length ? | Deeper | BIKE | Formal intro after 5.1. | verified |
| 5.O2 | DeepMind x UCL RL Lecture Series - Model-free Control [6/13] | Google DeepMind | https://www.youtube.com/watch?v=t9uf9cuogBo | length ? | Scholar | DESK | Control methods (title: model-free control), after 5.4. | verified |
| 5.O3 | DeepMind x UCL RL Lecture Series - Policy-Gradient and Actor-Critic methods [9/13] | Google DeepMind | https://www.youtube.com/watch?v=y3oqOjHilio | length ? | Scholar | DESK | Second take on policy gradients, after 5.5. | verified |

**Full circle:** you can describe the agent-environment loop, the exploration/exploitation trade-off, how an MDP is solved by dynamic programming when the model is known and by Monte Carlo/TD when it is not, and how policy gradients and deep networks extend this.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is the exploration vs exploitation trade-off? A: Exploiting means picking the action that looks best so far; exploring means trying others to learn if something is better; you need both to maximise long-run reward.
2. Q: How do Monte Carlo and TD differ? A: Monte Carlo waits until an episode ends and uses the actual total return; TD updates after each step by bootstrapping from its current estimate of the next state's value.
3. Q: What is the core idea of a policy gradient? A: Adjust the parameters of the policy itself in the direction that increases expected return, instead of first learning values and acting greedily.
</details>

---

## Block 6: Planning, search and reasoning under uncertainty

**Why it matters for UT:** the Planning course topics in the brief (heuristic search/A*, adversarial search, Bayesian state estimation, MDPs/POMDPs) are covered here; MDPs themselves were introduced in Block 5 (5.3).

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.1 | Step-by-Step: A Star Search | CS188Spring2013 | https://www.youtube.com/watch?v=sAoBeujec74 | 22:17 | Start | BIKE | A worked A* example from the Berkeley CS188 channel. | verified |
| 6.2 | COMPSCI 188 - 2018-08-30 - A* Search and Heuristics | Webcast Departmental | https://www.youtube.com/watch?v=Mlwrx7hbKPs | length ? | Deeper | BIKE | Berkeley lecture on A* and heuristics. Full lecture. | verified |
| 6.3 | CS 188 Lecture 5: Adversarial Search | CS 188 | https://www.youtube.com/watch?v=_3djr6ZXLzQ | length ? | Deeper | BIKE | Berkeley lecture on adversarial (game) search. Full lecture. | verified |
| 6.4 | CS 188 Lecture 18: Hidden Markov Models | CS 188 | https://www.youtube.com/watch?v=0u80UvCAKVo | length ? | Deeper | BIKE | Bayesian state estimation with HMMs. Full lecture. | verified |
| 6.5 | DLRLSS 2019 - POMDPs - Pascal Poupart | Amii | https://www.youtube.com/watch?v=K0wcWi38IGA | length ? | Scholar | BIKE | POMDPs from a summer-school lecture. The only POMDP source I verified from a recognised expert; long. | verified |

**Optional desk:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 6.O1 | Lecture 13: Bayes Nets | CS188Fall2013 | https://www.youtube.com/watch?v=VfyxPtlqZh4 | length ? | Deeper | DESK | Prerequisite for 6.4 if Bayes nets are rusty (also see 2.14). | verified |
| 6.O2 | CS 188 Lecture 19: Particle Filtering | CS 188 | https://www.youtube.com/watch?v=r-bHqY5gaPw | length ? | Scholar | DESK | Approximate state estimation, after 6.4. | verified |
| 6.O3 | Lecture 8: Markov Decision Processes (MDPs) | CS188Spring2013 | https://www.youtube.com/watch?v=i0o-ui1N35U | length ? | Deeper | DESK | Berkeley's MDP lecture as a bridge between Blocks 5 and 6. | verified |

**Full circle:** you can say how A* uses a heuristic to search efficiently, how minimax with pruning handles an opponent, how an HMM keeps a belief about a hidden state, and how POMDPs extend MDPs to act on that belief.

<details>
<summary>Recap questions (3)</summary>

1. Q: What is A*'s evaluation function and when is it optimal? A: f(n) = g(n) + h(n), cost so far plus estimated cost to go; it finds an optimal solution when h never overestimates the true remaining cost (admissible), plus consistency for graph search.
2. Q: What does alpha-beta pruning save? A: It skips branches of the minimax tree that cannot change the final decision, giving the same answer with fewer node evaluations.
3. Q: What is a belief state? A: The probability distribution over hidden states given all actions and observations so far; a POMDP can be treated as an MDP over belief states.
</details>

---

## Block 7: Ethics in AI

**Why it matters for UT:** Ethics in AI is a required MSAI course (per the brief); this block mixes an overview of guidelines, two case-based talks (bias in face analysis, bias in recidivism prediction), and one talk on accountability.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.1 | What is trustworthy AI? | DigitalEU | https://www.youtube.com/watch?v=Imv9SG-zfkU | length ? | Start | BIKE | A short orientation on trustworthy-AI guidelines from the channel named DigitalEU (title match only). | verified |
| 7.2 | FAT* 2018: Joy Buolamwini - Intersectional Accuracy Disparities in Commercial Gender Classification | ACM FAccT Conference | https://www.youtube.com/watch?v=Af2VmR-iGkY | length ? | Deeper | BIKE | Case-based bias talk: accuracy gaps across groups in commercial face analysis. | verified |
| 7.3 | The Accuracy, Fairness, and Limits of Predicting Recidivism | Berkman Klein Center for Internet & Society | https://www.youtube.com/watch?v=G0OE8p-fc10 | length ? | Deeper | BIKE | Case-based fairness talk on a recidivism prediction tool. | verified |
| 7.4 | Turing Lecture: Algorithmic Accountability: Professor Ben Shneiderman, University of Maryland | The Alan Turing Institute | https://www.youtube.com/watch?v=UWuDgY8aHmU | length ? | Deeper | BIKE | A university-professor lecture on accountability and transparency. | verified |

**Optional (extra or desk):**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 7.O1 | What is our ethical responsibility with AI & Machine Learning? - Fei-Fei Li & Andrew Ng | Stanford Online | https://www.youtube.com/watch?v=Aws-cOIXsNQ | length ? | Start | BIKE | A conversational overview from two prominent researchers. | verified |
| 7.O2 | Fairness, part 1 - Moritz Hardt - MLSS 2020, Tübingen | virtual mlss2020 | https://www.youtube.com/watch?v=Igq_S_7IfOU | length ? | Scholar | DESK | The formal fairness criteria, after 7.3. | verified |
| 7.O3 | What is the Problem to Which Fair Machine Learning is the Solution? \| Solon Barocas \| AI Now 2017 | AI Now Institute | https://www.youtube.com/watch?v=S_AkPi6-r3Y | length ? | Scholar | DESK | A critical look at what "fair ML" is for. | verified |

**Full circle:** you can describe where bias enters an ML pipeline, give two concrete cases, and say how accountability and transparency differ.

<details>
<summary>Recap questions (3)</summary>

1. Q: How can a model with high overall accuracy still be unfair? A: Its errors can be concentrated on certain groups, so average accuracy hides large gaps for those groups (the face-analysis case in 7.2).
2. Q: Why can't every fairness criterion be satisfied at once in the recidivism setting? A: When groups have different base rates, criteria such as calibration and equal error rates cannot all hold together, so choosing one is a value judgment, not only a technical one.
3. Q: What is the difference between transparency and accountability? A: Transparency is being able to see how a system works or decides; accountability is having someone answerable and a way to challenge or remedy its outcomes.
</details>

---

## Block 8: Generative models overview

**Why it matters for UT:** it ties together Blocks 3 and 4 and prepares you for the generative-AI material in later electives and in the Deep Learning course.

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.1 | But how do AI images and videos actually work? \| Guest video by Welch Labs | 3Blue1Brown | https://www.youtube.com/watch?v=iv-5mZ_9CPY | length ? | Start | BIKE | Visual explanation of how AI image generators work (diffusion family, by title). | verified |
| 8.2 | Generative Adversarial Networks (GANs) - Computerphile | Computerphile | https://www.youtube.com/watch?v=Sw9r8CL98N0 | length ? | Start | BIKE | The generator-vs-discriminator idea. | verified |
| 8.3 | Variational Autoencoders - EXPLAINED! | CodeEmporium | https://www.youtube.com/watch?v=fcvYpzHmhvA | length ? | Deeper | BIKE | Autoencoders and the variational twist. | verified |

Autoregressive language models are covered by 4.1 to 4.4, so no extra video is needed here.

**Optional desk:**

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| 8.O1 | Stanford CS236: Deep Generative Models I 2023 I Lecture 1 - Introduction | Stanford Online | https://www.youtube.com/watch?v=XZ0PMRWXBEU | length ? | Scholar | DESK | University introduction to the families of generative models; full lecture, only if you want the formal view. | verified |

**Full circle:** you can say in one sentence how each family generates: autoregressive (next token), GAN (adversarial game), VAE (decode a sampled latent), diffusion (reverse a noising process).

<details>
<summary>Recap questions (3)</summary>

1. Q: How does a diffusion model generate an image? A: It is trained to remove noise step by step; to generate, it starts from pure noise and repeatedly denoises toward an image.
2. Q: What are the two players in a GAN? A: A generator that makes fakes and a discriminator that tries to tell fakes from real data; training pits them against each other.
3. Q: How does a VAE differ from a plain autoencoder? A: The encoder outputs a distribution over a latent space (with a regularizer), so you can sample latents and decode new examples, not just reconstruct inputs.
</details>

---

## Gap-fill pass 1 (2026-11-10)

Method: every video below passed the same YouTube oEmbed check as the main path (the lookup returned the title and channel copied here, for the ID in the link). I did not watch any of them, and a length is shown only where I saw one on a page (the source is named); otherwise it says "length ?".

### Short overview of the kinds of learning (Block 1 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G1 | Supervised vs. Unsupervised Learning | IBM Technology | https://www.youtube.com/watch?v=W01tIRP_Rqs | 6:54 (per tubescript transcript page) | Start | BIKE | A short explainer on supervised learning (classification and regression) versus unsupervised learning (clustering, association, dimensionality reduction), with a brief mention of semi-supervised. It does not cover reinforcement learning; that is introduced by 5.1. | verified; content per tubescript transcript page |

Belongs after #1.1 (the gentle first picture of machine learning): suggested watch order 1.1, then G1 as a quick vocabulary pass, then 1.2. For the reinforcement side, 5.1 is the existing introduction, so G1 plus 5.1 together cover the three kinds.

### Training and debugging neural networks (Block 3 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G2 | Lecture 6 \| Training Neural Networks I | Stanford University School of Engineering | https://www.youtube.com/watch?v=wEoyxE0GP2M | length ? | Deeper | BIKE | Stanford CS231n (Spring 2017) lecture whose course-syllabus line reads "Activation functions, initialization, dropout, batch normalization". Slide-heavy, so glance at the screen between pedals. | verified; content per CS231n 2017 syllabus line |
| G3 | Lecture 7 \| Training Neural Networks II | Stanford University School of Engineering | https://www.youtube.com/watch?v=_JB0AO7QxSA | length ? | Deeper | BIKE | Next CS231n lecture; the syllabus line reads "Update rules, ensembles, data augmentation, transfer learning" (update rules are the optimizer variants such as momentum). Slide-heavy; pause for any formulas. | verified; content per CS231n 2017 syllabus line |

Belongs after #3.6 (CS231n Lecture 5 on CNNs, which Lectures 6 and 7 follow in the same course): suggested watch order 3.6, then G2, then G3. Both assume backprop from 3.3. Neither is a hands-on debugging walkthrough as far as I can tell from the syllabus lines, so 3.O3 (DESK) is still the closest item for diagnosing training in code. I did not find a Karpathy "Recipe for Training Neural Networks" video (only the blog post and third-party read-throughs), and the Andrew Ng CS230 lectures did not pass the oEmbed check.

### Fine-tuning, LoRA and scaling (Block 4 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G4 | State of GPT \| BRK216HFS | Microsoft Developer | https://www.youtube.com/watch?v=bZQun8Y4L2A | length ? | Deeper | BIKE | Karpathy's Microsoft Build 2023 talk. Third-party notes list the assistant training pipeline (pre-training, supervised fine-tuning, reward modelling, RLHF), then applications such as prompting techniques, retrieval-augmented LLMs and a finetuning section with default recommendations. | verified; content per third-party notes gist (section headings) |
| G5 | What is LoRA? Low-Rank Adaptation for finetuning LLMs EXPLAINED | AI Coffee Break with Letitia | https://www.youtube.com/watch?v=KEv-F5UkhxU | at least 6:14 (last chapter marker) | Deeper | BIKE | A short explainer; the chapter list reads: why finetuning LLMs is costly, how LoRA works, low-rank adaptation, LoRA vs other approaches. | verified; content per watch-page chapter list |
| G6 | RAG vs Fine-Tuning vs Prompt Engineering: Optimizing AI Models | IBM Technology | https://www.youtube.com/watch?v=zYGDpG-pTho | 11:18 (per sozai transcript page) | Start | BIKE | A comparison of the three ways to adapt a model to a task: what each costs, what each can and cannot add, and how they are combined. | verified; content per sozai transcript page |
| G7 | Chinchilla Explained: Compute-Optimal Massive Language Models | Edan Meyer | https://www.youtube.com/watch?v=PZXN7jm9IC0 | 32:45 (per the watch page) | Deeper | BIKE | A walk through DeepMind's Chinchilla paper; chapters: overview, paper introduction, methods, scaling implications, Chinchilla overview and performance, summary, critiques. It covers the model-size versus data trade-off for a compute budget, not scaling laws in general. A solo creator's channel, not a university; paper figures are shown, so glance at the screen. | verified; content per watch-page chapter list and summary |

Belongs after #4.4 (the post-training and RLHF story): suggested watch order G4 (the assistant pipeline and when to fine-tune), G5 (what LoRA changes), G6 (choosing between fine-tuning, retrieval and prompting), then G7, which extends the scaling-laws chapter at 25:43 of 4.3 and could also be placed right after 4.3.

### POMDPs (Block 6 gap)

| # | Title | Channel | Link | Length | Level | Mode | What you will get | Status |
|---|-------|---------|------|--------|-------|------|-------------------|--------|
| G8 | Lecture 15 Partially Observable MDPs (POMDPs) -- CS287-FA19 Advanced Robotics at UC Berkeley | Pieter Abbeel | https://www.youtube.com/watch?v=2dNp7QyoF_k | length ? | Scholar | DESK | A Berkeley graduate lecture on POMDPs (title and short description only; no chapter list was available). Expect a full, mathematical lecture that assumes MDPs, not a short intro. | verified; title-based |

Belongs after #6.5 (Poupart's POMDP lecture): suggested watch order 6.5 first, then G8 only if you want a second, graduate-course view. Treat it as optional.

---

## Gaps

- **Training, tuning and debugging neural networks (Block 3):** no concept-level, BIKE-friendly video was verified. The closest items are CS231n 2016 Lecture 6 (3.4, title only) and Karpathy's makemore Part 3 (3.O3, DESK). Filled in gap-fill pass 1: G2, G3 (two full CS231n lectures; still no short, hands-on debugging video).
- **Short animated overview of supervised vs unsupervised vs reinforcement learning (Block 1):** candidates from small channels were found but not included; Caltech Lecture 1 (1.4) is the verified source. Filled in gap-fill pass 1: G1 (supervised vs unsupervised only; no credible short that covers all three kinds was found, and reinforcement learning is introduced by 5.1).
- **PAC learning and VC dimension (Block 2):** only one small-channel PAC video (2.O2) and the long Caltech lecture sequence; no short visual VC video verified. Still open after pass 1: the candidates that passed oEmbed came from small channels ("PAC Learning and VC Dimension" by John Mount, ID X4Oxst5huQA, and a worked-example video by Mahesh Huddar, ID vbQovP_Y9p8) and I could not read a page that describes their content, so I added none. 2.O2 and the Caltech lectures (2.5, 2.O3, 2.O4) stay the only PAC/VC sources.
- **Graphical models (Block 2):** a single introductory lecture (2.14); no dedicated short visual video. Still open after pass 1: the oEmbed-passing candidates were a full Heidelberg lecture (ID KnDP8-S7gl4, "Lecture 15.1: Bayesian Networks/Probabilistic Graphical Models | ML19", whose watch page I could not read) and small-channel videos on d-separation and Bayes nets; none is short and visual from a credible channel, so none is added. 6.O1 and 2.14 stay the references.
- **Scaling laws and fine-tuning concepts (Block 4):** only as chapters inside Karpathy's talks (4.3, 4.4). Dedicated videos exist but their channels were not vetted. Filled in gap-fill pass 1: G4, G5, G6, G7 (fine-tuning, LoRA, fine-tuning vs retrieval vs prompting, and Chinchilla only). A general scaling-laws lecture is still open: the Stanford CS336 scaling-laws lecture and the Stanford CS229 "Building LLMs" lecture failed the oEmbed check, and the other scaling-law explainers that passed came from small channels I did not trust.
- **POMDPs (Block 6):** one long expert lecture (6.5). A short POMDP intro from a small channel exists (ID Ggcl0GfJjfc, oEmbed ok) but I did not include it because I could not judge its quality. Filled in gap-fill pass 1: G8 (a long Berkeley graduate lecture, not a short intro). The Ggcl0GfJjfc candidate ("POMDP Introduction", channel yagcik) passed oEmbed again but its page could not be read, so it is still not used; the Stanford AA228 "Offline Belief State Planning" lecture (ID vmwq4w53e9Q) failed the oEmbed check, so it is not listed.
- **Ethics guidelines (Block 7):** only a short orientation (7.1); no university lecture on the EU/OECD guidelines was verified. Still open after pass 1: nothing from a university or standards body on the EU, OECD or NIST guidelines passed the check; the EU AI Act and NIST videos found came from a law firm, a training company or small channels. Two credible but general items passed oEmbed and are not guideline-specific, so I did not add them: "What is AI ethics? Oxford Professor Edward Harcourt explains" (University of Oxford, ID Gpf_ttt_c8M) and "The Turing Lectures: Can we trust AI?" (The Alan Turing Institute, ID 7SyAC5TsEsQ).
- **Stanford CS25 introduction to transformers (ID XfpMkf4rD6E):** oEmbed refused, so excluded. Still open after pass 1: no other verified version came up in this pass; several other Stanford Online lecture IDs also failed oEmbed, so a Stanford Online transformers lecture may be a general limitation of the check.

## Not checked

- I have not watched any video; "What you will get" is from titles and, for two Karpathy talks, chapter lists on the watch page.
- Lengths: the watch page stated a duration for only 11 main videos. The rest read "length ?". I did not estimate, so total hours are not available.
- The UT syllabus mapping: https://cdso.utexas.edu/msai could not be opened in this session. Course-topic claims come from the task brief.
- Gap-fill rows (G1 to G8): I did not watch any of them. Lengths are given only where I saw one on a page (G1 and G6 on third-party transcript pages, G5 as a lower bound from its last chapter marker, G7 on the YouTube watch page); every other row shows "length ?". Content notes come from the named syllabus lines, chapter lists, notes or transcript pages, or from the title only (G8), as marked in the Status column. Level and Mode tags for these rows are my judgement.
- Whether each video remains available over time, and whether Level/Mode tags match the actual pace and need for pausing.
- Whether channel re-uploads exist for lectures I selected (I used the original or official channel where search surfaced it, and dropped third-party re-uploads).
