
# LLM bases stock-news sentimentan alysis


A sentiment analysis pipeline for financial news headlines related to various stocks (AMZN, GOOG, NFLX, TSLA, NVDA) using a fine-tuned LLaMA-2 model. It installs necessary libraries, loads the base and PEFT (Parameter Efficient Fine-Tuning) models, and processes multiple CSV files containing stock-related news headlines. For each headline, the model predicts the sentiment as positive, neutral, or negative based on a task-specific prompt. The results are saved into new CSV files for each stock, ensuring sentiment-labeled data is generated for further analysis.

