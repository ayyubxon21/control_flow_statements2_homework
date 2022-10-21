def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    return  max(n%10,n//10%10,n//1000%10,n//10000,(n//100%10))
print(main(12345))