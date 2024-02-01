use std::collections::{HashMap, HashSet};

fn union(i: usize, j: usize, parent: &mut Vec<usize>) {
    let p1 = find(i, parent);
    let p2 = find(j, parent);

    if p1 < p2 {
        parent[p2] = p1;
    } else {
        parent[p1] = p2;
    }
}

fn find(i: usize, parent: &mut Vec<usize>) -> usize {
    if i != parent[i] {
        parent[i] = find(parent[i], parent);
    }

    return parent[i];
}

impl Solution {
    pub fn smallest_string_with_swaps(s: String, pairs: Vec<Vec<i32>>) -> String {
        // do a union-find to find the groups
        let n = s.len();
        let mut parent: Vec<usize> = (0..n).collect();

        for pair in &pairs {
            union(pair[0] as usize, pair[1] as usize, &mut parent);
        }

        for i in 0..n {
            find(i, &mut parent);
        }

        // prepare a group based on the parent
        let parents: HashSet<usize> = parent.iter().cloned().collect();
        let mut groups: HashMap<usize, Vec<usize>> = HashMap::new();
        for p in &parents {
            groups.insert(*p, vec![*p]);
        }

        // add the indices to their group
        for i in 0..n {
            if !parents.contains(&i) {
                let p = parent[i];
                if let Some(group) = groups.get_mut(&p) {
                    group.push(i);
                }
            }
        }

        let s_chars: Vec<char> = s.chars().collect();
        let binding = "".to_string();
        let mut str_builder: Vec<String> = vec![binding; n];
        for (k, v) in groups {
            let mut chars: Vec<String> = vec![];
            for index in &v {
                chars.push(s_chars[*index].to_string());
            }

            chars.sort();
            for i in 0..chars.len() {
                let ch = &chars[i];
                let index = v[i];
                str_builder[index] = ch.clone();
            }
        }

        return str_builder.join("");
    }
}
