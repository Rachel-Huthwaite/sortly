# Sortly 🗂️
### A personal desktop file organiser — built to solve a real problem.

---

## Motivation

As a former graphic designer, I developed a bad habit of saving files fast
and asking questions later. Working at speed meant my Desktop and Downloads
folders became overwhelmingly cluttered — a graveyard of assets, exports,
and half-finished projects with no clear structure.

I always wanted a tool that could do the tidying for me. Something where I
could point at a folder, press a button, and have everything land where it
belongs. Sortly is that tool — built first for me, but designed to be useful
for anyone who's ever looked at their Downloads folder and felt despair.

---

## What Sortly Does

Sortly lets you navigate your computer's directories and choose which folders
you want to organise. It scans the selected directory and automatically sorts
files into categorised subfolders — images, documents, videos, code files,
and more.

It also includes a **selective mode** where instead of organising everything,
you can target specific file types. Only want to round up your images? Done.

Sortly is built around one rule: it should never do something you didn't
ask it to. Files that shouldn't move, won't — and the app will always give
you control over what happens.

---

## Features

- Navigate and select any directory on your machine
- Automatically sort files into categorised folders
- Selective mode — choose specific file types to organise
- Safe handling — prompts before moving files that may have path dependencies

---

## Roadmap

Sortly is being built in phases:

| Phase | Description | Status |
|-------|-------------|--------|
| v0.1 | Project setup and scaffolding | ✅ Complete |
| v0.2 | Core CLI — directory navigation and file organisation via terminal | 🔄 In Progress |
| v0.3 | Testing and documentation | ⏳ Planned |
| v0.4 | GUI — visual directory navigation with Tkinter | ⏳ Planned |
| v0.5 | Packaging — installable desktop application | ⏳ Planned |

---

## Getting Started

> Full installation instructions will be added as the project develops.

For now, Sortly runs via the terminal. To get started locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/sortly.git
cd sortly

# Set up virtual environment
python -m venv .venv
source .venv/Scripts/activate  # Windows (bash)
source .venv/bin/activate       # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run Sortly
python main.py
```

---

## Project Structure

sortly/
├── main.py          # Entry point — CLI argument parsing
├── organiser.py     # Core logic — scans and moves files
├── categories.py    # File type definitions and extensions
├── utils.py         # Shared helper functions
├── tests/           # Unit tests
├── docs/            # Extended documentation
├── requirements.txt
└── .gitignore

> This structure will expand as the project grows.

---

## Contributing

Contributions, suggestions, and feedback are welcome. Please read
[CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

---

## License

This project is licensed under the MIT License.
See [LICENSE](LICENSE) for details.