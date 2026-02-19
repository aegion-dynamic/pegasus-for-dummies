# Hackathon Guide

Electronic Lab Notebooks (ELNs) are software tools that replicate the traditional paper notebooks scientists use to record experiments. An ELN lets a researcher enter protocols (step-by-step methods), observations, notes, and data on a computer or tablet. These digital lab notebooks make experiment records easy to search, share, and back up. ELNs allow scientists to access, search, and share results from an experiment, offering advantages like data security, auditing, and collaboration over analog notebooks. In practice, ELNs often include time stamps and access controls, so each entry is tracked and legally traceable, just like a paper lab notebook.

## How ELNs are used in life sciences

In biology, chemistry and biomedical labs, ELNs are used every day to plan, run, and document experiments. A typical workflow might look like:

- **Planning an experiment:** The scientist writes the objective and detailed procedure (the "protocol") in the ELN. This can include listing reagents, equipment, and expected outcomes.
- **Recording results:** As the experiment proceeds, the researcher enters observations (e.g. color changes, measurements) and data (tables of values, spectra, etc.) into the notebook. They can also attach images (microscope pictures, gel photos) or instrument output files directly to the entry.
- **Inventory and resources:** ELNs often link to inventories of samples and reagents. Lab members note which chemicals or biological samples they used, helping track inventory and avoid waste. Some systems even record equipment calibrations or maintenance.
- **Analysis and conclusions:** After finishing the experiment, scientists can use the ELN to analyze data (plotting graphs, computing results) and write conclusions. For instance, one lab's Notion-based ELN has a section for conclusions and even offers an AI-assisted draft to overcome writer's block.
- **Collaboration and review:** ELNs make it easy to share work with teammates. Colleagues can be assigned to review an experiment entry (e.g. a status field "In Review" prompts a peer check). Because entries are digital, others can search previous experiments or comment asynchronously, greatly improving communication. ELNs support the FAIR principles (making data Findable, Accessible, Interoperable, Reusable) and allow oversight by PIs, which paper notebooks cannot.

In summary, an ELN in a life-science lab becomes the central record of everything: from experimental goals and protocols, through raw data and images, to final results and interpretations. Modern ELNs may also integrate with lab instruments, automatically importing measurements instead of printing them out by hand.

## Data types in a lab notebook

A lab notebook entry can contain many kinds of data, often more than on paper. Common data types include:

- **Structured data:** Numeric or tabular data already in a standard format (e.g. a spreadsheet of absorbance readings, a CSV file of instrument results). Structured data is easy to parse automatically.
- **Unstructured data:** Free-form content that needs processing. Examples: photographs (e.g. of cell cultures or gels), microscopy images, handwritten notes (if scanned), graphs, maps, and sequence data. A lab notebook might include raw photos of a gel or an X-ray crystallography image. These require digitization or AI tools to interpret. Any handwritten observations or printed reports fall under unstructured data as well.
- **Semi-structured data:** A mix of both. For instance, a scanned instrument printout with metadata (time, sample ID) is semi-structured – the numbers are structured but still need context. Similarly, a table of PCR cycle data with attached notes is semi-structured: it's tabular data plus descriptive tags. Semi-structured data has some metadata (e.g. experiment date, sample name) that can help make sense of it.
- **Attachments and multimedia:** ELNs can store any file type. Common attachments include charts and plots (graphs of experimental results), raw data files (CSV, Excel, or proprietary instrument files), PDFs of articles or reports, and chemical diagrams (drawings of molecular structures). For biological labs, this could also include DNA sequence files or images from sequence alignments.
- **Protocol and method text:** The detailed written protocol itself (often copied from published sources or standardized methods) lives in text form. This may be entered as structured fields (e.g. steps in a checklist) or free-form text, and it can be linked to resources like reagent data sheets or literature references.

In essence, the ELN captures everything about an experiment: the narrative text, the quantitative measurements, and any supporting media. Modern data management views this as the "central repository of facts, statistics, results, and other project information," integrating experimental methods, raw data, and metadata.

## Ideas for AI extensions and projects

Since Pegasus uses open standards and provides a local API, it's ideal for building AI plugins. Here are some seed ideas and inspiration.

