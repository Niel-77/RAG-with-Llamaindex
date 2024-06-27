## Implementing Rag with llamaindex

### Question
How good Query2CAD performs with GPT-4 in comparison to GPT-3.5?

### Answer given by the LLM
The performance of Query2CAD using GPT-4 as a language model surpasses that achieved with GPT-3.5 when it comes to easy and medium difficulty levels, registering accuracies of 95.23% and 70%, respectively. Conversely, the use of GPT-3.5-Turbo resulted in lower accuracy rates on these same difficulty levels - an ease level performance at 85.71% and medium/hard levels at 35% and 37.5%. This comparison demonstrates a significant improvement when using GPT-4 over GPT-3.5 for the Query2CAD system in generating correct 3D CAD models as per user queries, particularly on easier and somewhat challenging tasks.

---

### Notes
- Though the LLM answered the question correctly, it also gave a nonsense answer unrelated to the question.
- It takes a long time for inference, causing the reply to be delayed. The request timeout has been increased to 600 seconds, but sometimes the LLM still fails to infer the answer. Prompt engineering might help.
- Finding a specific answer using the Vector Query Engine is less GPU-intensive than the Summary Query Engine.
- The RouterQueryEngine() was effective in selecting the required query engine as per the question.

### You can find the detailed documentation in 'llamaindexlearn.ipynb'.
