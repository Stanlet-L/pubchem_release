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
    # file routes
    # Case 1: Ux1 -> X
    #input_file = "4-hydroxyphenyl.csv"
    #output_file = "4-hydroxyphenyl_CHO.csv"
    # Case 1: Uy11 -> Y1 & Case 2: Ux1 -> X
    #input_file = "3,4-dihydroxyphenyl.csv"
    #output_file = "3,4-dihydroxyphenyl_CHO.csv"
    # Case 1: Uy22 -> Y2
    # input_file = "1,2-diol.csv"
    # output_file = "1,2-diol_CHO.csv"
    # Case 2: Uy1 -> Y1
    # input_file = "4-hydroxy-3-methoxyphenyl.csv"
    # output_file = "4-hydroxy-3-methoxyphenyl_CHO.csv"
    # Case 2: Uy2 -> Y2
    input_file = "3-hydroxy-4-methoxyphenyl.csv"
    output_file = "3-hydroxy-4-methoxyphenyl_CHO.csv"

    df = pd.read_csv(input_file)
    df_filtered = df[df["Molecular_Formula"].apply(is_CHO_only)]
    df_filtered.to_csv(output_file, index=False)

if __name__ == "__main__":
    main()
