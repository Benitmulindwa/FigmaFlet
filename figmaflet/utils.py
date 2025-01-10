import io
import requests
from PIL import Image


def get_fonts_urls(font_family):
    # Format the font-family name for URL
    font_family_name = font_family.split()
    # print(font_family_url)
    google_fonts_url = f"https://fonts.googleapis.com/css2?family={font_family_name[0]}"
    # print(google_fonts_url)
    # Fetch the font CSS
    response = requests.get(google_fonts_url)
    if response.status_code == 200:
        css_content = response.text

        # # Extract font file URLs from the CSS and download them
        font_urls = [
            line.split("url(")[-1].split(")")[0].strip('"')
            for line in css_content.splitlines()
            if "url(" in line
        ]
        page_settings = f"{font_family}:{font_urls[0]}"
        return page_settings

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
