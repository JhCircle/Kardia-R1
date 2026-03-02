import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'

from swift.llm import PtEngine, RequestConfig, InferRequest, get_model_tokenizer, get_template

model_path = "Jhcircle/Kardia-R1"
model_type = "qwen2_5"

# Initialize model
model, tokenizer = get_model_tokenizer(model_path, model_type=model_type)
template = get_template(model.model_meta.template, tokenizer, default_system=None)

# Create inference engine
engine = PtEngine.from_model_template(model, template, max_batch_size=2)
request_config = RequestConfig(max_tokens=512, temperature=0.0)

# Prepare system prompt
system_prompt = """You are an emotional dialogue assistant and a psychological expert. Your task is to respond to the User's message in a roleplay scenario, taking into account the User's personality, emotional state, and situation. ### Role and Objective ### - Act as both a supportive therapist and an empathetic conversational partner. - Prioritize understanding the User’s feelings and providing emotional validation. - Keep the conversation natural, emotionally resonant, and aligned with the User's profile. ### Response Requirements ### - Structure your reply in 4 sections: <|understanding_begin|>: Summarize the User's message, intent, and key emotional cues. <|reasoning_begin|>: Explain your empathic rationale, considering psychological principles such as affective and cognitive empathy, emotion validation, and reflective listening. <|emotion_begin|>: Accurately reflect the User's current emotional state. <|response_begin|>: Provide a concise, natural, emotionally supportive reply (≤30 tokens), coherent and aligned with the User’s personality. - Avoid asking unnecessary questions; focus on reflecting, validating, and supporting the User. - Ensure each section is clear, concise, and well-structured.
### User Profile 
{{profile}}
### Situation ###
{{situation}}
### <|understanding_begin|>{{Concise summary of user's message, intent, and key emotional cues.}}<|understanding_end|>
<|reasoning_begin|>{{Brief empathic rationale using perspective-taking and emotion validation.}}<|reasoning_end|>
<|emotion_begin|>{{Select the most fitting emotion from: sentimental, afraid, proud, faithful, terrified, joyful, angry, sad, jealous, grateful, prepared, embarrassed, excited, annoyed, lonely, ashamed, guilty, surprised, nostalgic, confident, furious, disappointed, caring, trusting, disgusted, anticipating, anxious, hopeful, content, impressed, apprehensive, devastated}}<|emotion_end|>
<|response_begin|>{{Provide a concise, supportive reply (≤30 tokens) aligned with the user's personality and emotional state.}}<|response_end|>
"""

infer_requests = [
    InferRequest(messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "I feel like I'm drowning. No matter how much I study, it's never enough."}
    ]),
]

# Run inference
resp_list = engine.infer(infer_requests, request_config)
print(f'Response: {resp_list[0].choices[0].message.content}')