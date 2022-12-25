impl Solution {
    
    // O(nlogn + mlogm) time,
    // O(1) space,
    // Approach: two pointers, sorting, 
    pub fn match_players_and_trainers(mut players: Vec<i32>, mut trainers: Vec<i32>) -> i32 {
        players.sort();
        trainers.sort();
        
        let mut pairs = 0;
        let mut start = 0;
        for (i, player) in players.iter().enumerate() {
            while start < trainers.len() && trainers[start] < *player {
                start += 1;
            }
            
            if start < trainers.len() && trainers[start] >= *player {
                pairs += 1;
            }
            start += 1;
            if start >= trainers.len() {
                break;
            }
        }
        
        return pairs;
    }
}