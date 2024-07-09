import streamlit.web.cli as web
import click
import os
import re
import pandas as pd


@click.group(
    epilog="Check out readme at https://github.com/lewinkoon/databoard for more details."
)
def cli():
    """
    Deploy an interactive webapp to show data results from scientific experiments.
    """
    pass


@cli.command(help="Serve application.")
def run():
    web.main_run(["taviloc/run.py"])


@cli.command(help="Split multi-table csv file.")
@click.argument("file", required=True, type=click.Path(exists=True))
def split(file):
    with open(file, "r") as f:
        lines = f.readlines()

    tables = []
    buffer = []
    counter = 1
    delimiter = ","

    for idx, line in enumerate(lines):
        if "[Name]" in line:
            if buffer:
                df = pd.DataFrame([x.split(delimiter) for x in buffer])
                df.columns = header
                df.insert(1, "Location", location)
                df.insert(1, "Height", height)
                counter += 1
                buffer = []
                tables.append(df)

            name = lines[idx + 1].strip().split(delimiter)[0].split()
            location = name[0]
            height = name[3]
        elif "[Data]" in line:
            raw_header = lines[lines.index(line) + 1].strip()
            header = re.sub(r"\s*\[.*?\]\s*", "", raw_header).split(delimiter)
        elif line.strip().split(delimiter)[0].isdigit():
            buffer.append(line.strip())
        # elif any(char != delimiter for char in line.strip()):
        #     buffer.append(line.strip())

    if buffer:
        df = pd.DataFrame([x.split(delimiter) for x in buffer])
        df.columns = header
        df.insert(1, "Location", location)
        df.insert(1, "Height", height)
        tables.append(df)

    res = pd.concat(tables, ignore_index=True)
    res.to_csv("test.csv", index=False, header=True)
