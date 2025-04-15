# Smart Property Assistant

A powerful AI assistant that helps with property-related tasks by detecting property issues from images and answering tenancy-related questions.

## Table of Contents
1. [Introduction](#introduction)
2. [Technologies Used](#technologies-used)
3. [Agent Logic and Switching](#agent-logic-and-switching)
4. [Image-Based Issue Detection](#image-based-issue-detection)
5. [Use Case Examples](#use-case-examples)
6. [Installation and Setup](#installation-and-setup)
7. [Contributing](#contributing)
8. [License](#license)

---

## Introduction

The **Smart Property Assistant** leverages AI-powered agents to provide two main services:

- **Agent 1 (Issue Detection)**: Analyzes property images to detect issues like damage, mold, cracks, etc.
- **Agent 2 (Tenancy FAQ)**: Answers tenancy-related questions, including rent laws, tenant rights, etc.

This assistant allows users to either upload images for property issue detection or ask text-based questions related to tenancy.

---

## Technologies Used

- **LangGraph**: A framework for creating agent-based workflows.
- **CustomAzureChatOpenAI**: A custom class for invoking Azure-based OpenAI models.
- **Streamlit**: A framework for building interactive UI applications.
- **Pillow (PIL)**: Python Imaging Library used for processing images.
- **Base64**: For encoding images to be passed to AI models in the form of base64 strings.

---

## Agent Logic and Switching

The routing logic uses an AI-based router to decide which agent (Agent 1 or Agent 2) should handle the request. The router decides based on two factors:

1. **Image Presence**: If an image is uploaded, it tries to determine whether the query involves visible issues with the property.
2. **Query Type**: If the query involves legal terms or tenancy rights, it switches to Agent 2, which handles tenancy-related FAQs.

If the input is unclear, the system asks clarifying questions to ensure the right agent is selected.

---

## Image-Based Issue Detection

Agent 1 (Property Issue Detection) uses image inputs to identify issues in properties. The uploaded image is encoded in base64 and passed to an AI model, which detects visible issues (such as cracks, mold, or damage) from the image. Additionally, the user may provide a textual description to provide context for the analysis.

---

## Use Case Examples

### Example 1: Property Issue Detection
- **Input**: Image of a wall with visible cracks + "What is wrong with the wall?"
- **Output**: "The wall has visible cracks. This may require repairs."

### Example 2: Tenancy FAQ
- **Input**: "What are the tenant rights regarding late payment in California?"
- **Output**: "In California, tenants have a 5-day grace period for late rent payments before eviction proceedings can start."

---

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/smart-property-assistant.git

2. Navigate to the project folder:
    ```bash
    cd propertyLoopAssessment

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Setup your .env file:
    # Azure OpenAI Configuration
    AZURE_OPENAI_ENDPOINT="https://your-azure-openai-endpoint.openai.azure.com"
    OPENAI_API_TYPE="azure"
    OPENAI_API_KEY="your-azure-openai-api-key"
    OPENAI_API_VERSION="2024-03-01-preview"  # Or your specific API version

    # Deployment Configuration
    DEPLOYMENT_NAME="your-deployment-name"
    MODEL_NAME="gpt-4"  # Or "gpt-4-32k", "gpt-35-turbo", etc.

    # App Specific
    USER_ID="your-username-or-id"


5. Run the Streamlit UI :
    ```bash
    streamlit run streamlitUI/streamlit_ui.py

6. Access the app in your browser.

## Contributing

1. Fork the repository.
    
2. Create a feature branch (`git checkout -b feature-name`).
    
3. Commit your changes (`git commit -am 'Add new feature'`).
    
4. Push to the branch (`git push origin feature-name`).
    
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
