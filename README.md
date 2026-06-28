# pdf-to-markdown-for-ai
pdf2md — PDF to Markdown for AI chats (macOS)  Convert PDFs to Markdown before pasting into Claude, ChatGPT, or Gemini. Reduces token usage by up to 90%. Drop PDFs in a folder, run pdf2md, paste into chat. Built on Microsoft's MarkItDown. Python 3.10+ required.


# pdf2md — Cut Your AI Token Usage by Up to 90%

> Convert PDFs to Markdown before sending them to Claude, ChatGPT, or any LLM — and stop burning through your context limits.

---

## The Problem

Uploading a PDF directly to an AI chat interface is expensive in tokens. The AI processes every page as an image, which can consume **60,000–120,000 tokens for a 20-page document**. Heavy users hit their daily limits fast — sometimes multiple times in a single work session.

## The Solution

Convert the PDF to Markdown first. Plain text is a fraction of the token cost, and the AI reads it just as accurately.

| Method | Approx. Tokens (20-page PDF) |
|---|---|
| Upload PDF directly | 60,000 – 120,000 |
| Paste converted Markdown | 4,000 – 12,000 |

**That's up to a 90% reduction.**

---

## How It Works

1. Drop one or more PDFs into a dedicated folder
2. Run one command: `pdf2md`
3. The Markdown text is automatically copied to your clipboard
4. Paste directly into Claude, ChatGPT, or any AI chat

---

## Requirements

- macOS only (uses `pbcopy` for automatic clipboard copy)
- Python 3.10 or higher → [Download from python.org](https://www.python.org/downloads/)

---

## Installation

**Step 1 — Install MarkItDown**

[MarkItDown](https://github.com/microsoft/markitdown) is Microsoft's open-source document-to-Markdown converter. Install it via pip:

```bash
python3 -m pip install 'markitdown[all]'
```

> If you have multiple Python versions, use the specific version (e.g. `python3.14 -m pip install ...`)

**Step 2 — Create your folder**

```bash
mkdir ~/PDFs-for-Claude
```

**Step 3 — Add the script**

Download `convert_pdfs.py` from this repo and place it in `~/PDFs-for-Claude/`.

**Step 4 — Create the `pdf2md` shortcut**

```bash
echo 'alias pdf2md="python3 ~/PDFs-for-Claude/convert_pdfs.py"' >> ~/.zshrc && source ~/.zshrc
```

> Replace `python3` with your specific version if needed (e.g. `python3.14`)

---

## Usage

```bash
pdf2md
```

That's it. Drop PDFs into `~/PDFs-for-Claude`, run the command, paste into your AI chat.

**What the script does:**
- Scans the folder for PDFs
- Skips any PDF that already has a matching `.md` file
- Converts new PDFs to Markdown using MarkItDown
- Saves `.md` files alongside the originals
- Copies the converted text to your clipboard automatically

**To re-convert a PDF:** delete its `.md` file and run `pdf2md` again.

---

## Example Output

```
Skipping 2 already-converted PDF(s):
  ↷ contract-2025.pdf
  ↷ proposal-v2.pdf

Converting 1 new PDF(s)...

Converting: invoice-june.pdf → invoice-june.md
  ✓ Done — invoice-june.md

All done! Your .md files are in ~/PDFs-for-Claude

📋 Copied to clipboard — just Cmd+V into Claude chat!
```

---

## Works With

- [Claude](https://claude.ai) (Anthropic)
- [ChatGPT](https://chat.openai.com) (OpenAI)
- [Gemini](https://gemini.google.com) (Google)
- Any LLM interface that accepts pasted text

---

## Supported File Types

Because this uses MarkItDown under the hood, the same script can be extended to convert:

- PDF
- DOCX (Word)
- XLSX (Excel)
- PPTX (PowerPoint)
- HTML
- Images (with OCR)
- Audio (with transcription)

> This repo currently focuses on PDFs. PRs welcome for other formats.

---

## Contributing

Pull requests are welcome. Found a bug or want to add support for additional file types? Open an issue or PR.

---

## Credits

Built on top of [MarkItDown](https://github.com/microsoft/markitdown) by Microsoft.  
Workflow designed by [Andrew St. Royal](https://stroyalentertainment.com).

---

## License

MIT — use it, fork it, share it.
