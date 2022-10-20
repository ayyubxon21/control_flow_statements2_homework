def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = n%10
    b = n//10%10
    c = n//100//10%10
    d = n//1000%10
    e = n//10000
    return max(a,b,c,d,e)
print(main(13245))