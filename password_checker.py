import streamlit as st
import re
import random
import string


def check_password_strength(password):
    strength = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Increase the length to 8 or more characters.")

    # Check for lowercase
    if any(char.islower() for char in password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check for uppercase
    if any(char.isupper() for char in password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check for digits
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        suggestions.append("Include some numbers.")

    # Check for special characters
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        suggestions.append("Use special characters like @, #, $.")

    return strength, suggestions


def generate_strong_password(base_password):
    while True:
        strong_password = list(base_password)

        if not any(char.islower() for char in strong_password):
            strong_password.append(random.choice(string.ascii_lowercase))

        if not any(char.isupper() for char in strong_password):
            strong_password.append(random.choice(string.ascii_uppercase))

        if not any(char.isdigit() for char in strong_password):
            strong_password.append(random.choice(string.digits))

        if not any(char in string.punctuation for char in strong_password):
            strong_password.append(random.choice(string.punctuation))

        if len(strong_password) < 8:
            strong_password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

        random.shuffle(strong_password)
        generated_password = ''.join(strong_password)

        if len(generated_password) >= 8:
            return generated_password


def main():
    st.title("🔐 Password Strength Checker & Generator")
    st.write("Enter a password to check its strength or generate a strong one!")

    user_password = st.text_input("Enter your password:", type="password")

    if st.button("Check Strength"):
        if user_password:
            strength, suggestions = check_password_strength(user_password)

            # Show Strength
            st.progress(strength * 20)

            if strength == 5:
                st.success("💪 Strong Password!")
            elif strength >= 3:
                st.warning("🟡 Medium Password. Improve further!")
            else:
                st.error("🔴 Weak Password! Needs significant improvements.")

            if suggestions:
                st.subheader("Suggestions to Improve:")
                for suggestion in suggestions:
                    st.write(f"- {suggestion}")

                # Generate Strong Password
                st.warning("⚠️ Your password is weak! Generating a stronger suggestion...")
                generated_password = generate_strong_password(user_password)
                st.info("💡 Suggested Strong Password:")
                st.write(f"**{generated_password}**")
                st.write("Select and press Ctrl+C to copy!")
        else:
            st.warning("Please enter a password to check!")


if __name__ == "__main__":
    main()