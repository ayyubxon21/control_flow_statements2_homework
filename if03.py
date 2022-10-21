def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>=b>=c:
        return b
    if b>=a>=c:
        return a
    if c>=a>=b:
        return a
    if a>=c>=b:
        return c
    if c>=b>=a:
        return b
print(main(5,6,3))
