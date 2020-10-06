from .src.parse_accepts import parse_listings # accepts_df
from .src.util.paging import dfpager

if __name__ == "__main__":
    accepted_paper_list = parse_listings()
    print(f"Parsed ⠶ {accepted_paper_list}")
