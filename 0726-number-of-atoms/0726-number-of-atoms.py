class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        import re
        
        def parse_formula(formula):
            n = len(formula)
            stack = [defaultdict(int)]
            i = 0
            while i < n:
                if formula[i] == '(':
                    stack.append(defaultdict(int))
                    i += 1
                elif formula[i] == ')':
                    i += 1
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    multiplier = int(formula[i_start:i] or 1)
                    top = stack.pop()
                    for elem, cnt in top.items():
                        stack[-1][elem] += cnt * multiplier
                else:
                    i_start = i
                    i += 1
                    while i < n and formula[i].islower():
                        i += 1
                    elem = formula[i_start:i]
                    i_start = i
                    while i < n and formula[i].isdigit():
                        i += 1
                    cnt = int(formula[i_start:i] or 1)
                    stack[-1][elem] += cnt
            return stack[0]
        
        atom_counts = parse_formula(formula)
        result = ""
        for atom in sorted(atom_counts.keys()):
            result += atom + (str(atom_counts[atom]) if atom_counts[atom] > 1 else "")
        return result

# Example Usage
solution = Solution()
print(solution.countOfAtoms("H2O"))       # Output: "H2O"
print(solution.countOfAtoms("Mg(OH)2"))   # Output: "H2MgO2"
print(solution.countOfAtoms("K4(ON(SO3)2)2"))  # Output: "K4N2O14S4"
