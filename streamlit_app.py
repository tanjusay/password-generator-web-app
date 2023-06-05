import random
import streamlit as st


def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special):
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = lowercase_letters.upper()
    numbers = "1234567890"
    special_characters = "@#$&%<>"

    character_set = ""
    
    if use_lowercase:
        character_set += lowercase_letters
    if use_uppercase:
        character_set += uppercase_letters
    if use_numbers:
        character_set += numbers
    if use_special:
        character_set += special_characters
    
    password = "".join(random.sample(character_set, length))
    
    return password


def colorize_password(password):
    colorized_password = ""
    
    for char in password:
        if char.isdigit():
            colorized_password += f"<span style='color: red;'>{char}</span>"
        elif char in ["@", "#", "$", "&", "%", "<", ">"]:
            colorized_password += f"<span style='color: green;'>{char}</span>"
        else:
            colorized_password += char
    
    return colorized_password


def main():
    st.set_page_config(page_title="Password Generator")
    st.header("🎲 Password Generator")

    length = st.slider("Password Length", min_value=8, max_value=20, step=1, value=12)
    use_lowercase = st.checkbox("Include Lowercase Letters")
    use_uppercase = st.checkbox("Include Uppercase Letters")
    use_numbers = st.checkbox("Include Numbers")
    use_special = st.checkbox("Include Special Characters")
    
    if st.button("Generate Password"):
        password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special)
        colorized_password = colorize_password(password)
        st.markdown(f"Generated Password: <h5>{colorized_password}</h5>", unsafe_allow_html=True)
    

if __name__ == "__main__":
    main()
