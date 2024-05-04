way = input("Do You Want Every Word To Be Capitalized (Yes/No):  ")

if way.lower() == "yes":    

    def capitalize_sentences(input_text):
        sentences = input_text.split(' ')  # Split input into sentences based on periods followed by a space
        processed_sentences = [sentence.capitalize() for sentence in sentences]
        formatted_text = ' '.join(processed_sentences)  # Join the processed sentences back together
        return formatted_text

    # Example usage
    input_text = input("Enter multiple sentences: ")
    formatted_output = capitalize_sentences(input_text)
    print(formatted_output)

if way.lower() == "no":
    def capitalize_sentences(input_text):
        sentences = input_text.split('. ')  # Split input into sentences based on periods followed by a space
        processed_sentences = [sentence.capitalize() for sentence in sentences]
        formatted_text = '. '.join(processed_sentences)  # Join the processed sentences back together
        return formatted_text


    # Example usage
    input_text = input("Enter multiple sentences: ")
    formatted_output = capitalize_sentences(input_text)
    print(formatted_output)