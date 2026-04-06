import json
from datetime import datetime

def main():
    with open("Words.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    index = datetime.now().toordinal() % len(data)
    entry = data[index]

    # New section to insert
    new_section = f"""## Word of the day

### 🇯🇵 {entry['Japanese']}
- **Reading:** {entry['ReadableVersion']}
- **Translation:** {entry['EnglishTranslation']}
- **Type:** {entry['Tags']}

"""

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find("## Word of the day")
    end = content.find("## Sources")

    # If the sections are not found
    if start == -1 or end == -1:
        raise ValueError("Sections 'Word of the day' ou 'Sources' introuvables dans README.md")

    updated_content = content[:start] + new_section + content[end:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    main()