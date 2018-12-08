for a in range(10):
    for b in range(20):
        if something(a, b):
            # Break the inner loop...
            break
    else:
        # Continue if the inner loop wasn't broken.
        continue
    # Inner loop was broken, break the outer.
    break