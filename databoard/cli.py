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
    web.main_run(["databoard/run.py"])


@cli.command(help="Split multi-table csv file.")
@click.argument("file", required=True, type=click.Path(exists=True))
def split(file):
    with open(file, "r") as f:
        lines = f.readlines()

    datatable = {}
    buffer = []
    counter = 1
    name = ""
    delimiter = ";"

    for line in lines:
        if "[Name]" in line:
            if buffer:
                df = pd.DataFrame([x.split(delimiter) for x in buffer])
                output = f"{counter}.csv"
                df.to_csv(output, index=False, header=False)
                counter += 1
                buffer = []

            name = lines[lines.index(line) + 1].strip().split(delimiter)[0]
        elif "[Data]" in line:
            raw_header = lines[lines.index(line) + 1].strip().split(delimiter)[0]
            header = re.sub(r"\s*\[.*?\]\s*", "", raw_header)
        elif any(char != delimiter for char in line.strip()):
            buffer.append(line.strip())

    if buffer:
        df = pd.DataFrame([x.split(delimiter) for x in buffer])
        output = f"{counter}.csv"
        df.to_csv(output, index=False, header=False)
