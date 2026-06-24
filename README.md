# LLM-Guided Deep Reinforcement Learning for Autonomous GUI Testing

An intelligent GUI testing framework that combines Large Language Models (LLMs), Deep Reinforcement Learning (DQN), Selenium automation, and Computer Vision to perform autonomous software testing and self-healing test execution.

---

## Overview

Traditional GUI testing requires manually written test scripts that are difficult to maintain when user interfaces change.

This project introduces an autonomous testing framework where:

- A Large Language Model converts natural language testing requirements into executable test plans.
- A Deep Q-Network (DQN) agent learns optimal testing actions.
- Selenium executes browser interactions.
- OpenCV performs visual validation of UI states.
- A Critic Agent analyzes failures and suggests recovery actions.
- The system continuously improves through reinforcement learning.

---

## Key Features

- Natural Language Test Instructions
- LLM-Based Test Planning
- Autonomous GUI Navigation
- Deep Reinforcement Learning (DQN)
- Selenium Browser Automation
- Screenshot-Based Validation
- OpenCV Visual Comparison
- Bug Detection and Logging
- Self-Healing Recovery Mechanism
- Continuous Learning Through Experience Replay

---

## Project Architecture

```text
User Input
    ↓
LLM Planner
    ↓
Test Plan Generation
    ↓
DQN Agent
    ↓
Selenium Environment
    ↓
Action Execution
    ↓
Visual Verification
    ↓
Bug Detection
    ↓
Critic Agent
    ↓
Recovery Action
    ↓
Replay Memory Update
    ↓
DQN Training
```

## Workflow Diagram

See:

```text
docs/workflow_diagram.pdf
```

---

## Project Structure

```text
LLM-Guided-DRL-for-Autonomous-GUI-Testing/
│
├── main.py
├── config.py
│
├── docs/
│   └── workflow_diagram.pdf
│
├── llm/
│   ├── ollama_client.py
│   ├── planner.py
│   └── critic.py
│
├── rl/
│   ├── dqn_agent.py
│   ├── replay_buffer.py
│   └── model.py
│
├── selenium/
│   ├── selenium_env.py
│   └── state_extractor.py
│
├── agents/
│   └── executor.py
│
├── utils/
│   ├── logger.py
│   ├── vision.py
│   └── bug_detector.py
│
├── dashboard/
│   └── app.py
│
├── tests/
│   └── sample_prompt.txt
│
├── outputs/
│   ├── screenshots/
│   └── logs/
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt

```
---

## Technologies Used

### Artificial Intelligence
- Llama 3 (Ollama)
- Deep Q-Network (DQN)
- Reinforcement Learning

### Automation
- Selenium WebDriver
- ChromeDriver

### Computer Vision
- OpenCV
- Pillow

### Backend
- Python
- PyTorch

### Dashboard
- Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Subhra0309/LLM-Guided-DRL-for-Autonomous-GUI-Testing.git
cd LLM-Guided-DRL-for-Autonomous-GUI-Testing
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Execute the main workflow:

```bash
python main.py
```

Launch the dashboard:

```bash
streamlit run dashboard/app.py
```

---

## Example Input

```text
Test login functionality using valid and invalid credentials
```

The LLM converts the instruction into a structured testing plan that is executed autonomously.

---

## Future Improvements

- Multi-browser support
- PPO and A3C reinforcement learning agents
- Dynamic web application adaptation
- Multi-agent collaboration
- Distributed test execution
- Automated bug report generation

---

## Author

Subhrajit Jana

M.Sc. Computer Science
Ramakrishna Mission Vivekananda Educational and Research Institute

GitHub: https://github.com/Subhra0309

Email: subhrajitjana2018@gmail.com


---

## License

This project is licensed under the MIT License.
