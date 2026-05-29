from pathlib import Path
import csv
import pandas as pd
from utils.table import Table
from utils.colleague import Colleague
import pandas as pd

def parse_list(value):
    if pd.isna(value) or value == "":
        return []
    return [int(x) for x in str(value).split(",") if x.strip()]

def load_names(input_filepath):
    path = Path(input_filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {input_filepath}")

    # # -------- CSV --------
    # if path.suffix == ".csv":
    #     new_colleagues = []
    #     with open(path, "r", encoding="utf-8") as f:
    #         reader = csv.reader(f)
    #         for row in reader:
    #             if row:
    #                 new_colleagues.append(row[0])
    #     return new_colleagues

    # -------- Excel --------
    elif path.suffix in [".xlsx", ".xls"]:
        df = pd.read_excel(path)
        new_colleagues = []
        for _, row in df.iterrows():
            new_colleagues.append(
                Colleague(
                    id=int(row["ID"]),
                    name=row["Name"],
                    late=bool(row["Late"]),
                    wishlist=parse_list(row["Wishlist"]),
                    blacklist=parse_list(row["Blacklist"])
                )
            )

        return new_colleagues
    
    else:
        raise ValueError("Unsupported file type. Use CSV or Excel.")
    
def store_file(tables: Table = [], filepath: str = "output.csv"):
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # header
        writer.writerow(["Table", "Seat", "Name"])
        # content
        for table_index, table in enumerate(tables):
          for seat_index, seat in enumerate(table.seats):
              writer.writerow([
                table_index + 1,
                seat_index + 1,
                seat.occupant,
              ])