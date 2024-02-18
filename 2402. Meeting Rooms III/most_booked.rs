use std::collections::BinaryHeap;
use std::cmp::Reverse;


impl Solution {
    
    // O(nlogn + m) time, m -> len(meetings)
    // O(n) space,
    // Approach: heap, greedy, 
    pub fn most_booked(n: i32, mut meetings: Vec<Vec<i32>>) -> i32 {
        let mut meeting_held = vec![0;n as usize];
        let mut available_rooms: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        for i in 0..n {
            available_rooms.push(Reverse(i));
        }
        let mut next_ending: BinaryHeap<Reverse<(i64, i32)>> = BinaryHeap::new();
        
        meetings.sort();
        
        for meeting in meetings {
            let start = meeting[0] as i64;
            let end = meeting[1] as i64;
            
            while let Some(Reverse((end_time, room))) = next_ending.peek() {
                if *end_time <= start {
                    if let Some(Reverse((end_time, room))) = next_ending.pop() {
                    available_rooms.push(Reverse(room));
                    }
                } else {
                    break;
                }
            }
            
            if let Some(Reverse(room)) = available_rooms.pop() {
                meeting_held[room as usize] += 1;
                next_ending.push(Reverse((end, room)));
            } else {
                if let Some(Reverse((end_time, room))) = next_ending.pop() {
                    meeting_held[room as usize] += 1;
                    
                    let diff = end_time-start;
                    next_ending.push(Reverse((end+diff, room)));
                }
            }
        }
        
        let mut most_booked = 0;
        let mut most_bookings = 0;
        for (room, booking) in meeting_held.iter().enumerate() {
            if *booking > most_bookings {
                most_booked = room;
                most_bookings = *booking;
            }
        }
        
        most_booked as i32
    }
}