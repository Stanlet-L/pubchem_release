import pandas as pd
import re

# Ensure formula only contains CHO and no invalid symbols
def is_CHO_only(formula):
    if pd.isna(formula):
        return False

    if re.search(r'[^CHO0-9]', formula):
        return False

    elements = re.findall(r'([A-Z][a-z]?)', formula)
    return all(elem in {"C", "H", "O"} for elem in elements)

def main():
    input_file = "3-hydroxy-4-methoxyphenyl.csv"
    output_file = "3-hydroxy-4-methoxyphenyl_CHO.csv"

    df = pd.read_csv(input_file)

    df_filtered = df[df["Molecular_Formula"].apply(is_CHO_only)]

    print(f"Output as: {output_file}")
    df_filtered.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
