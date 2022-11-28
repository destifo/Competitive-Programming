use std::collections::HashMap;

impl Solution {
    
    // O(nlogn) time,
    // O(n) space,
    // Approach: hashtable, sorting, 
    pub fn find_winners(matches: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
      
        let mut no_loss = Vec::new();
        let mut one_loss = Vec::new();
        
        let mut player_loss: HashMap<i32, i32> = HashMap::new();
        
        for result in matches {
            
            let loser = result[1];
            let winner = result[0];
            
            let mut lost_matches = 0;
            
            if !player_loss.contains_key(&winner) {
                player_loss.insert(winner, 0);
            }
            
            if player_loss.contains_key(&loser) {
                lost_matches = *player_loss.get(&loser).unwrap_or(&0);
            }
            
            lost_matches += 1;
            player_loss.insert(loser, lost_matches); 
        }
        
        
        for (player, losses) in &player_loss {
            
            if *losses == 1 {
                one_loss.push(*player);
            }
            else if *losses == 0 {
                no_loss.push(*player);
            }
            
        }
        
        no_loss.sort();
        one_loss.sort();
        return vec![no_loss, one_loss];
    }
}