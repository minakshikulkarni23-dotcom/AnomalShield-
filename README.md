# 🛡️ AnomalShield - AI-Powered Threat & Fraud Detection

AnomalShield is an automated security and anomaly detection intelligence backend engineered during the **FinSpark '26 Hackathon**. The system monitors incoming structural requests, utilizes Machine Learning to calculate threat probabilities, logs historical incident profiles into a database, and flags real-time threats directly to operators.

---

## 🛠️ The Hackathon Architecture & Tech Stack

This project leverages an optimized Python ecosystem to achieve low-latency execution and high system uptime:

* **Backend Framework:** `FastAPI` — Handles rapid JSON data endpoints, routes data traffic seamlessly, and provides built-in Swagger testing interfaces.
* **Predictive AI Engine:** `Scikit-learn` — Powering our core `ml_engine.py` script to classify risk levels and detect behavioral or financial anomalies.
* **Relational Storage:** `PostgreSQL` — Serves as the high-availability security vault to write and store immutable system events and alert logs.
* **Notification Interface:** `Twilio API` — Instantly dispatches SMS warning alerts directly to system administrators when severe anomalies are flagged.
* **Development & Tooling:** Developed in `PyCharm` and managed via the `Command Prompt` CLI.

---

## ⚙️ System Workflow Logic
