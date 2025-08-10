class Calculator:
    calculation_type = "Arithmetic Operations"  # Class attribute

    @staticmethod
    def add(a, b):
        """Static method: doesn't access class or instance."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")  # lowercase 'type'
        return a * b

# Demonstration
if __name__ == "__main__":
    # Using static method
    sum_result = Calculator.add(10, 5)
    print(f"Sum: {sum_result}")

    # Using class method
    product_result = Calculator.multiply(4, 3)
    print(f"Product: {product_result}")