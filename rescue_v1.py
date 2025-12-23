import pandas as pd
import re
from collections import defaultdict

def filter_smile_CO_only(smile):
    return ''.join(re.findall(r'[CO]', str(smile)))

def is_match_by_removing_one_O(x_filtered, y_filtered):
    if len(y_filtered) != len(x_filtered) + 1:
        return False
    for i, c in enumerate(y_filtered):
        if c == 'O':
            candidate = y_filtered[:i] + y_filtered[i+1:]
            if candidate == x_filtered:
                return True
    return False

def main():
    x_file = "2_W1.csv"     
    y_file = "2_Y.csv"         

    out_match = "2_WW1.csv"
    out_unmatch = "2_Z1.csv"
    out_y_filtered = "Y12_filtered_with_CO.csv"

    df_x = pd.read_csv(x_file)
    df_y = pd.read_csv(y_file)

    df_y["Filtered_SMILES_Y"] = df_y["SMILES"].apply(filter_smile_CO_only)
    df_y.to_csv(out_y_filtered, index=False)

    y_map = defaultdict(list)
    for _, row in df_y.iterrows():
        mf = row["Molecular_Formula"]
        if pd.notna(mf):
            y_map[mf].append(row)

    matched_rows = []
    unmatched_rows = []


    for _, row in df_x.iterrows():
        modified_formula = row["Modified_Formula"]
        x_smile = row["SMILES"]

        if pd.isna(modified_formula) or pd.isna(x_smile):
            continue

        x_filtered = filter_smile_CO_only(x_smile)
        matched_cids = []

        for y_row in y_map.get(modified_formula, []):
            y_filtered = y_row["Filtered_SMILES_Y"]
            if is_match_by_removing_one_O(x_filtered, y_filtered):
                matched_cids.append(str(y_row["Compound_CID"]))

        new_row = row.copy()
        new_row["Filtered_SMILES_X"] = x_filtered
        new_row["Matched_Y_SMILES_Count"] = len(matched_cids)
        new_row["Matched_Y_CIDs"] = ";".join(matched_cids)

        if matched_cids:
            matched_rows.append(new_row)
        else:
            unmatched_rows.append(new_row)

    pd.DataFrame(matched_rows).to_csv(out_match, index=False)
    pd.DataFrame(unmatched_rows).to_csv(out_unmatch, index=False)

    print(f"{len(matched_rows)} → {out_match}")
    print(f"{len(unmatched_rows)} → {out_unmatch}")

if __name__ == "__main__":
    main()
