def format_chat(messages):
    output = ""
    for m in messages:
        output += f"<|{m['role']}|>\n{m['content']}<|end|>\n"
    output += "<|assistant|>\n"
    return output

def format_for_training(messages):
    output = ""
    for m in messages:
        output += f"<|{m['role']}|>\n{m['content']}<|end|>\n"
    return output
