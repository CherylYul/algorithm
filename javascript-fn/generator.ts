// iterable
let range = {
  from: 1,
  to: 5,
  [Symbol.iterator]: () => {
    return {
      current: this.from,
      last: this.to,
      next: () => {
        if (this.current <= this.last)
          return {
            done: false,
            value: this.current++,
          };
        return { done: true };
      },
    };
  },
};

// iterator
function makeRangeIterator(start = 0, end = Infinity, step = 1) {
  let nextIndex = start;
  let iterationCount = 0;

  const rangeIterator = {
    next: function () {
      let result;
      if (nextIndex <= end) {
        result = { value: nextIndex, done: false };
        nextIndex += step;
        iterationCount++;
        return result;
      }
      return { value: iterationCount, done: true };
    },
  };
  return rangeIterator;
}

let iterator = makeRangeIterator(1, 10, 2);
let result = iterator.next();
while (!result.done) {
  console.log(result.value); // 1 3 5 7 9
  result = iterator.next();
}

console.log("Iterated over sequence of size: ", result.value); // 5

// generator is also an iterator
function* makeRangeGenerator(start = 0, end = Infinity, step = 1) {
  let iterationCount = 0;
  for (let i = start; i < end; i += step) {
    iterationCount++;
    yield i;
  }
}
let exRange = makeRangeGenerator(1, 10, 2);
exRange.next().value;
exRange.next().done;
for (let num in makeRangeIterator(1, 10, 2)) console.log(num);
for (let value of exRange) {
  console.log(value); // Outputs 1, then 2, then 3
}

// Use generators and iterators to handle data structures
function* treeTraversal(tree) {
  yield tree.value;
  if (tree.left) {
    yield* treeTraversal(tree.left);
  }
  if (tree.right) {
    yield* treeTraversal(tree.right);
  }
}

const binaryTree = {
  value: "root",
  left: {
    value: "left",
    left: {
      value: "left-left",
    },
    right: {
      value: "left-right",
    },
  },
  right: {
    value: "right",
  },
};

for (let value of treeTraversal(binaryTree)) {
  console.log(value);
}
// Output: root, left, left-left, left-right, right
