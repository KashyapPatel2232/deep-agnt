def first_call(llm, question, system, max_tokens=100):
    """Ask one question. Return the text, the stop reason and the token counts."""
    output = llm.messages.create(system = system, messages = [{"role": "user", "content": question}], max_tokens = max_tokens)
    usage_input = output.usage.input_tokens
    usage_output = output.usage.output_tokens
    stop_reason = output.stop_reason
    text = output.text.strip()
    return {'text':text, 'stop_reason':stop_reason, 'input_tokens':usage_input,'output_tokens':usage_output}
