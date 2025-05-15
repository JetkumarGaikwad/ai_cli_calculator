import re

def calculate_expression(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression."

def parse_natural_language(query):
    query = query.lower()
    if "add" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        return f"{sum(numbers)}"
    elif "subtract" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        return f"{numbers[0] - numbers[1]}" if len(numbers) >= 2 else "Need two numbers."
    elif "multiply" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        result = 1
        for num in numbers:
            result *= num
        return f"{result}"
    elif "divide" in query:
        numbers = list(map(int, re.findall(r'\d+', query)))
        return f"{numbers[0] / numbers[1]}" if len(numbers) >= 2 and numbers[1] != 0 else "Invalid division."
    elif "%" in query or "percent" in query:
        match = re.search(r'(\d+)% of (\d+)', query)
        if match:
            return f"{(int(match.group(1)) * int(match.group(2))) / 100}"
    return "Couldn't understand the query."

def main():
    print("Welcome to AI-Powered CLI Calculator!")
    while True:
        query = input("\nEnter your expression or question (or 'exit' to quit): ")
        if query.lower() == "exit":
            break
        if any(x in query.lower() for x in ["add", "subtract", "multiply", "divide", "%", "percent"]):
            print("Result:", parse_natural_language(query))
        else:
            print("Result:", calculate_expression(query))

if __name__ == "__main__":
    main()
