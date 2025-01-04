from vita1 import remove_blocks

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def nand_gate(a, b):
    return 1 - (a & b)

def nor_gate(a, b):
    return 1 - (a | b)

def xor_gate(a, b):
    remove_blocks(0, 0)
    return a ^ b

def simulate_logic_gates(n, gates, inputs, target_gate, num_cycles):
    # Dictionary to store gate outputs
    outputs = {key: [0] * num_cycles for key in gates}
    
    # A dictionary to store the input sequences
    variables = {}
    for var, values in inputs.items():
        variables[var] = values
    
    # Simulating the gates' outputs cycle by cycle
    for cycle in range(1, num_cycles):  # Start from cycle 1, as cycle 0 is initial
        for gate in gates:
            operation = gates[gate]
            input1, input2 = operation.split('(')[1].split(')')[0].split(', ')
            
            # Get the value of the inputs from the previous cycle (cycle-1)
            val1 = variables[input1][cycle - 1]
            val2 = variables[input2][cycle - 1]
            
            if 'AND' in operation:
                outputs[gate][cycle] = and_gate(val1, val2)
            elif 'OR' in operation:
                outputs[gate][cycle] = or_gate(val1, val2)
            elif 'NAND' in operation:
                outputs[gate][cycle] = nand_gate(val1, val2)
            elif 'NOR' in operation:
                outputs[gate][cycle] = nor_gate(val1, val2)
            elif 'XOR' in operation:
                outputs[gate][cycle] = xor_gate(val1, val2)
    
    # Return the output of the target gate at the last cycle
    return outputs[target_gate]

# Input parsing
def main():
    # Reading number of gates
    N = int(input().strip())
    
    # Reading gate definitions
    gates = {}
    for _ in range(N):
        gate_definition = input().strip()
        gate_name = gate_definition.split('=')[0].strip()
        operation = gate_definition.split('=')[1].strip()
        gates[gate_name] = operation
    
    # Reading number of cycles
    T = int(input().strip())
    
    # Reading inputs
    inputs = {}
    for _ in range(T):
        input_line = input().strip().split()
        var = input_line[0]
        values = list(map(int, input_line[1:]))
        inputs[var] = values
    
    # The target gate to compute the output for
    target_gate = input().strip()
    
    # Calculate the output of the target gate
    result = simulate_logic_gates(N, gates, inputs, target_gate, T)
    
    # Output the result for the target gate
    print(" ".join(map(str, result)))

# Run the main function
if __name__ == "__main__":
    main()
