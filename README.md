<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">RESEARCHASSISTANT_APP.GIT</h1></p>
<p align="center">
    <em>Empowering Research, One Query at a Time!</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/jeet-ss/researchAssistant_App.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/jeet-ss/researchAssistant_App.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/jeet-ss/researchAssistant_App.git?style=default&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/jeet-ss/researchAssistant_App.git?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
    <!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Main Idea](#-main-idea)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

The researchAssistantApp is an innovative open-source project designed to streamline the research process. It serves as a virtual research assistant, capable of conducting interviews, generating questions, and synthesizing information into comprehensive reports. Key features include AI analyst personas, web search capabilities, and a user-friendly interface. This tool is ideal for researchers, students, and professionals seeking efficient and organized data collection and analysis.


- **🌟 Most Important Features**:
  
  - **🌐 Multi-Agent Architecture using LangGraph**:
    - The app employs a **multi-agent architecture** powered by LangGraph, enabling **parallel research** across various perspectives.
    - Users can select from a **single agent** to **multiple agents**, allowing for flexibility based on the desired depth and breadth of research.
    - This architecture enhances the ability to gather **diverse insights simultaneously**, making the research process more efficient and comprehensive.

  - **🔍 Tool Calling for LLM Agents**:
    - The app includes a **tool calling functionality** that empowers LLM agents to perform **web searches** for the most recent documents and information.
    - This feature ensures that agents can access **up-to-date resources**, enhancing the quality and relevance of the information gathered.
    - Additionally, agents can retrieve results from **Wikipedia**, providing a reliable source of general knowledge and context for the research topic.

  - **🔗 Managing LangGraph and Streamlit States**:
    - Both LangGraph and Streamlit maintain their own **state stores**, which can complicate the integration and management of data between the two systems.
    - Developing a cohesive solution to synchronize these states is a **non-trivial challenge** that requires careful consideration of data flow and user interactions.
    - Addressing this issue is crucial for ensuring a **seamless user experience** and maintaining the integrity of the research process.


---
## Main Idea

### 🎯 Purpose
- **Facilitate comprehensive research** on a specific topic from multiple perspectives.
- Utilize **Interview personas** to simulate diverse viewpoints during the research process.

### 🛠️ User Interaction
#### 1. Selection of Interview Agents
- Users can choose the **number of Interview agents** to engage for their query.
- Options range from a **single agent** to **multiple agents**, depending on the depth of research desired.

#### 2. Persona Generation
- The app generates **unique personas** for each selected agent, reflecting different fields, backgrounds, and expertise.
- Users can **review and customize** the generated personas based on their research needs.

#### 3. Feedback Mechanism
- Users can provide feedback to include **additional interviewers** from different fields or backgrounds.
- This allows for a more **tailored and relevant research experience**.

### 🗣️ Interview Process
#### 1. Engagement with Expert LLM Agent
- Once the user is satisfied with the personas, the agents conduct an interview with an **expert LLM agent**.
- The LLM agent has access to **web search** and **Wikipedia search tools** to provide accurate and up-to-date information.

#### 2. Interview Dynamics
- The interview continues for a **predetermined number of turns**, as specified by the user at the beginning.
- The interview may also conclude earlier if the agents are **satisfied with the responses** received.

### 📄 Report Compilation
#### 1. Findings Consolidation
- After the interviews, the findings from all personas are compiled into a **comprehensive report**.

#### 2. Structured Report Creation
- Three specialized agents are assigned to write distinct sections of the report:
  - **Introduction**: Summarizes the research topic and objectives.
  - **Body**: Presents detailed findings, insights, and perspectives gathered from the interviews.
  - **Conclusion**: Offers a synthesis of the research findings and potential implications.

### 🌈 User Benefits
- Gain insights from **diverse perspectives**, enhancing the depth and breadth of research.
- Streamlined process for **gathering and organizing information** efficiently.
- **Customizable experience** tailored to individual research needs and preferences.

### 🚀 Future Enhancements
- Potential integration of **additional data sources** and research tools.
- Continuous improvement of **persona generation algorithms** for more nuanced perspectives.
- User feedback will be actively sought to **refine and enhance app functionality**.

<p align="center">
    <img src="https://github.com/jeet-ss/researchAssistant_App/blob/main/resources/researchAssistant_graph.jpeg" alt="app graph">
</p>

---
##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>The project is structured around a main entry point `app.py` which manages the application's state, user input, and interactions with language models and web search tools.</li><li>The architecture includes a `models` directory that defines data structures for managing the state of research analysis.</li><li>Utilities for web searching, question generation, and report writing are leveraged to ensure a structured and efficient process for information gathering and synthesis.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>The codebase is written in Python, with a focus on readability and maintainability.</li><li>It uses `pydantic` for data validation and `typing_extensions` for additional typing capabilities, enhancing the code's robustness and clarity.</li><li>The project follows good practices of error handling.</li></ul> |
| 📄 | **Documentation** | <ul><li>The project's primary language is Python</li><li>Installation, usage, and test commands are well-documented, providing clear instructions for setting up and running the project.</li><li>The `LICENSE.txt` file contains the GNU General Public License (GPL) version 3, outlining the terms and conditions for copying, modifying, and distributing the software.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>The project integrates with language learning models (LLM) from either OpenAI or Google, as seen in `utils/llms.py`.</li><li>It also supports the Tavily search tool for web searching, as seen in `utils/webSearchTool.py`.</li><li>User interface elements are managed using `streamlit`, a Python library for data apps.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>The project is highly modular, with separate utilities for web searching, question generation, report writing, and more.</li><li>It has a `models` directory that encapsulates data structures for managing the state of research analysis.</li><li>Each utility module has a specific role, enhancing the code's readability and maintainability.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>The App is able to check for valid API keys.</li><li>It is capable of Generating research level answers and cite their sources.</li></ul> |

---

##  Project Structure

```sh
└── researchAssistant_App.git/
    ├── LICENSE.txt
    ├── README.md
    ├── app.py
    ├── models
    │   ├── constants.py
    │   ├── graph.py
    │   ├── models.py
    │   └── states.py
    ├── requirements.txt
    └── utils
        ├── analyst_utils.py
        ├── interview_utils.py
        ├── llms.py
        ├── print_helpers.py
        ├── sidebar.py
        ├── webSearchTool.py
        └── writer_utils.py
```


###  Project Index
<details open>
    <summary><b><code>RESEARCHASSISTANT_APP.GIT/</code></b></summary>
    <details> <!-- __root__ Submodule -->
        <summary><b>__root__</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/LICENSE.txt'>LICENSE.txt</a></b></td>
                <td>- The file 'LICENSE.txt' is a crucial part of the project's codebase<br>- It contains the GNU General Public License (GPL) version 3, which outlines the terms and conditions for copying, modifying, and distributing the software<br>- This license ensures the software remains free and open-source, allowing users to share and modify the program while maintaining the freedom of software distribution<br>- It's not directly involved in the functionality or architecture of the software but serves as a legal framework that governs its use and distribution.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/app.py'>app.py</a></b></td>
                <td>- App.py serves as the main entry point for a research assistant application<br>- It manages the application's state, user input, and interactions with language models and web search tools<br>- The application allows users to ask questions, receive responses from simulated analysts, provide feedback, and receive a final report<br>- It also handles API key management and user interface elements such as forms, buttons, and containers.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
                <td>- Requirements.txt manages the dependencies for the project, specifying the exact versions of the libraries needed<br>- It ensures consistent environment setup across different stages of the project, including langchain modules, pydantic for data validation, python-dotenv for environment variable management, streamlit for data apps, and typing extensions for additional typing capabilities.</td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- models Submodule -->
        <summary><b>models</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/models/states.py'>states.py</a></b></td>
                <td>- The 'states.py' in the 'models' directory defines data structures for managing the state of research analysis<br>- It includes classes for generating analysts, managing the research graph, and conducting interviews<br>- These classes handle tasks such as tracking research topics, managing analyst feedback, and structuring the final report.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/models/graph.py'>graph.py</a></b></td>
                <td>- The 'graph.py' in the 'models' directory constructs a state graph for a research assistant system<br>- It outlines the flow of operations from creating analysts, conducting interviews, to writing and finalizing reports<br>- It leverages various utilities for web searching, question generation, and report writing, ensuring a structured and efficient process for information gathering and synthesis.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/models/constants.py'>constants.py</a></b></td>
                <td>- The 'constants.py' file in the 'models' directory serves as a repository for instructions and guidelines used across the project<br>- It contains predefined instructions for various tasks such as creating AI analyst personas, conducting interviews, writing search queries, answering questions, and crafting different sections of a report<br>- These instructions are used to guide the behavior of different components within the system.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/models/models.py'>models.py</a></b></td>
                <td>- Models.py defines data models for the project, specifically the Analyst, Perspectives, and SearchQuery classes<br>- These classes represent an analyst's information, a collection of analysts, and a search query respectively<br>- They are crucial for data validation, serialization, and documentation in the project's architecture.</td>
            </tr>
            </table>
        </blockquote>
    </details>
    <details> <!-- utils Submodule -->
        <summary><b>utils</b></summary>
        <blockquote>
            <table>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/webSearchTool.py'>webSearchTool.py</a></b></td>
                <td>- WebSearchTool.py in the Langchain project serves as a utility for instantiating a web search tool<br>- It primarily supports the Tavily search tool, using an API key and a maximum result limit as parameters<br>- The code also includes error handling for incorrect or missing API keys.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/llms.py'>llms.py</a></b></td>
                <td>- The llms.py utility in the Langchain project serves to instantiate Language Learning Models (LLM) from either OpenAI or Google<br>- It validates the provided API keys, sets the model parameters, and handles exceptions, ensuring the correct and efficient operation of the chosen LLM within the broader codebase.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/analyst_utils.py'>analyst_utils.py</a></b></td>
                <td>- Analyst_utils.py contributes to the project by managing the creation of analysts and handling human feedback within the GenerateAnalystsState<br>- It enforces structured output, generates system messages, and determines the next node to execute based on the presence of human feedback<br>- It also plays a role in ending the process when necessary.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/interview_utils.py'>interview_utils.py</a></b></td>
                <td>- The 'interview_utils.py' module in the project serves as a utility for conducting simulated interviews<br>- It generates questions, searches the web and Wikipedia for relevant information, formulates answers, and saves the interview data<br>- It also routes messages between the question and answer phases and initiates all interviews in parallel using the Send API.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/writer_utils.py'>writer_utils.py</a></b></td>
                <td>- Writer_utils.py is a utility module in the project that focuses on generating various sections of a research report<br>- It includes functions to write individual sections, an introduction, a conclusion, and a final report based on the state of the research graph<br>- The module interacts with the language model to generate content and format it into a cohesive report.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/sidebar.py'>sidebar.py</a></b></td>
                <td>- The 'sidebar.py' module in the project creates a user interface sidebar for a web application powered by Langchain<br>- It allows users to select and configure language learning models (LLM) and web search tools from providers like OpenAI and Tavily<br>- The module also handles the input of API keys and other parameters for these services.</td>
            </tr>
            <tr>
                <td><b><a href='https://github.com/jeet-ss/researchAssistant_App.git/blob/master/utils/print_helpers.py'>print_helpers.py</a></b></td>
                <td>- Print_helpers.py, located in the utils directory, serves as a utility module for displaying analyst data<br>- It empties a given container and populates it with formatted information about each analyst, including their name, affiliation, role, and description<br>- A separate function for Streamlit integration is also defined but currently unimplemented.</td>
            </tr>
            </table>
        </blockquote>
    </details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with researchAssistant_App.git, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip


###  Installation

Install researchAssistant_App.git using one of the following methods:

**Build from source:**

1. Clone the researchAssistant_App.git repository:
```sh
❯ git clone https://github.com/jeet-ss/researchAssistant_App.git
```

2. Navigate to the project directory:
```sh
❯ cd researchAssistant_App.git
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```




###  Usage
Run researchAssistant_App.git using the following command:
**Using `streamlit`**  &nbsp;  [<img align="center" src="https://img.shields.io/badge/Streamlit-3776AB.svg?style={badge_style}&logo=streamlit&logoColor=white" />](https://streamlit.io/)

```sh
❯ python {entrypoint}
```



---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement Interview based Agents.</strike>
- [ ] **`Task 2`**: Implement Query Generator and Answer agent.


---

##  Contributing

- **💬 [Join the Discussions](https://github.com/jeet-ss/researchAssistant_App.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/jeet-ss/researchAssistant_App.git/issues)**: Submit bugs found or log feature requests for the `researchAssistant_App` project.
- **💡 [Submit Pull Requests](https://github.com/jeet-ss/researchAssistant_App.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/jeet-ss/researchAssistant_App.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/jeet-ss/researchAssistant_App.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=jeet-ss/researchAssistant_App.git">
   </a>
</p>
</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
