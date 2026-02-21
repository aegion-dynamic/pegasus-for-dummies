# Start Here

This book is the **open source ecosystem contributor guide** for **Pegasus**, an open standard Electronic Lab Notebook (ELN) system. It sets context for ELNs and AI in life sciences, explains the ELN open standard, and supports hackathon participants and implementers building on Pegasus.

## Who this is for

- **Ecosystem contributors** — anyone extending or integrating with Pegasus
- **Hackathon and buildathon participants** — teams building AI modules, plugins, or tools that use ELN data
- **Implementers** — developers adopting the open standard or building compatible tools

## Pegasus overview

The Pegasus ELN desktop app uses an IDE-like layout: a left sidebar for navigation and file management, and a main area for editing and viewing content. The welcome screen helps you get started; once you add workspaces, you'll use the same layout for your lab notebooks.

![Pegasus ELN Desktop layout](./images/eln-guide/pegasus-layout.png)

**Main elements:**

- **File Pane** — The **WORKSPACES** section in the left sidebar. It shows a hierarchical file tree of your projects and files (e.g. folders, `.eln` notebooks, `.md`, images). Use it to open files, organize projects, and track what you're working on.
- **Agents** — Accessed via the sidebar (e.g. the person/assistant icon). Agents help you work with your notebook content using AI—search, summarization, or task automation from within the app.
- **Knowledge Index** — The stacked-documents/database icon in the sidebar. It indexes your workspace content so you can search across files and use that context with agents and smart search.
- **Command Palette** — Press **Cmd/Ctrl+K** (or use the "Open Command Palette" option) for quick access to features and commands without hunting through menus.
- **Workspace Management** — Add and switch between workspaces from the sidebar. Each workspace is a root folder (e.g. a project or lab); the file tree under WORKSPACES reflects the files in the active workspace. Use "Add a Workspace" to track your first (or additional) project folders.

## How to use this book

| Chapter | What you'll find |
|---------|------------------|
| **1. ELNs and AI in Life Sciences** | Context and hackathon ideas: what ELNs are, how they're used, and AI opportunities. |
| **2. The ELN Open Standard** | XML spec, primitives, API: root structure, metadata, content, tables, protocols (LabOP), knowledge graph, audit. |
| **3. ELNs at Work** | How life-science practitioners use ELNs day-to-day (planning, recording, data management, inventory, instruments, collaboration, compliance, knowledge management, integration, project management). |
| **4. Hackathon Guide** | Workflows, data types, AI extension ideas, and what buildathon judges look for. |
| **5. Pegasus API** | API reference for building on Pegasus (TBA). |
| **6. Inspirations and Learning** | Creators, tracks, and patterns from the ecosystem (ELN tutorials, research workflows, open science, Jupyter/Git). |
| **7. Idea Bank: BioProtocol and Decentralized Science** | In-depth coverage of open protocols, DeSci, and reproducibility; integrating with Pegasus. |
| **8. Idea Bank: LabOP** | In-depth coverage of the LabOP protocol standard and how it fits with the Pegasus ELN. |

### What buildathon judges care about

When evaluating projects, judges score five areas (substance over polish; evidence required):

- **Scientific utility (30%)** — Solves real researcher pain points (e.g. reproducibility, provenance).
- **Local-first (25%)** — Offline-capable; data stays on the researcher's machine; local models (e.g. Ollama).
- **Open standards (20%)** — Correct use of Pegasus data formats and local API (see [Chapter 2](./chapter_2.md) and [Pegasus API](./chapter_5.md)).
- **Extensibility (15%)** — Others can build on or extend the project; clear structure and docs.
- **Creativity (10%)** — Novel use of AI/ML with notebook data.

Weighted total (max 5.0): **4.2+** winning, **3.8–4.1** strong finalist, **&lt;3.0** participation. Details are in the [Hackathon Guide](./chapter_4.md#evaluation-at-a-glance).

## I want to...

- **Understand ELNs and get hackathon ideas** → Start with [Chapter 1](./chapter_1.md).
- **Implement the standard or build on the API** → Go to [Chapter 2](./chapter_2.md).
- **Prepare for the hackathon** → Read [Chapters 3–4](./chapter_3.md) (ELNs at Work, Hackathon Guide) and the evaluation notes there; then [Chapters 6–8](./chapter_6.md) (Inspirations, Idea Banks).
- **Explore idea banks** → See [Chapter 7](./chapter_7.md) (BioProtocol / DeSci) and [Chapter 8](./chapter_8.md) (LabOP).

---

*© Aegion Dynamic. See [Copyright and Legal Notice](./copyright.md) for full terms and repository information.*
