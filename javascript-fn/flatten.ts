type ArrayValue = any | Array<ArrayValue>;

export default function flatten(value: Array<ArrayValue>): Array<any> {
  const res: Array<any> = [];
  let copy: Array<ArrayValue> = value.slice();

  while (copy.length) {
    const item: ArrayValue = copy.shift();
    if (Array.isArray(item)) {
      copy.unshift(...item);
    } else {
      res.push(item);
    }
  }

  return res;
}

// check if there is an even number in the array
// console.log([1, 2, 3].some((item) => item % 2 === 0)); // true

export function concatFlatten(value: Array<ArrayValue>): Array<any> {
  while (value.some(Array.isArray)) {
    value = [].concat(...value);
  }
  return value;
}

export function recursiveFlatten(value: Array<ArrayValue>): Array<any> {
  return value.reduce(
    (acc, curr) => acc.concat(Array.isArray(curr) ? flatten(curr) : curr),
    []
  );
}
