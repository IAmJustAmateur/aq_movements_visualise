#!/usr/bin/env python3
"""
Visualize GPS movements from a CSV on an interactive map using Folium.

CSV format:
timestamp,latitude,longitude
2025-05-09T08:15:00,54.6872,25.2797
2025-05-09T08:45:00,54.6890,25.2830
...
"""

import pandas as pd
import folium
from folium.plugins import AntPath


def load_data(csv_path):
    # Read CSV; parse timestamps if you need them later
    df = pd.read_csv(csv_path, parse_dates=["timestamp"])
    # Ensure required columns exist
    required = {"latitude", "longitude"}
    if not required.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required}")
    return df


def create_map(df, start_zoom=13):
    # Calculate center of map
    avg_lat = df["latitude"].mean()
    avg_lon = df["longitude"].mean()

    # Initialize map
    m = folium.Map(location=[avg_lat, avg_lon], zoom_start=start_zoom)

    # Draw a time-animated line (AntPath) for nice effect
    coords = df[["latitude", "longitude"]].values.tolist()
    AntPath(
        locations=coords,
        dash_array=[10, 20],
        delay=1000,
        color="blue",
        pulse_color="red",
    ).add_to(m)

    # Add a marker for each point (optional; you can comment this out)
    for idx, row in df.iterrows():
        folium.CircleMarker(
            location=(row["latitude"], row["longitude"]),
            radius=4,
            popup=str(row["timestamp"]),
            color="black",
            fill=True,
            fill_opacity=0.7,
        ).add_to(m)

    return m


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Plot GPS path from CSV on a map.")
    parser.add_argument("csv", help="Path to your movements CSV file")
    parser.add_argument(
        "--out", default="map.html", help="Output HTML file (default: map.html)"
    )
    args = parser.parse_args()

    df = load_data(args.csv)
    map_obj = create_map(df)
    map_obj.save(args.out)
    print(f"Map has been saved to {args.out}. Open it in your browser to view it.")


if __name__ == "__main__":
    main()
