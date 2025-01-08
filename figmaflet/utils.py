import io
import requests
from PIL import Image


def download_font(font_family, output_path):
    # Format the font-family name for URL
    font_family_url = font_family.replace(" ", "+")
    google_fonts_url = (
        f"https://fonts.googleapis.com/css2?family={font_family_url}&display=swap"
    )

    # Fetch the font CSS
    response = requests.get(google_fonts_url)
    if response.status_code == 200:
        css_content = response.text

        # Save the CSS file
        css_path = output_path / f"{font_family}.css"
        with open(css_path, "w") as css_file:
            css_file.write(css_content)

        # Extract font file URLs from the CSS and download them
        font_urls = [
            line.split("url(")[-1].split(")")[0].strip('"')
            for line in css_content.splitlines()
            if "url(" in line
        ]

        for font_url in font_urls:
            font_response = requests.get(font_url)
            if font_response.status_code == 200:
                font_file_name = font_url.split("/")[-1]
                font_file_path = output_path / font_file_name
                with open(font_file_path, "wb") as font_file:
                    font_file.write(font_response.content)
                print(f"Downloaded {font_file_name} to {font_file_path}")
    else:
        print(
            f"Failed to fetch font CSS for {font_family}. Status code: {response.status_code}"
        )


def download_image(url, image_path):
    response = requests.get(url)
    content = io.BytesIO(response.content)
    im = Image.open(content)
    im = im.resize((im.size[0] // 2, im.size[1] // 2), Image.LANCZOS)
    with open(image_path, "wb") as file:
        im.save(file)
