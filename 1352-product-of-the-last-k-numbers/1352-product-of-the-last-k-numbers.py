class ProductOfNumbers:
    def __init__(self):
        self.prefix_product = [1]  # Start with 1 for easy multiplication handling

    def add(self, num: int) -> None:
        if num == 0:
            # Reset prefix product list when zero is encountered
            self.prefix_product = [1]
        else:
            # Append the new cumulative product
            self.prefix_product.append(self.prefix_product[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_product):
            # If k is greater than or equal to the size of the list, a zero was added, so the product is 0
            return 0
        # Calculate product of the last k numbers
        return self.prefix_product[-1] // self.prefix_product[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)