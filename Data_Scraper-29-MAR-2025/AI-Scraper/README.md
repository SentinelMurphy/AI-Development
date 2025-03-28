
**Step 1: Install the necessary dependencies**

Open a terminal or command prompt and run the following commands:

```
conda create --name AI_Scraper python=3.13
conda activate AI_Scraper
cd AI-Development/Data_Scraper-29-MAR-2025/AI-Scraper/
pip install -r requirements.txt
```

This will install the necessary dependencies for our project, including Python 3.13 and the selenium library.

---

**Step 2: Run the AI Scraper application**

Once the installation is complete, run the following command to start the AI Scraper application:

```
streamlit run ai_scraper.py
```

This will launch a web interface where we can interact with the AI Scraper.

---

**Step 3: Test the selenium Ollama API**

Open a web browser and navigate to `http://localhost:8501` (or the address displayed in the terminal). This will take you to the web interface of our AI Scraper application.

**Question 1:** What are the supported languages in llama3.3 ?

To answer this question, we need to interact with the selenium API using the `Enter url` input field. Please enter a valid URL and press Enter.

(Note: You can replace `https://ollama.com/library/llama3.3` with any other valid URL to test the selenium API.)

---

**Step 4: Test the selenium Wikipedia API**

Let's try another example by entering a different URL:

```
Enter url : https://en.wikipedia.org/wiki/Vibe_coding
```

Please enter this URL and press Enter.

**Question 2:** Who is Andrej Karpathy ?

To answer this question, we can interact with the selenium API again using the `Enter url` input field. Please enter a valid URL that contains information about Andrej Karpathy, such as his Wikipedia page, and press Enter.

(Note: You can replace `https://en.wikipedia.org/wiki/Vibe_coding` with any other valid URL to test the Llama API.)
