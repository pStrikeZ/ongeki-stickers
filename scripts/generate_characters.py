import os
import json

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'public', 'img')
OUTPUT_FILE = os.path.join(BASE_DIR, 'src', 'characters.json')

# Default text configuration
DEFAULT_TEXT_CONFIG = {
    "text": "请输入文本",
    "x": 148,
    "y": 200,
    "r": 0,
    "s": 40
}

# Default color (Black)
DEFAULT_COLOR = "#000000"

# Color map for specific characters
# Format: "character_folder_name": "#HEXCOLOR"
COLOR_MAP = {
    "akari": "#ffd0d4",
    "yuzu": "#fef7c3",
    "aoi": "#868397",
    "rio": "#a69fc3",
    "riku": "#6e6061",
    "tsubaki": "#798288",
    "haruna": "#857674",
    "ayaka": "#d3ad99",
    "saki": "#e2e4e4",
    "koboshi": "#8b96a6",
    "akane": "#e2686c",
    "kaede": "#7d7e80",
    "arisu": "#99b9d3",
    "chinatsu": "#d49486",
    "mia": "#d7d6d6",
    "tsumugi": "#7e5b5f",
    "setsuna": "#ecebeb"
}

def generate_characters():
    characters = []
    id_counter = 1

    if not os.path.exists(IMG_DIR):
        print(f"Error: Directory {IMG_DIR} does not exist.")
        return

    # Walk through the directory according to COLOR_MAP order
    # Only process characters defined in COLOR_MAP
    for char_name in COLOR_MAP.keys():
        char_dir = os.path.join(IMG_DIR, char_name)
        
        # Check if the character directory exists
        if not os.path.exists(char_dir) or not os.path.isdir(char_dir):
            # Skip if directory doesn't exist (user might not have created it yet)
            continue
            
        # Determine color for this character
        # Use mapped color if available, otherwise default
        current_color = COLOR_MAP.get(char_name, DEFAULT_COLOR)

        # List files in the character directory
        for filename in os.listdir(char_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Generate a readable name from filename (e.g., "Char_01.png" -> "Char 01")
                name = os.path.splitext(filename)[0].replace('_', ' ')
                
                # Relative path for the image
                img_path = f"{char_name}/{filename}"
                
                character_entry = {
                    "id": str(id_counter),
                    "name": name,
                    "character": char_name,
                    "img": img_path,
                    "color": current_color,
                    "defaultText": DEFAULT_TEXT_CONFIG.copy()
                }
                
                characters.append(character_entry)
                id_counter += 1

    # Write to JSON file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(characters, f, indent=4, ensure_ascii=False)
        print(f"Successfully generated characters.json with {len(characters)} entries.")
    except Exception as e:
        print(f"An error occurred while writing to {OUTPUT_FILE}: {e}")

if __name__ == "__main__":
    generate_characters()
