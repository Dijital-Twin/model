### Deploying the finetuned tts model

This readme describes how to deploy the finetuned tts model on a server.

#### Step 1: Use Finetune Notebook
First, you need to finetune the model using the finetune notebook. The finetune notebook is located at `text-to-speech/finetune/XTTS_FT.ipynb`. Follow the instructions in the notebook to finetune the model.

#### Step 2: Export the model
After finetuning the model, you need to export the model. The model is exported as config.json, model.pth and vocab.json. Place these files in 'model' directory with in same folder as 'Dockerfile'. Also create a 'speaker' directory in the same folder as 'Dockerfile' and place the wav files of spekaer there.

#### Step 3: Build the docker image
Run the following command to build the docker image
```bash
docker build -t tts .
```

#### Step 4: Run the docker container
Run the following command to run the docker container
```bash
docker run -p 8020:8020 tts
```