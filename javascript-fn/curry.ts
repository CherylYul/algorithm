// Currying is the technique of converting a function that takes multiple arguments into a sequence of functions that each takes a single argument.

// const add = (a: number, b: number) => a + b;
// const curriedAdd = curry(add);
// curriedAdd(3)(4); // 7
// const alreadyAddedThree = curriedAdd(3);
// alreadyAddedThree(4); // 7

// Clarification Questions
// 1. What value types will curry expect?
// 2. Should the function expect values of different types?

// Arity: The number of arguments or operands taken by a function.
// Closure: A closure is the combination of a function bundled together with references to its lexical environment (surrounding state).

export default function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func.apply(this, args);
    }

    return (arg) =>
      arg === undefined
        ? curried.apply(this, args)
        : curried.apply(this, [...args, arg]);
  };
}

export function tsCurry(func: Function): Function {
  return function curried(this: any, ...args: Array<any>) {
    if (args.length >= func.length) {
      return func.apply(this, args);
    }

    return (arg: any) =>
      arg === undefined
        ? curried.apply(this, args)
        : curried.apply(this, [...args, arg]);
  };
}
