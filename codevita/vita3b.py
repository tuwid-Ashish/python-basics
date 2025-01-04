def max_worth_alternating(binary_string, worths):
    n = len(binary_string)
    stack = []  
    removed_worth = 0  

    for i in range(n):
        current_char = binary_string[i]
        current_worth = worths[i]

        if not stack:
            stack.append((current_char, current_worth))
        else:
            top_char, top_worth = stack[-1]
            if top_char != current_char:
                stack.append((current_char, current_worth))
            else:
                if current_worth > top_worth:
                    removed_worth += top_worth
                    stack.pop()
                    stack.append((current_char, current_worth))
                else:
                    removed_worth += current_worth

    total_worth_stack = sum(w for _, w in stack)
    total_worth_input = sum(worths)

    removed_worth = total_worth_input - total_worth_stack
    return removed_worth


binary_string = input().strip()
worths = list(map(int, input().strip().split()))

result = max_worth_alternating(binary_string, worths)
print(result)

# resolved  