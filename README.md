# Stock-Market Agent 🤖

A multi-agent AI system built with crewAI for financial analysis and research. This project leverages autonomous AI agents that collaborate to perform complex financial analysis tasks, demonstrating the power of multi-agent orchestration in finance.

## 📋 Overview

Memory-Bot is powered by [crewAI](https://crewai.com), a framework designed for orchestrating role-playing autonomous AI agents. The system enables multiple specialized agents to work together seamlessly on financial analysis tasks, combining their expertise to generate comprehensive research reports.

## ✨ Features

- **Multi-Agent Collaboration**: Specialized AI agents work together on complex financial tasks
- **Autonomous Research**: Agents can independently gather, analyze, and synthesize financial information
- **Customizable Workflows**: Flexible agent and task configuration through YAML files
- **LLM-Powered Analysis**: Leverages large language models for intelligent financial insights
- **Automated Reporting**: Generates detailed financial analysis reports automatically

## 🛠️ Technology Stack

- **Framework**: crewAI
- **Language**: Python 3.10 - 3.13
- **Package Manager**: UV (for fast, reliable dependency management)
- **LLM Provider**: Groq API
- **AI Model**: Llama

## 📦 Installation

### Prerequisites

- Python >= 3.10 and < 3.14
- UV package manager (recommended) or pip

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abishek0070/Memory-Bot.git
   cd Memory-Bot
   ```

2. **Install UV** (if not already installed)
   ```bash
   pip install uv
   ```

3. **Install dependencies**
   ```bash
   crewai install
   ```
   
   Or using UV directly:
   ```bash
   uv sync
   ```

4. **Configure environment variables**
   
   Create a `.env` file in the root directory and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 🚀 Usage

Run the finance crew from the root folder:

```bash
crewai run
```

This command will:
- Initialize the finance analysis crew
- Assemble the configured AI agents
- Execute the defined tasks in sequence
- Generate a `report.md` file with the analysis results

## ⚙️ Configuration

The project uses YAML configuration files for easy customization:

### Agent Configuration
Edit `src/finance/config/agents.yaml` to:
- Define agent roles and responsibilities
- Set agent goals and backstories
- Configure agent capabilities and tools

### Task Configuration  
Edit `src/finance/config/tasks.yaml` to:
- Define analysis tasks
- Set task descriptions and expected outputs
- Configure task dependencies and workflows

### Custom Logic
Modify the following files for advanced customization:
- `src/finance/crew.py` - Add custom logic, tools, and arguments
- `src/finance/main.py` - Configure custom inputs for agents and tasks

## 📁 Project Structure

```
Memory-Bot/
├── knowledge/              # Knowledge base and reference materials
├── src/
│   └── finance/           # Main application code
│       ├── config/        # YAML configuration files
│       ├── crew.py        # Crew orchestration logic
│       └── main.py        # Entry point
├── .gitignore
├── pyproject.toml         # Project dependencies
├── uv.lock               # Locked dependencies
└── README.md
```

## 📊 Example Output

By default, the system generates a comprehensive research report on LLMs (Large Language Models) in the finance domain, saved as `report.md` in the root folder.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📚 Resources

- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub Repository](https://github.com/joaomdmoura/crewai)
- [crewAI Discord Community](https://discord.com/invite/X4JWnZnxPb)
- [crewAI Chat Assistant](https://chatg.pt/DWjSBZn)

## ⚠️ Disclaimer

This project is for demonstration and educational purposes only. The financial analysis and reports generated should not be construed as financial, investment, or trading advice. Always consult with qualified financial professionals before making investment decisions.


## 👨‍💻 Author

**Abishek0070**
- GitHub: [@Abishek0070](https://github.com/Abishek0070)

---

Built with ❤️ using [crewAI](https://crewai.com)
