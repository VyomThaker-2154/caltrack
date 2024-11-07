import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import matplotlib.pyplot as plt

load_dotenv()

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

def get_calorie_response(user_input):
    
    inputs_outputs = [
        "input: apple", "output: 52 calories gained",
        "input: banana", "output: 89 calories gained",
        "input: running 30 minutes", "output: 300 calories burned",
        "input: yoga 1 hour", "output: 200 calories burned",
        "input: pizza slice", "output: 285 calories gained",
        "input: cycling 1 hour", "output: 500 calories burned",
        "input: orange", "output: 62 calories gained",
        "input: grapes 100g", "output: 69 calories gained",
        "input: walking 1 hour", "output: 200 calories burned",
        "input: swimming 30 minutes", "output: 250 calories burned",
        "input: chocolate bar", "output: 210 calories gained",
        "input: fried chicken", "output: 400 calories gained",
        "input: carrot", "output: 41 calories gained",
        "input: spinach", "output: 23 calories gained",
        "input: weightlifting 30 minutes", "output: 180 calories burned",
        "input: steak", "output: 500 calories gained",
        "input: salad with dressing", "output: 150 calories gained",
        "input: running 1 hour", "output: 600 calories burned",
        "input: muffin", "output: 250 calories gained",
        "input: avocado", "output: 160 calories gained",
    ]

    inputs_outputs.append(f"input: {user_input}")
    inputs_outputs.append("output: ") 

    response = model.generate_content(inputs_outputs)

    return response.text

def suggest_exercise(current_calories):
    
    exercises = [
        ("running", 600),
        ("cycling", 500),
        ("swimming", 250),
        ("yoga", 200),
        ("walking", 200),
        ("weightlifting", 180),
        ("jump rope", 700),
        ("hiking", 400),
        ("dancing", 300),
    ]

    suggested_exercises = []
    
    
    for exercise, calories_burned in exercises:
        
        if calories_burned <= current_calories:
            
            duration = round(current_calories / calories_burned * 60)
            if duration > 5:  
                suggested_exercises.append(f"Do {exercise} for {duration} minutes to burn {current_calories} calories.")
    
    
    if not suggested_exercises:
        suggested_exercises.append(f"Do {exercises[0][0]} for {round(current_calories / exercises[0][1] * 60)} minutes.")  # First exercise in list

    return suggested_exercises


def main():
    
    st.title("Calorie Tracker")
    st.write("Track your calorie intake/expenditure and get exercise suggestions.")

    
    if 'current_calories' not in st.session_state:
        st.session_state.current_calories = 0  

    
    user_input = st.text_input("Enter food or exercise performed:", "")

   
    if user_input:
        
        response = get_calorie_response(user_input)
        st.write(f"Response: {response}\n")

        calorie_info = [word for word in response.split() if word.isdigit()]

        if calorie_info:
            calories = int(calorie_info[0])

            if "burned" in response:
                
                st.session_state.current_calories -= calories
                st.write(f"You have burned {calories} calories. Updated daily calorie count: {st.session_state.current_calories} calories.")
            elif "gained" in response:
                
                st.session_state.current_calories += calories
                st.write(f"You have gained {calories} calories. Updated daily calorie count: {st.session_state.current_calories} calories.")
        else:
            st.write("No calorie data found in the response. Please try again.")

        
        st.write(f"Your current daily calorie count: {st.session_state.current_calories} calories\n")

        
        if st.session_state.current_calories > 0:
            st.write(f"Suggested exercises to burn {st.session_state.current_calories} calories:")
            exercises = suggest_exercise(st.session_state.current_calories)
            for exercise in exercises:
                st.write(f"- {exercise}")
        elif st.session_state.current_calories < 0:
            st.write(f"Your daily calorie target is overshot by {-st.session_state.current_calories} calories. You might want to consider reducing intake.")
        else:
            st.write("You have reached your daily calorie target!")

    
    st.write("## Calorie Intake/Expenditure Over Time")
    if 'calories_history' not in st.session_state:
        st.session_state.calories_history = [st.session_state.current_calories]
        st.session_state.time_steps = [0]

    st.session_state.calories_history.append(st.session_state.current_calories)
    st.session_state.time_steps.append(len(st.session_state.time_steps))

    fig, ax = plt.subplots()
    ax.plot(st.session_state.time_steps, st.session_state.calories_history, label="Calories", color="blue")
    ax.set_xlabel("Time Steps")
    ax.set_ylabel("Calories")
    ax.set_title("Calorie Intake/Expenditure Over Time")
    ax.legend()
    
    st.pyplot(fig)

if __name__ == "__main__":
    main()
