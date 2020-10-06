from .src.parse_accepts import parse_listings
from .src.util.paging import dfpager
from .src.util.tsv_writer import write_df_to_tsv

OVERWRITE_TSV = False

if __name__ == "__main__":
    accepted_paper_list = parse_listings()
    print(f"Parsed ⠶ {accepted_paper_list}")
    if OVERWRITE_TSV:
        write_df_to_tsv(accepted_paper_list.as_df())
