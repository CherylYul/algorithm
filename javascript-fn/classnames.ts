// Ask Interviewer:
// 1. Can there be duplicated classes in the input? Should the output contain duplicated classes?
// 2. What if a class was added and then later turned off? E.g. classNames('foo', { foo: false })

// Handling of each data type
// Recursing for array type

export type ClassValue =
  | ClassArray
  | ClassDictionary
  | string
  | number
  | null
  | boolean
  | undefined;
export type ClassDictionary = Record<string, any>;
export type ClassArray = Array<ClassValue>;

export default function classNames(...args: Array<ClassValue>): string {
  const classes: Array<string> = [];
  args.forEach((arg) => {
    if (!arg) return;
    const argType = typeof arg;

    if (argType === "string" || argType === "number") {
      classes.push(String(arg));
      return;
    }

    if (Array.isArray(arg)) {
      classes.push(classNames(...arg));
      return;
    }

    if (argType === "object") {
      const objArg = arg as ClassDictionary;
      for (const key in objArg) {
        if (Object.hasOwn(objArg, key) && objArg[key]) classes.push(key);
      }
      return;
    }
  });
  return classes.join(" ");
}
