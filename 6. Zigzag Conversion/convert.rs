impl Solution {

    // O(s.len() * num_rows) time,
    // O(s.len() * num_rows) space,
    // Approach: string, math
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1{
            return s;
        }

        let mut zigzag_form = vec![vec!['#'; (s.len()) as usize];(num_rows+1) as usize];
        let mut zigzaging = false;
        let mut upwards = false;
        let mut count = 0;
        let mut row = 0 as usize;
        let mut col = 0 as usize;

        for ch in s.chars() {
            // println!("{} {} {} {}", row, col, count, ch);
            zigzag_form[row][col] = ch;
            count += 1;
            if count % num_rows == 0 {
                upwards = !upwards;
                zigzaging = !zigzaging;
                count += 1;
            }

            if upwards && count % num_rows != 0 {
                row -= 1;
            }
            else {
                if count % num_rows != 0  {  
                    row += 1;
                }
            }

            if zigzaging && count % num_rows != 0 {
                col += 1;
            }
        }

        let mut zigzag = Vec::new();

        for i in 0..(num_rows+1) {
            for j in 0..(s.len()) {
                let val = &zigzag_form[i as usize][j as usize];
                if *val == '#' {
                    continue;
                }

                zigzag.push(*val);
            }
        }

        let answer = zigzag.iter().collect::<String>();

        return answer;
    }
}