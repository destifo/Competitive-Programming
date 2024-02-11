// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }

fn get_gcd(num1: i32, num2: i32) -> i32 {
    match num2 {
        0 => num1,
        _ => get_gcd(num2, num1 % num2),
    }
}

impl Solution {
    pub fn insert_greatest_common_divisors(
        mut head: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        /*
            1) store curr, and prev
            2) create gcd node, and add in the middle,
            3) update prev to curr, curr = curr.next
        */

        let mut curr = &mut head;

        while let Some(node) = curr {
            if let Some(mut next) = node.next.take() {
                let gcd = get_gcd(next.val, node.val);
                let mut gcd_node = Box::new(ListNode::new(gcd));
                gcd_node.next = Some(next);

                node.next = Some(gcd_node);
                curr = &mut node.next.as_mut().unwrap().next;
            } else {
                break;
            }
        }

        return head;
    }
}
