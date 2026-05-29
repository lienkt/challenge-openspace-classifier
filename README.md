# OpenSpace Organizer

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 🏢 Description

Your company moved to a new office at CEVI Ghent. Its an openspace with 6 tables of 4 seats. As many of you are new colleagues, you come up with the idea of changing seats everyday and get to know each other better by working side by side with your new colleagues.

This script runs everyday to re-assign everybody to a new seat.

![coworking_img](https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NDd8fGRpdmVyc2UlMjB0ZWFtfGVufDB8fDB8fHwy)

OpenSpace Organizer is a Python application that automatically assigns colleagues to seats in an open office space.

The system:

- Reads colleagues from an **Excel file**
- Stores people as structured objects (`Colleague`)
- Randomly assigns them to tables (`Table`)
- Displays seating arrangements in the terminal
- Saves results to a CSV file
- Provides a CLI menu to inspect the workspace

This project simulates a dynamic office where seating changes regularly to encourage collaboration.

## Features

- 📥 Load colleagues from Excel (`.xlsx`)
- 🧾 Parse structured data:
  - ID
  - Name
  - Late status
  - Wishlist (preferred colleagues)
  - Blacklist (avoid seating)
- 🪑 Automatic seat assignment
- 🏢 Configurable number of tables & capacity (`config.json`)
- 📊 Seating visualization in terminal
- 💾 Export results to CSV
- 🧭 Interactive CLI menu

## 📦 Repo structure

```
.
├── utils/
│   ├── openspace.py
│   ├── table.py
│   └── file_utils.py
│   └── colleague.py
├── config.json
├── .gitignore
├── main.py
├── new_colleagues.csv
├── new_colleagues.xlsx
├── output.csv
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.

   The system uses a `config.json` file for user to edit the information of the office:

   ```json
   {
     "NUMBER_OF_TABLES": 6,
     "TABLE_CAPACITY": 4
   }
   ```

2 .To run the script, you can execute the `main.py` file from your command line:

```
   python main.py
```

3. The script reads your input file, and organizes your colleagues to random seat assignments. The resulting seating plan is displayed in your console and also saved to an "output.csv" file in your root directory.

```python
def main():
    input_filepath = "new_colleagues.xlsx"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = utils.read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = OpenSpace()

    # assign a colleague randomly to a table
    open_space.organize(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display()

if __name__ == "__main__":
    main()
```

---

## ⏱️ Timeline

This project took two days for completion.

## 📌 Personal Situation

This project was done as part of the AI Boocamp at BeCode.org.

Connect with me on [LinkedIn](https://www.linkedin.com/in/vriveraq/).
