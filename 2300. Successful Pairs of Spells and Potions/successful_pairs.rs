impl Solution {
    
    fn find_above_success(spell: i32, success: i64, potions: &Vec<i32>) -> i32 {
        let mut answer = potions.len() as i32;
        let mut lo = 0;
        let mut hi = answer-1;
        
        while lo <= hi {
            let mid = ((lo+hi)/2) as usize;
            let combo = potions[mid] as i64 * spell as i64;
            
            if combo >= success {
                answer = mid as i32;
                hi = answer-1;
            } else {
                lo = (mid+1) as i32;
            }
        }
        
        return answer;
    }
    
    
    // O(nlogm + mlogm) time, n --> len(spells), m --> len(potions),
    // O(n) space,
    // Approach: binary search, sorting, 
    pub fn successful_pairs(spells: Vec<i32>, potions: Vec<i32>, success: i64) -> Vec<i32> {
        let mut pairs = vec![0; spells.len()];
        let mut potions = potions;
        potions.sort();
        for (i, spell) in spells.iter().enumerate() {
            pairs[i] = potions.len() as i32 - Solution::find_above_success(*spell, success, &potions);
        }
        
        return pairs;
    }
}