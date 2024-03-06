import json

def read_json_and_write_dialogues(json_file_path, output_file_path):
    # Open and read the JSON file
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_input = json.load(file)
    
    # Open the output file in write mode and write the dialogues
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for episode in json_input:
            for dialogue in episode['dialogues']:
                # Replace newline characters with spaces for continuity
                dialogue_text = dialogue["dialogue"].replace("\n", " ")
                file.write(f'{dialogue["speaker"]} says that {dialogue_text}\n')

json_path = "./friends-1-227.json"
output_path = "./dialogues_parsed.txt"

read_json_and_write_dialogues(json_path, output_path)