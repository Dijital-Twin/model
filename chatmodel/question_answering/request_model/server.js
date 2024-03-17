const express = require('express');
const { PythonShell } = require('python-shell');

const app = express();
const port = 8001;

app.use(express.json());

app.post("/get_answer", (req, res) => {
    const question = req.body.question;
    console.log(question);

    PythonShell.run('./HaystackModel.py', { args: [JSON.stringify(question)] }).then(results => {
        const predictionResult = JSON.parse(results);

        console.log("Model Prediction: ", predictionResult);
        res.json({ prediction: predictionResult });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
