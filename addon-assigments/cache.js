class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map();
    }

    get(key) {
        if (this.cache.has(key)) {
            const value = this.cache.get(key);
            this.cache.delete(key);
            this.cache.set(key, value);
            return value;
        }
        return -1;
    }

    put(key, value) {
        if (this.cache.has(key)) {
            this.cache.delete(key);
        } else if (this.cache.size >= this.capacity) {
            this.cache.delete(this.cache.keys().next().value);
        }
        this.cache.set(key, value);
    }
}

class MultilevelLRUCache {
    constructor(l1Capacity, l2Capacity) {
        this.l1Cache = new LRUCache(l1Capacity);
        this.l2Cache = new LRUCache(l2Capacity);
    }

    get(key) {
        let value = this.l1Cache.get(key);
        if (value !== -1) {
            return value;
        }
        value = this.l2Cache.get(key);
        if (value !== -1) {
            this.l1Cache.put(key, value);
        }
        return value;
    }

    put(key, value) {
        this.l1Cache.put(key, value);
        this.l2Cache.put(key, value);
    }
}

// Test code
const cache = new MultilevelLRUCache(3, 5);
cache.put(1, 10);
cache.put(2, 20);
cache.put(3, 30);
cache.put(4, 40);

console.log(cache.get(1)); // Output: 10
console.log(cache.get(4)); // Output: 40
console.log(cache.get(5)); // Output: -1
/*```
Time Complexity Analysis:

get(key):
L1 Cache Hit: O(1)
L1 Cache Miss, L2 Cache Hit: O(1) for L2 get + O(1) for L1 put = O(1)
Both Miss: O(1)*/
