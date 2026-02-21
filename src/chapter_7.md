# Idea Bank: BioProtocol and Decentralized Science

This chapter is a single reference for hackathon and contributor ideas around **open protocols**, **decentralized science (DeSci)**, and **reproducibility**. It ties these themes to the Pegasus ELN: exporting and importing protocols, persistent identifiers, and open-notebook science.

## Introduction

Protocol sharing and decentralized science matter for ELNs and reproducibility. When methods are findable, accessible, and reusable, other labs can replicate experiments and build on them. Open-notebook and DeSci approaches extend this idea: making data and protocols public (including failures), using persistent identifiers, and sometimes tokenizing or decentralizing research infrastructure. Pegasus’s open data format and local API make it a good fit for plugins that link notebook entries to community protocol libraries, publish protocols with persistent IDs, or sync select content to public repositories.

## Bio-protocol (the protocol repository)

**Bio-protocol** ([en.bio-protocol.org](https://en.bio-protocol.org)) is an online, peer-reviewed protocol journal that curates and hosts high-quality, free-access, step-by-step protocols across the life sciences. It was launched in 2011 by a group of Stanford postdoctoral researchers to address a core problem: the methods sections of research articles are often brief and incomplete, making it difficult to replicate experiments without extensive troubleshooting.

### What Bio-protocol provides

- **Peer-reviewed protocols** in categories such as molecular biology, cell biology, systems biology, microbiology, immunology, neuroscience, plant science, cancer biology, and others.
- **Preprint repository and Exchange** — for sharing and discussing protocols before or alongside formal publication.
- **Webinars** — for discussing methods and technologies.
- **Editorial model** — editorial and review boards are largely made up of postdocs, early-career faculty, and staff scientists who actively design and conduct experiments, which helps keep protocols practical and clear.

Bio-protocol’s vision is to improve reproducibility by sharing detailed methods and fostering direct communication among researchers. The organization aims not only to be a database of reliable protocols but also a community platform for sharing ideas and promoting good research practices.

### Integrating with Pegasus

- **Query published protocols** — By protocol name or category, a Pegasus plugin could retrieve matching Bio-protocol (or protocols.io) entries and suggest them when a user is drafting a method in the ELN.
- **Compare lab procedures to standards** — Check whether a lab’s written procedure aligns with a published standard (e.g. same key steps, reagents) and flag gaps or deviations.
- **Export for submission or sharing** — Allow users to export a protocol from Pegasus in a form suitable for submission to Bio-protocol, or for sharing via protocols.io or other open databases, so the global “distributed science” community can reuse and cite it.

## Decentralized science (DeSci) and open-notebook science

### Open-notebook science

**Open-notebook science** is the practice of making research data and methods public in real time, including failed experiments and raw notes. Benefits include earlier feedback, stronger provenance, and a shared record that others can build on. ELNs are a natural place to implement open-notebook practices: select notebook entries or protocols can be synced to public repositories or wikis, with clear licensing and persistent identifiers.

### Blockchain and tokenized research (DeSci)

**Decentralized science (DeSci)** uses blockchain and related technologies to fund, share, and sometimes tokenize research. **Bio Protocol (BIO)** is one example of a blockchain-based DeSci platform where research can be shared and tokenized (as referenced in [Chapter 1](./chapter_1.md)). It is **distinct from** the Bio-protocol journal/repository above: the former is a DeSci/token platform; the latter is a peer-reviewed protocol journal and community site.

For hackathon ideas, “publishing” parts of a lab notebook onto a decentralized network could mean: saving a protocol or dataset with a persistent identifier (e.g. DOI, or a blockchain-anchored ID), or designing a bridge between Pegasus and a DeSci platform so that selected ELN content can be registered or shared there. The exact design depends on which DeSci platform and standards you target.

## Hackathon idea bank

Concrete project ideas that combine Pegasus with open protocols and DeSci/open science:

- **Sync select ELN entries to a public repo or wiki** — Let users choose which experiments or protocols to publish; export to a public repository or wiki with metadata and (where applicable) persistent IDs; enable community feedback or versioning.
- **Publish protocols with persistent identifiers** — From a Pegasus protocol entry, generate a minimal, citable package (e.g. RO-Crate or similar) and register it to get a DOI or other persistent ID so others can cite and reuse it.
- **Link notebook entries to Bio-protocol or protocols.io** — When writing a protocol in Pegasus, search Bio-protocol or protocols.io by name or key step; embed a link or citation to the published protocol; optionally check alignment with that standard.
- **Reproducibility report** — A tool that checks protocol completeness against community standards (e.g. required fields, materials, step clarity) and produces a short “reproducibility readiness” report for an experiment or protocol.
- **Contribute Pegasus protocols to open databases** — A one-click or guided flow to export a protocol from Pegasus in a format suitable for submission to Bio-protocol, protocols.io, or another open database, with proper attribution and licensing.

These ideas keep data sovereignty in mind: optional publishing and clear user control over what is shared and where.

## References and further reading

- [Bio-protocol: About Us](https://en.bio-protocol.org/en/about) — Aims, scope, editorial model, and community.
- [Protocols.io: Virtual Communities for Protocol Development and Discussion - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4993360/)
- [Open-notebook science - Wikipedia](https://en.wikipedia.org/wiki/Open-notebook_science)
- [Bio Protocol (BIO) – Help Centre](https://help.wealthsimple.com/hc/en-ca/articles/41701045785883-Bio-Protocol-BIO) — DeSci/token platform (distinct from Bio-protocol journal).
- [Chapter 1: Open/Distributed Science](./chapter_1.md) — Related hackathon ideas in this book.

---

*© Aegion Dynamic. See [Copyright and Legal Notice](./copyright.md) for full terms and repository information.*