### Open Data & Interoperability

Ensure that experimental data is exported in open, machine-readable formats (e.g. CSV, JSON, RO-Crate packages). Relying on proprietary formats risks vendor lock-in. Pegasus's open-standard approach means all notebook data (text, tables, images, metadata) can be parsed by any tool. Hackathon modules should leverage this – for example, define a clear JSON schema for experiment entries or use community standards (like the ELN Consortium file format). This makes it easy for an AI to read any experiment's data or to write back a report or summary.

### Local AI Integration (Ollama, Local LLMs)

Pegasus runs on the local desktop, just like tools such as Ollama allow running LLMs on-premise. Ollama exposes a chat API endpoint on the local machine. A hackathon project could connect Pegasus to a local LLM via Ollama: for instance, call `/api/chat` with lab data as context. This means the AI skill runs offline, keeping all lab data secure. For example, an AI skill might fetch an experiment's contents from Pegasus's API, send it to the local model for analysis or question-answering, and then return a written summary or insight – all without ever hitting the internet.

### AI use cases in life sciences

There are many promising applications of ML/AI in lab research that can integrate Pegasus data:

- **Experiment Summarization:** Use an LLM to read the weekly log of an experiment and generate a concise conclusion or abstract for it.
- **Semantic Search and Retrieval:** Create an embedding-based search engine so scientists can query: "Show me experiments involving protein X with positive results." The AI can interpret the query, embed it, and find relevant notebook pages.
- **Protocol Recommendation:** Given the metadata and partial results of an experiment, an AI could suggest next steps or alternative protocols (pulling from open resources like Bio-protocol).
- **Data Analysis Automation:** Use ML models to automatically analyze attached data. For instance, identify bands on a gel image, count cells in a microscopy photo, or normalize and graph numeric results.
- **Anomaly Detection:** Machine learning could flag unusual results (outliers) or missing steps in an experiment, prompting the user to double-check their procedure or data.
- **Hypothesis Testing:** Given past results stored in Pegasus, an AI could suggest hypotheses or design new experiments (a form of "lab notebook-powered intelligence").

Research in AI for science often combines retrieval-augmented generation (RAG) and knowledge graphs. Pairing an LLM with domain-specific knowledge graphs and curated data improves accuracy and traceability. A Pegasus plugin could, for instance, build a custom knowledge graph of the lab's experiments (linking reagents, methods, outcomes) and let an LLM query it to answer user questions more reliably.

### Interactive Knowledge Graphs

Build a graph database where nodes are experiments, protocols, samples, reagents, and results, and edges capture "used", "contains", or "derived from" relationships. An AI-driven interface could let users ask complex questions: e.g. "Which experiments used enzyme Y and what were their yields?" or "Show me the chain of methods and samples that led to this final result." Knowledge graphs make rich use of ELN data's structured relationships. By integrating Pegasus's data into a KG, we enable visual exploration of lab work and empower AI queries that trace reasoning steps.

### Agentic AI (OpenClaw/Moltbot inspiration)

Imagine an AI assistant for the lab, inspired by projects like OpenClaw/Moltbot. OpenClaw (formerly Moltbot) is an open-source AI agent that runs on your own computer, with the ability to install software and manipulate files by itself. It "gives [the AI model] so-called hands…so it can run commands and manipulate files". In a lab context, one could build an "auto lab assistant" that watches Pegasus's events. For example, a scientist could tell it (by chat or voice): "Take the latest sequencing results, run the analysis pipeline, and update the notebook with a summary." The agent would then break this goal into steps, run the pipeline software, and write the output back into Pegasus. A hackathon task might be to create a simple local agent that uses Pegasus's API: e.g., an AI that, when a new data file appears, automatically generates a report entry or reminds the user about an incomplete protocol.

### Open Protocols & Distributed Science

Leverage open sharing of experimental protocols to link Pegasus with distributed science. Bio-protocol is an open-access repository of peer-reviewed life science protocols, and platforms like protocols.io allow researchers to share and discuss detailed methods. A Pegasus plugin could, for example, query these services: given a protocol name or key step, retrieve matching published protocols, or check whether a lab's procedure follows a known standard. Conversely, users could export their own experimental protocol from Pegasus and contribute it to an open database, helping the global "distributed science" community. This fosters reproducibility: anyone could see exactly how an experiment was done, compare methods, or even crowdsource improvements.

