from .src.parse_accepts import *# accepts_df

def main():
    accepts_df = process_papers()
    print(accepts_df) 

if __name__ == "__main__":
    main()
