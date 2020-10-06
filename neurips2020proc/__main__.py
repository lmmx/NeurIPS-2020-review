from .src.parse_accepts import *# accepts_df

if __name__ == "__main__":
    accepted_paper_list = process_papers()
    print(f"Parsed ⠶ {accepted_paper_list}")
