from ...data import data_dir

def write_df_to_tsv(df, fname="accepted_paper_listings", dest_dir=data_dir):
    output_tsv = dest_dir / f"{fname}.tsv"
    with open(output_tsv, "w") as f:
        f.write(df.to_csv(sep="\t"))
