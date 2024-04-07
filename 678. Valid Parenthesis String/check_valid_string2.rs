impl Solution {
    // O(n) time,
    // O(1) space,
    // Approach: greedy,
    pub fn check_valid_string(s: String) -> bool {
        let (mut left_min, mut left_max) = (0, 0);

        for ch in s.chars() {
            match ch {
                '(' => {
                    left_min += 1;
                    left_max += 1
                }
                ')' => {
                    left_min -= 1;
                    left_max -= 1
                }
                _ => {
                    left_min -= 1;
                    left_max += 1
                }
            }

            if left_max < 0 {
                return false;
            }
            if left_min < 0 {
                left_min = 0;
            }
        }

        left_min == 0
    }
}
