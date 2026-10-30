class Chat:
    """A conversation with a model."""

    def __init__(self, llm, system):
        self.llm = llm
        self.system = system
        self.messages = []

    def send(self, text):
        """Send a message with conversation history and return the model's reply."""
        user_message = {"role": "user", "content": text}
        request_messages = [*self.messages, user_message]

        response = self.llm.messages.create(
            messages=request_messages,
            system=self.system,
            max_tokens=300,
        )

        assistant_message = {"role": "assistant", "content": response.text}
        self.messages.extend([user_message, assistant_message])
        return response.text
