
impl Solution {

    // O(n) time, n --> len(text),
    // O(1) space,
    // Approach: hash map, counting
    pub fn can_be_typed_words(text: String, broken_letters: String) -> i32 {
        let alphabet_count = 26;
        let mut broken_letters_map = vec![false;alphabet_count];

        for ch in broken_letters.chars() {
            let ascii = (ch as u8) as usize - 97;
            broken_letters_map[ascii] = true;
        }

        let mut typed_words = 0;
        let words: Vec<String> = text.split_whitespace().map(str::to_string).collect();
        for word in words {
            let mut can_be_typed = true;
            for ch in word.chars() {
                let ascii = (ch as u8) as usize - 97;
                if broken_letters_map[ascii] {
                    can_be_typed = false;
                    break;
                }
            }
            if can_be_typed {
                typed_words += 1;
            }
        }

        typed_words
    }
}
