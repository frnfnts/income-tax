import matplotlib.pyplot as plt


def get_tax_rate(tax):
    if tax < 1000:
        return (0, 0)
    elif tax < 1950000:
        return (0.05, 0)
    elif tax < 3300000:
        return (0.1, 97500)
    elif tax < 6950000:
        return (0.2, 427500)
    elif tax < 9000000:
        return (0.23, 636000)
    elif tax < 18000000:
        return (0.33, 1536000)
    elif tax < 40000000:
        return (0.40, 2796000)
    else:
        return (0.45, 4796000)


def calculate_tax(income):
    tax_rate, deduction = get_tax_rate(income)
    return income * tax_rate - deduction


income = range(1000, 45000000, 1000)
tax = [i - calculate_tax(i) for i in income]

plt.plot(income, income)
plt.plot(income, tax)
# plt.yscale('log')
# plt.xscale('log')
plt.grid(which='major', color='black', linestyle='-')
plt.grid(which='minor', color='black', linestyle='-')
plt.show()

# print(calculate_tax(330 * 10000) / 10000)
# print(calculate_tax(331 * 10000) / 10000)
# print(calculate_tax(889 * 10000) / 10000)
# print(calculate_tax(900 * 10000) / 10000)
