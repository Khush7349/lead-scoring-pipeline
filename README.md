# Lead Scoring and Ranking Pipeline

This project implements a simple, reproducible **rule-based lead scoring pipeline** using Python and pandas.

The script reads a CSV file containing lead information, applies multiple scoring rules based on role, domain relevance, activity, funding, and location, and outputs a ranked list of leads with a final probability score.

The focus of this project is on **clear logic, transparency, and reproducibility**, not UI or automation at scale.

---

## Project Structure
```
lead_scoring_demo/
│
├── data/
│ └── raw_leads.csv # Input lead data
│
├── scoring/
│ └── lead_scoring.py # Scoring and ranking logic
│
├── output/
│ └── ranked_leads.csv # Ranked output with scores
│
└── README.md
```
---

## Input Data

The input file `raw_leads.csv` contains one row per lead with fields such as:

- Job title
- Company and company type
- Company headquarters location
- Domain or focus area
- Recent activity indicator
- Funding or budget status
- Contact information

Column names are normalized (trimmed and lowercased) at runtime to avoid formatting issues.

---

## Scoring Logic

Each lead is scored using independent, rule-based signals.

### 1. Role Score
Based on seniority inferred from the job title:
- Director / Head / VP → 30
- Associate Director / Principal Scientist → 20
- Senior Scientist → 10

### 2. Domain Relevance Score
Based on keyword matching in the focus/domain field:
- Drug-Induced Liver Injury → 40
- 3D, Organ-on-chip, Hepatic spheroids → 30
- Investigative Toxicology → 20
- General Toxicology → 10

### 3. Recent Activity Score
- Recent publication = Yes → 15
- Otherwise → 0

### 4. Funding / Company Type Score
- Big Pharma or Series B / Public → 20
- Series A → 10
- Grant-funded → 5

### 5. Location Score
Additional weight is given if the company HQ is located in a predefined hub:
- Cambridge, Boston, Bay Area, Basel, London, Oxford

---

## Final Score and Ranking

All individual scores are summed to produce a `probability_score`.

- The final score is capped at **100**
- Leads are sorted in descending order of score
- A `rank` column is assigned based on this ordering

The output includes both the individual signal scores and the final rank to keep the results **explainable and auditable**.

---

## Output

The final output is written to:

output/ranked_leads.csv

This file contains:
- Original lead attributes
- Individual score components
- Final probability score
- Rank

---

## How to Run

From the project root directory:

```bash
cd scoring
python lead_scoring.py
