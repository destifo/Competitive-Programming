use rand::Rng;
use std::collections::HashMap;


struct Codec {
	encodings: HashMap<String, String>, // (original_site, encoding)
    reverse_encodings: HashMap<String, String>, // (encoding, orignal site)
    domain: String
}

/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Self {
            encodings: HashMap::new(),
            reverse_encodings: HashMap::new(),
            domain: "http://leetcode.com".to_string()
        }
    }
    
    fn generate_unique_string(&self) -> String {
        let choices: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890".chars().collect();
        
        let mut rng = rand::thread_rng();
        let mut rand_str = "".to_string();
        for i in 0..9 {
            let rand_index = rng.gen_range(0, choices.len()) as usize;
            rand_str.push(choices[rand_index]);
        }
        
        rand_str
    }
	
    // Encodes a URL to a shortened URL.
    fn encode(&mut self, longURL: String) -> String {
        let mut short_tail = self.generate_unique_string();
        let mut short_url = format!("{}/{}", self.domain, short_tail);
        while self.reverse_encodings.contains_key(&short_url) {
            short_tail = self.generate_unique_string();
            short_url = format!("{}/{}", self.domain, short_tail);
        }
        
        self.encodings.insert(longURL.clone(), short_url.clone());
        self.reverse_encodings.insert(short_url.clone(), longURL.clone());
        
        short_url
    }
	
    // Decodes a shortened URL to its original URL.
    fn decode(&self, shortURL: String) -> String {
        self.reverse_encodings.get(&shortURL).unwrap().to_string()
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let s: String = obj.encode(strs);
 * let ans: VecVec<String> = obj.decode(s);
 */