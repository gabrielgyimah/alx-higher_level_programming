#!/usr/bin/python3

def safe_print_division(a, b):
    ans = 0

    try:
        ans = a / b
        return ans

    except Exception:
        ans = None
        return ans

    finally:
        print("Inside result: {}".format(ans))
        return ans
