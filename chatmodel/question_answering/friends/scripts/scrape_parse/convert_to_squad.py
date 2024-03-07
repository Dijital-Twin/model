# This code conerts the friendsqa_dev.json file to SQuAD format
import json

def find_answer_start(context, answer_text, speaker):
    answer_start = context.find(answer_text)
    if answer_start != -1:
        return answer_start
    return context.find(speaker)

def convert_to_squad_format(input_data):
    squad_formatted_data = {
        "version": "v2.0",
        "data": []
    }

    for article in input_data['data']:
        squad_article = {
            "title": article['title'],
            "paragraphs": []
        }
        for paragraph in article['paragraphs']:
            context = ' '.join([f"{utterance['speakers'][0]} says that {utterance['utterance']}" for utterance in paragraph.get('utterances:', [])])
            qas = []
            for qa in paragraph['qas']:
                squad_qa = {
                    "id": qa['id'],
                    "question": qa['question'],
                    "answers": [],
                    "is_impossible": False
                }
                for answer in qa['answers']:
                    answer_text = answer['answer_text']
                    if answer['inner_start'] == -1 and 'speakers' in answer:
                        speaker = answer['speakers'][0]
                        answer_text = speaker
                    answer_start = find_answer_start(context, answer_text, speaker if 'speaker' in locals() else '')
                    squad_answer = {
                        "text": answer_text,
                        "answer_start": answer_start
                    }
                    squad_qa['answers'].append(squad_answer)
                qas.append(squad_qa)
            squad_paragraph = {
                "context": context,
                "qas": qas
            }
            squad_article['paragraphs'].append(squad_paragraph)
        squad_formatted_data['data'].append(squad_article)

    return squad_formatted_data


input_data = json.load(open('friendsqa_dev.json'))

squad_formatted_data = convert_to_squad_format(input_data)

with open('squad_formatted_data.json', 'w') as f:
    json.dump(squad_formatted_data, f, ensure_ascii=False, indent=4)
