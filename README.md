# 🏥 MediBot – AI-Powered Medical Chatbot  

MediBot is an AI-driven medical chatbot designed to provide informative responses to medical queries. It leverages **Gemini** for natural language understanding, **Pinecone** for vector search, and **Flask** for deployment, featuring an intuitive **UI** for seamless user interaction.  

## 📌 Features  
✅ **AI-Powered Responses** – Uses Gemini for accurate medical query resolution.  
✅ **Vector Search** – Pinecone ensures fast and relevant information retrieval.  
✅ **Web-Based Interface** – Built using Flask and an interactive UI.  
✅ **Modular Design** – Well-structured code for easy scalability.  

---

## 🛠 Tech Stack  
| Component  | Technology |
|------------|-----------|
| **LLM** | Gemini |
| **Vector DB** | Pinecone |
| **Backend** | Flask |
| **Frontend** | HTML, CSS, JavaScript |
| **Deployment** | Flask Server |

---

## 📂 Project Structure  
```
MediBot/
│── Data/                  # Dataset storage
│── Demo/                  # Demo-related files
│── research/              # Research-related content
│── src/                   # Core logic
│   ├── helper.py          # Helper functions
│   ├── prompt.py          # Prompt engineering for Gemini
│── static/                # Frontend assets (CSS, JS)
│── templates/             # HTML templates for UI
│   ├── index.html         # Main UI page
│── .env                   # API keys (GEMINI, PINECONE)
│── .gitignore             # Files to ignore in Git
│── app.py                 # Main Flask app
│── LICENSE                # License information
│── README.md              # Documentation
│── requirements.txt       # Python dependencies
│── setup.py               # Setup configurations
│── store_index.py         # Indexing medical data in Pinecone
│── template.py            # Template-related code
│── test.py                # Unit tests
```

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-repo/MediBot.git
cd MediBot
```

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Keys  
Create a `.env` file in the root directory and add the following:  
```
GEMINI_API_KEY=your_api_key
PINECONE_API_KEY=your_pinecone_key
```

### 4️⃣ Run the Application  
```bash
python app.py
```  
Visit [`http://127.0.0.1:5000`](http://127.0.0.1:5000) in your browser to access the chatbot.  

---

## 📺 Demo  
📹 [Watch the demo here](Demo/MediBot.mp4)  

---

## 🧪 Testing  
To run tests:  
```bash
python test.py
```

---

## 🤝 Contribution  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Commit changes (`git commit -m "Added new feature"`)  
4. Push to the branch (`git push origin feature-name`)  
5. Open a pull request  
