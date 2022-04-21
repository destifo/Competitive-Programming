/**
 * https://leetcode.com/problems/lru-cache/submissions/
 */

import java.util.HashMap;
import java.util.Map;

public class LRUCache {

    private class Node {
        public int key;
        public int val;
        public Node left;
        public Node right;

        Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private int capacity;
    private Map<Integer, Node> cache = new HashMap<>();
    private Node l = new Node(0, 0);
    private Node r = new Node(0, 0);

    public LRUCache(int capacity) {
        this.capacity = capacity;
        l.right = r;
        r.left = l;
    }

    public int get(int key) {
        if (!cache.containsKey(key))
            return -1;

        Node node = cache.get(key);
        int val = node.val;
        this.remove(node);
        this.addAsMostRecent(node);
        return val;

    }

    public void put(int key, int value) {
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.val = value;
            this.remove(node);
            this.addAsMostRecent(node);
            return;
        } else {
            if (cache.size() == capacity) {
                int prevLeast = l.right.key;
                Node lru = cache.get(prevLeast);
                this.remove(lru);
                Node node = new Node(key, value);
                this.addAsMostRecent(node);
                cache.put(key, node);
                cache.remove(prevLeast);
            } else {
                Node node = new Node(key, value);
                this.addAsMostRecent(node);
                cache.put(key, node);
            }
        }

    }

    private void makeMostRecent(Node node) {
        if (node.key == r.left.key)
            return;

        if (node.key == l.right.key){
            Node temp = l;
            l.right = r.left;
            r.left = temp;
            r.left = l;
            r.right = null;
            l.right = r;
            l.left = null;
        }else {
            node.left.right = node.right;
            node.right.left = node.left;
            r.right = node;
            node.right = null;
            r = node;
        }
    }

    private void addAsMostRecent(Node node) {
        r.left.right = node;
        r.left = node;
        node.left = r.left;
        node.right = r;
    }

    private void replaceLeastRecent(int key, int val) {
        l.right.key = key;
        l.right.val = val;
        this.makeMostRecent(l.right);
    }

    private void add(Node node){
        r.right = node;
        node.left = r;
        r = node;
    }

    private void remove(Node node){
        node.left.right = node.right;
        node.right.left = node.left;
    }

    public static void main(String[] args) {
        LRUCache lRUCache = new LRUCache(2);
        lRUCache.put(1, 1); // cache is {1=1}
        lRUCache.put(2, 2); // cache is {1=1, 2=2}
        lRUCache.get(1); // return 1
        lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        lRUCache.get(2); // returns -1 (not found)
        lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        lRUCache.get(1); // return -1 (not found)
        lRUCache.get(3); // return 3
        lRUCache.get(4); // return 4
    }

}
