/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function (word1, word2) {
  const len1 = word1.length;
  const len2 = word2.length;
  let i = 0;
  let j = 0;
  let res = "";
  while (i < len1 && j < len2) {
    res += word1[i] + word2[j];
    i += 1;
    j += 1;
  }
  return i < len1 ? res + word1.slice(i) : res + word2.slice(j);
};

// var mergeAlternately = function (word1, word2) {
//   const arr1 =word1.split("");
//   const arr2 =word2.split("");
//   const lengths =Math.max(arr1.length, arr2.length);
//   let result ="";
//   for(let i=0;i<lengths;i++){
//     if(arr1[i]) result +=arr1[i];
//     if(arr2[i]) result +=arr2[i];
//   }
//   return result;
// };
