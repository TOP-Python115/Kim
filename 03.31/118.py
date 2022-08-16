words = [w.lower().strip('.,!?;:-"') for w in input().split()]
print('Yes' if words == words[::-1] else 'No')

# Herb the sage eats sage, the herb
# Yes

# Herb the sage eats sage, the herbal
# No
