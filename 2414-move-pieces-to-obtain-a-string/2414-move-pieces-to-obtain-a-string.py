class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove `_` and check the sequence of `L` and `R`
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Check valid moves for `L` and `R`
        start_pos = 0
        for i, char in enumerate(target):
            if char == 'L':
                # Find the next `L` in `start`
                while start_pos < len(start) and start[start_pos] != 'L':
                    start_pos += 1
                # Invalid if no `L` or position is incorrect
                if start_pos >= len(start) or start_pos < i:
                    return False
                start_pos += 1  # Move pointer forward
            
            elif char == 'R':
                # Find the next `R` in `start`
                while start_pos < len(start) and start[start_pos] != 'R':
                    start_pos += 1
                # Invalid if no `R` or position is incorrect
                if start_pos >= len(start) or start_pos > i:
                    return False
                start_pos += 1  # Move pointer forward
        
        return True