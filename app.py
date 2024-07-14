from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

app = Flask(__name__)

# Load the fine-tuned tokenizer and model
model_name = "/Users/bhavishachaudhari/Desktop/QnA/models"  # Update this to the local path where your model is saved
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def ask_question(question, context):
    inputs = tokenizer(
        question,
        context,
        max_length=384,
        truncation="only_second",
        return_tensors="pt"
    )
    input_ids = inputs["input_ids"].to(model.device)
    attention_mask = inputs["attention_mask"].to(model.device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        answer_start_scores = outputs.start_logits
        answer_end_scores = outputs.end_logits

    answer_start = torch.argmax(answer_start_scores)
    answer_end = torch.argmax(answer_end_scores) + 1
    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(input_ids[0][answer_start:answer_end])
    )
    return answer

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    context = data['context']

    answer = ask_question(question, context)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
