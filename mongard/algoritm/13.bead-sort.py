"""
- bead-sort
    * یک لیست نامرتب را گرفته و آیتم‌های داخل آن را مرتب میکند.

"""

def bead_sort(seq):
    if any(not isinstance(x, int) or x<0 for x in seq):
        raise TypeError

    for _ in range(len(seq)):
        for i, (rod_upper, rod_lower) in enumerate(zip(seq, seq[1:])):
            print(i, (rod_upper, rod_lower))
            if rod_upper > rod_lower:
                # seq[i] -= rod_upper - rod_lower
                # seq[i+1] += rod_upper - rod_lower
                seq[i], seq[i+1] = seq[i+1], seq[i]

    return seq

print(bead_sort([5, 4, 6, 2, 1]))
