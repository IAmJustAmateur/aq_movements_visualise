# Movements Map Visualizer

An interactive Python application that reads your GPS movement data from a CSV file and displays it on a map with animated paths, hover tooltips, and click popups showing exact timestamps.

## Features

* **Animated Route**: Uses Folium’s `AntPath` to animate your movement path.
* **Datetime Popups & Tooltips**: Hover over or click any point to see the precise `YYYY-MM-DD HH:MM:SS` timestamp.
* **Customizable**: Easily switch to a static polyline, adjust zoom levels, marker styles, and more.

## Requirements

* Python 3.6 or newer
* [pandas](https://pandas.pydata.org/)
* [folium](https://python-visualization.github.io/folium/)

## Installation

1. Clone this repository:

   ```bash
   git git@github.com:IAmJustAmateur/aq_movements_visualise.git
   cd <your-repo-folder>
   ``` 
2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # on Linux/macOS
   venv\Scripts\activate     # on Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

## Usage

1. Prepare your CSV file (`movements.csv`) with columns:

   ```csv
   timestamp,latitude,longitude
   2025-05-09T08:15:00,54.6872,25.2797
   2025-05-09T08:45:00,54.6890,25.2830
   ```
2. Run the script:

   ```bash
   python plot_movements_with_time.py movements.csv --out my_map.html
   ```
3. Open the generated `my_map.html` in your browser.

## Customization

* **Zoom Level**: Modify the `start_zoom` parameter in `create_map()`.
* **Path Style**: Replace `AntPath` with `folium.PolyLine` for a static path:

  ```python
  folium.PolyLine(coords, color='blue', weight=3).add_to(m)
  ```
* **Marker Styles**: Swap `CircleMarker` for `Marker`, change colors, add clustering, etc.

## .gitignore

This project’s `.gitignore` excludes generated HTML maps and common Python artifacts:

```gitignore
*.html
__pycache__/
*.py[cod]
venv/
.env/
.vscode/
.idea/
```

## License

This project is released under the MIT License. Feel free to use, modify, and distribute.
