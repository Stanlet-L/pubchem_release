# Chemical Data Mining Pipeline

A Python-based pipeline for processing PubChem-derived chemical compound datasets and identifying candidate molecules through formula filtering and comparison.

## Overview

This project processes compound records containing molecular formulas, IUPAC names, SMILES strings, molecular weights, and PubChem metadata.

The pipeline cleans raw compound data, keeps molecules containing only carbon, hydrogen, and oxygen, compares molecular formulas, and applies rule-based recovery logic to identify additional candidate compounds.

## Required Input Columns

Before running the scripts, make sure the input dataset contains the following columns:

```text
Compound_CID
Molecular_Weight
IUPAC_Name
Molecular_Formula
SMILES
Linked_PubChem_Literature_Count
Linked_PubChem_Patent_Count
```

Missing columns may result in incomplete outputs or runtime errors.

## Workflow & Usage

For general use, download the packaged GUI application from the Release section.

The Python scripts are included for transparency and workflow reference. If running the pipeline manually, execute the scripts in the following order:

```bash
python src/iupac_name_filter.py          # clean and keep required compound information
python src/filter_cho_compounds.py       # select molecules containing only C, H, and O
python src/formula_comparison.py         # compare molecular formulas
python src/rescue_candidates.py          # recover additional candidates using rule-based filtering
```

## Notes

This project focuses on data filtering, formula comparison, and candidate extraction.  
Further chemical interpretation should be validated separately by domain experts.
