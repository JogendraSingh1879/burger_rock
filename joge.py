import streamlit as st

st.title('Jogendras First Apply')
st.image("burger gif.gif")

import random
import streamlit as st

# Title of the app
st.title("Rock, Paper, Scissors Game")

# Instructions
st.write("Choose Rock, Paper, or Scissors to play against the computer!")

# Options for the user
user_choice = st.selectbox("Make your choice:", ["Rock", "Paper", "Scissors"])

# Function to determine winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "Computer wins!"

# When the user clicks the button, the game is played
if st.button("Play"):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.write(f"Your choice: {user_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    st.write(result)
