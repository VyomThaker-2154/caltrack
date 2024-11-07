# Calorie Tracker

A web application that tracks calorie intake and expenditure while providing personalized exercise suggestions. Built using Streamlit, Google Generative AI, and Matplotlib.

## Features

- **Calorie Tracking**: Log calories from food intake and calories burned through various exercises.
- **Exercise Suggestions**: Receive personalized exercise recommendations based on your calorie balance to help burn excess calories.
- **Calorie Trends**: Visualize changes in your daily calorie balance over time with an interactive, real-time graph.

## Technologies Used

- **Streamlit**: For building the web interface.
- **Google Gemini API (Generative AI)**: To process and provide calorie-related data.
- **Matplotlib**: For generating visualizations.
- **Python**: Core language for development.
- **dotenv**: To manage environment variables securely.

## Setup Instructions

### Prerequisites

- Python 3.x installed
- Install dependencies by running the following command in your terminal:

   ```bash
   pip install streamlit google-generativeai matplotlib python-dotenv
   ```

### Configuration

1. Create a `.env` file in the project directory to store your API key:

   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

2. Launch the application:

   ```bash
   streamlit run app.py
   ```

## Usage Guide

1. Enter a food item or exercise (e.g., "apple", "running 30 minutes") in the app interface.
2. View the calorie information associated with your input.
3. Track your daily calorie balance.
4. Receive exercise recommendations to reach your calorie goals.
5. Explore your calorie intake/expenditure trends on the interactive graph.

## Example Inputs and Outputs

- **Input**: `apple`
  - **Output**: `52 calories gained`
  
- **Input**: `running 30 minutes`
  - **Output**: `300 calories burned`

## Code Overview

- **`get_calorie_response(user_input)`**: Determines calorie intake or expenditure based on user input.
- **`suggest_exercise(current_calories)`**: Provides exercise suggestions to offset a specified number of calories.
- **`main()`**: Manages the Streamlit interface, handles inputs, updates calorie counts, and displays the calorie graph.

## Project Structure

```
Calorie-Tracker/
├── .env               # Environment file containing API keys
└── fine_tune.py       # Main application file
```

## Contributing

To contribute, fork the repository, create a branch for your feature or fix, and submit a pull request. Contributions are welcome!
