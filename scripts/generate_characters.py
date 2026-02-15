import os
import json

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, 'public', 'img')
OUTPUT_FILE = os.path.join(BASE_DIR, 'src', 'characters.json')

# Default text configuration
DEFAULT_TEXT_CONFIG = {
    "text": "Enter text...",
    "x": 148,
    "y": 200,
    "r": 0,
    "s": 40
}

# Default color (Black)
DEFAULT_COLOR = "#000000"

def generate_characters():
    characters = []
    id_counter = 1

    if not os.path.exists(IMG_DIR):
        print(f"Error: Directory {IMG_DIR} does not exist.")
        return

    # Walk through the directory
    for root, dirs, files in os.walk(IMG_DIR):
        # We only care about subdirectories of IMG_DIR, not recursive ones deeper than 1 level
        # root equals IMG_DIR means we are at the top level
        if root == IMG_DIR:
            for char_name in dirs:
                char_dir = os.path.join(IMG_DIR, char_name)
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
                            "color": DEFAULT_COLOR,
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
