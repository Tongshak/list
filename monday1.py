# Define your system
candidates = {}
voters = []

def register_candidates(*args):
    for name in args:
        candidates[name] = 0

def cast_vote(voter_id, candidate):
    if voter_id in voters:
        return "You have already voted."
    if candidate not in candidates:
        return "Candidate not found."

    candidates[candidate] += 1
    voters.append(voter_id)
    return f"Vote casted for {candidate}."

def election_result():
    if not candidates:
        return "No candidates registered."

    max_votes = max(candidates.values())
    winners = []

    for name in candidates:
        if candidates[name] == max_votes:
            winners.append(name)

    return {
        "winners": winners,
        "candidates": candidates
    }

# Test the code
register_candidates("Alice", "Bob", "Charlie")
print(cast_vote("voter1", "Alice"))
print(cast_vote("voter2", "Bob"))
print(cast_vote("voter1", "Charlie"))  # Already voted
print(cast_vote("voter3", "Alice"))
print(election_result())

