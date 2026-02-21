# Idea Bank: LabOP

This chapter explains the **LabOP** protocol standard in depth and how it fits with the Pegasus ELN. It is a single reference for implementers and hackathon teams working on protocol interoperability and automation.

## What is LabOP?

**LabOP** is an ontology and schema for representing **laboratory protocols** in a machine-readable way. Goals include:

- **Reproducibility** — Protocols can be shared, versioned, and compared in a standard form.
- **Automation** — Protocol representations can drive or interface with lab automation (e.g. liquid handlers, sequencers) and execution pipelines.
- **Interoperability** — Tools and ELNs that speak LabOP can exchange protocol structure (steps, parameters, reagents, equipment) without proprietary formats.

LabOP is typically expressed in **JSON-LD** and is aligned with semantic-web and ontology practices so that protocols can be linked to samples, parameters, and equipment in a consistent way. The schema is referenced at **https://labop.org/schema**; implementers should check [labop.org](https://labop.org) for the latest schema and documentation.

## LabOP in the Pegasus standard

The Pegasus ELN XML standard embeds LabOP protocol content inside a `<protocol>` element. The protocol is stored **verbatim** as JSON-LD inside a `<labop>` child, with a schema reference. This keeps the ELN format tool-agnostic while allowing any LabOP-aware tool to parse the embedded protocol.

From [Chapter 2: Protocol Support (LabOP)](./chapter_2.md#8-protocol-support-labop):

```xml
<protocol id="urn:lab:protocol:ampicillin-test" title="Ampicillin MIC" version="1.0">
  <labop format="json-ld" schema="https://labop.org/schema">
    {
      "@type": "Protocol",
      "name": "Ampicillin MIC Test",
      "steps": [
        { "description": "Prepare bacterial culture" },
        { "description": "Add antibiotic gradient" }
      ]
    }
  </labop>
</protocol>
```

**What gets stored:**

- **Notebook-side:** A protocol container with an optional `id`, `title`, and `version`, plus the raw LabOP payload (format `json-ld`, schema URL).
- **Inside the payload:** Protocol name, steps (with descriptions and, in full LabOP, parameters, reagents, equipment), and any other fields the LabOP schema defines. The ELN does not mandate a specific LabOP version; the schema URL indicates which schema the payload conforms to.

This design supports: (1) human-readable protocol titles and versions in the ELN, (2) machine-readable protocol structure for automation and validation, and (3) future evolution of the LabOP schema without breaking the ELN container.

## Core concepts

Concepts that commonly appear in LabOP and map well to ELN entities:

- **Protocol** — A named, versioned procedure (e.g. "Ampicillin MIC Test"). In the ELN, this is the top-level experiment or method.
- **Steps** — Ordered actions (e.g. "Prepare bacterial culture", "Add antibiotic gradient"). Can carry parameters, timing, and references to reagents or equipment.
- **Parameters** — Inputs that can vary between runs (e.g. concentration, temperature, duration). Map to ELN metadata or structured fields.
- **Reagents / materials** — Substances used in the protocol. Can be linked to inventory or sample IDs in the ELN.
- **Equipment** — Instruments or devices. Can be linked to instrument metadata or calibration records.

Together, these support **experiment lineage**: which protocol was used, which samples and reagents, and which parameters—so that results can be traced back to a precise, machine-readable protocol. Execution or simulation of protocols (e.g. by lab robotics or simulation engines) is an extension of this ecosystem; the Pegasus standard focuses on storing and referencing the protocol, not on defining execution semantics.

## Hackathon idea bank

Project ideas that combine Pegasus and LabOP:

- **Validate ELN protocol entries against LabOP schema** — When a user adds or edits a `<labop>` block, validate the JSON-LD against the declared LabOP schema and report missing required fields or invalid structure.
- **Convert free-text protocols to LabOP JSON-LD** — Use a local LLM or rule-based parser to turn a free-text protocol (e.g. from a notebook section) into a draft LabOP structure that the user can review and store in the ELN.
- **Protocol diff** — Compare two protocol versions (e.g. two `<protocol>` elements or two LabOP JSON-LD blobs) and produce a human-readable or structured diff (steps added/removed/changed, parameters changed).
- **Integrate with automation/execution pipelines** — Build a bridge that reads LabOP from Pegasus (via API or export) and feeds it into an execution engine or scheduler (e.g. for liquid handling or sequencing runs), so that “run this protocol” is driven by the same representation stored in the ELN.
- **Auto-suggest protocol steps from past notebook entries** — Use past experiments and their protocol steps (either already in LabOP or extracted from text) to suggest the next step or a template protocol for a new experiment, using a local model and Pegasus data only.

These ideas assume protocols are (or can be) stored in the Pegasus format shown in [Chapter 2](./chapter_2.md); validation and conversion should respect the `schema` URL and the JSON-LD format.

## References and further reading

- **LabOP schema** — [https://labop.org/schema](https://labop.org/schema); check [labop.org](https://labop.org) for current documentation and schema versions.
- [Chapter 2: The ELN Open Standard](./chapter_2.md) — Section 8 (Protocol Support (LabOP)) and design philosophy.
- **Pegasus ELN standard** — Full ELN XML specification (e.g. `standard.md` in the repository) including the protocol container and LabOP embedding.

---

*© [Aegion Dynamic](https://aegiondynamic.com). See [Copyright and Legal Notice](./copyright.md) for full terms and repository information.*
