"""
Output power calculator for a microwave network.

Network rules:
  - Power divider: one input node, multiple output nodes → power split equally.
  - Power combiner: multiple input nodes, one output node → powers summed.
  - Microwave device: one input, one output, transmission coefficient Γ ∈ [0,1].
      P_out = Γ * P_in

The network is read from a .txt file where each line has:
    input_node, output_node, gamma

Algorithm (O(n)):
  1. Parse all edges.
  2. Find the network input node (no device feeds into it) and
     output node (no device takes from it).
  3. Propagate power from the input node toward the output using
     a topological BFS/DFS on the implicit DAG of nodes.
     - When a node has multiple incoming edges (combiner), we wait
       until all contributors have been resolved before proceeding.
     - When a node has multiple outgoing edges (divider), each
       outgoing device gets power / number_of_outputs.
"""

from collections import defaultdict, deque


def output_power(network_file, input_power):
    """
    Calculate the output power of a microwave network.

    Parameters
    ----------
    network_file : str
        Path to the .txt file describing the network.
    input_power : float
        Power level at the network input (>= 0).

    Returns
    -------
    float
        Power level at the network output.
    """
    edges = []

    with open(network_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            in_node  = int(parts[0].strip())
            out_node = int(parts[1].strip())
            gamma    = float(parts[2].strip())
            edges.append((in_node, out_node, gamma))

    outgoing = defaultdict(list)
    in_degree = defaultdict(int)
    all_out_nodes = set()
    all_in_nodes  = set()

    for in_node, out_node, gamma in edges:
        outgoing[in_node].append((out_node, gamma))
        in_degree[out_node] += 1
        all_out_nodes.add(out_node)
        all_in_nodes.add(in_node)

    all_nodes = all_in_nodes | all_out_nodes

    input_nodes  = all_in_nodes  - all_out_nodes
    output_nodes = all_out_nodes - all_in_nodes

    network_in  = next(iter(input_nodes))
    network_out = next(iter(output_nodes))

    node_power = defaultdict(float)
    node_power[network_in] = input_power

    remaining = dict(in_degree)

    queue = deque([network_in])

    while queue:
        node = queue.popleft()
        p_node = node_power[node]
        successors = outgoing[node]

        if not successors:
            continue

        power_per_device = p_node / len(successors)

        for next_node, gamma in successors: 
            node_power[next_node] += gamma * power_per_device

            remaining[next_node] -= 1
            if remaining[next_node] == 0:
                queue.append(next_node)

    return node_power[network_out]

if __name__ == "__main__":
    import os
    import time

    net1 = "test_network1.txt"
    with open(net1, "w") as f:
        f.write("11, 8, 0.5\n")
        f.write("3, 11, 0.5\n")
        f.write("11, 1, 0.5\n")
        f.write("3, 8, 0.5\n")
        f.write("8, 1, 0.5\n")

    result1 = output_power(net1, 100.0)
    print(f"Test 1 result: {result1:.4f}  (expected 21.875)")
    os.remove(net1)

    net2 = "test_network2.txt"
    with open(net2, "w") as f:
        f.write("0, 1, 0.75\n")

    result2 = output_power(net2, 200.0)
    print(f"Test 2 result: {result2:.4f}  (expected 150.0)")
    os.remove(net2)

    net3 = "test_network3.txt"
    with open(net3, "w") as f:
        for i in range(10):
            f.write(f"{i}, {i+1}, 0.9\n")

    start = time.perf_counter()
    result3 = output_power(net3, 1000.0)
    elapsed = time.perf_counter() - start
    expected3 = 1000.0 * (0.9 ** 10)
    print(f"Performance test (10 devices): {result3:.6f}  "
          f"(expected {expected3:.6f}), time={elapsed:.4f}s")
    os.remove(net3)