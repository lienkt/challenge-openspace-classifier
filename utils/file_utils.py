from pathlib import Path
import csv
import pandas as pd
from utils.table import Table
from utils.colleague import Colleague

def parse_list(value):
    """
    Convert a string representation of a list into a Python list of integers.

    This function is used to transform Excel cell values like:
    "1,2,3" → [1, 2, 3]

    :param value: The input value from Excel (string, number, or NaN)
    :return: A list of integers
    """
    if pd.isna(value) or value == "":
        return []
    return [int(x) for x in str(value).split(",") if x.strip()]

def load_names(input_filepath):
    """
    Load colleagues data from an Excel file and convert it into Colleague objects.

    Each row in the Excel file represents one colleague with:
    ID | Name | Late | Wishlist | Blacklist

    :param input_filepath: Path to the input Excel file.
    :return: List of Colleague objects.
    :raises FileNotFoundError: If the file does not exist.
    :raises ValueError: If the file type is not supported.
    """
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
    
def store_file(tables: Table = [], filepath: str = "output.csv") -> None:
    """
    Export seating arrangement into a CSV file.

    The output format is:
    Table, Seat, Name

    :param tables: List of Table objects containing seated colleagues.
    :param filepath: Output file path (default: output.csv).
    """
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