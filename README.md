# FigmaFlet

FigmaFlet is a tool that generates Flet UI code directly from Figma designs. It streamlines the process of transforming your Figma prototypes into production-ready Python code using the Flet framework. 

## Features

- **Figma Integration**: Fetch designs directly from Figma using the file URL and API key.
- **Automatic Code Generation**: Generate Flet UI code from your designs with minimal manual effort.
- **Multi-line Text Handling**: Supports multi-line text elements seamlessly.
- **Graphical Interface**: Provides an intuitive GUI for entering API keys, file URLs, and output paths.

## Installation

### From Source
1. Clone the repository:
   ```bash
   git clone https://github.com/Benitmulindwa/figmaflet.git
   cd figmaflet
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
### From PyPI

```
pip install figmaflet
```

## Usage

1. Launch the GUI to interactively input your API key, file URL, and output path:

```bash
python -m figmaflet.gui
```
![figmaflet_gui](https://github.com/user-attachments/assets/1e6a79bd-3bae-4378-acc2-9c8664a1fd1f)
### How It Works
- Input your API key, file URL and output path.
- FigmaFlet fetches the design data using Figma's API.
- The tool processes the design elements and generates Flet-compatible Python code.
- The generated code is saved to your specified output path.

2. Command-Line Interface (CLI)
Once installed, use the CLI to generate Flet code:

```bash
python -m figmaflet --apikey YOUR_API_KEY --fileurl YOUR_FILE_URL --output YOUR_OUTPUT_PATH
```


Figma API Key
You will need your Figma API key to access design files. Generate your key by visiting your [Figma](https://figma.com) account settings.


File URL
Provide the Figma file URL containing your design.

## Results:
### Figma design
![figmaOriginal](https://github.com/user-attachments/assets/054e5b07-aece-45ba-812b-4b6dceaaeb86)

### Figmaflet output
![figmaflet_5th_try](https://github.com/user-attachments/assets/15727ba1-b619-4e5f-a4be-f410231f9658)
## Upcoming Features
- **Images** and **Icons**
- **TextFields**
- **Buttons** + **Events handling**(eg: on_hover)
- **Fonts support**
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
Benit Mulindwa - GitHub

### Acknowledgments
Special thanks to the tkinterdesigner and Figma communities for their support and inspiration.

### Contact
For questions, suggestions, or feedback, feel free to open an issue or reach out to mulindwabenit@gmail.com.

