
### Generic stack data structure ###
class Stack:

    def __init__(self, size=100):
        self.stack = [None] * size
        self.top = -1
        self.size = size

    def is_empty(self):
        return self.top == -1
    

    def push(self, item):
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        item = self.stack[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        return self.stack[self.top]
    

### uses two stacks -- one for number and one for symbols ###
## the evaluate_expression method parses the input expression and evaluates it using the stack-based algorithm
class ExpressionEvaluator:

    def __init__(self):
        self.num_stack = Stack()
        self.symbol_stack = Stack()


    def evaluate_expression(self, expression):
        for i in range(len(expression)):

            # is the current character a number?
            if expression[i].isdigit():
                num = 0

                # while loop runs until reaching the end of that number (ex. a multiple-digit number like 100)
                while i < len(expression) and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                i -= 1
                self.num_stack.push(num)

            # otherwise the current character is a symbol
            else:
                # continues to evaluate symbols at the top of the symbol stack while the symbol stack is not empty
                # and the priority of the current symbol is less than or equal to the priority of the symbol at the top of the stack
                while not self.symbol_stack.is_empty() and self.priority(expression[i]) <= self.priority(self.symbol_stack.peek()):
                    self.evaluate_top()
                self.symbol_stack.push(expression[i])
                # once all symbols with higher priority are evaluated, the current symbol is pushed onto the symbol stack

        
        # after iterating through all the characters in the expression, ensure that any remaining symbols on the symbol stack are evaluated
        while not self.symbol_stack.is_empty():
            self.evaluate_top()

        # return the result of the expression, which is the top element of the number stack
        return self.num_stack.peek()
    

    def priority(self, symbol):
        if symbol in '()+-':
            return 1
        elif symbol in '*/':
            return 2
        return 0


    def evaluate_top(self):
        operator = self.symbol_stack.pop()
        num2 = self.num_stack.pop()
        num1 = self.num_stack.pop()
        if operator == '+':
            self.num_stack.push(num1 + num2)
        elif operator == '-':
            self.num_stack.push(num1 - num2)
        elif operator == '*':
            self.num_stack.push(num1 * num2)
        elif operator == '/':
            self.num_stack.push(num1 / num2)


class Calculator:

    def main(self):
        print("Enter the expression (no blank, no decimals): ")
        expression = input()
        evaluator = ExpressionEvaluator()
        result = evaluator.evaluate_expression(expression)
        print("The result is:", result)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()