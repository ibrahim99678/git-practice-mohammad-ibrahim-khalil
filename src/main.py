import datetime
import utils

def main():
    print("Name: Mohamamd Ibrahim khalil")
    print(f"Todays Date: {datetime.date.today()}")

    print(f"Addition: {utils.add(10, 5)}")
    print(f"Subtraction: {utils.subtract(15, 5)}")
    print(f"Multiplication: {utils.multiply(10, 5)}")

    try:
        print(f"10 / 0 = {utils.divide(10, 0)}")
    except ValueError as e:
        print(f"Error handling test: {e}")

if __name__ == "__main__":
    main()

