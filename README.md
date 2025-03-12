# 🏛️ MA_Thesis: Generative Agents in Parliamentary Debate  
**Simulating Rhetoric, Memory, and Cross-Party Interactions**  

📌 **Author:** Hao-Ting Chan  
📌 **Institution:** University of Mannheim  
📌 **Theis Supervisor:** Prof. Marc Ratkovic, Ph.D.  
📌 **Date:** March 2025  

## 📖 Overview  
This repository contains the code, data, and results from my Master’s thesis: **“Generative Agents in Parliamentary Debate: Simulating Rhetoric, Memory, and Cross-Party Interactions.”**  

The thesis investigates how **large language model (LLM)-based generative agents** can be used to **simulate UK parliamentary debates**. It explores the effectiveness of **fine-tuning, retrieval-augmented memory, and persona-based prompting** in achieving semantic, topical, and rhetorical fidelity to real debates. The study applies various NLP techniques to measure how well AI-generated debates reflect actual legislative discussions.

---

## 🚀 Key Features  
✅ **Multi-agent debate simulation**: Fine-tuned LLMs simulate UK House of Commons debates using persona-driven agents.  
✅ **Fine-tuned Llama model**: Trained on historical parliamentary debates to enhance rhetorical accuracy.  
✅ **Evaluation metrics**: **Topical coherence, semantic similarity, and linguistic style analysis** via **BERTopic, LIWC, LSM, and cosine similarity metrics**.  
✅ **Perturbation experiments**: Simulates real-world political crises to assess linguistic and argumentative shifts in AI-driven debates.  
✅ **Comparative analysis**: Evaluates GPT-3.5 vs. Llama-3.2 models to determine realism in simulated legislative debates.  

---

## 📊 Methodology  

1️⃣ **Data Collection**  
- Historical UK parliamentary transcripts (ParlSpeech dataset).  
- Speaker-specific fine-tuning datasets for MPs to capture rhetorical and ideological alignment.  

2️⃣ **Model Training & Inferencing**  
- **Base models**: GPT-3.5, Llama-3.2  
- **Fine-tuned models**: Llama-3.2 fine-tuned on parliamentary debates  
- **Inferencing tests** on Theresa May’s real debate responses  

3️⃣ **Evaluation Metrics**  
- **Topical Coherence:** BERTopic  
- **Semantic Similarity:** BERTScore & Sentence Embeddings  
- **Stylistic Fidelity:** LIWC & LSM  
- **Perturbation Studies:** Analyzing linguistic coordination under crisis events  

---

## 📖 Notebooks  
| Notebook                                | Description                                        |
|-----------------------------------------|----------------------------------------------------|
| `Data_PreProcessing.qmd`                | Prepares raw parliamentary data.                 |
| `Inferencing_Gpt3.5.ipynb`              | Tests GPT-3.5 inferencing ability.                 |
| `Inferencing_Llama3.2_base.ipynb`       | Evaluates Llama 3.2 before fine-tuning.            |
| `Inferencing_Llama3.2_finetuned.ipynb`  | Analyzes fine-tuned Llama model.                   |
| `MiniHOC_v4.ipynb`                      | Simulates a multi-agent debate.                    |
| `Text_analysis_Debates.ipynb`           | Evaluates linguistic structure.                  |

---

## 📌 How to Use

### 1️⃣ Exploratory Data Analysis & Preprocessing  
- **Data Preparation:**  
  - `code/Data_PreProcessing.qmd` – Prepares and cleans the ParlSpeech V2 dataset, the results of the cleaned dataset can be found on [Kaggle Dataset](https://www.kaggle.com/datasets/haotingchan/parlspeech/data?select=df_HoC_miniDebate.csv)
- **Exploratory Analysis:**  
  - `code/parlspeech_EDA.ipynb` – Conducts comprehensive exploratory data analysis on the ParlSpeech data and generate 
- **Training Data Preparation:**  
  - `code/Preprocess_data_TheresaMay.ipynb` – Prepares training data for fine-tuning using Theresa May’s debate transcripts.
  - `code/Preprocess_data_sixMPs.ipynb` – Converts training data from six Members of Parliament into a JSON chat format for fine-tuning.

### 2️⃣ Fine-tuning Llama-3.2-Instruct Model
Navigate to the `code/finetuning` folder and run the corresponding Python notebook to replicate the fine-tuning process. Each notebook fine-tunes a Llama 3.2-Instruct model on the transcript data of a specific Member of Parliament.
(_Note: `finetune_Llama_TheresaMay.ipynb` is only used for inferencing_)

### 3️⃣ Running Inferencing & Simulation
Run inferencing with `code/Inferencing_Gpt3.5.ipynb`, `code/Inferencing_Llama3.2_base.ipynb`, and `code/Inferencing_Llama3.2_finetuned.ipynb` to generate the output response of each model to parliamentary prompts.

Four different Python notebooks for using different model combinations to run a mini House of Commons (MiniHoC) simulation of a debate on the "Free Movement of EU Nationals"
- `code/MiniHOC_v1.ipynb` runs a mini 
- `code/MiniHOC_v2.ipynb`
- `code/MiniHOC_v3.ipynb`
- `code/MiniHOC_v4.ipynb`

### 4️⃣ Evaluating Model Performance  




