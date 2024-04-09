# DIGITAL TWIN MODEL

This repository is dedicated to exploring, experimenting, and finetuning various pre-trained models, primarily from Huggingface, to develop a customized chatbot. Our aim is to delve into language models, enhancing their capabilities for personalized user interactions.

## Chat Model Section

In the `chatmodel` directory, you'll find finetuning notebooks along with the associated model weights. Each model has its dedicated folder.

### Included Models:
- Blenderbot (variants: 400M, 1B)
- DialoGPT (sizes: small, medium, large)
- GPT-2
- Llama2 (7B version)
- Mistral (7B version)
- QA (Question Answering) Model

## Text-to-Speech (TTS) Model Section

The `text-to-speech` directory houses finetuning notebooks, sample voices, and a preprocessing notebook for TTS models. Detailed finetuning guidelines and deployment instructions for the XTTS model are also available.

### Available TTS Models:
- MetaVoice (1B version)
- Speech T5
- XTTS
- OpenVoice

### XTTS Finetuning and Deployment:
- Finetuning the XTTS model is user-friendly through a GUI, detailed in `text-to-speech\finetune\XTTS_FT.ipynb`.
- Post-finetuning, model weights are available for creating a new Docker image, simplifying deployment. For detailed deployment instructions, refer to the `text-to-speech\deploy` directory.
