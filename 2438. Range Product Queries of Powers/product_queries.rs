fn mod_pow(mut base: i64, mut exp: i64, modu: i64) -> i64 {
    let mut result = 1;
    while exp > 0 {
        if exp % 2 == 1 {
            result = (result * base) % modu;
        }
        base = (base * base) % modu;
        exp /= 2;
    }
    result
}

fn mod_inv(b: i64, modu: i64) -> i64 {
    mod_pow(b, modu - 2, modu)
}


impl Solution {

    // O(logn + m) time, m --> len(queries),
    // O(logn) space,
    // Approach: prefix sum, bit manipulation
    pub fn product_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<i32> {
        let bin_n = format!("{:b}", n);
        let mut powers = vec![];
        
        let mut curr_power = 0;
        for ch in bin_n.chars().rev() {
            let val = ch.to_digit(10).unwrap();
            if val != 0 {
                powers.push(2_i64.pow(curr_power));
            }
            curr_power += 1;
        }
        println!("{:?}", powers);
        let MOD = 10_i64.pow(9) + 7;
        let mut prod_prefix = vec![1_i64];
        for power in powers {
            let last_val = prod_prefix[prod_prefix.len()-1] as i64;
            prod_prefix.push((last_val * power) % MOD);
        }

        let mut answers = vec![];
        for query in queries {
            let (left, right) = (query[0] as usize, query[1] as usize);
            let query_answer = (prod_prefix[right+1] * mod_inv(prod_prefix[left], MOD)) % MOD;
            answers.push((query_answer % MOD) as i32);
        }

        answers
    }
}
