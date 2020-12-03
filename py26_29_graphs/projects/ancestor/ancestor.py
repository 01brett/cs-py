def get_parents(data, target):
    parents = []

    for relations in data:
        parent, child = relations[0], relations[1]

        if child == target:
            parents.append(parent)

        if len(parents) == 2:
            break

    if len(parents) > 0:
        parents.sort(reverse=True)
        return parents

    return None


def earliest_ancestor(ancestors, starting_node):
    q = []
    q.append(starting_node)

    ans = -1

    while len(q) > 0:
        node = q.pop(0)

        parents = get_parents(ancestors, node)

        if parents:
            for parent in parents:
                q.append(parent)
        else:
            if node == starting_node:
                break

            ans = node

    return ans