# Usage

For general use, please download the packaged GUI application from the Release section. The GUI version provides a ready-to-use interface and does not require manually running each script.

Due to updates in PubChem file naming conventions, users are advised to verify that the downloaded file contains the following required columns prior to use:

	•	Compound_CID
	•	Molecular_Weight
	•	IUPAC_Name
	•	Molecular_Formula
	•	SMILES
	•	Linked_PubChem_Literature_Count
	•	Linked_PubChem_Patent_Count

Failure to include these fields may result in unexpected behavior or incomplete analysis.

The Python scripts in this repository are provided separately for transparency, maintenance, and workflow reference. If running the scripts manually, please execute them in the following order:

	1. IUPAC_Name_Filter.py
    	Cleans the downloaded dataset and keeps only the required columns.
	2. CHO_selected.py
    	Filters the dataset to keep molecules containing only C, H, and O.
	3. Formula_Comparesion.py
    	Modifies and compares molecular formulas to identify potential new molecules.
	4. rescue_v1.py
    	Applies rule-based recovery to rescue potential candidates from the discarded data.

These scripts automate the data filtering and comparison steps. Further chemical interpretation should be validated separately.
