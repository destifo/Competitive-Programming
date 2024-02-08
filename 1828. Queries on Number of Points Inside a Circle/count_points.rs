fn get_euclid_dist(x1: f64, x2: f64, y1: f64, y2: f64) -> i32 {
    let mut result = (x1 - x2).powi(2) + (y1 - y2).powi(2);

    result.sqrt().ceil() as i32
}

impl Solution {
    pub fn count_points(points: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let mut ans = vec![0; queries.len()];

        for (index, q) in queries.iter().enumerate() {
            let x1 = q[0];
            let y1 = q[1];
            let r = q[2];
            for p in &points {
                let x2 = p[0];
                let y2 = p[1];
                if get_euclid_dist(x1 as f64, x2 as f64, y1 as f64, y2 as f64) <= r {
                    ans[index] += 1;
                }
            }
        }

        ans
    }
}
