constantNum = int(input("num: "))
result = constantNum
while (True):
    op = input("operator(+ - * / =)")
    if (op == "="):
        break
    if op not in ["+", "-", "*", "/"]:
        print("Invalid operator. Please enter +, -, *, /, or =")
        continue  # invalid giriş olursa tekrar başa dön
    num = int(input("number:"))
    if (op == "-"):
        result -= num
    elif (op == "*"):
        result *= num
    elif (op == "/"):
        result /= num
    elif (op == "+"):
        result += num
print(result)