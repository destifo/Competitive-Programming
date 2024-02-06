use std::collections::HashMap;


fn serialize(chars: Vec<char>) -> String {
    let mut count: HashMap<char, i32> = HashMap::new();
    
    for ch in chars {
        let mut prev_count = 0;
        if let Some(cnt) = count.get(&ch) {
            prev_count = *cnt;
        }
        count.insert(ch, prev_count+1);
    }
    
    let mut sorted_keys: Vec<char> = count.keys().cloned().collect();
    sorted_keys.sort();
    
    let mut str_builder: Vec<String> = vec![];
    for k in sorted_keys {
        let curr_count = *count.get(&k).unwrap();
        str_builder.push(k.to_string());
        str_builder.push(curr_count.to_string());
    }
    
    str_builder.join("")
}



impl Solution {
    
    // O(n) time, n -> sum(str) for str in strs,
    // O(1) space,
    // Approach: hash map, 
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut answer: Vec<Vec<String>> = vec![];
        let mut serialized_index: HashMap<String, usize> = HashMap::new();
        
        
        for s in strs {
            let chars: Vec<char> = s.chars().collect();
            let serialized_str = serialize(chars);
            if let Some(index) = serialized_index.get(&serialized_str) {
                answer[*index].push(s);
            } else {
                let index = answer.len();
                serialized_index.insert(serialized_str, index);
                answer.push(vec![s]);
            }
        }
        
        answer     
    }
}