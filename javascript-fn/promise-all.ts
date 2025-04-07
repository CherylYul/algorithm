// 1. Promises are meant to be chained, so the function needs to return a Promise.
// 2. If the input array is empty, the returned Promise resolves with an empty array.
// 3. The returned Promise contains an array of resolved values in the same order as the input if all of them are fulfilled.
// 4. The returned Promise rejects immediately if any of the input values are rejected or throw an error.
// 5. The input array can contain non-Promises.

type ReturnValue<T> = { -readonly [P in keyof T]: Awaited<T[P]> };

export default function promiseAll<T extends readonly unknown[] | []>(
  iterable: T
): Promise<ReturnValue<T>> {
  return new Promise((resolve, reject) => {
    const results = new Array(iterable.length);
    let unresolved = iterable.length;

    if (unresolved === 0) {
      resolve(results as ReturnValue<T>);
      return;
    }

    iterable.forEach(async (item, index) => {
      try {
        const value = await item;
        results[index] = value;
        unresolved -= 1;

        if (unresolved === 0) {
          resolve(results as ReturnValue<T>);
        }
      } catch (err) {
        reject(err);
      }
    });
  });
}
