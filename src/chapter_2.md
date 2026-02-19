# The ELN Open Standard

This chapter describes the XML-based Electronic Lab Notebook (ELN) standard that underpins Pegasus and compatible tools. It provides structured scientific documentation, addressable data, protocol interoperability, and semantic extensibility while remaining machine-readable, AI-compatible, and tool-agnostic. A dedicated [Pegasus API](./chapter_5.md) chapter (TBA) will document the local API and endpoints for reading and writing this data.

---

## 1. Overview

This ELN XML standard is designed to provide:

- Structured scientific documentation
- Rich text + Markdown + LaTeX support
- Addressable tabular data
- Protocol embedding via LabOP
- Knowledge graph construction
- Deep linking & cross-notebook references
- Embeddable web content
- Workflow triggers
- Audit and compliance support

All resources are addressable using **URI or URN identifiers**.

---

## 2. Root Structure

```xml
<notebook id="urn:lab:notebook:assay-2026-01">
  <metadata>...</metadata>
  <layout>...</layout>
  <content>...</content>
  <interfaces>...</interfaces>
  <knowledge>...</knowledge>
</notebook>
```

---

## 3. Metadata Section

Stores high-level notebook information.

```xml
<metadata>
  <title>Antibiotic Susceptibility Assay</title>
  <created>2026-02-01T09:30:00Z</created>
  <author>Dr. A. Raman</author>
  <tags>microbiology,assay,phase1</tags>
</metadata>
```

### Supported Concepts

- Versioning (optional extension)
- Access classification
- Audit metadata

---

## 4. Layout Section

Separates layout concerns from content.

```xml
<layout>
  <position container="urn:lab:container:intro" x="0" y="0" width="12" height="4"/>
  <position container="urn:lab:container:data" x="0" y="5" width="12" height="8"/>
</layout>
```

This enables:

- Grid-based rendering
- PDF export formatting
- Dashboard-style layouts

---

## 5. Content Section

The heart of the notebook.

```xml
<content>
  <container id="urn:lab:container:intro" type="text">
    <element format="markdown"><![CDATA[
# Objective

Test bacterial resistance to **Ampicillin**.

Formula used:

$$
OD_{corrected} = OD_{sample} - OD_{blank}
$$
    ]]></element>
  </container>
</content>
```

### 5.1 Text Formats

Supported via:

```xml
<element format="plain|markdown|latex|html|code">
```

Example (LaTeX):

```xml
<element format="latex">
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
</element>
```

---

## 6. Addressable Tables

Tables support row-level primary keys.

```xml
<container id="urn:lab:container:results" type="table">
  <table id="urn:lab:table:assay-results" label="Assay Data">
    <header>
      <cell>Sample</cell>
      <cell>OD600</cell>
      <cell>Replicate</cell>
    </header>
    <row id="urn:lab:row:sample-001">
      <cell>Sample-001</cell>
      <cell>0.87</cell>
      <cell>1</cell>
    </row>
    <row id="urn:lab:row:sample-002">
      <cell>Sample-002</cell>
      <cell>0.91</cell>
      <cell>1</cell>
    </row>
  </table>
</container>
```

### Linking to a Specific Row

```xml
<link
  type="internal"
  target="urn:lab:table:assay-results"
  fragment="urn:lab:row:sample-001"
  label="Sample 001 Data"/>
```

---

## 7. Embeddable Content

Supports iframe-like rendering.

```xml
<embed
  type="iframe"
  src="https://plotly.com/~lab/123"
  width="800"
  height="600"
  sandbox="allow-scripts allow-same-origin"
  allowfullscreen="true"/>
```

Use cases:

- Interactive plots
- Remote dashboards
- Computational notebooks

---

## 8. Protocol Support (LabOP)

Protocols are embedded verbatim.

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

---

## 9. Measurements & Instrument Data

```xml
<measurement
  id="urn:lab:measurement:od600-001"
  parameterRef="urn:lab:param:od600"
  value="0.87"
  unit="OD"/>

<spectrum
  id="urn:lab:spectrum:uvvis-001"
  type="UV-Vis"
  dataRef="urn:lab:file:uvvis-data.csv"/>
```

---

## 10. Action Triggers

Used to launch external scripts or automation.

```xml
<action
  id="urn:lab:action:export"
  label="Export Results"
  trigger="manual"
  method="POST"
  uri="https://lab-system/export"
  format="application/json"/>
```

Permissions are managed externally by the calling tool.

---

## 11. Interfaces Section

For cross-document linking.

```xml
<interfaces>
  <link
    type="external"
    target="urn:lab:notebook:previous-study"
    label="Previous Study"/>
</interfaces>
```

Supports:

- Cross-notebook linking
- LIMS references
- DOI references

---

## 12. Knowledge Graph

Enables structured scientific reasoning.

```xml
<knowledge>
  <triple
    subject="urn:lab:row:sample-001"
    predicate="urn:ontology:hasResistance"
    object="urn:lab:compound:ampicillin"/>
</knowledge>
```

Enables:

- Semantic queries
- Automated reasoning
- AI-assisted analysis

---

## 13. Audit & Compliance

```xml
<auditTrail
  id="urn:lab:audit:entry-1"
  user="dr.raman"
  action="edit"
  timestamp="2026-02-01T10:00:00Z"/>

<signature
  id="urn:lab:signature:approval"
  signerRef="urn:user:dr.raman"
  role="PI"
  reason="Final Approval"/>
```

Supports:

- 21 CFR Part 11 compliance
- Traceability
- Regulatory review

---

## 14. URI/URN Design Rules

Recommended pattern:

```
urn:lab:{type}:{identifier}
```

Examples:

```
urn:lab:notebook:assay-2026-01
urn:lab:container:results
urn:lab:table:assay-results
urn:lab:row:sample-001
urn:lab:measurement:od600-001
```

Benefits:

- Globally unique
- Deep-linkable
- Semantic-friendly

---

## 15. Design Philosophy

| Principle                       | Implementation             |
| ------------------------------- | -------------------------- |
| Separation of layout & content  | `<layout>` vs `<content>`  |
| Semantic addressability         | URI/URN-based IDs          |
| Extensibility                   | Choice-based schema        |
| AI readiness                    | RDF-style triples          |
| Protocol standardization       | LabOP embedding            |
| Web-native                      | iframe embedding           |
| Tool-agnostic security         | Auth externalized          |

---

## 16. Complete Minimal Example

```xml
<notebook id="urn:lab:notebook:demo">
  <metadata>
    <title>Demo Notebook</title>
    <created>2026-02-19T12:00:00Z</created>
    <author>Dr. X</author>
  </metadata>

  <layout>
    <position container="urn:lab:container:main" x="0" y="0" width="12" height="6"/>
  </layout>

  <content>
    <container id="urn:lab:container:main">
      <element format="markdown">
        <![CDATA[
## Demo Entry
This notebook supports Markdown and LaTeX:

$$E = mc^2$$
        ]]>
      </element>
    </container>
  </content>

  <interfaces/>
  <knowledge/>
</notebook>
```

---

## Conclusion

This ELN XML standard provides:

- Structured scientific documentation
- Addressable data primitives
- Protocol interoperability
- Semantic extensibility
- Automation hooks
- Web-native rendering
- Regulatory readiness

It is designed to be:

- Machine-readable
- AI-compatible
- Long-term archival safe
- Tool-agnostic

Possible next steps for the ecosystem include a JSON representation of the standard, a validation checklist for implementers, a compliance mapping (e.g., FDA / ISO), and a versioned governance model for evolving the standard.
