import re
import argparse
from pathlib import Path
from figmaflet.generateUI import UI


def extract_file_key(url):
    match = re.search(r"/design/([a-zA-Z0-9]+)", url)
    if match:
        return match.group(1)
    return None


def main():
    parser = argparse.ArgumentParser(description="Generate Flet UI from Figma designs.")
    parser.add_argument("--apikey", required=True, help="Your Figma API key.")
    parser.add_argument("--fileurl", required=True, help="The URL of the Figma file.")
    parser.add_argument(
        "--output", required=True, help="Output file for the generated UI code."
    )

    args = parser.parse_args()

    ui = UI(
        token=args.apikey,
        file_key=extract_file_key(args.fileurl),
        local_path=Path(args.output),
    )
    ui.generate()

    print(f"UI code has been successfully generated and saved to {args.output}.")


if __name__ == "__main__":
    main()