Inspiration for this hackathon includes open-source AI projects like OpenClaw/Moltbot (local AI agents that "run your computer") and collaborative science platforms like Bio-protocol. Participants should feel free to mix and match ideas: for instance, build a knowledge-graph explorer that uses an LLM backend (via Ollama) and displays results in the Pegasus UI, or a voice-activated lab assistant that reads your notebook and responds. The key is to harness Pegasus's open data – structured experiment records, metadata, and attachments – to create AI tools that make lab work easier, more insightful, and more collaborative.

## Evaluation at a glance

Buildathon projects are scored 1–5 on five criteria (weighted total, max 5.0). Judges prioritize **substance over polish** and require **evidence** (demo/code).

| Criterion | Weight | What counts |
|-----------|--------|-------------|
| Scientific utility | 30% | Solves real researcher problems (reproducibility, provenance, workflow gaps); clear impact. |
| Local-first design | 25% | Works offline; data stays on machine; local models (e.g. Ollama); no cloud dependency for core function. |
| Open standards compliance | 20% | Correct use of Pegasus data formats and API; see [Chapter 2](./chapter_2.md) and [Pegasus API](./chapter_5.md) (TBA). |
| Extensibility | 15% | Others can extend or build on the project; clear structure, docs, extension points. |
| Creativity | 10% | Novel combination of AI/ML with notebook data; strong domain adaptation. |

**Thresholds:** 4.2+ winning; 3.8–4.1 strong finalist; &lt;3.0 participation. A short summary of what judges look for is also in [Start Here](./chapter_0.md#what-buildathon-judges-care-about).

## Summary

An ELN is a digital lab notebook that captures all aspects of scientific experiments. In life sciences, ELNs are used daily to plan experiments, record detailed data (numbers, images, notes), manage samples, and share results with colleagues. Lab notebooks contain varied data: structured spreadsheets, unstructured images and text, and everything in between. The Pegasus platform's open standard makes it ideal for AI extensions: developers can use local LLM frameworks (like Ollama) to analyze notebook data, incorporate domain knowledge graphs to improve reasoning, draw on community protocol databases (Bio-protocol), or even create local AI agents akin to OpenClaw that automate lab tasks. This guide should spark ideas for modules that link life-science knowledge, AI models, and the rich content of the ELN to advance research productivity and reproducibility.

## References and further reading

- [Electronic Laboratory Notebook (ELN) | NNLM](https://www.nnlm.gov/guides/data-glossary/electronic-laboratory-notebook-eln)
- [Electronic Lab Notebooks | Data Management](https://datamanagement.hms.harvard.edu/collect-analyze/electronic-lab-notebooks)
- [Electronic lab notebook - Wikipedia](https://en.wikipedia.org/wiki/Electronic_lab_notebook)
- [An AI-ready lab notebook for life science](https://erikaaldendeb.substack.com/p/an-ai-ready-lab-notebook-for-life)
- [Taming Big Data with an Electronic Lab Notebook (ELN) - LabVantage](https://www.labvantage.com/blog/taming-big-data-with-an-electronic-lab-notebook-eln/)
- [Ten simple rules for implementing electronic lab notebooks (ELNs) - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11189195/)
- [How to use an open source LLM model locally and remotely](https://thoughtbot.com/blog/how-to-use-open-source-LLM-model-locally)
- [LLM experimentation through knowledge graphs - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1570826824000398)
- [OpenClaw is an open-source AI agent that runs your computer | Scientific American](https://www.scientificamerican.com/article/moltbot-is-an-open-source-ai-agent-that-runs-your-computer/)
- [Moltbot Is Taking Over Silicon Valley | WIRED](https://www.wired.com/story/clawdbot-moltbot-viral-ai-assistant/)
- [Bio-protocol (en.bio-protocol.org)](https://en.bio-protocol.org/en/about/)
- [Protocols.io: Virtual Communities for Protocol Development and Discussion - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4993360/)
