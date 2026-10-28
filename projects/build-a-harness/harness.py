def tool_spec(name, description, properties=None, required=None):
    if properties is None:
        properties = {}

    if required is None:
        required = []

    input_schema = {'type':'object', 'properties':properties, 'required': required}
    return {'name':name, 'description':description, 'input_schema':input_schema}
