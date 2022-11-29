class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
      return max([sum(customer_data) for customer_data in accounts])