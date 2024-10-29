# InsightForge

InsightForge is a multi-agent, LLM-based project designed to automate the process of researching and writing articles on specified topics. The system employs a researcher agent to gather information using Google Search, followed by a writer agent that composes a coherent blog or article based on the findings. InsightForge provides an efficient, intelligent solution for generating content from scratch, leveraging the latest in large language models (LLMs) and multi-agent collaboration.

## Key Features

- **Multi-Agent Architecture**: The project utilizes a dual-agent system with specialized roles.
  - **Researcher Agent**: Conducts research using Serper API for Google search, compiles relevant findings, and formulates a conclusion.
  - **Writer Agent**: Uses the researcher's findings to write a structured and well-articulated article.
- **Dynamic Content Generation**: Each article is generated based on real-time data gathered by the researcher agent.
- **LLM-Driven Agents**: Powered by Google’s Gemini model, allowing for natural language comprehension and coherent article generation.
- **Serper API Integration**: Enables the researcher agent to gather up-to-date information from Google Search, ensuring relevance and accuracy.
  
## Tools and Frameworks

- **Crew AI Agent Framework**: Used for building, managing, and orchestrating the multi-agent system.
- **Serper API**: For retrieving real-time information to guide the research phase.
- **Google Gemini Model**: Powers the LLM-driven responses for both researcher and writer agents.
- **Python**: Primary language for project scripts.

## Getting Started

### Prerequisites

- Python 3.8 or later
- API keys for Serper API
- Access to Google Gemini model for agent responses

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/InsightForge.git
    cd InsightForge
    ```

2. **Install Required Packages**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**
   - Create a `.env` file in the root directory with the following details:
     ```plaintext
     SERPER_API_KEY=your_serper_api_key
     GEMINI_API_KEY=your_google_gemini_api_key
     ```

4. **Configure Agent Settings**
   - Adjust agent behavior (e.g., search depth, article length) in `config.py`.

### Running the Project

1. **Start the Research and Writing Process**
    ```bash
    python main.py --topic "Your chosen topic"
    ```

   - The researcher agent will conduct searches on the specified topic, summarize findings, and pass these to the writer agent for article composition.

2. **View Output**
   - The resulting article will be saved in the `output/` directory as a text file named after the topic.

## Future Enhancements

- **Feedback Mechanism**: Implement a feedback loop for iterative improvement of the article quality.
- **Enhanced Summarization**: Refine the researcher agent to create more granular, topic-specific summaries.
- **Advanced Style Options**: Enable the writer agent to adapt writing style based on the target audience.

## Contributing

We welcome contributions to InsightForge! Please create a pull request with any improvements or submit issues for bug reports or feature requests.

## License

This project is licensed under the MIT License.

---

**InsightForge**: Automating research and content creation through collaborative LLM agents.
