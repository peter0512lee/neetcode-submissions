class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # 存索引，對應高度遞增
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            # i == n 時用高度 0 觸發清空堆疊
            cur = heights[i] if i < n else 0
            while stack and heights[stack[-1]] >= cur:
                h = heights[stack.pop()]
                # 寬度：左邊界為新的堆疊頂端（不含），右邊界為 i（不含）
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        return max_area