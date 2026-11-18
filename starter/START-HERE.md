# Start Track H on your Mac

This gets your MacBook (Apple silicon) ready for **Milestone 1 only** (Blocks 1-6). Docker, Ollama, Postgres and AWS are not installed now; each arrives in the block that needs it, so nothing here is a cold start later.

Total time: about 1 to 1.5 hours, split over a ride and a desk session.

---

## Step 1 (on the bike, 44 minutes): Block 0, the map

Watch these in order. They are the boxes of the diagram at the top of Track H.

| # | Video | Length |
|---|---|---|
| 0.1 | ByteByteGo: What happens when you type a URL into your browser? | 5:20 |
| 0.2 | IBM Technology: What is a REST API? | 9:12 |
| 0.3 | NGINX: What is an API Gateway? | 2:16 |
| 0.4 | Gaurav Sen: What is LOAD BALANCING? | 13:50 |
| 0.5 | IBM Technology: RAG vs Fine-Tuning vs Prompt Engineering | 13:10 |

Afterwards (5 minutes, paper is fine): draw the Track H diagram from memory, from "You (browser)" down to "Model". Keep the drawing; you will redraw it at each milestone.

---

## Step 2 (desk, about 20 minutes): install the tools

Open **Terminal** and run the check first. It only looks; it installs nothing and changes nothing.

```bash
bash check_mac.sh
```

Then install whatever it reports as missing:

1. **Homebrew** (the Mac package manager), if missing: the one-line install command is on https://brew.sh. When it finishes, run the two `echo ... >> ~/.zprofile` / `eval ...` lines it prints so `brew` is on your PATH, then open a new Terminal window.
2. **Python 3.12** (Track H needs 3.11 or later; the Python that ships with macOS is older):
   ```bash
   brew install python@3.12
   python3.12 --version
   ```
   In this track, create virtual environments with `python3.12 -m venv .venv`. Inside an activated venv, plain `python` and `pip` are the right ones.
3. **Git** (comes with Apple's command line tools, which Homebrew installs). Tell Git who you are, once:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "the-email-you-use-on-github"
   git config --global init.defaultBranch main
   ```
4. **VS Code**:
   ```bash
   brew install --cask visual-studio-code
   ```
   Open it, install the **Python** extension (by Microsoft), then press Cmd+Shift+P and run "Shell Command: Install 'code' command in PATH" so `code .` works from Terminal.

Run `bash check_mac.sh` again: everything should say OK except the OpenAI key, which is next.

---

## Step 3 (desk, about 15 minutes): the OpenAI account, with a spending cap

You do this part yourself in the browser; never paste the key into a chat.

1. Sign in at https://platform.openai.com (this is the API platform; a ChatGPT subscription does not include API usage).
2. Under Billing, add a small prepaid credit (Track H's first six blocks cost cents to a few dollars in total with a small model).
3. Under the organization's Limits page, set a monthly budget and an email alert, so a bug can never run up a bill.
4. Create a **project** called `docdesk`, then an API key inside it. Copy the key once into a safe place (your password manager). You will paste it into a `.env` file in Block 1, never into code.

(Anthropic works too: https://console.anthropic.com, same idea. Track H's main videos use OpenAI.)

---

## Step 4 (desk, 10 minutes): your DocDesk repository

DocDesk is the project you grow through all 22 blocks. The `docdesk/` folder in this kit has only the files that are not part of any lesson: a `.gitignore` that keeps secrets and venvs out of Git, a `.env.example`, and a README with a block log.

```bash
mkdir -p ~/code
cp -R docdesk ~/code/docdesk
cd ~/code/docdesk
git init
git add .
git commit -m "DocDesk: empty skeleton"
```

Then create an empty **private** repository called `docdesk` on GitHub (no README, no .gitignore; you already have them) and push to it with the two commands GitHub shows you. A private repo is right: it will hold your code, never your keys (`.env` is ignored).

---

## Step 5 (desk, about 1 hour): Block 1

Open the Track H page at Block 1 and follow it exactly:

1. Video 1.1 (Corey Schafer, venv, 14 min): practise in a scratch folder `~/code/llm-hello/`.
2. Video 1.2 (Data with Dylan, first OpenAI call, 17 min): type along in the same folder.
3. Then **Carry it into DocDesk**: the venv, `.env` (copy `.env.example` to `.env` and paste your key), `requirements.txt` and `smoke_test.py` go into `~/code/docdesk/`.
4. **Done when:** `python smoke_test.py` prints OK, and `git status` does not list `.env`. Commit, push, and tick 1.1 and 1.2 on the Track H page.

Write one line in the README's block log ("Block 1, date, what worked, what confused me"). That log is what makes the capstone design document easy in Block 22.

---

## If something goes wrong

- `command not found: brew` after installing it: you skipped the PATH lines Homebrew printed; open a new Terminal after adding them.
- `python3.12: command not found`: run `brew link python@3.12` or open a new Terminal.
- `pip` installs into the wrong place: the venv is not active. Run `source .venv/bin/activate`; the prompt shows `(.venv)` and `which python` points inside `.venv`.
- `openai.AuthenticationError`: the key in `.env` is wrong, has a space or quotes around it, or `.env` is not in the folder you run from.
- `openai.RateLimitError` mentioning quota: the account has no prepaid credit yet (Step 3).
- You see `openai.ChatCompletion.create` in a tutorial: that is the old SDK; use `client = OpenAI()` and `client.chat.completions.create(...)` or `client.responses.create(...)`.
