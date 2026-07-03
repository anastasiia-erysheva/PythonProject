from zipfile import ZipFile
import json
arsenal_players = []
with ZipFile("data.zip") as zip_file:
    for info in zip_file.infolist():
        if info.filename.endswith('.json'):
            try:
                file_content = zip_file.read(info.filename).decode("utf-8")
                data = json.loads(file_content)
                if data.get('team') == 'Arsenal':
                    arsenal_players.append((data['first_name'], data['last_name']))
            except json.JSONDecodeError:
            try:
                
                pass
arsenal_players.sort()
for first_name, last_name in arsenal_players:
    print(f"{first_name} {last_name}")