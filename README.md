# Simulating UK Parliamentary Debates with Generative Agents



MiniHoc_v1 (Gpt 4.0)

MiniHoc_v2 + finetune_v2 + preprocess_v1
+ GPT 4.0 +  
+ Llama 3.2 Instruct

MiniHoc_v3 + finetune_v3 + preprocess_v2 + preprocess_v3
+ GPT 4.0
+ Llama 3.2 Instruct



This project explores how **large language models (LLMs)** can simulate **UK House of Commons debates** using generative agents with **memory, saliency scoring, and dialogue generation**. The goal is to evaluate how well AI-driven agents replicate **real-world parliamentary discourse** by comparing generated debates to actual **House of Commons transcripts**.

## 🛠️ Approaches Used  
The project utilizes three primary methods for developing LLM-driven parliamentary debate agents:

1. **Retrieval-Augmented Generation (RAG)** – Enables agents to recall past discussions using **time-weighted memory retrieval**.  
2. **In-Context Learning (ICL)** – Role-playing MPs through structured prompts.  
3. **Fine-Tuning** – Training a **Llama-3 model** on historical parliamentary transcripts to replicate MP rhetoric.

## 🏛️ Implementation Details  
- **Memory and Reflection:** GPT-3.5 manages agents’ **memory retrieval and reflection processes**.  
- **Dialogue Generation:** A **fine-tuned Llama-3.2-Instruct** model generates responses, deciding whether to engage in debate.  
- **Debate Framework:** Agents store past observations, evaluate personal relevance (**saliency scoring 1-10**), and contribute dynamically based on a pre-defined cut-in threshold.

## 🔍 Evaluation Metrics  
To compare AI-generated debates against real parliamentary transcripts, the following **NLP evaluation techniques** are applied:

- **BERTopic & NER** – Topic alignment and entity extraction.
- **BERT-score** – Semantic similarity measurement.
- **LIWC (Linguistic Inquiry & Word Count)** – Linguistic and psychological analysis.

## 📅 Next Steps  
- Simulate **multi-agent debates** and compare them with **real-world House of Commons discussions**.  
- Conduct **model comparisons** across different agent architectures:
  1. **Llama-3 fine-tuned on debate history + Generative Agent framework**.  
  2. **Llama-3 fine-tuned on debate history only**.  
  3. **Llama-3-Instruct** (Meta's official fine-tuned model).  
  4. **GPT-3.5** (baseline).  
- Explore potential applications in **political science, policymaking simulations, and AI-assisted debate training**.

---

## 🚀 Installation & Usage  
### **🔧 Dependencies**  
Ensure you have Python 3.10+ and install the required dependencies:

```bash
pip install -r requirements.txt
