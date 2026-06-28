# pdf-to-markdown-for-ai
pdf2md — PDF to Markdown for AI chats (macOS)  Convert PDFs to Markdown before pasting into Claude, ChatGPT, or Gemini. Reduces token usage by up to 90%. Drop PDFs in a folder, run pdf2md, paste into chat. Built on Microsoft's MarkItDown. Python 3.10+ required.

# pdf2md — Cut Your AI Token Usage by Up to 90%

> Cut AI token usage by up to 90%. Convert PDFs to Markdown before pasting into Claude, ChatGPT, or Gemini. macOS · Python · MarkItDown.

---

## The Problem

When you upload a PDF directly to an AI chat like Claude or ChatGPT, the AI processes every page as an image. This uses a massive number of tokens — sometimes hitting your daily limit after just a few documents.

| Method | Approx. Tokens (20-page PDF) |
|---|---|
| Upload PDF directly | 60,000 – 120,000 |
| Paste converted Markdown | 4,000 – 12,000 |

**That's up to a 90% reduction** — meaning you can work through far more documents without hitting limits.

---

## How It Works (Once Set Up)

1. Drop your PDF into a folder on your Mac
2. Type `pdf2md` in Terminal and hit Enter
3. The converted text is automatically copied to your clipboard
4. Paste (`Cmd+V`) directly into Claude, ChatGPT, Gemini, or any AI chat

---

## Requirements

- Mac (macOS)
- Python 3.10 or higher

---

## Step-by-Step Setup

### Step 1 — Check Your Python Version

Open **Terminal** (press `Cmd + Space`, type "Terminal", hit Enter) and run:

```bash
python3 --version
```

If it shows **3.10 or higher**, you're good. If it shows something older (like 3.9), download the latest Python from [python.org](https://www.python.org/downloads/) and install it. Then confirm with:

```bash
python3.14 --version
```

> Note: replace `python3.14` throughout these steps with whatever version you installed (e.g. `python3.12`, `python3.13`).

---

### Step 2 — Install MarkItDown

In Terminal, run:

```bash
python3.14 -m pip install 'markitdown[all]'
```

This will download and install everything needed. It may take a minute or two — that's normal.

---

### Step 3 — Create Your PDF Folder

Run this to create a dedicated folder in your home directory:

```bash
mkdir ~/PDFs-for-Claude
```

You'll now see a folder called **PDFs-for-Claude** in your Mac's home directory (the one with your name on it in Finder).

---

### Step 4 — Add the Script

Download `convert_pdfs.py` from this repo and move it into your `PDFs-for-Claude` folder.

---

### Step 5 — Create the `pdf2md` Shortcut

Run this in Terminal (it creates a shortcut so you only ever have to type `pdf2md`):

```bash
echo 'alias pdf2md="python3.14 ~/PDFs-for-Claude/convert_pdfs.py"' >> ~/.zshrc && source ~/.zshrc
```

> Replace `python3.14` with your version if different.

---

### Step 6 — Test It

Drop any PDF into your `PDFs-for-Claude` folder, then run:

```bash
pdf2md
```

You should see something like:

```
Converting 1 new PDF(s)...

Converting: my-document.pdf → my-document.md
  ✓ Done — my-document.md

All done! Your .md files are in ~/PDFs-for-Claude

📋 Copied to clipboard — just Cmd+V into Claude chat!
```

Then just paste into your AI chat. Done.

---

## Every Time You Use It

1. Drop PDF(s) into `~/PDFs-for-Claude`
2. Open Terminal and type `pdf2md`
3. `Cmd+V` into your AI chat

**Already converted a PDF before?** The script skips it automatically. Delete the `.md` file if you want to re-convert.

**Multiple PDFs at once?** Drop them all in and run `pdf2md` — they'll all be converted and combined on your clipboard.

---

## Works With

- [Claude](https://claude.ai) (Anthropic)
- [ChatGPT](https://chat.openai.com) (OpenAI)
- [Gemini](https://gemini.google.com) (Google)
- Any AI chat that accepts pasted text

---

## Credits

Built on top of [MarkItDown](https://github.com/microsoft/markitdown) by Microsoft.
Workflow designed by [Andrew St. Royal](https://stroyalentertainment.com).

---

## License

MIT — use it, fork it, share it.
