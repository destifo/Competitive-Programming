impl Solution {
    // O(n) time,
    // O(n) space,
    // Approach: stack,
    pub fn make_good(s: String) -> String {
        let mut stack: Vec<char> = vec![];

        for letter in s.chars() {
            if let Some(top) = stack.last() {
                if top.is_uppercase() {
                    if top.to_ascii_lowercase() == letter {
                        stack.pop();
                        continue;
                    }
                } else if top.is_lowercase() {
                    if top.to_ascii_uppercase() == letter {
                        stack.pop();
                        continue;
                    }
                }
            }
            stack.push(letter);
        }

        let ans: String = stack.iter().collect();
        ans
    }
}
