from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    if request.method == 'POST':
        # Get parameters from the form
        length = int(request.form.get('length', 12))
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_numbers = 'numbers' in request.form
        use_special_characters = 'special_characters' in request.form
        avoid_ambiguous = 'avoid_ambiguous' in request.form

        # Get words input by the user
        words = request.form.get('words', '').split()

        # Generate password based on parameters
        password = generate_password_with_parameters(length, use_uppercase, use_lowercase, use_numbers, use_special_characters, avoid_ambiguous, words)
    
        return render_template('index.html', password=password)
    


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    if request.method == 'POST':
        # Get parameters from the form
        length = int(request.form.get('length', 12))
        use_uppercase = 'uppercase' in request.form
        use_lowercase = 'lowercase' in request.form
        use_numbers = 'numbers' in request.form
        use_special_characters = 'special_characters' in request.form
        avoid_ambiguous = 'avoid_ambiguous' in request.form

        # Get words input by the user
        words = request.form.get('words', '').split()

        # Generate password based on parameters
        generated_password = generate_password_with_parameters(length, use_uppercase, use_lowercase, use_numbers, use_special_characters, avoid_ambiguous, words)

        # Check the strength of the generated password
        strength = password_strength(generated_password)

        return render_template('index.html', password=generated_password, strength=strength)

def generate_password_with_parameters(length, use_uppercase, use_lowercase, use_numbers, use_special_characters, avoid_ambiguous, words):
    # Define character sets
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation

    # For removing ambiguous characters if specified
    if avoid_ambiguous:
        characters = characters.translate(str.maketrans('', '', '1l0O'))

    # Check if there are characters available for password generation
    if not characters:
        return "Error: Please select at least one character type for password generation."

    # Generate the random password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # Add words if specified by the user
    if words:
        password = ' '.join(words) + ' ' + password

    return password

def password_strength(password):
    # Define a simple strength metric
    strength = 0

    # Check for the presence of different character types
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in string.punctuation for char in password):
        strength += 1

    # Increase strength if length is above a certain threshold
    if len(password) >= 12:
        strength += 1

    return strength

if __name__ == '__main__':
    app.run(debug=True)

