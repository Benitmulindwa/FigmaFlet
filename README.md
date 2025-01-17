# FigmaFlet

FigmaFlet is a tool that generates Flet UI code directly from Figma designs. It streamlines the process of transforming your Figma prototypes into production-ready Python code using the Flet framework. 

## Features

- **Figma Integration**: Fetch designs directly from Figma using the file URL and API token.
- **Automatic Code Generation**: Generate Flet UI code from your designs with minimal manual effort.
- **Multi-line Text Handling**: Supports multi-line text elements seamlessly.
- **Graphical Interface**: Provides an intuitive GUI for entering API tokens, file URLs, and output paths.
- **Images**
- **Font-families**
- **Shadow**
- **LinearGradient**
- **TextFields**

## Installation

### From Source
1. Clone the repository:
```bash
git clone https://github.com/Benitmulindwa/figmaflet.git
cd figmaflet
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
### From PyPI

```
pip install figmaflet
```

## Usage

1. Launch the GUI to interactively input your API token, file URL, and output path:

```bash
python -m figmaflet.gui
```
![figmaflet_gui](https://github.com/user-attachments/assets/10ed6ffa-9deb-4e7d-94b2-11489d4ebf23)
### How It Works
- Input your API token, file URL and output path.
- FigmaFlet fetches the design data using Figma's API token.
- The tool processes the design elements and generates Flet-compatible Python code.
- The generated code is saved to your specified output path.

2. Command-Line Interface (CLI)
Once installed, use the CLI to generate Flet code:

```bash
figmaflet --apitoken YOUR_API_TOKEN --fileurl YOUR_FILE_URL --output YOUR_OUTPUT_PATH
```


Figma API Key
You will need your Figma API token to access design files. Generate your key by visiting your [Figma](https://figma.com) account settings.


File URL
Provide the Figma file URL containing your design; This is your figma project's URL.

## 🔥Examples:

![figmaOriginal](https://github.com/user-attachments/assets/054e5b07-aece-45ba-812b-4b6dceaaeb86)
##
![figmaflet0 0 4](https://github.com/user-attachments/assets/5fd92ffe-7c82-4f52-8dcd-85585a70d553)

## Upcoming Features
- **Icons**
- **Buttons** + **Events handling**(eg: on_hover)
- **Style Improvements**: better handling of **shadows**, **gradients** and other advanced figma styles
- **UI Responsivity**
- **Flexibiliy**: the generated code must be more flexible and easy to edit
- **Animations**


## Contributing
Contributions to FigmaFlet are highly welcomed! 

#### To contribute:

- **Fork the repository.**
- **Create a feature branch.**
- **Submit a pull request with a detailed explanation of your changes.**
## License
This project is licensed under the Apache-2.0 License. See the LICENSE file for details.

## Author
Benit Mulindwa - [GitHub](https://github.com/benitmulindwa)

### Acknowledgments
Special thanks to the tkinterdesigner and Figma communities for their support and inspiration.

### Contact
For questions, suggestions, or feedback, feel free to open an issue or reach out to mulindwabenit@gmail.com.

