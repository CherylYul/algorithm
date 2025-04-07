// control how many times we allow a function to be executed over time
// it must wait after X milliseconds before running, along with throttle

export default function debounce(func: Function, wait: number): Function {
  let timeoutID: ReturnType<typeof setTimeout> | null = null;
  return function (this: any, ...args: any[]) {
    const context = this;
    clearTimeout(timeoutID ?? undefined);
    timeoutID = setTimeout(function () {
      timeoutID = null;
      func.apply(context, args);
    }, wait);
  };
}

// Sự ra đời của context: đảm bảo ngữ cảnh truyền vào setTimeout là đúng, nếu mình call this trong method apply, ngữ cảnh sẽ khác
// Sự ra đời của timeoutID: cần phải clear timeout nếu func được invoke lại ở khoảng pending invocation
// Lưu ý khi gọi setTimeout cần trả về giá trị null để biết rằng k còn timeout nào đang chờ xử lý

// arrow function don't need context since it kept the context of the parent scope
// export default function debounce(func, wait) {
//   let timeoutID = null
//   return function(...args) {
//     clearTimeout(timeoutID ?? undefined)
//     timeoutID = setTimeout(() => {
//       timeoutID = null
//       func.apply(this, args)
//     }, wait)
//   }
// }
