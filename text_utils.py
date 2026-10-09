# text_utils.py - A module containing reusable string manipulation functions
def truncate_text(text, max_length=20):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def slugify(text):
    return text.lower().strip().replace(" ", "-")

if __name__ == "__main__":
    print("Testing text_utils functions directly...")
    print(truncate_text("Hello, welcome to Python development!", 15))
    print(slugify("Hello World From Python"))