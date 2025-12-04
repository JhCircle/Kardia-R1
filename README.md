<div align="center"> <h2><img src="./assets/Kardia-R1-Logo.png" width="32" style="margin-bottom: -4px;"/> 
 <strong>Kardia-R1: Unleashing LLMs to Reason toward Understanding and Empathy for Emotional Support via Rubric-as-Judge Reinforcement Learning</strong></h2>


<h4 align="center"> <h4> 💗 We introduce <strong>Kardia-R1</strong>: teaching LLMs to understand, reason, and care — with transparent empathy 🌱</h4>

[![Paper](https://img.shields.io/badge/arXiv-2512.01282-b31b1b.svg)](https://arxiv.org/abs/2512.01282)
![GitHub Repo stars](https://img.shields.io/github/stars/JhCircle/Kardia-R1?style=social)
[![HuggingFace](https://img.shields.io/badge/🤗%20HuggingFace-KardiaBench-orange.svg)](https://huggingface.co/datasets/Jhcircle/KadiaBench)
</div>

<p align="center"> <strong>💌 Contact:</strong> <a href="mailto:jamse_yuan@163.com">jamse_yuan@163.com</a> </p>

<p align="center">
<img src="./assets/Kardia-R1.png" align="center" width="90%">
</p>

---


## 🔥 News
* ```2025.12.02``` 🎉 Our [_Kardia-R1_](https://arxiv.org/abs/2512.01282) paper released on arXiv — check it out now!
* ```2025.12.03``` 🚀 The full **[_KardiaBench_](https://huggingface.co/datasets/Jhcircle/KadiaBench)** dataset (22K multi-turn dialogues, 671 personas) is **now officially released and open-sourced** on HuggingFace!
> ```markdown
> ### Authentication & Loading the Dataset
> huggingface-cli login
> from datasets import load_dataset
> dataset = load_dataset("Jhcircle/KadiaBench")
> ```
---

## 💞 What is Kardia-R1?

> 🧠 **Kardia-R1** is a reasoning-centric empathetic dialogue framework that unifies  
> **user understanding → emotional reasoning → safe, supportive responses**,  
> empowered by **Rubric-as-Judge GRPO Reinforcement Learning** for transparent and controllable empathy.

---

### 🧩 Key Features

- **KardiaBench**: 671 real-world user profiles + 22,080 multi-turn empathetic dialogues  
- **Four-span structured cognition**  
  - `<|understanding_begin|>...<|understanding_end|>` — Interpret user intent & emotions using persona and context  
  - `<|reasoning_begin|>...<|reasoning_end|>` — Perform internal appraisal and empathetic reasoning  
  - `<|emotion_begin|>...<|emotion_end|>` — Identify the correct fine-grained emotion label  
  - `<|response_begin|>...<|response_end|>` — Generate supportive, persona-aligned empathetic replies  
- **Rubric-as-Judge RL (Verifiable)**  
  - Interpretable, criterion-based, LLM-judged reinforcement learning  
- **Backbone-Agnostic Gains**  
  - Improves Qwen, Gemma, and more across **all empathy metrics**  
- **Superior to SoTA LLMs**  
  - Outperforms **GPT-4o, DeepSeek-R1, PsyLLM** in emotion accuracy & empathetic quality  

---

### 🎯 Rubric-as-Judge RL (Verifiable Reinforcement Learning)

- Human-interpretable rubric: **Relevance · Empathy · Persona Consistency · Safety · Fluency**  
- Transparent scoring → controllable improvement  
- No black-box reward models → fully interpretable and aligned behavior  

---

### 📈 Superior Performance

- Consistent gains across **every empathy dimension**  
- Stronger emotional grounding and persona alignment  
- Scalable to **Qwen (3B/7B) / Gemma (2B/7B）** backbones  
- Robust, generalizable empathetic cognition across diverse emotional contexts  

<p align="center">
<img src="./assets/Kardia-R1-Radar.png" width="43%">
</p>

> 🌟 **Kardia-R1 achieves state-of-the-art empathy, persona consistency, and emotion accuracy**,  
> surpassing both **general-purpose LLMs** and **specialized empathetic dialogue systems**.

---
### 📦 KardiaBench Dataset
#### 📂 Dataset Overview

**KardiaBench** is a large-scale empathetic dialogue dataset designed for  
reasoning-centered emotional support, containing:

- **22,080 empathetic multi-turn dialogues**
- **671 fully documented personas**
- **Fine-grained emotional states**
- **Four-span structured reasoning format**
- Fully anonymized & cleaned

HuggingFace dataset: 👉 **[_KardiaBench_](https://huggingface.co/datasets/Jhcircle/KadiaBench)**

---

#### 📥 Load the Dataset
To prevent misuse of sensitive data, our dataset requires an access request on HuggingFace. Please follow the instructions below to obtain access.
- Submit an Access Request describing the intended use
- Wait for approval from the maintainers — we will review and approve requests as quickly as possible
```python
from datasets import load_dataset

dataset = load_dataset("Jhcircle/KadiaBench")
```
If you encounter AccessDenied or 403 Forbidden errors, your access request may still be pending or your [HuggingFace authentication](https://huggingface.co/docs/huggingface_hub/main/en/guides/cli) may be missing.

Login manually if needed:
```markdown
huggingface-cli login
```
#### 📘**Data Fields**
| Field | Description |
|-------|-------------|
| **person** | Full raw user profile string including MBTI, About, Signature, and Recent Activities. |
| **mbti** | The user’s MBTI type extracted from the profile (e.g., “INFP”, “ISTP”). |
| **emotion** | Target emotional state representing the user’s current feelings in the scenario (e.g., “anxious”, “terrified”). |
| **situation** | Starting background context or emotional scenario for the conversation. |
| **anon_username** | An anonymized username for privacy-preserving user identity. |
| **messages** | Full structured dialogue as a list of message objects, including the system prompt, user turns, and assistant responses. |

## 📚 Citation

If our work is helpful, please cite:

```bibtex
@article{yuan2025kardia,
  title={Kardia-R1: Unleashing LLMs to Reason toward Understanding and Empathy for Emotional Support via Rubric-as-Judge Reinforcement Learning},
  author={Yuan, Jiahao and Cui, Zhiqing and Wang, Hanqing and Gao, Yuansheng and Zhou, Yucheng and Naseem, Usman},
  journal={arXiv preprint arXiv:2512.01282},
  year={2025}
}
```

## 🙇 Acknowledgement

We gratefully acknowledge EmpatheticDialogues for foundational inspiration, PersonalityCafe for publicly shared personas, DeepSeek-R1 and Qwen3 for their GRPO insights, and all annotators and psychology experts for their invaluable support in building KardiaBench.
